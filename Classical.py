import inquirer
from Newtons_Second_Law_of_Motion import Newtons_second_law_of_motion
from Speed import Speed
from VelocityTime import Velocity
from DistanceTime import Distance_Time
from FinalVelocity import Final_Velocity
from Work_Energy_Theorem import Work_Energy_Therom
from KineticEnergy import KineticEnergy
from potentialenergy import PotentialEnegry
from Conservation_of_Mechanical_Energy import Conservation_of_Mechanical_Energy
from Momentum import Momentum
import subprocess as sub 

def ClassicalMain():
    Classical = [
        inquirer.List
        (    'Main',
                message="Choice a branch",
                choices=['Speed',
                        'Newtons Second Law of Motion', 
                        'Velocity-Time Relationship', 
                        'Displacement-Time', 
                        'FinalVelocity', 
                        'Work-Energy Theorem',
                        'KineticEnergy',
                        'PotentialEnegry',
                        'Conservation_of_Mechanical_Energy',
                        'Momentum'
                        ],
                carousel=True,
        ),
    ]
    Classicalanswers = inquirer.prompt(Classical)
    if Classicalanswers['Main'] == 'Newtons Second Law of Motion':
        sub.run('cls',shell=True)
        Newtons_second_law_of_motion()
    if Classicalanswers['Main'] == 'Speed':
        sub.run('cls',shell=True)
        Speed()
    if Classicalanswers['Main'] == 'Velocity-Time Relationship':
        sub.run('cls',shell=True)
        Velocity()
    if Classicalanswers['Main'] == 'Displacement-Time':
        sub.run('cls',shell=True)
        Distance_Time()
    if Classicalanswers['Main'] == 'FinalVelocity':
        sub.run('cls',shell=True)
        Final_Velocity()
    if Classicalanswers['Main'] == 'Work-Energy Theorem':
        sub.run('cls',shell=True)
        Work_Energy_Therom()
    if Classicalanswers['Main'] == 'KineticEnergy':
        sub.run('cls',shell=True)
        KineticEnergy()
    if Classicalanswers['Main'] == 'PotentialEnegry':
        sub.run('cls',shell=True)
        PotentialEnegry()
    if Classicalanswers['Main'] == 'Conservation_of_Mechanical_Energy':
        sub.run('cls',shell=True)
        Conservation_of_Mechanical_Energy()
    if Classicalanswers['Main'] == 'Momentum':
        sub.run('cls',shell=True)
        Momentum()
    