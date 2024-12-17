import inquirer
import math

def KineticEnergy():
    print('k = 1/2 * m * v2')
    print('This equation Calculates the Kenetic enegry of a object.')
    KineticEnergy = [
        inquirer.List
        (   'Main',
            message='What do you want to find',
            choices = [
                'KineticEnegry',
                'mass',
                'Velocity'
            ],
            carousel=True
        ),
    ]
    answers = inquirer.prompt(KineticEnergy)
    if answers['Main'] == 'KineticEnegry':
        Mass = int(input('What is the Mass : '))
        Velocity = int(input('what is the Acceleration : '))
        answer  = 0.5 * Mass * Velocity * Velocity
        print(f'The Kinetic Enegry is {answer}')
    elif answers['Main'] == 'mass':
        Kinetic_Energy = int(input('what is the Kinetic Enegry : '))
        Velocity = int(input('what is the Velocity : '))
        Answer = 2 * Kinetic_Energy / Mass * Velocity * Velocity 
        print(f'The Mass is {Answer}')
    elif answers['Main'] == 'Velocity':
        kinetic_Enegry = int(input('what is the kinetic Enegry : '))
        Mass = int(input('what is the Mass : '))
        Answer = math.sqrt(2 * kinetic_Enegry / Mass)
        print(f'The Velocity is {Answer}')



            