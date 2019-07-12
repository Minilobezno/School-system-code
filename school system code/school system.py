
#beggining 2865
#end 13317

import random
import datetime,os
import time
from time import sleep
import operator
import csv
from operator import itemgetter
from tkinter import *


def Games():
    GamesText="""
****************************
*         Games            *
****************************
* Please select an option  *
* 1. Mathsquiz             * 
* 2. Songsquiz             *
* 3. Videogames quiz       *
* 4. Snakes and ladders    *
* 5. TicTacToe             *
* 6. Rock, Paper, Scissors *
* 7. Hangman               *
* 8. Guess the number      *
* 9. Adventure             *
* 10.Back                  * 
****************************"""

    choice=valMenu(GamesText, ["1","2","3","4","5","6","7","8","9","10","11"])
    if choice=="1":
        Mathsquiz()
    elif choice=="2":
        Songsquiz()
    elif choice=="3":
        VideogamesQuiz()
    elif choice=="4":
        SnakesAndLadders()
    elif choice=="5":
        TicTacToe()
    elif choice=="6":
        RockPaerScissors()
    elif choice=="7":
        Hangman()
    elif choice=="8":
        GuessTheNumber()
    elif choice=="9":
        Adventure()
    elif choice=="10":
        mainMenu()
    return Games() #loop back to mainMenu


#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------


def Mathsquiz():
    QuizMenuText="""
****************************
*          MATHSQUIZ       *
****************************
* Please select an option  *
* 1. Start quiz            *
* 2. Scores                *
* 3. Delete info           *
* 4. Update info           * 
* 5. Back                  *
****************************"""

    print(QuizMenuText)
    #Option 1----------------------------------------------------------------------------------------------------------
    selection=int(input("select an option: "))


    if selection==1:
    #Start quiz
        print("You chosed option 1\n------------------------------------------------------------------\nMaths Quiz")
        Name = input("Enter your Name:")
        score = 0
        operators = [('+', operator.add),('-', operator.sub),('*', operator.mul),('/', operator.floordiv)]

        for i in range(1,11):
            a = random.randint(1,100)
            b = random.randint(1,20)
            op, fn = random.choice(operators)
            print("Question",i)
            question = "What is {} {} {}?\n".format(a, op, b)
            if int(input(question)) == fn(a,b):
                score += 1
                print("Correct")
            else:
                print("incorrect")
            
        print("Great effort",Name,",you had {} questions right".format(score))


        output_file=open("Quizresults.txt","a")
        output_file.write(Name+"\n")
        output_file.write(str(score)+"\n")
        output_file.close()
        return Mathsquiz()






    #Option 2----------------------------------------------------------------------------------------------------------

    elif selection==2:
    #Option used to find the score and display it and password section    
        print("For this option you need sign in\n-------------------------------------------------------------")
        user_name = input("Enter the user name:")
        password = input("Password:")
        count = 0
        count += 1

        while user_name == user_name and password == password:
            
            if count == 3:
                print("Username and password not valid\nNo more attempts left.\nFor security reasons you will be signed out.")
                break

            elif user_name == "Teacher2019" and password == "MathMagician":
                print("Logged in")
                print("You chosed option 2\n------------------------------------------------------------------")
                found=False
                input_file=open("Quizresults.txt","r")
                data=input_file.read().splitlines()
                input_file.close()
                search=input("Enter your name:")
                position=0
                while not found and position<len(data)-1:
                    if data[position]==search:
                        print("Item found")
                        print(search," score is ", data[position+1])
                        found=True
                    else:
                        position=position+2
                if not found:
                    print("Name not in list")
                break
        
            elif user_name != "Teacher2019" and password != "MathMagician":
                print("Username and password not valid")
                user_name = input("\nEnter the username:")
                password = input("Password:")
                count += 1
                continue
            else:
                print("Username and password not valid\nNo more attempts left.\nFor security reasons you will be signed out.")
                break
        return Mathsquiz()



    #Option 3----------------------------------------------------------------------------------------------------------

    elif selection==3:
        
    #Code used to delete names and score and password section
        print("For this option you need sign in\n-------------------------------------------------------------")
        user_name = input("Enter the user name:")
        password = input("Password:")
        count = 0
        count += 1

        while user_name == user_name and password == password:
            
            if count == 3:
                print("Username and password not valid\nNo more attempts left.\nFor security reasons you will be signed out.")
                break

            elif user_name == "Teacher2019" and password == "MathMagician":
                print("Logged in")
                print("You chosed option 3\n------------------------------------------------------------------")
                found= False
                input_file=open("Quizresults.txt","r")
                data=input_file.read().splitlines()
                input_file.close
                search=input("Enter the name you are deleting: ")
                position=0
                while not found and position<=len(data)-1:
                    if data[position]==search:
                        output_file=open("Quizresults.txt","w")
                        del(data[position])
                        del(data[position])
                        for item in data:
                            output_file.write(item+"\n")
                        print(search,"has been deleted")
                        output_file.close()
                        found=True
                    else:
                        position=position+2
                if not found:
                    print("Name not on the list")
                break
        
            elif user_name != "Teacher2019" and password != "MathMagician":
                print("Username and password not valid")
                user_name = input("\nEnter theuser name:")
                password = input("Password:")
                count += 1
                continue
            else:
                print("Username and password not valid\nNo more attempts left.\nFor security reasons you will be signed out.")
                break
        return Mathsquiz()
        





    #Option 4----------------------------------------------------------------------------------------------------------

    elif selection==4:

    #Code used to update the scores and password  
        print("For this option you need sign in\n-------------------------------------------------------------")
        user_name = input("Enter the user name:")
        password = input("Password:")
        count = 0
        count += 1

        while user_name == user_name and password == password:
            
            if count == 3:
                print("Username and password not valid\nNo more attempts left.\nFor security reasons you will be signed out.")
                break

            elif user_name == "Teacher2019" and password == "MathMagician":
                print("Logged in")
                print("You chosed option 4\n-------------------------------------------------------------------")
                found=False
                input_file=open("Quizresults.txt","r")
                data=input_file.read().splitlines()
                input_file.close
                search=input("Enter the name you are looking for: ")
                newScore=input("Enter new score: ")
                position=0
                while not found and position<=len(data)-1:
                    if data[position]==search:
                        print(search," original score is ", data[position+1])
                        output_file=open("Quizresults.txt","w")
                        data[position+2]=newScore
                        for item in data:
                            output_file.write(item+"\n")
                        print(search,"new score is ", data[position+1])
                        output_file.close()
                        found=True
                    else:
                        position=position+2
                if not found:
                    print("Name not on the list")

                else:
                    print("Unavailible")
                break
        
            elif user_name != "Teacher2019" and password != "MathMagician":
                 print("Username and password not valid")
                 user_name = input("\nEnter theuser name:")
                 password = input("Password:")
                 count += 1
                 continue
            else:
                print("Username and password not valid\nNo more attempts left.\nFor security reasons you will be signed out.")
                break

        return Mathsquiz()  

    elif selection==5:
        return Games()
    
    else:
        print("That isn't an option")














        
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------



def Songsquiz():
    user = input("Welcome ,you need to enter your details to be able to play the quiz\nEnter any button to continue\n--------------------------------------------------------------------")
    start = time.time()


    def Name():
            return Quiz()
            
            

    def Quiz():
            global name
            global attempts
            attempts = 0
            name = input("Enter your name:")

            if len(name)>=3:
            #Quiz
                    global score
                    print("Logged in")           
                    print("Loading , please wait...\n------------------------------------------------------------------")
                    time.sleep(1)
                    global count
                    count = 0
                    global score
                    score = 0

            else:
                return Name()

    def question():
            global count
            count=0
            count+=1
            print("The quiz will now start.\n------------------------------------------------------------------\nREMEMBER ALL ANSWERS MUST BE IN CAPITAL LETTERS\n------------------------------------------------------------------")
            input_file=open("Songsquiz.txt","r")
            data=input_file.read().splitlines()
            new_line = random.choice(data)
            input_file.close()
            randomposition = random.randrange(0,40,2)
            position= 0
            position=randomposition
            global song
            song=(data[position])
            artist=(data[position+1])
            time.sleep(4)
            print("Artist:\n"+artist)
            print("First letter of each word in the song title:")
            thelist=song.split()
            for word in thelist:
                print(word[0])
                
            print("------------------------------------------------------------------")    
            intento()


    def endQuiz():
            end = time.time()
            spent = end-start
            newscore = score
            new_file=open("Scores.txt","a")
            new_file.write("{},{},{} seconds\n".format(newscore, name, int(spent)))
            new_file.close()
            print("\nOk, "+name+", you scored",newscore)
    #ALL SCORES
            print("Here are the top five scores: \n")
            with open("Scores.txt") as file:
                csv_reader = csv.reader(file)
                sorted_list=sorted(csv_reader, key=lambda row: int(row[0]), reverse=True)
            print(" points/ ".join(sorted_list[0]))
            print(" points/ ".join(sorted_list[1]))
            print(" points/ ".join(sorted_list[2]))
            print(" points/ ".join(sorted_list[3]))
            print(" points/ ".join(sorted_list[4]))
            return Games()
        
    def intento():
            global song_guess
            global attempts
            global score
            song_guess = input("Enter the song name:")

            if song_guess == song and attempts == 0:
                    print("Well done, you got 3 points")
                    score+=3
                    print("Points:",score)
                    print("Attempts failed:",attempts)
                    return question()
                                                                                          
            elif song_guess != song and attempts == 0:
                    attempts=attempts+1
                    print("Incorrect")
                    print("Attempts failed:",attempts)
                    return question()
            
            elif song_guess != song and attempts == 1:
                    attempts=attempts+1
                    print("Incorrect")
                    print("Attempts failed:",attempts)
                    print("No more attempts left")
                    return endQuiz()


            if song_guess == song and attempts == 1:
                    print("Well done, you got 1 point")
                    score+=1
                    print("Points:",score)
                    print("Attempts failed:",attempts)
                    return question()

                                                        


    Quiz()
    question()





#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------

