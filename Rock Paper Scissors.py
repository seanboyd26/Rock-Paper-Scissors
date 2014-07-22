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
    print(lets_begin, "\nOkay, lets begin")
elif lets_begin == "No":
    print(lets_begin, "\nOhh, well let me know when you are ready!")

print("Round 1")
print("\nPlayer Score=", Player)
print("\nComputer Score=", Computer)



input("\n\nPress the enter key to exit.")
