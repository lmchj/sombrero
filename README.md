![Logo](logo.png)

## A generator of random tests

This is __sombrero__, a project whose aim is to ease the task of design tests, mainly for upper mathematics courses.

It is sometimes a pain in the ass to design examination tests for courses that require proofs.
If you make right (I mean, as a responsible teacher) the process is something like this:

1. You have to look for the exercises.
2. Check if your students can actually solve them given what you taught them.
3. Solve them consiously, which implies maybe look for multiple proofs and shit like that.
4. Transcribe the exercises to a test sheet, or in case that you designed them, write them well.

Of course plenty of teachers are not that responsible and will not make a proper test for their examinatios, often failing on the second and third step.

With __sombrero__ I want a tool to generate random tests selected from a database, where the exercises are categorized by __topic__ and __relative difficulty__.
In which the problem statements and solutions are written with LaTeX syntax and then it compile the document to give you one `PDF` __with the problems__ and __another one with the solutions__.

## Current status

Right now sombrero works properly as a command line tool, which is my main goal.

The procedure to use it is:

1. Build your problems data base following the `problems2.txt` template.
2. 

## Future work

I want to make a couple of things, but the main one is to give the user the possibility to make their own `.tex` document with all the problems they would like to place on an examination test.
This is for the user to be able to compile their document, and see LaTeX syntax errors, for __sombrero__ to run smothly.
Then use a simple shell script to translate that `.tex` file into a readable database for sombrero.
That is the firs step on the future work.

1. Shell script that thanslates `.tex` file with problems into a readable database for sombrero.
2. Convert the python script into a shell script.
3. Make it a web platform with problems from people all over the world.
