# https://www.astronomer.io/blog/airflow-dbt-2
# This DAG uses the manifest file copied to a set location
#   to populate the DAG and run each dbt model independently.

import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta

default_dag_args = {
"start_date": datetime.datetime(2020, 11, 24),
"retry_delay": datetime.timedelta(minutes=10),
"on_failure_callback": notify_all_of_failure,
"depends_on_past": True,
"wait_for_downstream": True,
"retries": 0,
}

DAG_NAME = "standard_schedule"

dag = DAG(
    f"dbt_{DAG_NAME}", schedule_interval="@daily", max_active_runs=1, catchup=False, default_args=default_dag_args,
)

# Load dependencies from configuration file
dag_def = load_dag_def_pickle(f"{DAG_NAME}.pickle")

# Returns a dictionary of bash operators corresponding to dbt models/tests
dbt_tasks = create_task_dict(dag_def, dag)

# Set dependencies between tasks according to config file
for edge in dag_def:
    dbt_tasks[edge[0]] >> dbt_tasks[edge[1]]