#!/usr/bin/python3
import random
import argparse
import os
import subprocess
import sys
import cgi
import cgitb
import time

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from text fields
name = form.getvalue('nombre')
title = form.getvalue('titulo')
amount = int(form.getvalue('numero'))

#Get data from dropdown box
if form.getvalue('status'):
    area = form.getvalue('status')
else:
    area = "Not entered"

if form.getvalue('dificultad'):
    diff = int(form.getvalue('dificultad'))
else:
    diff = "Not entered"

#Get data from checkboxes
if form.getvalue('limites'):
   limites_flag = "lim"
else:
   limites_flag = "OFF"

if form.getvalue('reglasderiv'):
   reglasderiv_flag = "rd"
else:
   reglasderiv_flag = "OFF"

if form.getvalue('maxmin'):
   maxmin_flag = "maxmin"
else:
   maxmin_flag = "OFF"

if form.getvalue('derivos'):
   derivos_flag = "derivos"
else:
   derivos_flag = "OFF"

if form.getvalue('derivim'):
   derivim_flag = "derivim"
else:
   derivim_flag = "OFF"

if form.getvalue('intindef'):
   intindef_flag = "intindef"
else:
   intindef_flag = "OFF"

if form.getvalue('intfp'):
   intfp_flag = "intfp"
else:
   intfp_flag = "OFF"

if form.getvalue('intpart'):
   intpart_flag = "intpart"
else:
   intpart_flag = "OFF"

if form.getvalue('intdef'):
   intdef_flag = "intdef"
else:
   intedef_flag = "OFF"

if form.getvalue('intapl'):
   intapl_flag = "intapl"
else:
   intapl_flag = "OFF"

#Lectura de problemas y selección según los argumentos de diseño
#data_base = pd.read_csv("/home/luismario/Dropbox/Proyecto de Matematicas/sombrero_code/db/problems2.txt",
#            engine='python',
#            sep="%@%/")

#with open('/usr/lib/cgi-bin/problems2.txt', 'r') as file:
#    data_base = csv.reader(file, delimiter = '%@%/')

data_base = open('/usr/lib/cgi-bin/problems2.txt', 'r')
matching_problems = []
matching_ans = []

if data_base.mode == 'r':
    data_base = data_base.readlines()
    l = len(data_base)
    for k in range(l):
    	if ((data_base[k].split("%@%/")[2] == area) and
       	    (data_base[k].split("%@%/")[3] == limites_flag) and
       	    (int(data_base[k].split("%@%/")[4]) == diff)):
    		matching_problems.append(data_base[k].split("%@%/")[0])
    		matching_ans.append(data_base[k].split("%@%/")[1])

#matching_problems = data_base[(data_base.Asignatura == area) &
#                                (data_base.Dificultad == diff) &
#				(data_base.Tema == limites_flag)]

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
Escuela: \\
Asignatura: \\
Profesor: }
\title{%s}
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
	\begin{enumerate}
''' % (title)

i = 0
while(i < len(problems)):
	content += r'''\item ''' + problems[i]
	i += 1

content += r'''\end{enumerate}

\end{document}'''


#print(content)
t = str(time.time())
with open('/var/www/html/examenes/sombrero_test_%s.tex' % (t),'w') as f:
    f.write(content)

cmd = ['pdflatex', '-interaction', 'nonstopmode', '-output-directory', '/var/www/html/examenes/', '/var/www/html/examenes/sombrero_test_%s.tex' % (t)]
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink('/var/www/html/examenes/sombrero_test_%s.pdf' % (t))
    #raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd)))

os.unlink('/var/www/html/examenes/sombrero_test_%s.tex' % (t))
os.unlink('/var/www/html/examenes/sombrero_test_%s.log' % (t))
os.unlink('/var/www/html/examenes/sombrero_test_%s.aux' % (t))

# HTTP Header
print ("Content-Type: application/octet-stream; charset = UTF-8; name = \"FileName\"\r\n")
#print ("\r\n")
print ("Content-Disposition: attachment; filename = \"FileName\"\r\n\n")

# Actual File Content will go here
#fo = open("/var/www/html/examenes/sombrero_test_%s.pdf" % (t), "rb")
fo = open("/var/www/html/examenes/sombrero_test_%s.pdf" % (t), "rb")

str = fo.read()
print (str)

# Close opend file
fo.close()
