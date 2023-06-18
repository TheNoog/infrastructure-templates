# This DAG is to run in Azure Kubernetes Services (AKS) and
#   pull the image at run-time into the pod from an Azure
#   container registry.

# https://www.astronomer.io/blog/airflow-dbt-1
# This DAG uses the manifest file copied to a set location
#   to populate the DAG and run each dbt model independently.
# This is a monolithic model with all DBT models in a single DAG.

import json
from datetime import timedelta
from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from airflow.kubernetes.secret import Secret
from kubernetes.client import models as k8s
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta

default_args = {
    'owner': 'test',
    'depends_on_past': False,
    'start_date': days_ago(0),
    'catchup': False,
    'email': ['test@test.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dbt_monolithic_dag',  # name of the DAG in Airflow menu
    default_args=default_args,
    schedule_interval=timedelta(minutes=30),
    max_active_runs=1,
    concurrency=10,
    description='A dbt wrapper for airflow.'
)

# the manifest file for dbt must be in this location
def load_manifest():
    local_filepath = "/usr/local/airflow/dags/dbt/manifest.json"
    with open(local_filepath) as f:
        data = json.load(f)

    return data

def make_dbt_task(node, dbt_verb):
    """Returns an Airflow operator either run and test an individual model"""
    DBT_DIR = "/usr/local/airflow/dags/dbt"
    GLOBAL_CLI_FLAGS = "--no-write-json"
    model = node.split(".")[-1]

    if dbt_verb == "run":
        dbt_task = BashOperator(
            task_id=node,
            bash_command=f"""
            cd {DBT_DIR} &&
            dbt {GLOBAL_CLI_FLAGS} {dbt_verb} --target prod --models {model}
            """,
            dag=dag,
        )

    elif dbt_verb == "test":
        node_test = node.replace("model", "test")
        dbt_task = BashOperator(
            task_id=node_test,
            bash_command=f"""
            cd {DBT_DIR} &&
            dbt {GLOBAL_CLI_FLAGS} {dbt_verb} --target prod --models {model}
            """,
            dag=dag,
        )

    return dbt_task

data = load_manifest()

dbt_tasks = {}
for node in data["nodes"].keys():
    if node.split(".")[0] == "model":
        node_test = node.replace("model", "test")

        dbt_tasks[node] = make_dbt_task(node, "run")
        dbt_tasks[node_test] = make_dbt_task(node, "test")

for node in data["nodes"].keys():
    if node.split(".")[0] == "model":

        # Set dependency to run tests on a model after model runs finishes
        node_test = node.replace("model", "test")
        dbt_tasks[node] >> dbt_tasks[node_test]

        # Set all model -> model dependencies
        for upstream_node in data["nodes"][node]["depends_on"]["nodes"]:

            upstream_node_type = upstream_node.split(".")[0]
            if upstream_node_type == "model":
                dbt_tasks[upstream_node] >> dbt_tasks[node]