import inquirer

def Speed():
    print('S = D / T')
    print('This equation describes that speed is derictly proptional to the distance and indericlty propotional to Time .')
    Speed = [
        inquirer.List
        (   'Main',
            message='What do you want to find',
            choices = [
                'Speed',
                'Distance',
                'Acceleration'
            ],
            carousel=True
        ),
    ]
    answers = inquirer.prompt(Speed)
    if answers['Main'] == 'Speed':
        Time = int(input('What is the Time(m) : '))
        Distance = int(input('what is the Distance(d) : '))
        answer  = Time / Distance 
        print(f'The Speed is {answer}')
    elif answers['Main'] == 'Distance':
        Time = int(input('what is the Time : '))
        Speed = int(input('what is the Speed : '))
        Answer = Time * Speed 
        print(f'The Distance is {Answer}')
    elif answers['Main'] == 'Acceleration':
        Force = int(input('what is the force : '))
        Mass = int(input('what is the Mass : '))
        Answer = Force / Mass 
        print(f'The Acceleration is {Answer}')



            