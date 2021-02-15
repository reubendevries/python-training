options = """ Please choose your option from the list below:\n
1.\t Learn Python\n
2.\t Learn Java\n
3.\t Learn Go\n
4.\t Learn Rust\n
5.\t Learn JavaScript\n
6.\t Learn C\n
7.\t Learn Swift\n
8.\t Learn Perl\n
9.\t Learn Ruby\n
0.\t Quit\n"""
choose = None
while True:
    if choose == "0":
        break
    elif choose in "123456789":
        print("You chose {}".format(choose))
    else:
        print(options)
    
    choose = input()