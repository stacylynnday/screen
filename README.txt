Run this command to get datasets from github:
/bin/bash -c mkdir data && cd data && while read i; do git clone $i; done < <(curl -s https://api.github.com/orgs/datasets/repos?per_page=100 | jq -r '.[].clone_url')

Run Docker image: "docker run stacylynn333/iheartmediachallenge"

Output is printed to bash shell (for questions 1 and 3)

To cp cvs file (named value_counts.csv) of value, count to localhost:
    "docker ps -a" - to get container id
    "docker cp <container_id>:/app/value_counts.csv ."


