import inquirer

def Velocity():
    print('v = U + AT')
    print('This equation describes the relationship between velocity, acceleration, and time.')
    Velocity = [
        inquirer.List
        (   'Main',
            message='What do you want to find',
            choices = [
                'Final Velocity',
                'Intital Velocity',
                'Acceleration',
                'Time'
            ],
            carousel=True
        ),
    ]
    answers = inquirer.prompt(Velocity)
    if answers['Main'] == 'Final Velocity':
        Time = int(input('What is the Time : '))
        IntialVelocity = int(input('what is the Intial Velocity : '))
        Acc = int(input('what is the Acceleration : '))
        answer  = IntialVelocity + Time * Acc
        print(f'The Final Velocity is {answer}')
    elif answers['Main'] == 'Intital Velocity':
        Time = int(input('what is the Time : '))
        Acc = int(input('what is the Acceleration : '))
        velocity = int(input('what is the Velocity : '))
        Answer = velocity - Time * Acc 
        print(f'The Intital Velocity is {Answer}')
    elif answers['Main'] == 'Acceleration':
        Time = int(input('what is the Time : '))
        velocity2 = int(input('what is the velocity : '))
        Intial_Velocity = int(input('what is the Intial Velocity : '))
        Answer =  velocity2 - Intial_Velocity / Time
        print(f'The Acceleration is {Answer}')
    elif answers['Main'] == 'Time':
        Acc = int(input('what is the Acceleration : '))
        velocity2 = int(input('what is the velocity : '))
        Intial_Velocity = int(input('what is the Intial Velocity : '))
        Answer =  velocity2 - Intial_Velocity / Acc
        print(f'The Time is {Answer}')



            