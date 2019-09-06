Run Docker image: "docker run -p stacylynn333/iheartmediachallenge:latest"

Output is printed to bash shell (for questions 1 and 3)

To cp cvs file (named valuecounts.csv) of value, count to localhost:
    docker create -ti --name dummy iheartmediachallenge bash
    docker cp dummy:app/valuecounts.csv .
    docker rm -fv dummy
    
Question 1: what's the average number of fields across all the .csv files?  11 (rounded to nearest integer)

Question 2: create a csv file that shows the word count of every value of every dataset (dataset being a .csv file)
    Filename is valuecounts.csv and it's in the app directory
    
Question 3:  what's the total number or rows for the all the .csv files?  3185413
    
