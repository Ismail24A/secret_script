from os import system, remove


def spacing():
    system('cls')
    for i in range(1, 10):
        print()


def interface():
    system("color a")
    system('cls')
    print('''
    ######################################################

    #  ███████╗███████╗ ██████╗██████╗ ███████╗████████╗ #  
    #  ██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝ #   
    #  ███████╗█████╗  ██║     ██████╔╝█████╗     ██║    # 
    #  ╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║    #   
    #  ███████║███████╗╚██████╗██║  ██║███████╗   ██║    #  
    #  ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝    #   

    ######################################################
    ''')


def pause():
    system('pause >> null.txt')
    remove('null.txt')
    system('EXIT')