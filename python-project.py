# write your code here
print("""---------
|       |
|       |
|       |
---------""")
'''useri = input("Enter cells: ")
# splitted = [at for at in useri]
print("---------")
print(f"| {useri[0]} {useri[1]} {useri[2]} |")
print(f"| {useri[3]} {useri[4]} {useri[5]} |")
print(f"| {useri[6]} {useri[7]} {useri[8]} |")
print("---------")'''
'''separated = []
ii = 1
for _ in range(3):
    init = []
    for t in useri[((ii * 3) - 3):(ii * 3)]:
        init.append(t)
    ii += 1
    separated.append(init)'''
user = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
useri = ["", "", "", "", "", "", "", "", ""]
count = 1 
while True:
    user_input = input().split()
    try:
        i = int(user_input[0])
        j = int(user_input[1])
        index = ((i - 1) * 3) + j - 1
        if i > 3 or j > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            if user[i - 1][j - 1] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                if count % 2 == 1:
                    user[i - 1][j - 1] = "X"
                    useri[index] = "X"
                    print("---------")
                    for tell in user:
                        print("|", " ".join(tell), "|")
                    print("---------")
                else:
                    user[i - 1][j - 1] = "O"
                    useri[index] = "O"
                    print("---------")
                    for tell in user:
                        print("|", " ".join(tell), "|")
                    print("---------")
                count += 1
                if useri[0] == useri[1] == useri[2] == "O" or useri[0] == useri[3] == useri[6] == "O" or useri[0] == useri[4] == useri[8] == "O" or useri[1] == useri[4] == useri[7] == "O" or useri[2] == useri[5] == useri[8] == "O" or useri[3] == useri[4] == useri[5] == "O" or useri[6] == useri[7] == useri[8] == "O" or useri[2] == useri[4] == useri[6] == "O":
                    print("O wins")
                    break
                elif useri[0] == useri[1] == useri[2] == "X" or useri[0] == useri[3] == useri[6] == "X" or useri[0] == useri[4] == useri[8] == "X" or useri[1] == useri[4] == useri[7] == "X" or useri[2] == useri[5] == useri[8] == "X" or useri[3] == useri[4] == useri[5] == "X" or useri[6] == useri[7] == useri[8] == "X" or useri[2] == useri[4] == useri[6] == "X":
                    print("X wins")
                    break
                elif not (useri[0] == useri[1] == useri[2] == "O" or useri[0] == useri[3] == useri[6] == "O" or useri[0] == useri[4] == useri[8] == "O" or useri[1] == useri[4] == useri[7] == "O" or useri[2] == useri[5] == useri[8] == "O" or useri[3] == useri[4] == useri[5] == "O" or useri[6] == useri[7] == useri[8] == "O" or useri[2] == useri[4] == useri[6] == "O") and not (useri[0] == useri[1] == useri[2] == "X" or useri[0] == useri[3] == useri[6] == "X" or useri[0] == useri[4] == useri[8] == "X" or useri[1] == useri[4] == useri[7] == "X" or useri[2] == useri[5] == useri[8] == "X" or useri[3] == useri[4] == useri[5] == "X" or useri[6] == useri[7] == useri[8] == "X" or useri[2] == useri[4] == useri[6] == "X"):
                    if useri.count("") == 0:
                        print("Draw")
                        break     
    except:
         print("You should enter numbers!")   
        
"""if splitted.count("X") - splitted.count("O") > 1 or splitted.count("O") - splitted.count("X") > 1:
    print("Impossible")
else:
    if (useri[0] == useri[1] == useri[2] == "X" or useri[0] == useri[3] == useri[6] == "X" or useri[0] == useri[4] == useri[8] == "X" or useri[1] == useri[4] == useri[7] == "X" or useri[2] == useri[5] == useri[8] == "X" or useri[3] == useri[4] == useri[5] == "X" or useri[6] == useri[7] == useri[8] == "X" or useri[2] == useri[4] == useri[6] == "X") and (useri[0] == useri[1] == useri[2] == "O" or useri[0] == useri[3] == useri[6] == "O" or useri[0] == useri[4] == useri[8] == "O" or useri[1] == useri[4] == useri[7] == "O" or useri[2] == useri[5] == useri[8] == "O" or useri[3] == useri[4] == useri[5] == "O" or useri[6] == useri[7] == useri[8] == "O" or useri[2] == useri[4] == useri[6] == "O"):
        print("Impossible")
    elif useri[0] == useri[1] == useri[2] == "O" or useri[0] == useri[3] == useri[6] == "O" or useri[0] == useri[4] == useri[8] == "O" or useri[1] == useri[4] == useri[7] == "O" or useri[2] == useri[5] == useri[8] == "O" or useri[3] == useri[4] == useri[5] == "O" or useri[6] == useri[7] == useri[8] == "O" or useri[2] == useri[4] == useri[6] == "O":
        print("O wins")
    elif useri[0] == useri[1] == useri[2] == "X" or useri[0] == useri[3] == useri[6] == "X" or useri[0] == useri[4] == useri[8] == "X" or useri[1] == useri[4] == useri[7] == "X" or useri[2] == useri[5] == useri[8] == "X" or useri[3] == useri[4] == useri[5] == "X" or useri[6] == useri[7] == useri[8] == "X" or useri[2] == useri[4] == useri[6] == "X":
        print("X wins")
    elif not (useri[0] == useri[1] == useri[2] == "O" or useri[0] == useri[3] == useri[6] == "O" or useri[0] == useri[4] == useri[8] == "O" or useri[1] == useri[4] == useri[7] == "O" or useri[2] == useri[5] == useri[8] == "O" or useri[3] == useri[4] == useri[5] == "O" or useri[6] == useri[7] == useri[8] == "O" or useri[2] == useri[4] == useri[6] == "O") and not (useri[0] == useri[1] == useri[2] == "X" or useri[0] == useri[3] == useri[6] == "X" or useri[0] == useri[4] == useri[8] == "X" or useri[1] == useri[4] == useri[7] == "X" or useri[2] == useri[5] == useri[8] == "X" or useri[3] == useri[4] == useri[5] == "X" or useri[6] == useri[7] == useri[8] == "X" or useri[2] == useri[4] == useri[6] == "X"):
        if splitted.count("_") == 0:
            print("Draw")
        else:
            print("Game not finished")"""
