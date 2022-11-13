import PARADICE
import Doraemon
import scoreboard

def playgame():
    print('''Press 1 to Paradice''')
    print('''Press 2 to Doraemon''')
    print('''Press 3 to look at the score me''')
    choose = input("Please press 1 or 2 or 3: ")
    if choose == "1":
        PARADICE.welcome()
    elif choose == "2":
        Doraemon.welcome_rock()
    elif choose == "3":
        scoreboard.score_board()
