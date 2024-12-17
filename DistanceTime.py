import inquirer
import math
 
def Distance_Time():
    print('s=ut+1/2*a*t2')
    print('This equation describes the displacement of an object when it is under constant acceleration.')
    Velocity = [
        inquirer.List
        (   'Main',
            message='What do you want to find',
            choices = [
                'Displacement',
                'Intital ',
                'Acceleration',
                'Time'
            ],
            carousel=True
        ),
    ]
    answers = inquirer.prompt()
    if answers['Main'] == 'Distance':
        Time = int(input('What is  Time : '))
        Intial_Velocity = int(input('what is the Intial velocity : '))
        Acc = int(input('what is the Acceleration : '))
        answer  = Intial_Velocity * Time + 0.5 * Time * Time
        print(f'The Velocity is {answer}')
    elif answers['Main'] == 'Intital Velocity':
        Time = int(input('what is the Time : '))
        Acc = int(input('what is the Acceleration : '))
        Distance = int(input('what is the Distance : '))
        Answer = Distance - 0.5 * Acc * Time * Time / Time
        print(f'The Intital velocity is {Answer}')
    elif answers['Main'] == 'Acceleration':
        Time = int(input('what is the Time : '))
        Distance = int(input('what is the Distance : '))
        Intial_Velocity = int(input('what is the Intial Velocity : '))
        Answer = 2 * Distance  - Intial_Velocity / Time / Time * Time
        print(f'The Acceleration is {Answer}')
    elif answers['*Main'] == 'Time':
        Acc = int(input('what is the Acceleration : '))
        Distance = int(input('what is the Distance : '))
        Intial_Velocity = int(input('what is the Intial Velocity : '))
        Answer =  -Intial_Velocity + math.sqrt(Intial_Velocity * Intial_Velocity + 2 *Acc * Distance) / Acc
        Answer2 =  -Intial_Velocity - math.sqrt(Intial_Velocity * Intial_Velocity + 2 *Acc * Distance) / Acc
        print(f'The Time is {Answer} or {Answer2}')



            