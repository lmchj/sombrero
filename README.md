![Logo](logo.png)

## A generator of random tests

This is __Sombrero__, a project whose aim is to ease the task of design tests, mainly for upper mathematics courses.

It is sometimes a pain in the ass to design examination tests for courses that require proofs.
If you make right (I mean, as a responsible teacher) the process is something like this:

1. You have to look for the exercises.
2. Check if your students can actually solve them given what you taught them.
3. Solve them consiously, which implies maybe look for multiple proofs and shit like that.
4. Transcribe the exercises to a test sheet, or in case that you designed them, write them well.

Of course plenty of teachers are not that responsible and will not make a proper test for their examinatios, often failing on the second and third step.

With __Sombrero__ I want a tool to generate random tests selected from a database.
In which the problem statements and solutions are written with LaTeX syntax and then it compile the document to give you one `PDF` _with the problems_ and _another one with the solutions_.

## Current status

Right now sombrero works properly as a command line tool, which is my main goal.

The procedure to use it is:

1. Build your problems data base following the `problems2.txt` template.
2. 

## Future work

1. Shell script that thanslates `.tex` file with problems into a readable database for sombrero.
2. Convert the python script into a shell script.
3. Make it a web platform with problems from people all over the world.
