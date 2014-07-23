#Rock Paper Scissors Game

print("""
          // // // // // // // // // // // // // // // // // // // // // 
        //  Hello and welcome to Rock, Paper, Scissors. You will be    //
        //  playing against the computer. Good Luck!                   //
          // // // // // // // // // // // // // // // // // // // // // 
""")             

Player = 0
Computer = 0
lets_begin = input("Are you ready to begin?")



    
if lets_begin == "Yes":
    print(lets_begin, "\nOkay, lets begin, first to win 3 rounds is the ultimate winner")
elif lets_begin == "No":
    print(lets_begin, "\nOhh, well let me know when you are ready!")

print("Round 1")
print("\nPlayer Score=", Player)
print("Computer Score=", Computer)

Round = 0
while Round <= 2:

    player_choice = input("\nWould you like Rock, Paper or Scissors?.")

    if player_choice == "Rock" or player_choice == "Paper" or player_choice == "Scissors":
        print(player_choice, "Ohhh, good pick!")
    else:
        print("\nSorry that is not recognised try again")
    
    import random
    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice = "Rock"
    elif comp_choice == 2:
        comp_choice = "Paper"
    elif comp_choice == 3:
        comp_choice = "Scissors"
    print("\nOkay, I choose " + str(comp_choice))

    if player_choice == comp_choice:
        print("\nOhhh, looks like its a tie")
        Round += 1
        print("\nLet's play again")
        print("\nOnto round: ", Round)
    elif (comp_choice == "Rock" and player_choice == "Paper") or (comp_choice == "Paper" and player_choice == "Scissors") or \
(comp_choice == "Scissors" and player_choice == "Rock"):
        Player += 1
        print("\nOhh, looks like you win this round" + "\nPlayer Score =", Player, "\nComputer Score= ", Computer)
        Round += 1
        
    else:
        Computer += 1
        print("\nOppps, sorry looks like you lose this round!" + "\nComputer Score= ", Computer)
        Round += 1
        

#Game Results
print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@'FINAL SCORES!!!'@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")
print("\nPlayer Score: ", Player)
print("\nComputer Score: ", Computer)
if Player > Computer:
    print("Player wins...")
elif Player < Computer:
    print("Computer wins...")
else:
    print("It's a tie")

print("Thank You for playing, hope you enojoyed it")

    

input("\n\nPress the enter key to exit.")
