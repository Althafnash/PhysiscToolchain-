import inquirer

def PotentialEnegry ():
    print('U = mgh')
    print('This equation calculates the potential enegry of a object.')
    PotentialEnegry = [
        inquirer.List
        (   'Main',
            message='What do you want to find',
            choices = [
                'PotentialEnergy',
                'Mass',
                'Gravity',
                'Height'
            ],
            carousel=True
        ),
    ]
    answers = inquirer.prompt(PotentialEnegry)
    if answers['Main'] == 'PotentialEnegry':
        Mass = int(input('What is the Mass : '))
        Gravity = int(input('what is the Gravity : '))
        Height = int(input('what is the Height : '))
        answer  = Mass * Gravity * Height
        print(f'The Kinetic Enegry is {answer}')
    elif answers['Main'] == 'Mass':
        PotentialEnegry = int(input('what is the PotentialEnegry : '))
        Gravity = int(input('what is the Gravity : '))
        Height = int(input('what is the Height : '))
        Answer = PotentialEnegry / Gravity * Height
        print(f'The Mass is {Answer}')
    elif answers['Main'] == 'Gravity':
        PotentialEnegry = int(input('what is the PotentialEnegry : '))
        Mass = int(input('what is the Mass : '))
        Height = int(input('what is the Height : '))
        Answer = PotentialEnegry / Mass  * Height
        print(f'The Gravity is {Answer}')
    elif answers['Main'] == 'Height':
        PotentialEnegry = int(input('what is the PotentialEnegry : '))
        Mass = int(input('what is the Mass : '))
        Gravity = int(input('what is the Gravity : '))
        Answer = PotentialEnegry / Mass  * Gravity
        print(f'The Height is {Answer}')



            