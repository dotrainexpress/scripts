import time
import os
from random import randint

# Define the cls variable
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
reset = 0
while reset == 0:
    nameselect = 0
    while nameselect == 0:
        print('Please type your name:')
        myName = input()
        cls()
        if myName != '':
            print('Hi, ' + str(myName.capitalize()) + '! Let\'s do some math!')
            time.sleep(3)
            nameselect = 1
            cls()
        while myName == '':
            print('You failed to enter a name.')
            time.sleep(1)
            cls()
            print('Please type your name:')
            myName = input()
            if myName != '':
                print('Hi, ' + str(myName.capitalize()) + '! I knew you could do it! Let\'s do some math!')
                time.sleep(3)
                nameselect = 1
                cls()

    howhard = 0
    while howhard < 1:
        # Question Difficulty
        print('Please chose a level')
        print('_____________________')
        print('1) Easy')
        print('2) Medium')
        print('3) Hard')
        print('')
        levelDiff = input()
        howhard = howhard + 1

        # EASY
        if levelDiff == str(1):
            mathProblem = 1
            while mathProblem < 2: #(int(problemCount) + 1):
                print('Problem ' + str(mathProblem) + ' of 10') # + str(problemCount))
                time.sleep(1)
                var1 = randint(0,9)
                var2 = randint(0,9)
                print('\n')
                print(str(var1) + ' + ' + str(var2) + ' = ?')
                correct = var1 + var2
                answer = input()
                if int(answer) == int(correct):
                    print('That' + "'" + 's correct! ')
                    time.sleep(3)
                    cls()
                else:
                    print('Nope. Try again!')
                    print(str(var1) + ' + ' + str(var2) + ' = ?')
                    answer = input()
                    if int(answer) == int(correct):
                        print('That\'s correct! Great job!')
                        time.sleep(3)
                        cls()
                    else:
                        print('That is still incorrect. The correct answer is:')
                        print(str(var1) + ' + ' + str(var2) + ' = ' + str(correct))
                        time.sleep(6)
                        cls()
                mathProblem = mathProblem + 1
                
        # Medium
        if levelDiff == str(2):
            mathProblem = 1
            while mathProblem < 2: #(int(problemCount) + 1):
                print('Problem ' + str(mathProblem) + ' of 10') # + str(problemCount))
                time.sleep(1)
                var1 = randint(0,9)
                var2 = randint(0,9)
                print('\n')
                print(str(var1) + ' + ' + str(var2) + ' = ?')
                correct = var1 + var2
                answer = input()
                if int(answer) == int(correct):
                    print('That' + "'" + 's correct! ')
                    time.sleep(3)
                    cls()
                else:
                    print('Nope. Try again!')
                    print(str(var1) + ' + ' + str(var2) + ' = ?')
                    answer = input()
                    if int(answer) == int(correct):
                        print('That\'s correct! Great job!')
                        time.sleep(3)
                        cls()
                    else:
                        print('That is still incorrect. The correct answer is:')
                        print(str(var1) + ' + ' + str(var2) + ' = ' + str(correct))
                        time.sleep(6)
                        cls()
                mathProblem = mathProblem + 1
        
        # Hard
        if levelDiff == str(3):
            mathProblem = 1
            while mathProblem < 2: #(int(problemCount) + 1):
                print('Problem ' + str(mathProblem) + ' of 10') # + str(problemCount))
                time.sleep(1)
                var1 = randint(0,9)
                var2 = randint(0,9)
                print('\n')
                print(str(var1) + ' + ' + str(var2) + ' = ?')
                correct = var1 + var2
                answer = input()
                if int(answer) == int(correct):
                    print('That' + "'" + 's correct! ')
                    time.sleep(3)
                    cls()
                else:
                    print('Nope. Try again!')
                    print(str(var1) + ' + ' + str(var2) + ' = ?')
                    answer = input()
                    if int(answer) == int(correct):
                        print('That\'s correct! Great job!')
                        time.sleep(3)
                        cls()
                    else:
                        print('That is still incorrect. The correct answer is:')
                        print(str(var1) + ' + ' + str(var2) + ' = ' + str(correct))
                        time.sleep(6)
                        cls()
                mathProblem = mathProblem + 1
        else:
            print('Please select a number from the menu')
            time.sleep(1)
            cls()
        howhard = 0

    print('Great job, ' + str(myName.capitalize()) + '!')
    time.sleep(2)
    print('Shall we play again?')
    print('1) Yes')
    print('2) No')
    print('')
    yesorno = input()

    if yesorno == str(1):
        print('Okay, here we go!')
        time.sleep(2)
        cls()
        howhard = 0

    if yesorno == str(2):
        cls()
        print('Resetting Program. Please wait.')
        time.sleep(1)
        cls()
        print('Resetting Program. Please wait..')
        time.sleep(1)
        cls()
        print('Resetting Program. Please wait...')
        time.sleep(1)
        cls()
        print('Resetting Program. Please wait....')
        time.sleep(1)
        cls()
        print('Resetting Program. Please wait.....')
        time.sleep(1)
        cls()
        reset = 0
        break

