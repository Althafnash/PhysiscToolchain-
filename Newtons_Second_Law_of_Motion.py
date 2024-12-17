import inquirer

def Newtons_second_law_of_motion():
    print('F = M * A')
    print('This equation describes how the velocity of an object changes when a force is applied.')
    Newtons_second_law_of_motion = [
        inquirer.List
        (   'Main',
            message='What do you want to find',
            choices = [
                'Force',
                'mass',
                'Acceleration'
            ],
            carousel=True
        ),
    ]
    answers = inquirer.prompt(Newtons_second_law_of_motion)
    if answers['Main'] == 'Force':
        Mass = int(input('What is the Mass(m) : '))
        Acc = int(input('what is the Acceleration(a) : '))
        answer  = Mass * Acc 
        print(f'The Force is {answer}')
    elif answers['Main'] == 'mass':
        Force = int(input('what is the force : '))
        Acc = int(input('what is the Acceleration : '))
        Answer = Force / Acc 
        print(f'The Mass is {Answer}')
    elif answers['Main'] == 'Acceleration':
        Force = int(input('what is the force : '))
        Mass = int(input('what is the Mass : '))
        Answer = Force / Mass 
        print(f'The Acceleration is {Answer}')



            