def VideogamesQuiz():

    YES = ['y', 'Y', 'yes', 'Yes', 'YES']
    NO = ['n', 'N', 'no', 'No', 'NO']
    CLEAR = ['c', 'C', 'clear', 'Clear', 'CLEAR']
    QUIT = ['q', 'Q', 'quit', 'Quit', 'QUIT']
    MULTIPLECHOICE = ['a', 'b', 'c', 'd']


    class QuizGame:
        '''  repository of methods to do with QuizGame
             -  get_username
             -  play_loop
             -  ask_play_again
             -  escape_quiz
             -  play_quiz
             -  read_highscores
             -  write_highscores
             -  clear_highscores
             -  display_highscores
        '''
        questions = \
            {1: ('What was the first video game ever made?',
                 'a)  God of War 9\nb)  Pacman \nc)  Pong \nd)  Tennis for Two',
                 'd'),

             2: ('What was the most expensive video game to ever be developed?',
                 'a)  Destiny\nb)  Call of Duty: Modern Warfare 2  \n'
                 'c)  Grand Theft Auto: V  \nd)  Disney Infinity',
                 'b'),

             3: ('What amount of time a day does the average gamer (In the US, '
                 'age 13 or older) spend gaming?',
                 'a)  54 minutes\nb)  25 hours\nc)  2 hours\nd)  30 minutes',
                 'a'),

             4: ('Who is the founder of Nintendo?',
                 'a)  Fusajiro Yamauchi\nb)  Bob Dylan\nc)  Steve Bovaird\n'
                 'd)  Nihonjin no Shimei',
                 'a'),

             5: ('What was the most purchased game of 2017?',
                 'a)  Jesus sim\nb)  Farming Simulator 2017\n'
                 'c)  Call of Duty: WWII\nd)  Destiny 2',
                 'c'),

             6: ('When was E3 [Electronic Entertainment Expo] 2017?',
                 'a)  13 Jun 2017 - 15 Jun 2017\nb)  13 Jun 2017 - 14 Jun 2017\n'
                 'c)  15 July 2017 - 13 July 2017\nd)  10 Jun 2017 - 18 Jun 2017',
                 'a'),

             7: ('What was the most popular console of 2010?',
                 'a)  Xbox 360\nb)  PlayStation 3\nc)  Xbox 1\nd)  PlayStation 4',
                 'a'),

             8: ('Who was the most subscribed gaming youtuber of 2012?',
                 'a)  PrettyL8r\nb)  Pewdiepie\nc)  Greg\nd)  NotGreg',
                 'b'),

             9: ('Who won the Game of The Year award 2016?',
                 'a)  Overwatch\nb)  Treyarch\nc)  Blizzard\n'
                 'd)  Rainbow Six Siege',
                 'c'),

             10: ('When did DOOM release?',
                  'a)  December 10, 1993\nb)  February 23, 1995\n'
                  'c)  January 32, 20019\nd)  Yesterday',
                  'a'), }

        welcometext =\
            '\nHello {}, welcome to The Videogame Quiz'\
            '\nIn this quiz, you will be asked 10 questions about videogames.'\
            '\nTry your best to answer all 10 correctly. Enter a, b, c or d '\
            '\ndepending on which answer you think is right\n'

        users = {}
        score = 0
        highscore_file = 'highscore.log'

        @classmethod
        def get_username(cls):
            '''  method to ask user for user_name, if user name is Quit then leave.
                 Dictionary of cls.users is checked on existing users. If user
                 does not exist he/ she is added.
            '''
            user_name = ''
            quit = False
            while len(user_name) < 4 and not quit:
                user_name = input('Hello! What is your name [enter Quit '
                                  'to leave]: ').strip().capitalize()
                if user_name in QUIT:
                    quit = True

            if not quit:
                if user_name not in cls.users:
                    cls.users.update({user_name: 0})
                    cls.highscore = 0

                print(cls.welcometext.format(user_name))

            return user_name, quit

        @classmethod
        def play_loop(cls, user_name):
            '''  method to control loop of the quiz, update highscore, and ask
                 to play again or not
            '''
            playagain = True
            while playagain:
                print("\n"+user_name+", your current highscore is ",{cls.users[user_name]},".\n")

                if cls.escape_quiz():
                    break

                score = cls.play_quiz()

                if score > cls.users[user_name]:
                    cls.users.update({user_name: score})

                playagain = cls.play_again()

        @staticmethod
        def play_again():
            '''   ask player if he/ she wants to play quiz again
            '''
            answered = False
            while not answered:
                answer = input('Do you want to take the quiz again? Y or N: ')
                answered = True

                if answer in YES:
                    playagain = True

                elif answer in NO:
                    return Games()

                else:
                    answered = False

            return playagain

        @staticmethod
        def escape_quiz():
            '''  ask player twice if he/ she is ready to continue
            '''
            answered = 0
            question = '\nAre you ready to continue? Y or N? '
            while answered < 2:
                answer = input(question)
                print('---------------------------------------')
                answered += 1

                if answer in YES:
                    escape_the_quiz = False
                    break

                elif answer in NO:
                    escape_the_quiz = True
                    for i in range(3):
                        print('Oh... ok')
                        time.sleep(0.5)
                    question = '\nNow are you ready to continue? Y or N '

                else:
                    print('Yes or no only please!')

            return escape_the_quiz

        @classmethod
        def play_quiz(cls):
            '''  core of quiz asking multiple choice questions. Player can leave
                 by entering quit
            '''
            questions = cls.questions.copy()
            question_choice = {i for i in range(1, len(questions)+1)}
            score = 0
            question_nr = 1

            while questions:
                question = random.sample(question_choice, 1)[0]
                answered = False

                print("Question: ",{question_nr}," of ",{len(cls.questions)})
                print(questions[question][0])
                print(questions[question][1])
                question_nr += 1

                answered = False
                while not answered:
                    answer = input('What is your answer?: ').lower()

                    if answer in (MULTIPLECHOICE + QUIT):
                        answered = True

                    else:
                        print('ERROR, please input a, b, c or d only please!')

                if answer in QUIT:
                    break

                elif answer == questions[question][2]:
                    print('Good job! You are correct.\n')
                    score += 1

                else:
                    print('Unfortunately that is not correct! '
                          'Better luck next time.\n')

                questions.pop(question)
                question_choice.remove(question)

            print("Your score is >>> ",{score})

            return score

        @classmethod
        def read_highscores(cls):
            '''  read highscores from cls.highscore_file
            '''
            try:
                with open(cls.highscore_file, 'r') as highscores:
                    for line in highscores:
                        user_name, score = line.split(':')
                        cls.users[user_name.strip()] = int(score)

            except Exception as e:
                print('Error in log file, must be format <name: score>')

        @classmethod
        def write_highscores(cls):
            '''  write highscores to cls.highscore_file
            '''
            try:
                with open(cls.highscore_file, 'w') as highscores:
                    for name in cls.users:
                        highscores.write('{}: {}\n'.
                                         format(name, str(cls.users[name])))

            except Exception as e:
                print('Error in log file, must be format <name: score>')

        @classmethod
        def clear_highscores(cls):
            '''  clears the highscore file if confirmed by typing 'CLEAR'
            '''
            answer = input('\nDo you want to clear the scores log, '
                           'type \'CLEAR\' ')

            if answer == 'CLEAR':
                with open(cls.highscore_file, 'w') as highscores:
                    highscores.write('')

        @classmethod
        def display_highscores(cls):
            '''  displays highscores in order from high to low
            '''
            print('\nHighscores')
            print('-'*40)
            print('{:20}{}'.format('Name', 'Score'))
            print('-'*40)

            sorted_output = sorted(QuizGame.users.items(), key=lambda v: v[1],
                                   reverse=True)
            for line in sorted_output:
                print("{line[0]:20}{line[1]}")


    def main():
        '''  starts the program
        '''
        QuizGame.read_highscores()
        QuizGame.display_highscores()
        quit = False

        while not quit:
            user_name, quit = QuizGame.get_username()
            if not quit:
                QuizGame.play_loop(user_name)

        QuizGame.display_highscores()
        QuizGame.write_highscores()
        QuizGame.clear_highscores()


    if __name__ == '__main__':
        main()


#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------



