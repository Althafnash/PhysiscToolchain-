import inquirer
from Classical import ClassicalMain
import subprocess as sub 

questions = [
  inquirer.List
  (    'Main',
        message="Choice a branch",
        choices=['Classical Mechanics', 
                  'Thermodynamics', 
                  'Electromagnetism', 
                  'Optics', 
                  'Relativity'],
        carousel=True,
  ),
]
answers = inquirer.prompt(questions)

if answers['Main'] == 'Classical Mechanics':
  sub.run('cls',shell=True)
  ClassicalMain()