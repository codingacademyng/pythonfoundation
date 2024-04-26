import random
allusers = {
    1249:["Adeboal Ojo", "ade12", 4000]
}

def betingHome():
    user_inp = input("Enter 1 to login.\n2 for registration ")
    if user_inp == "1":
        log()
    elif user_inp == "2":
        reg()

def reg():
    user_info = []
    fullname = input("Enter your fullname ")
    password = input("Enter your password ")
    user_info.append(fullname)
    user_info.append(password)
    user_info.append(0)
    bet_id = random.randrange(1000, 2000)
    allusers.update({bet_id:user_info})
    print('Registertion successful')
    log()

def log():
    global bet_info
    bet_info = int(input("Enter your bet id"))
    if bet_info in allusers.keys():
        passw = input("Enter your password ")
        if allusers.get(bet_info)[1] == passw:
            print("Login successful")
            game()

def game():
    game_inp = input("Welcome to your betting app\n1 to fund wallet\n2 to check bal\n3 to play game ")
    if game_inp == "1":
        fund()
    elif game_inp == "2":
        checkbal()
    elif game_inp == "3":
        playgame()

def fund():
    amount = int(input("ENter the amount you want to deposit "))
    acct_bal = allusers.get(bet_info)[2]
    new_bal = amount + acct_bal
    allusers.get(bet_info)[2] = new_bal
    print("Deposit succesfukl")
    game()

def checkbal():
    acct_bal = allusers.get(bet_info)[2]
    print(f"Your account balance is {acct_bal}")
    game()

def playgame():
    acct_bal = allusers.get(bet_info)[2]
    print("Instructions.....")
    stake = int(input("Enter amount you want to stake "))
    if stake > acct_bal:
        print("Insufficient funds")
        user_inp = input("Enter 1 to stake again and any other key to go home ")
        if user_inp == "1":
            playgame()
        else:
            game()
    else:
        allusers.get(bet_info)[2] = acct_bal - stake
        count = 0
        colorList = ["red", "blue", "magenta", "white", "pink", "yellow"]
        comp_choice = random.sample(colorList, 3)
        user_color = []
        for i in range(3):
            inp = input(f"Enter color {i + 1} ")
            user_color.append(inp)
        for choice in user_color:
            if choice in comp_choice:
                count += 1
        reward = count * 2
        if count == 0:
            print("Sorry , you lost ypour wef")
        else:
            bet_bal = stake * reward
            new_bal = acct_bal + bet_bal
            allusers.get(bet_info)[2] = new_bal
            print(f"You won {bet_bal} after getting {count} colors right")
        play_inp = input("Enter 1 to play agian or any key to go home ")
        if play_inp == "1":
            playgame()
        else:
            game()

# comp_choice = ["red", "blue", "green"]
# user_choice = ["white", "red", "purple"]

# count = 0

# for choice in user_choice:
#     if choice in comp_choice:
#         count += 1