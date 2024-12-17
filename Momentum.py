import inquirer

def Momentum():
    print('P = M * V')
    print('This equation describes that Momentum is the product of mass and velocity .')
    Momentum = [
        inquirer.List
        (   'Main',
            message='What do you want to find',
            choices = [
                'Momentum',
                'Mass',
                'Velocity'
            ],
            carousel=True
        ),
    ]
    answers = inquirer.prompt(Momentum)
    if answers['Main'] == 'Momentum':
        Mass = int(input('What is the Time : '))
        Velocity = int(input('what is the Distance : '))
        answer  = Mass * Velocity
        print(f'The Momentum is {answer}')
    elif answers['Main'] == 'Mass':
        Momentum = int(input('what is the Momentum : '))
        Velocity = int(input('what is the Velocity : '))
        Answer = Momentum / Velocity
        print(f'The Mass is {Answer}')
    elif answers['Main'] == 'Velocity':
        Mass = int(input('what is the Mass : '))
        Momentum = int(input('what is the Momentum : '))
        Answer = Momentum / Mass
        print(f'The Velocity is {Answer}')



            