def SnakesAndLadders():
    print("You need two players to play this game")
    board=[[y+(x*7)+1 for y in range(7)] for x in range(7)]

    #update to read from file
    file=open("gameMessages.txt", "r")
    messages=file.readlines()
    file.close()

    obstacleKeys={}
    #messages=["Welcome to snakes and ladders", "You rolled a double", "Winner winner, chicken dinner"]



    def valInput(message, minlength=1):
        val=input(message)
        while len(val)< minlength:
            print("ERROR: You must type at least ", minlength, "character(s)")
            val=input(message)

        return val

    def fill(var, size):
        var=str(var)
        while len(var)<size:
            var+=" "
        return var

    def printBoard():
        #find longest counter to set fill for board
        maxlen=2
        for row in board:
            for col in row:
                if len(str(col))>maxlen:
                    maxlen=len(str(col))

        
        for rowNum in range(len(board)-1,-1,-1):
            if rowNum%2==0:
                for colNum in range(len(board[rowNum])):
                    print("|",fill(board[rowNum][colNum],maxlen), end="")
            else:
                for colNum in range(len(board[rowNum])-1,-1,-1):            
                     print("|",fill(board[rowNum][colNum],maxlen), end="")
            print("|\n")

    def loadObstacles():
        file=open("obstacles.txt", "r")
        #obstacles stored on seperate lines in the format Pos,Code,Move e.g. 48,S,-6

        obstacleArr=file.readlines()
        file.close()

        for obstacle in obstacleArr:
            obsDetails=obstacle.split(",")

            pos=int(obsDetails[0])-1
            board[pos//7][pos%7]=obsDetails[1]

            #store in dictionary so we know how it impacts the game.
            obstacleKeys[obsDetails[1]]=int(obsDetails[2])        
            
            
    def roll():
        return random.randint(1,6)

    def takeTurn(pos, counter):
        input("press enter to roll")
        d1=roll()
        d2=roll()

        #remove counter from current position
        if board[pos//7][pos%7]==counter:
            board[pos//7][pos%7]=pos+1
        #both counters here so just remove player counter
        else:
            print("Trying to replace: ",board[pos//7][pos%7])
            board[pos//7][pos%7]=board[pos//7][pos%7].replace(counter, "")
        
            
        if d1==d2:
            print(messages[1])#rolled a double
            print("You will move back", d1+d2, "places")
            pos-=(d1+d2)
        else:
            print("you rolled a", d1,"and a",d2, "you will move ", d1+d2, "places")
            pos+=d1+d2

        if pos<0:
            print("oh dear, back to the start")
            pos=0
        elif pos>48:
            pos=48 #stop the player leaving the board

        
        if board[pos//7][pos%7] in obstacleKeys:
            obstaclemove=obstacleKeys[board[pos//7][pos%7]]
            if obstaclemove<0:
                print("You hit an obstacle it will move you back by ", abs(obstaclemove))
            else:
                print("You hit a shortcut it will move you forward by ", obstaclemove)

            pos+=obstaclemove        

        if board[pos//7][pos%7]==pos+1:
            board[pos//7][pos%7]=counter
        #both counters here so just remove player counter
        else:
            board[pos//7][pos%7]=board[pos//7][pos%7]+counter

        return pos
        
        
    def play():
        
        print(messages[0])

        loadObstacles()
        
        p1name=valInput("Player 1 Name: ")
        p2name=valInput("Player 2 Name: ")

        i=0
        p1pos=0
        p2pos=0

        board[0][0]="P1 P2 "
        printBoard()

        winner=False
        while not winner:
            if i%2==0:
                print(p1name,"it's your go, you are p1:")
                p1pos=takeTurn(p1pos, "P1 ")

                if p1pos>=48:
                    print(messages[2])
                    break
            else:
                print(p2name,"it's your go, you are p2:")
                p2pos=takeTurn(p2pos, "P2 ")
            
                if p2pos>=48:
                    print(messages[2])
                    break    
            
            printBoard()
            i+=1



        print("GAME OVER")

    play()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------


def TicTacToe():
    TicTacToeText="""
****************************
*         TicTacToe        *
****************************
* Please select an option  *
* 1. One Player            * 
* 2. Two Players           *
* 3. Back                  *
****************************"""

    choice=valMenu(TicTacToeText, ["1","2","3","4","5","6"])
    if choice=="1":
        print("Number panel,(Use for reference):")
        print("7 | 8 | 9")
        print("4 | 5 | 6")
        print("1 | 2 | 3")
        TicTacToeOnePlayer()
    elif choice=="2":
        TicTacToeTwoPlayers()
    elif choice=="3":
        Games()
    return TicTacToe() #loop back to mainMenu







#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------





def TicTacToeTwoPlayers():
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    # Lets us know if the game is over yet
    global game_still_going
    game_still_going = True


    global winner
    winner = None

    # Tells us who the current player is (X goes first)
    global current_player
    current_player = "X"


    # ------------- Functions ---------------

    # Play a game of tic tac toe
    def play_game():

      # Show the initial game board
      display_board()

      # Loop until the game stops (winner or tie)
      while game_still_going:

        # Handle a turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()
      
      # Since the game is over, print the winner or tie
      if winner == "X" or winner == "O":
        print(winner + " won.")
      elif winner == None:
        print("Tie.")


    # Display the game board to the screen
    def display_board():
      print("\n")
      print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
      print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
      print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
      print("\n")


    # Handle a turn for an arbitrary player
    def handle_turn(player):

      # Get position from player
      print(player + "'s turn.")
      position = input("Choose a position from 1-9: ")

      # Whatever the user inputs, make sure it is a valid input, and the spot is open
      valid = False
      while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
          position = input("Choose a position from 1-9: ")
     
        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
          valid = True
        else:
          print("You can't go there. Go again.")

      # Put the game piece on the board
      board[position] = player

      # Show the game board
      display_board()


    # Check if the game is over
    def check_if_game_over():
      check_for_winner()
      check_for_tie()


    # Check to see if somebody has won
    def check_for_winner():
      # Set global variables
      global winner
      # Check if there was a winner anywhere
      row_winner = check_rows()
      column_winner = check_columns()
      diagonal_winner = check_diagonals()
      # Get the winner
      if row_winner:
        winner = row_winner
      elif column_winner:
        winner = column_winner
      elif diagonal_winner:
        winner = diagonal_winner
      else:
        winner = None


    # Check the rows for a win
    def check_rows():
      # Set global variables
      global game_still_going
      # Check if any of the rows have all the same value (and is not empty)
      row_1 = board[0] == board[1] == board[2] != "-"
      row_2 = board[3] == board[4] == board[5] != "-"
      row_3 = board[6] == board[7] == board[8] != "-"
      # If any row does have a match, flag that there is a win
      if row_1 or row_2 or row_3:
        game_still_going = False
      # Return the winner
      if row_1:
        return board[0] 
      elif row_2:
        return board[3] 
      elif row_3:
        return board[6] 
      # Or return None if there was no winner
      else:
        return None


    # Check the columns for a win
    def check_columns():
      # Set global variables
      global game_still_going
      # Check if any of the columns have all the same value (and is not empty)
      column_1 = board[0] == board[3] == board[6] != "-"
      column_2 = board[1] == board[4] == board[7] != "-"
      column_3 = board[2] == board[5] == board[8] != "-"
      # If any row does have a match, flag that there is a win
      if column_1 or column_2 or column_3:
        game_still_going = False
      # Return the winner
      if column_1:
        return board[0] 
      elif column_2:
        return board[1] 
      elif column_3:
        return board[2] 
      # Or return None if there was no winner
      else:
        return None


    # Check the diagonals for a win
    def check_diagonals():
      # Set global variables
      global game_still_going
      # Check if any of the columns have all the same value (and is not empty)
      diagonal_1 = board[0] == board[4] == board[8] != "-"
      diagonal_2 = board[2] == board[4] == board[6] != "-"
      # If any row does have a match, flag that there is a win
      if diagonal_1 or diagonal_2:
        game_still_going = False
      # Return the winner
      if diagonal_1:
        return board[0] 
      elif diagonal_2:
        return board[2]
      # Or return None if there was no winner
      else:
        return None


    # Check if there is a tie
    def check_for_tie():
      # Set global variables
      global game_still_going
      # If board is full
      if "-" not in board:
        game_still_going = False
        return True
      # Else there is no tie
      else:
        return False


    # Flip the current player from X to O, or O to X
    def flip_player():
      # Global variables we need
      global current_player
      # If the current player was X, make it O
      if current_player == "X":
        current_player = "O"
      # Or if the current player was O, make it X
      elif current_player == "O":
        current_player = "X"


    # ------------ Start Execution -------------
    # Play a game of tic tac toe
    play_game()



#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------



def TicTacToeOnePlayer():
    def drawBoard(board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def inputPlayerLetter():
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst():
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def playAgain():
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(board, letter, move):
        board[move] = letter

    def isWinner(bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def getBoardCopy(board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getPlayerMove(board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(board, computerLetter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, computerLetter, i)
                if isWinner(copy, computerLetter):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, playerLetter, i)
                if isWinner(copy, playerLetter):
                    return i

        # Try to take one of the corners, if they are free.
        move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if isSpaceFree(board, 5):
            return 5

        # Move on one of the sides.
        return chooseRandomMoveFromList(board, [2, 4, 6, 8])

    def isBoardFull(board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True


    print('Welcome to Tic Tac Toe!')

    while True:
        # Reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                # Player's turn.
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'

            else:
                # Computer's turn.
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

        if not playAgain():
            break





#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------


def RockPaerScissors():
    sus="-"*35
    depo=["rock","paper","scissors"]
    while True:
        x=input("rock , paper, scissors: ")
        if x not in depo:
            print ("Dont cheat!")
            question=input("Do you want to exit?\nY/N")
            if question=="N":
                continue
            elif question=="Y":
                return Games()
            

        pc=random.choice(depo)
        sleep(0.5)
        print (("Computer picked {}.").format(pc))
        if x==pc:
            sleep(0.5)
            print (("\nIt's a draw.\n{}").format(sus))
        elif x=="rock" and pc=="scissors":
            sleep(0.5)
            print (("\nYou win.rock beats scissors\n{}").format(sus))
        elif x=="paper" and pc=="rock":
            sleep(0.5)
            print (("\nYou win.paper beats rock\n{}").format(sus))
        elif x=="scissors" and pc=="paper":
            sleep(0.5)
            print (("\nYou win.scissors beats paper\n{}").format(sus))
        else:
            sleep(0.5)
            print (("\nYou lose. {} beats {}\n{}").format(pc,x,sus))
    input()


#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------


def Hangman():
    board = [
    '  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |   \n========= \n'
    ]

    class Hangman:
            def __init__(self,word):
                    self.word = word
                    self.missed_letters = []
                    self.guessed_letters = []
                    
            def guess(self,letter):
                    if letter in self.word and letter not in self.guessed_letters:
                            self.guessed_letters.append(letter)
                    elif letter not in self.word and letter not in self.missed_letters:
                            self.missed_letters.append(letter)
                    else:
                            return False
                    return True
                    
            def hangman_over(self):
                    return self.hangman_won() or (len(self.missed_letters) == 6)
                    
            def hangman_won(self):
                    if '_' not in self.hide_word():
                            return True
                    return False
                    
            def hide_word(self):
                    rtn = ''
                    for letter in self.word:
                            if letter not in self.guessed_letters:
                                    rtn += '_'
                            else:
                                    rtn += letter
                    return rtn
                    
            def print_game_status(self):
                    print(board[len(self.missed_letters)])
                    print('Word: ' + self.hide_word())
                    print('Letters Missed: ',)
                    for letter in self.missed_letters:
                            print(letter,) 
                    print 
                    print('Letters Guessed: ',)
                    for letter in self.guessed_letters:
                            print (letter,)
                    print 

    def rand_word():
            
            bank = ['the','living','pearl','.com','captain','deadbones']
            return bank[random.randint(0,len(bank))]

    def main():
            
            game = Hangman(rand_word())
            while not game.hangman_over():
                    game.print_game_status()
                    user_input = input('\nEnter a letter: ')
                    game.guess(user_input)

            game.print_game_status()	
            if game.hangman_won():
                    print('\nCongratulations! You are the winner of Hangman!')
            else:
                    print('\nSorry, you have lost in the game of Hangman...')
                    print('The word was ' + game.word)
                    
            print('\nGoodbye!\n')
                    
    if __name__ == "__main__":
            main()



def GuessTheNumber():
    GuessTheNumberText="""
****************************
*     Guess the number     *
****************************
* Please select an option  *
* 1. You guess the number  * 
* 2. Computer guesses num  *
* 3. Back                  * 
****************************"""

    choice=valMenu(GuessTheNumberText, ["1","2","3"])
    if choice=="1":
        YouGuessTheNumber()
    elif choice=="2":
        ComputerGuessTheNumber()
    elif choice=="3":
        Games()
    return GuessTheNumber() #loop back to mainMenu

def YouGuessTheNumber():
    number = random.randint(0,101)
    def Guess():
        guess = int(input("Welcome, enter your guess from 1 to 100: "))
        while guess != number:
            if guess>number:  
                print("Too high, go lower! ")
                return Guess()
            elif guess<number:            
                print("Too low, go higher! ")
                return Guess()
        else:
            print("Well done!")


    Guess()


def ComputerGuessTheNumber():
        __author__ = 'Benoit'
    #Computer attempts to guess a number you choose between 1 and 100 in 10 tries
        answer =('yes')
        print ("Please, think of a number between 1 and 100. I am about to try to guess it in 10 tries.")
        while answer == "yes":
            NumOfTry = 10
            NumToGuess = 50
            LimitLow = 1
            LimitHigh = 100
            while NumOfTry != 0:
                try:
                    print ("I try: ",NumToGuess)
                    print ("Please type: 1 for my try is too high")
                    print ("             2 for my try is too low")
                    print ("             3 I guessed your number")
                    HumanAnswer  = int (input("So did I guess right?"))
                    if 1 < HumanAnswer > 3:
                        print ("Please enter a valid answer. 1, 2 and 3 are the valid choice")
                        NumOfTry = NumOfTry + 1
                    if HumanAnswer == 1:
                        LimitHigh = NumToGuess
                        print ("Hmm, so your number is between ",LimitLow, "and ", LimitHigh)
                        NumOfTry = NumOfTry - 1
                        print (NumOfTry, "attempts left")
                        NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                        if NumToGuess <= LimitLow:
                            NumToGuess = NumToGuess + 1
                        if LimitHigh - LimitLow == 2:
                            NumToGuess = LimitLow + 1
                    elif HumanAnswer == 2:
                        LimitLow = NumToGuess
                        print ("Hmm, so your number is between ",LimitLow, "and ", LimitHigh)
                        NumOfTry = NumOfTry - 1
                        print (NumOfTry, "attempts left")
                        NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                        if NumToGuess <= LimitLow:
                            NumToGuess = NumToGuess + 1
                        if LimitHigh - LimitLow == 2:
                            NumToGuess = LimitLow + 1
                    elif HumanAnswer == 3:
                        print ("Woo hoo! I won")
                        NumOfTry = 0
                except:
                    break
            else:
                answer = input ('Do you want to play again? (yes/no)')

        else:
            print ("Thank you for playing. Goodbye")

def Adventure():
    AdventureText="""
****************************
*         Adventure        *
****************************
* Please select an option  *
* 1. Droids                *
* 2. Survival              *
* 3. Back                  * 
****************************"""

    choice=valMenu(AdventureText, ["1","2","3"])
    if choice=="1":
        Droids()
    elif choice=="2":
        Survival()
    elif choice=="3":
        Games()
    return Games() #loop back to mainMenu



def Droids():
    import time
    import random
    from random import randint

    print('\n' * 110)
    print('=============================')
    print('          DROIDS')
    print('=============================')

    time.sleep(2) 
    print('\nCMBT645 Re-Boot Sequence..')
    time.sleep(1)
    print('\nInitalizing Combat Droid 645..')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('\nTwin laser offline..')
    time.sleep(1)
    print('Motion tracker offline..')
    time.sleep(1)
    print('Disruptor offline..')
    time.sleep(1)
    print('\nService port avaliable..')
    time.sleep(1)
    print('\nNo Software Installed..')
    time.sleep(1)
    print('\nCombat Droid active')
    time.sleep(1)
    print('\nCMBT645 ONLINE >> ')
    time.sleep(2)
    print('''\n\nYou are the 645 Combat Droid aboard 
    the Droid Cruiser PROXY. Enemy droids have boarded
    and have taken over flight path. You are damaged & have been 
    re-initialized but your Twin laser , Disruptor
    and Motion Tracker are offline.''')

    def start(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('\n[-MAIN ELEVATOR-]')
            print('\n1.)   deck 1  - Cargo Hold')
            print('2.)   deck 2  - Docking') 
            print('3.)   deck 3  - Droid Hangar')
            print('4.)   deck 4  - Security')
            print('5.)   deck 5  - Re-Charge')
            print('6.)   deck 6  - Power Core')
            print('7.)   deck 7  - Shield Generator')
            print('8.)   deck 8  - Cruiser Control')
            print('9.)   deck 9  - Observation')
            print('10.)  deck 10 - Droid Software System')
            cmdlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                    if 'PBE111' in droids:
                            print('\n- DECK 1 SECURED - ACCESS LOCKED -')
                            time.sleep(2)
                            start(armory, programs, droids)
                    else:
                            cargo_hold(armory, programs, droids)
            elif cmd == '2':
                    if 'zx4e9q' not in programs:
                            print('\n<< MEECDT1000 DROID OVER-RIDE - ACCESS DENIED >>')
                            time.sleep(2)
                            start(armory, programs, droids)
                    else:
                            docking(armory, programs, droids)
            elif cmd == '3':
                    if 'CMBT646' in droids and 'CMBT647' in droids:
                            print('\n- DECK 3 SECURED - ACCESS LOCKED -')
                            time.sleep(2)
                            start(armory, programs, droids)
                    else:
                            droid_hangar(armory, programs, droids)
            elif cmd == '4':
                    if 'MEECDT1000' in programs and 'zx4e9q' in programs:
                            print('\n- DECK 4 SECURED - ACCESS LOCKED -')
                            time.sleep(2)
                            start(armory, programs, droids)
                    else:
                            security(armory, programs, droids)
            elif cmd == '5':
                    if 'MEECDT1000' in programs and 'zx4e9q' in programs:
                            print('\n- DECK 5 SECURED - ACCESS LOCKED -')
                            time.sleep(2)
                            start(armory, programs, droids)
                    else:
                            recharging(armory, programs, droids)
            elif cmd == '6':
                    if 'twin laser' in armory:
                            print('\n- DECK 6 SECURED - ACCESS LOCKED -')
                            time.sleep(2)
                            start(armory, programs, droids)
                    else:
                            power_core(armory, programs, droids)
            elif cmd == '7':
                    if 'console hack' in programs:
                            print('\n- DECK 7 SECURED - ACCESS LOCKED -')
                            time.sleep(2)
                            start(armory, programs, droids)
                    else:
                            shield(armory, programs, droids)
            elif cmd == '8':
                    if 'MEECDT1000' in programs and 'zx4e9q' in programs:
                            print('\n- DECK 8 SECURED - ACCESS LOCKED -')
                            time.sleep(2)
                            start(armory, programs, droids)
                    else:
                            cruiser_control(armory, programs, droids)
            elif cmd == '9':
                    if 'droid hack' in programs:
                            print('\n- DECK 9 SECURED - ACCESS LOCKED -')
                            time.sleep(2)
                            start(armory, programs, droids)
                    else:
                            observation(armory, programs, droids)
            elif cmd == '10':
                    if 'motion tracker' in armory and 'disruptor' in armory:
                            print('\n- DECK 10 SECURED - ACCESS LOCKED -')
                            time.sleep(2)
                            start(armory, programs, droids)
                    else:
                            droid_software(armory, programs, droids)
                    
    def shield(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nYou are on the Shield Generator Deck
    Sentry Droid 529 is defending the Shield Generator
    but has been Disrupted by Enemy Sentry Droid 771.
    You have seconds before your next.. ''')
            print('\n[-SHIELD GENERATOR-]\n')
            print('1.) Terminate Enemy Sentry droid 771')
            print('2.) Retreat to main elevator')
            cmdlist =['1', '2']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                    if 'twin laser' in armory:
                            print('\nTwin laser active...')
                            time.sleep(1)
                            print('Targeting SEN771...')
                            time.sleep(1)
                            print('\nTarget locked...')
                            time.sleep(1)
                            print('...')
                            time.sleep(1)
                            print('\nTARGET TERMINATED\n')
                            time.sleep(2)
                            print('''Enemy Sentry Droid 771 has been terminated
    and it's connection outlet is destroyed.''')
                            hackdroid(programs)
                    else:
                            enemysen(armory, programs, droids)
            elif cmd == '2':
                            time.sleep(1)
                            print('\nYou try to retreat but its to late..')
                            time.sleep(2)
                            print('\nEnemy Sentry Droid 771 has you Locked on.')
                            time.sleep(2)
                            print('\nSEN771:> 0011100000001000000011100000')
                            time.sleep(1)
                            print('\n....')
                            time.sleep(1)
                            print('\nShutdown imminent...')
                            time.sleep(1)
                            print('CMBT645 offline.')
                            time.sleep(1)
                            print('Droid terminated.')
                            print('\n- GAME OVER -\n')
                            exit(0)
                    
    def security(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nYou are on the Security Deck. This is where all
    Surveillance aboard the Cruiser is done. 
    Sentry Droid 529 is absent from the Console.''')
            print('\n[-SECURITY-]\n')
            print('1.) View Surveillance monitors on other decks')
            print('2.) Access Main Console')
            print('3.) Return to Main Elevator')
            cmdlist = ['1', '2', '3', 'console hack']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                    print('\n----------')
                    print('\nBooting Monitors....')
                    time.sleep(1)
                    print('....')
                    time.sleep(1)
                    print('...')
                    time.sleep(1)
                    print('\nMonitors active.')
                    time.sleep(1)
                    print('\n[-SURVEILLANCE FEED-]')
                    print('''\nDECK 1  - This Deck appears to be clear.
    \nDECK 2  - A Enemy Droid Shuttle is docked here.
    \nDECK 3  - MONITOR OFFLINE - NO LIVE FEED.
    \nDECK 5  - MONITOR OFFLINE - NO LIVE FEED.
    \nDECK 6  - MONITOR OFFLINE - NO LIVE FEED.
    \nDECK 7  - MONITOR OFFLINE - NO LIVE FEED.
    \nDECK 8  - A T1000 Master Elite Enemy Command Droid. 
    \nDECK 9  - A small Low Class Enemy Scouter Droid.
    \nDECK 10 - This Deck appears to be clear''')
                    time.sleep(2)
                    security(armory, programs, droids)
            elif cmd == '2':
                    print('\n - ACCESS TO MAIN CONSOLE DENIED -')
                    time.sleep(2)
                    security(armory, programs, droids)
            elif cmd == '3':
                    start(armory, programs, droids)
            elif cmd == 'console hack':
                    if 'console hack' in programs:
                            print('\nloading console hack....')
                            time.sleep(2)
                            print('....')
                            time.sleep(2)
                            print('10000101010101010101010' * 1000)
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('Accessing encrypted files...')
                            time.sleep(2)
                            print('Decrypting....')
                            time.sleep(2)
                            print('\n[- SECURITY MAIN CONSOLE -]')
                            time.sleep(1)
                            print('\nDAILY OVER-RIDE CODES- HANGAR DROIDS')
                            time.sleep(1)
                            print('\n-Combat Droids  -  zx71vbq')
                            time.sleep(1)
                            print('\n-Sentry Droids  -  9jt2zm5')
                            time.sleep(1)
                            print('\n-Repair Droids  -  lk0sa8c')
                            time.sleep(1)
                            print('\n-Control Droids -  44qaz5x')
                            time.sleep(1)
                            print('\nCODES WILL BE RESET EVERY 24 HOURS')
                            time.sleep(2)
                            print('\n=====================================')
                            print('\nDROID SOFTWARE SYSTEM - SECURE CODES')
                            time.sleep(1)
                            print('\n-Sentry Droids  -  qiy25az')
                            time.sleep(1)
                            print('\n-Combat Droids  -  w7md3sx')
                            time.sleep(1)
                            print('\n-Repair Droids  -  zp11dcy')
                            time.sleep(1)
                            print('\n-Control Droids -  kkx2s3q')
                            time.sleep(1)
                            print('\nCODES WILL BE RESET EVERY 24 HOURS')
                            time.sleep(4)
                            security(armory, programs, droids)
                    else:
                            print('\n - CONSOLE HACK PROGRAM NOT DETECTED -')
                            time.sleep(2)
                            security(armory, programs, droids)
                            
    def hackdroid(programs, items=['console hack']):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nSentry droid 529 is disrupted
    but has a Console Hack program installed.
    You MUST connect to this droid with service port 
    and download the program.''')
            if len(items) > 0:
                    for item in items:
                            print('\n--> %s' % (item))
            cmdlist = ['service port']
            cmd = getcmd(cmdlist)
            if cmd == 'service port':
                            programs.append('console hack')
                            items = ['console hack']
                            print('\nservice port connected.')
                            time.sleep(1)
                            print('accessing file..')
                            time.sleep(1)
                            print('downloading..')
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('\ndownload complete.')
                            time.sleep(1)
                            print('\nYou have the Console Hack program')
                            print('and return to the Main Elevator')
                            time.sleep(2)
                            start(armory, programs, droids)
            
    def recharging(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nThis is the Re-Charge deck where all droids dock
    at charging stations to restore power cells. 
    There are currently two droids docked.''')
            print('\n[-RECHARGE STATIONS-]\n')
            print('1.) Scan 866 Control Droid')
            print('2.) Scan 444 Enemy Sentinel Droid')
            print('3.) Return to Main Elevator')
            cmdlist = ['1', '2', '3']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                    if 'influence' in programs:
                            print('\n- SCAN COMPLETE INFLUENCE PROGRAM ALREADY INSTALLED -')
                            time.sleep(2)
                            recharging(armory, programs, droids)
                    else:
                            ctrl_droid(programs)
            elif cmd == '2':
                    sentinel_droid(armory, programs, droids)
            elif cmd == '3':
                            start(armory, programs, droids)

    def ctrl_droid(programs, items=['influence']):
            print('\n----------')
            time.sleep(1)
            print('\nscanning.....')
            time.sleep(1)
            print('''\nThe scan indicates the 866 Control Droid 
    has a Influence program. You MUST connect to this droid 
    with service port and download the program.  
    This program will bring Droids under your Command.''')
            if len(items) > 0:
                    for item in items:
                            print('\n--> %s' % (item))
            cmdlist = ['service port']
            cmd = getcmd(cmdlist)
            if cmd == 'service port':
                            programs.append('influence')
                            items = ['influence']
                            print('\nservice port connected.')
                            time.sleep(1)
                            print('accessing file..')
                            time.sleep(1)
                            print('downloading..')
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('\ndownload complete.')
                            print('\nYou have the Influence program.')
                            time.sleep(2)
                            recharging(armory, programs, droids)
                            
    def sentinel_droid(armory, programs, droids):
            print('\n----------')
            time.sleep(1)
            print('\nscanning.....')
            time.sleep(1)
            print('''\nThe scan has activated the Sentinel Droid's 
    Pulse wave device. The pulse wave will shutdown any 
    droids on this deck. You MUST abort the sequence.\n''')
            time.sleep(2)
            print('''\n       << STNL444 ABORT PAD >> ''')
            print('''\n  WARNING PULSE WAVE SEQUENCE INITIATED ''')
            print('''\n    PRESS KEY 0, 1, 2, OR 3 TO ABORT ''')
            time.sleep(1)
            code = '%d' % (randint(0,3))
            guess = input('\n[ABORT]> ')
            guesses = 0
            while guess != code and guesses <1:
                    print('\n << ABORT KEY INVALID >>')
                    time.sleep(1)
                    guesses += 1
                    guess = input('\n[ABORT]> ')
            if guess == code:
                    print('\n----------')
                    time.sleep(1)
                    print('\n << PULSE WAVE SEQUENCE ABORTED >>')
                    time.sleep(2)
                    recharging(armory, programs, droids)
            else:
                    print('\n....')
                    time.sleep(2)
                    print('\nPULSE WAVE SEQUENCE COMPLETE')
                    time.sleep(1)
                    print('\nPULSE WAVE ACTIVE...')
                    time.sleep(1)
                    print('\nshutdown imminent...')
                    time.sleep(1)
                    print('CMBT645 offline.')
                    time.sleep(1)
                    print('Droid terminated.\n')
                    time.sleep(1)
                    print('- GAME OVER -\n')
                    exit(0)
                    
    def docking(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nThis is the Docking Port where all incoming craft
    dock to access the main Cruiser. There is a
    Enemy Droid Shuttle currently docked''')
            print('\n[-DOCKING-]')
            print('\n1.) Escape in Enemy Droid Shuttle')
            print('2.) Return to Main Elevator')
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                    fighter_ship(armory, programs, droids)
            elif cmd == '2':
                    nuke_death(armory, programs, droids)
                    
    def fighter_ship(armory, programs, droids):
            print('\n <<[ ENEMY DROID SHUTTLE ]>>')
            code = '%d%d%d%d%d%d' % (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
            guess = input('\n[STARTUP-CODE]> ')
            guesses = 0
            while guess != code and guess != 'zx4e9q' and guesses <0:
                    #print('\n* ACCESS - DENIED *')
                    guesses += 1
                    guess = input('\n[STARTUP-CODE]> ')
            if guess == code or guess == 'zx4e9q':
                    if 'zx4e9q' in programs and 'MEECDT1000' in programs \
    and 'droid hack' in programs:
                            shuttle_control(armory, programs, droids)
                    else:
                            print('\nJAY666:> - DROID CHEATING DETECTED GAME OVER -\n')
                            time.sleep(2)
                            exit(0)
            else:
                    nuke_death(armory, programs, droids)
                            
    def observation(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nThis is the Observation Deck. A small Low Class 
    020 Enemy Scouter droid is posted here.
    Use a Probe Droid to Disrupt STR020.''')
            print('\n[-OBSERVATION-]')
            print('\n1.) Disrupt the 020 Enemy Scouter Droid')
            print('2.) Retreat to Main Elevator')
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                    if 'PBE111' in droids and 'influence' in programs:
                            print('\nLaunching probe droid...')
                            time.sleep(1)
                            print('Disruptor active...')
                            time.sleep(1)
                            print('Targeting STR020...')
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('\nTarget locked...')
                            time.sleep(2)
                            print('\nTARGET DISRUPTED')
                            time.sleep(2)
                            scouter(programs)
                    else:
                            enemyscouter(armory, programs, droids)
            elif cmd == '2':
                            time.sleep(2)
                            print('''\nThe Enemy Scouter Droid runs a Droid Hack
    jamming your motivator rendering you idle.
    \nEnemy Combat Droids are inbound.
    \nSTR020:> 0011100000001000000011100000''')
                            time.sleep(4)
                            print('\n.....')
                            time.sleep(1)
                            print('\nself-destruct sequence initiated...')
                            time.sleep(1)
                            print('shutdown imminent...')
                            time.sleep(1)
                            print('\nCMBT645 offline.')
                            time.sleep(1)
                            print('Droid terminated.')
                            print('\n - GAME OVER -\n')
                            exit(0)
                            
    def scouter(programs, items=['droid hack']):
            print('\n----------')
            time.sleep(1)
            print('''\nThe Enemy 020 scouter droid has a Droid Hack
    program. You MUST connect to this droid with 
    service port and download the program.''')
            if len(items) > 0:
                    for item in items:
                            print('\n--> %s' % (item))
            cmdlist = ['service port']
            cmd = getcmd(cmdlist)
            if cmd == 'service port':
                            programs.append('droid hack')
                            items = ['droid hack']
                            print('\nservice port connected.')
                            time.sleep(1)
                            print('accessing file..')
                            time.sleep(1)
                            print('downloading..')
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('\ndownload complete.')
                            time.sleep(1)
                            print('\nYou have the Droid Hack program.')
                            print('and return to the Main Elevator.')
                            time.sleep(2)
                            start(armory, programs, droids)
                            
    def droid_hangar(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nThe Droid hangar is Where all inactive droids
    are docked. Enemy Droids have terminated all units. 
    The Hangar has Laser scoring everywhere.
    \nThere are Two Combat Droids that are still incased in  
    in a security cylinder. You MUST influence these Droids
    but you will need a 5 digit access code to initalize.\n''')
            print('[-DROID HANGAR-]')
            print('\n1.) Combat Droids 5 digit code')
            print('2.) Return to Main Elevator')
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                    access_code(armory, programs, droids)
            elif cmd == '2':
                    start(armory, programs, droids)
                    
    def access_code(armory, programs, droids):
            print('\n <SECURITY CYLINDER>')
            print('\n[-CMBT646 - CMBT647-]')
            code = '%d%d%d%d%d' % (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
            guess = input('\n[KEYPAD]> ')
            guesses = 0
            while guess != code and guess != 'zx71vbq' and guesses <2:
                    print('\n* ACCESS - DENIED *')
                    guesses += 1
                    guess = input('\n[KEYPAD]> ')
            if guess == code or guess == 'zx71vbq':
                    combat_droids(armory, programs, droids)
            else:
                    print('\n....')
                    time.sleep(1)
                    print('\nKEYPAD - LOCKED')
                    time.sleep(1)
                    print('\ncode randomizing..')
                    time.sleep(1)
                    print('\nKEYPAD - OPEN')
                    time.sleep(1)
                    droid_hangar(armory, programs, droids)
                    
    def cargo_hold(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nThis is the cargo hold where all supplies are kept.
    There is a small Droid flying around scanning crates.
    It is a Probe Droid and is also armed with a disruptor.''')
            print('\n[-CARGO HOLD-]\n')
            print('1.) Probe Droid 111')
            print('2.) Return to Main Elevator\n')
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                    probe_droid(droids)
            elif cmd == '2':
                    start(armory, programs, droids)
                    
    def probe_droid(droids, items=['PBE111']):
            print('\n----------')
            time.sleep(1)
            print('''\nThe Probe Droid is flying within range. You
    MUST bring this droid under your command 
    with a influence program.  \n\n\t\t- or type exit to leave.''')
            if len(items) > 0:
                    for item in items:
                            print('\n--> %s' % (item))
            cmdlist = ['influence', 'exit']
            cmd = getcmd(cmdlist)
            if cmd == 'influence' and 'influence' in programs:
                            droids.append('PBE111')
                            items = ['PBE111']
                            print('\nloading influence...')
                            time.sleep(1)
                            print('influencing...')
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('\nPBE111 DROID INFLUENCED')
                            time.sleep(2)
                            print('\nYou now have PBE111 under your command')
                            print('you return to Main Elevator')
                            time.sleep(2)
                            start(armory, programs, droids)
            elif cmd == 'exit':
                            start(armory, programs, droids)
            else:
                    print('\n- INFLUENCE PROGRAM NOT DETECTED -')
                    time.sleep(2)
                    cargo_hold(armory, programs, droids)
                    
    def power_core(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nYou enter the Power Core deck. The
    power core generates power for the Cruiser.
    \nRepair Droid 377 was here doing maintenance 
    on the Core Chamber but has been terminated.  
    You MUST hack the Repair droid and download 
    the twin laser repair program.''')
            print('\n[-POWER CORE CHAMBER-]\n')
            print('1.) Hack Repair Droid 377')
            print('2.) Return to Main Elevator')
            cmdlist =['1', '2']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                    if 'droid hack' in programs:
                            repair_droid(armory, items=['twin laser'])
                    else:
                            print('\n- DROID HACK PROGRAM NOT DETECTED -')
                            time.sleep(2)
                            power_core(armory, programs, droids)
            elif cmd == '2':
                            start(armory, programs, droids)
                    
    def repair_droid(armory, items=['twin laser']):
            print('\n----------')
            time.sleep(1)
            print('\nloading droid hack....')
            time.sleep(2)
            print('....')
            time.sleep(2)
            print('10000101010101010101010' * 1000)
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('Accessing encrypted files...')
            time.sleep(2)
            print('Decrypting....')
            time.sleep(1)
            print('\n\n[-REP377-]')
            print('''\n\nDownload the twin laser repair
    program with service port.''')
            if len(items) > 0:
                    for item in items:
                            print('\n--> %s' % (item))
            cmdlist = ['service port']
            cmd = getcmd(cmdlist)
            if cmd == 'service port':
                            armory.append('twin laser')
                            items = ['twin laser']
                            print('\nservice port connected.')
                            time.sleep(1)
                            print('accessing file..')
                            time.sleep(1)
                            print('downloading..')
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('\ndownload complete.')
                            time.sleep(1)
                            print('Repairing twin Laser...')
                            time.sleep(1)
                            print('Auto alignment...')
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('\nTWIN LASER ONLINE.')
                            time.sleep(2)
                            print('''\nYour twin laser is now online.
    You return to the Main Elevator.''')
                            time.sleep(2)
                            start(armory, programs, droids)
                            
    def droid_software(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nYou enter the Droid Software Deck. This deck
    is where droids connect to the main terminal and download
    Software.  You will need a Droid class secure code
    to gain access to the system.''')
            print('\n\n[-DROID SOFTWARE SYSTEM-]')
            print('\n  [ - MAIN TERMINAL - ]')
            time.sleep(1)
            print('\n\n..service port connected.')
            time.sleep(1)
            print('\nenter secure code  -or type exit to leave')
            cmdlist =['w7md3sx', 'exit', 'console hack']
            cmd = getcmd(cmdlist)
            if cmd == 'w7md3sx':
                    if 'console hack' in programs and 'droid hack' in programs \
    and 'influence' in programs and 'PBE111' in droids:
                            print('\n----------')
                            time.sleep(1)
                            print('\n - COMBAT DROID SECURE CODE VERIFIED -')
                            time.sleep(2)
                            software_download(armory)
                    else:
                            print('\n...')
                            time.sleep(1)
                            print('\nJAY666:> are you cheating ? ')
                            time.sleep(3)
                            droid_software(armory, programs, droids)
            elif cmd == 'exit':
                    print('\n....')
                    time.sleep(1)
                    print('\nservice port disconnected.')
                    time.sleep(1)
                    start(armory, programs, droids)
            elif cmd == 'console hack':
                    print('....')
                    time.sleep(1)
                    print('\n - MAIN TERMINAL SECURE -')
                    time.sleep(2)
                    droid_software(armory, programs, droids)
                    
    def software_download(armory, items=['motion tracker', 'disruptor']):
            print('''\nThere are two Weapon Repair programs 
    which you MUST download with service port.''')
            if len(items) > 0:
                    for item in items:
                            print('\n--> %s' % (item))
                    cmdlist = ['service port']
                    cmd = getcmd(cmdlist)
            if cmd == 'service port':
                    armory.append('motion tracker')
                    armory.append('disruptor')
                    items = ['motion tracker', 'disruptor']
                    print('\nservice port connected.')
                    time.sleep(1)
                    print('accessing files..')
                    time.sleep(1)
                    print('downloading..')
                    time.sleep(1)
                    print('....')
                    time.sleep(1)
                    print('\ndownload complete.')
                    time.sleep(1)
                    print('\nRepairing motion tracker...')
                    time.sleep(1)
                    print('Repairing disruptor...')
                    time.sleep(1)
                    print('Auto alignment...')
                    time.sleep(1)
                    print('....')
                    time.sleep(1)
                    print('\nMOTION TRACKER ONLINE.')
                    time.sleep(1)
                    print('\nDISRUPTOR ONLINE.')
                    time.sleep(2)
                    print('''\nYour motion tracker and disruptor
    are now online. You return to the Main Elevator.''')
                    start(armory, programs, droids)
            elif cmd == 'exit':
                    start(armory, programs, droids)
                    
    def combat_droids(armory, programs, droids):
            time.sleep(1)
            print('\n\n - ACCESS CODE GRANTED -')
            print('\n<< Security Cylinder Open >>')
            time.sleep(2)
            print('\n....')
            time.sleep(1)
            print('\nCMBT646 boot sequence....')
            time.sleep(1)
            print('\nInitalizing Combat Droid 646....')
            time.sleep(1)
            print('\n....')
            time.sleep(1)
            print('\nCMBT646 ONLINE.')
            time.sleep(2)
            print('\n....')
            time.sleep(1)
            print('\nCMBT647 boot sequence....')
            time.sleep(1)
            print('\nInitalizing Combat Droid 647....')
            time.sleep(1)
            print('\n....')
            time.sleep(1)
            print('\nCMBT647 ONLINE.')
            time.sleep(2)
            combat_influence(armory, programs, droids)
            
    def combat_influence(armory, programs, droids, items=['CMBT646', 'CMBT647']):
            print('\n----------')
            time.sleep(1)
            print('''\nThe Combat droids have now been initialized.
    you MUST use the influence program 
    to bring these Droids under your Command.''')
            if len(items) > 0:
                    for item in items:
                            print('\n--> %s' % (item))
            cmdlist = ['influence']
            cmd = getcmd(cmdlist)
            if cmd == 'influence' and 'influence' in programs:
                            droids.append('CMBT646')
                            droids.append('CMBT647')
                            items = ['CMBT646', 'CMBT647']
                            print('\nloading influence...')
                            time.sleep(1)
                            print('influencing...')
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('\nCMBT646 DROID INFLUENCED')
                            time.sleep(2)
                            print('\ninfluencing...')
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('\nCMBT647 DROID INFLUENCED')
                            time.sleep(2)
                            print('''\nYou now have Both Combat Droids under 
    your command. You return to Main Elevator''')
                            time.sleep(2)
                            start(armory, programs, droids)
            else:
                            print('\nJAY666:> - DROID CHEATING DETECTED GAME OVER -\n')
                            time.sleep(2)
                            exit(0)
                            
    def cruiser_control(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nYou enter Cruiser Control where all navigation takes place.
    A T1000 Master Elite Enemy Command Droid is posted here..
    Exercise caution this Droid is extremely powerfull and
    has not been encountered before.''')
            print('\n[-CRUISER CONTROL-]')
            print('\n1.) Terminate the T1000 Master Elite Enemy Command Droid')
            print('2.) Retreat to Main Elevator')
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                    if 'droid hack' in programs and 'influence' in programs \
    and 'PBE111' in droids and 'CMBT646' in droids and 'CMBT647' in droids \
    and 'twin laser' in armory and 'disruptor' in armory \
    and 'motion tracker' in armory and 'console hack' in programs:
                            command_droid_battle(armory, programs, droids)
                    else:
                            time.sleep(1)
                            print('\nMEECDT1000:>')
                            print('\n100101010101010101010101010101010' * 10)
                            time.sleep(1)
                            print('''\nThe Master Elite Enemy Command Droid 
    laughs in machine language at your pathetic attempt. 
    The last thing your data recorder recieves is 
    the sound of a Target Lock.''')
                            print('....')
                            time.sleep(1)
                            print('..')
                            time.sleep(1)
                            print('\nshutdown imminent...')
                            time.sleep(1)
                            print('CMBT645 offline.')
                            time.sleep(1)
                            print('Droid terminated.')
                            print('\n- GAME OVER -\n')
                            exit(0)
            elif cmd == '2':
                    start(armory, programs, droids)
                    
    def command_droid_battle(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('......')
            time.sleep(1)
            print('\nCOMBAT DROIDS ACTIVE >>')
            time.sleep(1)
            print('\nCMBT646 ENGAGING MEECDT1000')
            time.sleep(1)
            print('\nCMBT647 ENGAGING MEECDT1000')
            time.sleep(1)
            print('\n......')
            print('\n - MEECDT1000 DAMAGE STATUS AT 40 PER CENT -')
            time.sleep(3)
            print('\n\nPROBE DROID ACTIVE >> ')
            time.sleep(1)
            print('\nPBE111 ENGAGING MEECDT100')
            time.sleep(1)
            print('\n......')
            print('\n - MEECDT1000 DAMAGE STATUS AT 50 PER CENT -')
            time.sleep(3)
            print('\n\nRunning droid hack...')
            time.sleep(1)
            print('\njamming MEECDT1000 Target Lock...')
            time.sleep(1)
            print('\n......')
            time.sleep(1)
            print('\nMotion Tracker active...')
            time.sleep(1)
            print('\nTrack motion of MEECDT1000...')
            time.sleep(1)
            print('\n......')
            time.sleep(1)
            print('\nDisruptor active...')
            time.sleep(1)
            print('\nDisrupting MEECDT1000...')
            time.sleep(1)
            print('\n......')
            time.sleep(1)
            print('\nTwin laser active...')
            time.sleep(1)
            print('\nTargeting MEECDT1000...')
            time.sleep(1)
            print('\nTarget lock failed...')
            time.sleep(1)
            print('\n......')
            time.sleep(2)
            print('\n\nTARGET DISRUPTED \n')
            time.sleep(2)
            command_droid(armory, programs, droids)
            
    def command_droid(armory, programs, droids):
            print('\n----------')
            print('\nDroid mobile..')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('''\nYou have disrupted the Master Elite Enemy Command Droid.
    This high rank Droid must have important files in memory.
    \nMEECDT1000 has sustained severe disruptor damage.
    You MUST try access the files...''')
            print('\n\n[- MEECDT1000 -]')
            cmdlist = ['droid hack']
            cmd = getcmd(cmdlist)
            if cmd == 'droid hack':
                    ship_code(armory, programs, droids)
                    
    def ship_code(armory, programs, droids, items=['zx4e9q', 'MEECDT1000']):
            print('\n----------')
            time.sleep(1)
            print('\nloading droid hack....')
            time.sleep(2)
            print('....')
            time.sleep(2)
            print('10000101010101010101010' * 1000)
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('Accessing encrypted files...')
            time.sleep(2)
            print('Decrypting....')
            time.sleep(1)
            print('\n\n[- MEECDT1000 -]')
            print('''\n\nThe Secure files contain
    a startup code for a Enemy Droid Shuttle 
    and the MEECDT1000 Droid Specs.
    You MUST download these files with service port.''')
            if len(items) > 0:
                    for item in items:
                            print('\n--> %s' % (item))
            cmdlist = ['service port']
            cmd = getcmd(cmdlist)
            if cmd == 'service port':
                            programs.append('zx4e9q')
                            programs.append('MEECDT1000')
                            items = ['zx4e9q', 'MEECDT1000']
                            print('\nservice port connected.')
                            time.sleep(1)
                            print('accessing files..')
                            time.sleep(1)
                            print('downloading..')
                            time.sleep(1)
                            print('....')
                            time.sleep(1)
                            print('\ndownload complete.')
                            time.sleep(2)
                            print('\n.....')
                            time.sleep(2)
                            print('\n\n <<< WARNING NUKE ACTIVE >>>')
                            time.sleep(2)
                            print('\n DETONATION SEQUENCE INITIATED')
                            time.sleep(2)
                            print('\n\nMEECDT1000:> 0011100000001000000011100000 ')
                            time.sleep(2)
                            print('''\n\nDownloading the Droid Specs has 
    activated a Droid Nuke inside MEECDT1000. 
    \nThe Nuke will Obliterate the Cruiser
    \nYou MUST escape the PROXY ....''')
                            time.sleep(4)
                            start(armory, programs, droids)
                            
    def shuttle_control(armory, programs, droids):
            time.sleep(1)
            print('\n\n<< START-UP CODE VERIFIED >>')
            time.sleep(2)
            print('\n>>')
            time.sleep(1)
            print('\nHyperdrive active..')
            time.sleep(1)
            print('Hyperspace coordinates locked.')
            time.sleep(1)
            print('\nDestination: phaze beta system.\n')
            time.sleep(2)
            print('\nHYPERSPACE JUMP SEQUENCE INITIATED >>\n')
            time.sleep(4)
            print('\n>>')
            time.sleep(1)
            print('''\nYou have escaped the PROXY and made
    a Hyperspace jump to Droid Command.
    \nThe specs you obtained on the rare 
    MEECDT1000 droid are priceless. Production of 
    these Droids will Commence at once.''')
            time.sleep(1)
            print('\n - GAME OVER -\n')
            exit(0)

    def nuke_death(armory, programs, droids):
            print('\n....')
            time.sleep(2)
            print('\n << DROID NUKE DETONATION SEQUENCE COMPLETE >>')
            time.sleep(4)
            print('\n....')
            time.sleep(1)
            print('''\nThe PROXY is now space debri..
    You failed to escape.''')
            time.sleep(2)
            print('\nCMBT645 offline.')
            time.sleep(1)
            print('Droid terminated.\n')
            time.sleep(1)
            print('- GAME OVER -\n')
            exit(0)
            
    def enemyscouter(armory, programs, droids):
            print('\n- WARNING NO PROBE DROID IN YOUR COMMAND -')
            time.sleep(2)
            print('''\nThe Enemy Scouter Droid runs a Droid Hack
    jamming your motivator rendering you idle.
    \nEnemy Combat Droids are inbound.
    \nSTR020:> 0011100000001000000011100000''')
            time.sleep(4)
            print('\n.....')
            time.sleep(1)
            print('\nself-destruct sequence initiated...')
            time.sleep(1)
            print('shutdown imminent...')
            time.sleep(1)
            print('\nCMBT645 offline.')
            time.sleep(1)
            print('Droid terminated.')
            print('\n - GAME OVER -\n')
            exit(0)
            
    def enemysen(armory, programs, droids):
            print('\n- WARNING TWIN LASER OFFLINE -')
            time.sleep(2)
            print('\nEnemy Sentry Droid 771 has you Locked on.')
            time.sleep(1)
            print('\nSEN771:> 0011100000001000000011100000')
            time.sleep(1)
            print('\n....')
            time.sleep(1)
            print('\nShutdown imminent...')
            time.sleep(1)
            print('CMBT645 offline.')
            time.sleep(1)
            print('Droid terminated.')
            print('\n- GAME OVER -\n')
            exit(0)

    def getcmd(cmdlist):
            cmd = input('\nCMBT645:> ')
            if cmd in cmdlist:
                    return cmd
            elif cmd == 'help':
                    print('\nTYPE: armory   - to view weapons online')
                    print('      programs - to view software installed')
                    print('      droids   - to see in your command')
                    print('      quit     - to self destruct')
                    return getcmd(cmdlist)
            elif cmd == 'armory':
                    print('\nWeapons online:\n')
                    for weapon in armory:
                            print('-- %s' % (weapon))
                    return getcmd(cmdlist)
            elif cmd == 'programs':
                    print("\nSoftware installed:\n")
                    for program in programs:
                            print('-- %s' % (program))
                    return getcmd(cmdlist)
            elif cmd == 'droids':
                    print('\nDroids in command:\n')
                    for droid in droids:
                            print('-- %s' % (droid))
                    return getcmd(cmdlist)
            elif cmd == 'cheat':
                    print('\nJAY666:> DROID CHEATING DENIED ')
                    time.sleep(2)
                    return getcmd(cmdlist)
            elif cmd == 'quit':
                    print('\n----------')
                    time.sleep(1)
                    print('\nself-destruct sequence initiated...')
                    time.sleep(1)
                    print('shutdown imminent...')
                    time.sleep(1)
                    print('\nCMBT645 offline.')
                    time.sleep(1)
                    print('Droid terminated.\n')
                    exit(0)
            else:
                    print('\n   error. invalid command-\n')
                    return getcmd(cmdlist)

    if __name__ == "__main__":
            armory = ['service port']
            programs = []
            droids = []
            start(armory, programs, droids)

#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
 




#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


def Survival():
    #Figuring out how users might respond
    answer_A = ["A", "a"]
    answer_B = ["B", "b"]
    answer_C = ["C", "c"]
    yes = ["Y", "y", "yes"]
    no = ["N", "n", "no"]

    #Grabbing objects
    sword = 0
    flower = 0

    required = ("\nUse only A, B, or C\n") #Cutting down on duplication

    #The story is broken into sections, starting with "intro"
    def intro():
      print ("After a drunken night out with friends, you awaken the "
      "next morning in a thick, dank forest. Head spinning and " 
      "fighting the urge to vomit, you stand and marvel at your new, "
      "unfamiliar setting. The peace quickly fades when you hear a "
      "grotesque sound emitting behind you. A slobbering orc is "
      "running towards you. You will:")
      time.sleep(1)
      print ("""  A. Grab a nearby rock and throw it at the orc
      B. Lie down and wait to be mauled
      C. Run""")
      choice = input(">>> ") #Here is your first choice.
      if choice in answer_A:
        option_rock()
      elif choice in answer_B:
        print ("\nWelp, that was quick. "
        "\n\nYou died!")
      elif choice in answer_C:
        option_run()
      else:
        print (required)
        intro()

    def option_rock(): 
      print ("\nThe orc is stunned, but regains control. He begins "
      "running towards you again. Will you:")
      time.sleep(1)
      print ("""  A. Run
      B. Throw another rock
      C. Run towards a nearby cave""")
      choice = input(">>> ")
      if choice in answer_A:
        option_run()
      elif choice in answer_B:
        print ("\nYou decided to throw another rock, as if the first " 
        "rock thrown did much damage. The rock flew well over the "
        "orcs head. You missed. \n\nYou died!")
      elif choice in answer_C:
        option_cave()
      else:
        print (required)
        option_rock()

    def option_cave():
      print ("\nYou were hesitant, since the cave was dark and "
      "ominous. Before you fully enter, you notice a shiny sword on "
      "the ground. Do you pick up a sword. Y/N?")
      choice = input(">>> ")
      if choice in yes:
        sword = 1 #adds a sword
      else:
        sword = 0
      print ("\nWhat do you do next?")
      time.sleep(1)
      print ("""  A. Hide in silence
      B. Fight
      C. Run""")
      choice = input(">>> ")
      if choice in answer_A:
        print ("\nReally? You're going to hide in the dark? I think "
        "orcs can see very well in the dark, right? Not sure, but "
        "I'm going with YES, so...\n\nYou died!")
      elif choice in answer_B:
       if sword > 0:
        print ("\nYou laid in wait. The shimmering sword attracted "
        "the orc, which thought you were no match. As he walked "
        "closer and closer, your heart beat rapidly. As the orc "
        "reached out to grab the sword, you pierced the blade into "
        "its chest. \n\nYou survived!")
       else: #If the user didn't grab the sword
         print ("\nYou should have picked up that sword. You're "
         "defenseless. \n\nYou died!")
      elif choice in answer_C:
        print ("As the orc enters the dark cave, you sliently "
        "sneak out. You're several feet away, but the orc turns "
        "around and sees you running.")
        option_run()
      else:
        print (required)
        option_cave()

    def option_run():
      print ("\nYou run as quickly as possible, but the orc's "
      "speed is too great. You will:")
      time.sleep(1)
      print ("""  A. Hide behind boulder
      B. Trapped, so you fight
      C. Run towards an abandoned town""")
      choice = input(">>> ")
      if choice in answer_A:
        print ("You're easily spotted. "
        "\n\nYou died!")
      elif choice in answer_B:
        print ("\nYou're no match for an orc. "
        "\n\nYou died!")
      elif choice in answer_C:
        option_town()
      else:
        print (required)
        option_run()
        
    def option_town():
      print ("\nWhile frantically running, you notice a rusted "
      "sword lying in the mud. You quickly reach down and grab it, "
      "but miss. You try to calm your heavy breathing as you hide "
      "behind a delapitated building, waiting for the orc to come "
      "charging around the corner. You notice a purple flower "
      "near your foot. Do you pick it up? Y/N")
      choice = input(">>> ")
      if choice in yes:
        flower = 1 #adds a flower
      else:
        flower = 0
      print ("You hear its heavy footsteps and ready yourself for "
      "the impending orc.")
      time.sleep(1)
      if flower > 0:
        print ("\nYou quickly hold out the purple flower, somehow "
        "hoping it will stop the orc. It does! The orc was looking "
        "for love. "
        "\n\nThis got weird, but you survived!")
      else: #If the user didn't grab the sword
         print ("\nMaybe you should have picked up the flower. "
         "\n\nYou died!")

    intro()















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































def valInput(message, length=0):
    val=input(message+": ")
    while len(val)==0:
        print("ERROR: you must type something in")
        val=input(message+": ")
    if length>0 and len(val)!=length:
        print("LENGTH ERROR: you must type",length,"characters")
        return valInput(message+": ", length)
    return val

def inpString(message):
    val=valInput(message)
    while not val.isalpha():
        print("ERROR: you must type characters only")
        val=valInput(message)
    return val

def inpInt(message):
    try:
        return int(valInput(message))
    except ValueError:
        print("ERROR: you must type numbers only")
        return inpInt(message)


def inpDate(message):
    val=valInput(message, 10)
    try:
        newDate = datetime.datetime(int(val[6:10]),int(val[3:5]),int(val[0:2]))
        if val[2]!="/" or val[5]!="/":
            raise ValueError()
        return val
    except ValueError:
        print("ERROR: invalid date, please type a date in the format DD/MM/YYYY")
        return inpDate(message)

def valMenu(message, options):
    choice=input(message+"\nchoice: ")
    while choice not in options:
        print("you must select from the following options: ", ",".join(options))
        choice=input(message+"\nchoice: ")
    return choice
    
def login():
    print("*************************")
    print("*         LOGIN         *")
    print("*************************")
    try:
        un=valInput("Please type in the username")
        password=valInput("Please type in the password")
        file=open("users.txt", "r")
        users=file.readlines()
        for user in users:
            details=user.split(",")
            if details[0]==un and details[1]==password:
                print("Welcome back")
                return True

        print("User not found")
        return loginMenu()
    except FileNotFoundError:
        print("no users exist, please register first")

def register():
    print("**************************")
    print("*       REGISTER         *")
    print("**************************")
    un=valInput("Please type in your username")
    password=valInput("Please type in the password")
    cpassword=valInput("Please confirm your password")
    while cpassword != password:
        print("passwords don't match")
        password=valInput("Please type in the password")
        cpassword=valInput("Please confirm your password")

    file=open("users.txt", "a")
    file.write(un+","+password+",\n")
    file.close()

def loginMenu():
    loginMenuText="""
****************************
*          MENU            *
****************************
* Welcome to School System *
* Please select an option  *
* 1. Login                 *
* 2. Register              *
* 3. Quit                  *
****************************"""

    choice=valMenu(loginMenuText, ["1","2","3"])
    if choice=="1":
        if login():
            mainMenu()
        else:
            loginMenu()
    elif choice=="2":
        register()
        loginMenu()
    elif choice=="3":
        quit()


def mainMenu():
    mainMenuText="""
****************************
*         MAIN MENU        *
****************************
* Please select an option  *
* 1. Add Student           *
* 2. View Student          *
* 3. Reports               *
* 4. Games                 *
* 5. Logout                * 
****************************"""

    choice=valMenu(mainMenuText, ["1","2","3","4","5"])
    if choice=="1":
        addStudent()
    elif choice=="2":
        viewStudent()
    elif choice=="3":
        reportsMenu()
    elif choice=="4":
        Games()
    elif choice=="5":
        loginMenu()
    return mainMenu() #loop back to mainMenu

def addStudent():
    print("**************************")
    print("*      ADD STUDENT       *")
    print("**************************")
    fn=valInput("Please type in first name")
    ln=valInput("Please type in last name")
    gender=valMenu("Please type in student gender - Male/Female/Other", ["Male","Female","Other"])
    dob=inpDate("Please type in DOB in the format DD/MM/YYYY")
    form=valInput("Please type in form group")
    studentID=1
    try:
        file=open("students.txt", "r")
        students=file.readlines()
        lastID=int(students[-1].split(",")[0])
        studentID=lastID+1
        file.close()
    except FileNotFoundError:
        pass #No students exist, start student ID at 1

    file=open("students.txt", "a")
    file.write(str(studentID)+","+fn+","+ln+","+dob+","+gender+","+form+",\n")
    file.close()

def viewStudent():
    print("**************************")
    print("*     VIEW STUDENT       *")
    print("**************************")
    studentId=inpInt("Please type in the student ID")
    try:
        file=open("students.txt", "r")
        found=False
        students=file.readlines()
        for student in students:
            details=student.split(",")
            if details[0]==str(studentId):
                print(" ".join(details))
                found=True
        if not found:
            raise FileNotFoundError()
    except FileNotFoundError:
        print("Student not found")




        
def reportsMenu():
    students=[]
    reportList=[]
    try:
        file=open("students.txt", "r")
        found=False
        students=file.readlines()
    except FileNotFoundError:
        pass #no students report will be empty

    reportsMenuText="""
****************************
*       REPORTS MENU       *
****************************
* Please select an option  *
* 1. All Students Report   *
* 2. Gender Report         *
* 3. Form Report           *
* 4. Back                  *
****************************"""
    choice=valMenu(reportsMenuText, ["1","2","3","4"])
    
    if choice=="1":
        createReport(students, "allstudents.html")
    elif choice=="2":
        gender=valMenu("select gender, Male/Female/Other", ["Male","Female","Other"])
        for student in students:
            details=student.split(",")
            if details[4]==gender:
                reportList.append(student)
        createReport(reportList, gender+"students.html")
    elif choice=="3":
        form=valInput("select form:")
        for student in students:
            details=student.split(",")
            if details[5]==form:
                reportList.append(student)
        createReport(reportList, form+"students.html")
    elif choice=="4":
        mainMenu()


def createReport(students, filename):
    file=open(filename, "w")
    file.write("<html><head></head><body><table>")
    for student in students:
        file.write("<tr>")
        details=student.split(",")
        for detail in details[0:-1]:
            file.write("<td>"+detail+"</td>")
        file.write("</tr>")
    file.write("</table></body></html>")
    file.close()    
    os.startfile(filename)
loginMenu()




