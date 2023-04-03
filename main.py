from colorama import Fore,Back

def welcome():
    print(Fore.LIGHTYELLOW_EX+'''
          
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣉⡙⠛⠿⣿⣶⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡌⢻⣿⣿⣷⣶⣤⣉⡙⠛⠿⣿⣿⣶⠆⡀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢃⣼⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣌⣉⠀⣿⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠟⠛⠛⠿⣿⣿⣿⣿⣿⡿⠟⢋⣥⡶⠟⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣇⠰⣿⣿⣦⡈⣿⠟⢋⣡⡴⠞⠋⠁⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣿⣿⣦⣌⡉⠉⣠⡴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠲⠆⢹⣿⣿⠿⠛⣉⡥⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⣰⣿⣿⠿⠛⣉⣤⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⡰⠟⢋⣤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⡴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')
    print(Fore.LIGHTMAGENTA_EX+'''
    
    __              __           _                         ____   ____  _               
   / /  ____ ______/ /_   ____  (____  ________     ____  / __/  / __ \(_________ ____ _
  / /  / __ `/ ___/ __/  / __ \/ / _ \/ ___/ _ \   / __ \/ /_   / /_/ / /_  /_  // __ `/
 / /__/ /_/ (__  / /_   / /_/ / /  __/ /__/  __/  / /_/ / __/  / ____/ / / /_/ // /_/ / 
/_____\__,_/____/\__/  / .___/_/\___/\___/\___/   \____/_/    /_/   /_/ /___/___\__,_/  
                      /_/                                                                                                                                                                                             
          ''')

def play():
    print("You set the rules and I choose who start the game first,that's the deal.")
    print("Lets set the rules.")
    n=10
    n=input("How many pieces we are going to divide pizza?")
    try:
        n = int(n)
        assert n >0
    except:
        print("That's not possible! Let's start again.")
    k=5
    k=input("How many pieces we could take every time at most?")
    try:
        k = int(k)
        assert k >0 and k<=n
    except:
        print("That's not possible! Let's start again.")
    win = [False]*(n+1)
    win[1]=True
    for i in range(0,n+1):
        for j in range(1,k+1):
            if i+j<=n and not win[i]:
                win[i+j]=True
    
    # print(win)
    turn = False # means human turn
    if win[n]:
        turn=True
        print(Fore.LIGHTRED_EX+"I play first!")
    else:
        print(Fore.LIGHTRED_EX+"You play first!")
    while True:
        print(Fore.LIGHTBLUE_EX+f"{n} pieces left now.")
        if turn:
            answer = -1
            for i in range(1,k+1):
                if not win[n-i]:
                    answer=i
                    break
            if answer==-1:
                print(Fore.LIGHTRED_EX+"I'm confused",end=",")
                answer=1
            print(Fore.LIGHTRED_EX+f"I take {answer}")
            n-=answer
            
        else:
            answer = "t"
            while True:
                answer = input(Fore.LIGHTGREEN_EX+"How many you want to take?")
                try:
                    answer = int(answer)
                    assert answer<=k and answer<=n and answer>=1
                    break
                except:
                    print(Fore.LIGHTBLUE_EX+"That's not possible,don't cheat ;|")
            n -= answer
        if n==0:
            if turn:
                print(Fore.LIGHTCYAN_EX+"I won!")
            else:
                print(Fore.LIGHTCYAN_EX+"You won!")
            print("---------------------------------------------------")
            break
        
        turn = not turn
    menu()





def about():
    print(Fore.LIGHTMAGENTA_EX+'''
    When I was 16 years old and I had started programming with C language for the computer student Olympiad, I was solving many classic questions. I happened to see some of my codes a few days ago and I decided to rewrite some of them. These code models and solves a very simple game that is related to the topic of game theory.
    Rules:
    The game starts with two people eating pizza At the beginning of the game, they decide to divide this pizza into N pieces and agree to eat some pieces from this pizza, which is at least 1, and at most M, which is a set value. The winner is the one who can eat the last piece of pizza.
    ''')
    menu()

def exit():
    print(Fore.LIGHTCYAN_EX+"GodBye")

def menu():
    print(Fore.LIGHTBLUE_EX+"1 - Play")
    print("2 - About")
    print("3 - Exit")
    option=1
    option = input("Please Choose an option:")
    try:
        option = int(option)
        assert option in [1,2,3]
    except:
        print(Fore.RED+"Invalid options!")
        menu()
        return
    if option==1:
        play()
    elif option==2:
        about()
    elif option==3:
        exit()

if __name__=='__main__':
    welcome()
    menu()
