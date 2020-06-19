# Escape Room Game for Computer Science CPT
# Parisa Acharya
# 19/06/2020

# Setup Questions, Answers and Hints in Dictionaries and Lists
question_dict = {
    1: "Seven figures join the white queen, who waits, facing the board. \nThe seats to the left of the white queen are labeled A, C, and E. \nThe seats to the right of the white queen are labeled B, D, and F."
    + " " + "Directly opposite the white queen is the seat labeled G. \nThe black queen, the black rook, and the white pawn stand on one side of the board."
    + " " + "The white bishop, the white rook, and the black rook stand opposite. \nThe black rook stands to the immediate right of the white king and directly across from the white bishop."  
    + " " + "\nThe white pawn stands directly across from the white rook and to the white queen's immediate left. \nThe black queen, white pawn, white king, and black rook leave the board first."
    + " " + "\nWhat is the code word revealed?",
    2: "We are all very little creatures, \neach of us have different features. \nOne of us in glass is set,"
    + " " + "another you will find in jet. \nThis other you will find in tin, \nor if you don't see, then look within."
    + " " + "\nYet if this one you should pursue, \nthen it can never fly from you. \nWhat are we?",
    3: "O T T F F S S. What are the next 3 letters in this pattern?",
    4: "Eiffel Tower: S _ _ n _ \nPyramid: _ _ _ _ \nStatue: _ _ _ _ _ _ \nArch: _ _ _ _ _ _ _ _ _ _ _ _ \nEye: _ _ _ _ _ _",
    5: "You tell Sam and Peter, 'I have chosen 2 different integers greater than one. Their sum is less than 100.' \nSam is whispered their sum, and Peter their product."
    + " " + "\nThen Peter says 'I don't know what the numbers are.' Then Sam says 'I knew that. I don't know them either.'"
    + " " + "\nPeter says 'Oh! Now I know the numbers.', and Sam says 'Now I know them too.' \nWhat were the numbers in ascending order?",
    6: "There are 5 houses in five different colors.\nIn each house lives a person with a different nationality. \nThese five owners drink a certain type of beverage, smoke a certain brand of cigar and keep a certain pet."
    + " " + "\nNo owners have the same pet, smoke the same brand of cigar or drink the same beverage.\nThe question is: Who owns the fish?"
    + " " + "\n****************************" + "\nThe Brit lives in the red house.\nThe Swede keeps dogs as pets.\nThe Dane drinks tea.\nThe green house is on the left of the white house."
    + " " +"The green house's owner drinks coffee.\nThe person who smokes Pall Mall rears birds.\nThe owner of the yellow house smokes Dunhill."
    + " " +"The man living in the center house drinks milk.\nThe Norwegian lives in the first house.\nThe man who smokes blends lives next to the one who keeps cats."
    + " " +"The man who keeps horses lives next to the man who smokes Dunhill.\nThe owner who smokes BlueMaster drinks beer.\nThe German smokes Prince."
    + " " +"The Norwegian lives next to the blue house.\nThe man who smokes blend has a neighbor who drinks water."
    }

hint_list = ["Position C is taken up by a black queen.", 
"Look very closely at the words.", 
"Each letter is the first letter of another word.",
"What can run, but never walks? Has a mouth, but never talks? Has a head, but never weeps? Has a bed, but never sleeps...?",
"One of the numbers is prime.",
"House 5 is the house that drinks beer and smokes BlueMaster."]

answers_dict = {
    1:"cage",
    2:"vowels",
    3:"e n t", 
    4:"seine nile hudson mississippi thames",
    5:"4 13",
    6:"german"}

# Functions to print questions, hints (defined above) and check answers  
def hints(level):
    hint_r = input("Would you like a hint?: Answer Y or N: ")
    if hint_r =="Y":
            hint_index = level - 1
            global hints_used
            hints_used = True
            print("*****************************")
            print("Hint: " + hint_list[hint_index])
            print("*****************************")
            print("")
    else:    
            print("")

def question(level):
    print("")
    print(question_dict[level])
    print("")
    print("* If the answer contains more than one word or number, separate them by spaces.")
    print("")
    answer = input("Answer: ")

    # to ensure format of user's answers doesn't impede validation, 
    # strip whitespace and change to lowercase
    answer = answer.strip().lower()
    
    if answer == answers_dict[level] and hints_used == False: 
        print("Your answer is correct and you didn't even need a hint, Well done!")
        # increment the level to the next number
        level = level + 1
        return (level)
    elif answer == answers_dict[level]: 
        print("Your answer is correct - with a little help :) Well done!")
        # increment the level to the next number
        level = level + 1
        return (level)
    else: 
        print("Your answer is incorrect.")
        return (level)

# Main Run Game Function
def run_game():

    print("")
    print("*****************************************************************************************")
    print("*                                                                                       *")
    print("*                            Welcome To Parisa's Escape Room                            *")
    print("*                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                            *")
    print("*                                                                                       *")
    print("*                  6 questions, No Googling, No Calculator, No Crying                   *")
    print("*          If you get the answer incorrect, you can get one hint per question           *")
    print("*                                                                                       *")
    print("*                        Made by Parisa Acharya, 19th June 2020                         *")
    print("*                                                                                       *")
    print("*****************************************************************************************")
    print("")

    # set variables
    current_level = 1
    global hints_used
    hints_used = False
    tries = 0

    while current_level < 7:
        
        input("Press Enter to proceed...")
        print(" ")
        next_level = question(current_level)
        tries = tries + 1
        
        if current_level == next_level:
            hints(current_level)
        else:
            current_level = next_level
            hints_used = False

    avg_attempts = float(tries / 6)

    if current_level == 7:
        print(" ")
        print("**********************************")
        print(" ")
        print("Congratulations, you have Escaped!")
        print(" ")
        print("**********************************")
        print(" ")
        print("Your stats (for bragging rights or to hide in shame):")
        print("You took", tries, "attempts in total to get through." )
        print("On average, that's", '{:.2f}'.format(avg_attempts), "attempts per question." )
        print(" ")
        if avg_attempts > 1:
            print("The best you could have got is 1 attempt per question. Try harder next time." )
        else:
            print("Well done, that's the lowest possible number of attempts!")
        print(" ")
        print("**********************************")
        print(" ")

run_game()