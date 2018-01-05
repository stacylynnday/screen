# Instructions

- Build this docker image
- Run `bash` as the command with an iteractive tty to get into the image:

```
docker run --rm -it ${whatever-you-named-the-image} /bin/bash
```

- The data is in the directory `/root/data` on said image
- Create a Pull Request with your code for review

> You're free to use whatever language you want just as long as you include the instructions on how to run your code. (Bonus points if you modify the `Dockerfile` instead)


# Questions

## what's the average number of fields across all the `.csv` files?

output should be a simple number

_sample output_

```
5
```

## create a csv file that shows the word count of every value of every dataset

output should be a csv file that has a header row with fields `value` and
`count` and one entry for every value found:

_sample output_

```
value,count
some value,435
another value,234
word,45
...
```

## what's the total number or rows for the `.csv` files?

output should be a simple number

_sample output_

```
1000000000
```
