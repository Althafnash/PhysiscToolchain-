import inquirer
import math

def Final_Velocity():
    print('v2 = u2 + 2as')
    print('This equation describes the relationship between velocity, acceleration, and time.')
    Velocity = [
        inquirer.List
        (   'Main',
            message='What do you want to find',
            choices = [
                'Final Velocity',
                'Intital Velocity',
                'Acceleration',
                'Displacemnet'
            ],
            carousel=True
        ),
    ]
    answers = inquirer.prompt(Velocity)
    if answers['Main'] == 'Final Velocity':
        Displacment = int(input('what is the Displacment : '))
        Acc = int(input('what is the Acceleration : '))
        IntialVelocity = int(input('what is the Intial Velocity : '))
        answer  = math.sqrt(IntialVelocity * IntialVelocity + 2 * Acc * Displacment)
        print(f'The Final Velocity is {answer}')
    elif answers['Main'] == 'Intital Velocity':
        Acc = int(input('what is the Acceleration : '))
        Displacment = int(input('what is the Displacment : '))
        FinalVelocity = int(input('what is the Final Velocity : '))
        answer  = math.sqrt(FinalVelocity * FinalVelocity + 2 * Acc * Displacment)
        print(f'The Intital Velocity is {Answer}')
    elif answers['Main'] == 'Acceleration':
        velocity2 = int(input('what is the velocity : '))
        Intial_Velocity = int(input('what is the Intial Velocity : '))
        Displacment = int(input('what is the Intial Displacment : '))
        Answer =  velocity2 * velocity2 - Intial_Velocity * Intial_Velocity / 2 * Displacment
        print(f'The Acceleration is {Answer}')
    elif answers['Main'] == 'Displacment':
        Acc = int(input('what is the Acceleration : '))
        velocity2 = int(input('what is the velocity : '))
        Intial_Velocity = int(input('what is the Intial Velocity : '))
        Answer =  velocity2 * velocity2 - Intial_Velocity * Intial_Velocity / 2 * Acc
        print(f'The Time is {Answer}')



            