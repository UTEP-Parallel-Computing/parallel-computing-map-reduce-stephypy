# Parallel-Computing-MapReduce
For this assignment you will write a parallel map reduce program. The program will search for a set 
of words among a set of documents that constitute the works of Shakespeare. The set of words is listed 
below. The assignment should use the map-reduce design pattern to split up the work. You should have
functions that count the number of a specific word within a specific document and combine the individual
word counts.

The program should output the total instances of all words and the counts for each individual word

Word list:
hate, love, death, night, sleep, time, henry, hamlet, you, my, blood, poison, macbeth, king, heart, honest

Once completed the repository should contain your code, a short report, and any instructions needed to run your code.

Hints: 
* Its easier to load all the files containing text before entering the processing region
* Some of the variables will need to be locked before updating, otherwise a difficult to debug race condition may occure
* This will take multiple loops (functions would be better though), you can iterate over the list of words

## Requirements 

Write a serial matrix multiply program in Python. The could should use reasonable decomposition, use reasonable variable names, and should generally follow good coding standards. Important, your assignment should include your name. 

The program shall count the number of each instances of each word for the set of documents, and the total of count of all words in the list

The program shall use PyMP to compute the number of words in parallel

The program shall time how long overall operation takes and how long the word count and file reading operations take individually

The program shall include any necessary instructions to properly run the program 

The assignment shall be submitted through github 

## Execution

For default run:
python3 MapReduce.py

For custom input:
python3 MapReduce.py --t #

In which # represents any positive number bigger than 1
