#!/usr/bin/python3
import random
import argparse
import pandas as pd
import os
import subprocess
import sys

parser = argparse.ArgumentParser()
#Argumentos para diseñar el examen
parser.add_argument('-a', '--area', required=True,
    help='Asignatura del examen', type=str)
parser.add_argument('-t', '--topic', required=True,
    help='Tema del examen', type=str)
parser.add_argument('-d', '--difficulty', required=True,
    help='Dificultad del examen', type=int)
parser.add_argument('-n', '--nproblems', required=True,
    help='Cantidad de problemas', type=int)
#Argumentos para identificar el examen
parser.add_argument('-c', '--course', default='Algebra I')
parser.add_argument('-e', '--exam', default='First term')
parser.add_argument('-p', '--prof', default='John Smith, PhD') 
parser.add_argument('-s', '--school', default='My U')


args_var = vars(parser.parse_args())
args = parser.parse_args()

area = str(args_var['area'])
topic = str(args_var['topic'])
diff = int(args_var['difficulty'])
amount = int(args_var['nproblems'])

#Lectura de problemas y selección según los argumentos de diseño
data_base = open('/home/luismario/Dropbox/Proyecto de Matematicas/sombrero_code/db/problems2.txt', 'r')
matching_problems = []
matching_ans = []

if data_base.mode == 'r':
    data_base = data_base.readlines()
    l = len(data_base)
    for k in range(l):
        if ((data_base[k].split("%@%/")[2] == area) and
            (data_base[k].split("%@%/")[3] == topic) and
            (int(data_base[k].split("%@%/")[4]) == diff)):
                matching_problems.append(data_base[k].split("%@%/")[0])
                matching_ans.append(data_base[k].split("%@%/")[1])

#print(matching_problems)

#Lista para almacenar los números aleatorios con los que se seleccionan los problemas
random_numbers = []
random_numbers = random.sample(range(len(matching_problems)), amount)

#Almacenamiento de los problemas y las respuestas correspondientes
problems = []
ans = []

for j in random_numbers:
    problems.append(matching_problems[j])
    ans.append(matching_ans[j])

#print(problems)
#print(ans)

content = r'''\documentclass[10pt,letterpaper]{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\author{
%(school)s\\
Asignatura: %(course)s\\
Profesor: %(prof)s}
\title{%(exam)s}
\date{\today}
\begin{document}
	\maketitle
	\textit{Instrucciones:}

	\begin{itemize}
		\item Lea cuidadosamente los siguientes problemas.
		\item Fundamente su respuesta de manera clara y limpia.
		\item Disfrute su examen.
	\end{itemize}

	\textbf{Problemas:}
	\begin{itemize}
'''

i = 0
while(i < len(problems)):
	content += r'''\item ''' + problems[i]
	i += 1

content += r'''\end{itemize}
	
\end{document}'''

print(content)

with open('sombrero_test.tex','w') as f:
    f.write(content%args.__dict__)

cmd = ['pdflatex', '-interaction', 'nonstopmode', 'sombrero_test.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink('sombrero_test.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

os.unlink('sombrero_test.tex')
os.unlink('sombrero_test.log')
os.unlink('sombrero_test.aux')