Run Docker image: "docker run -p stacylynn333/iheartmediachallenge:latest"

Output is printed to bash shell (for questions 1 and 3)

To cp cvs file (named valuecounts.csv) of value, count to localhost:
    docker create -ti --name dummy iheartmediachallenge bash
    docker cp dummy:app/valuecounts.csv .
    docker rm -fv dummy


