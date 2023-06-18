#!/usr/bin/env bash
cd /home/dbtUser
dbt init myProject
cd myProject

echo "Copy profiles across."
cp /home/dbtUser/profiles.yml /root/.dbt/profiles.yml
cp /home/dbtUser/myProject/dbt_project.yml /root/myProject/dbt_project.yml

echo "Starting debug..."
dbt debug
echo "dbt debug complete.\n\n"

dbt run

# Run the following to keep the container up until debugged.
# git clone $REMOTE_REPO
# cd $REPO_DIR

# dbt deps --profiles-dir .
# dbt docs generate --target prod --profiles-dir .
# dbt docs serve --profiles-dir . > /dev/null 2>&1 &
# while [ True ]
# do
#     sleep 600
#     if [ `git rev-parse --short HEAD` != `git rev-parse --short origin/master` ]; then
#         git fetch --all
#         git reset --hard origin/master
#         dbt deps --profiles-dir .
#         dbt docs generate --target prod --profiles-dir .
#     fi
# done