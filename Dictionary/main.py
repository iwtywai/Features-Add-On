import sys, os, sqlite3

def clear():
    #os.system("clear")
    os.system("cls")

#init
database=sqlite3.connect("dictionary.database")
cursor=database.cursor()
clear()

def split():
    print("----------")

def main():
    print("Welcome to Dictionary App.")
    split()
    print("0. Exit")
    print("1. Add New Word")
    print("2. Delete Word")
    print("3. Modify Word")
    print("4. Show All Words")
    split()
    select=input("> ")
    try:
        selected=int(select)
    except:
        print("Wrong choice.")
        input("Press Enter to go back.")
        main()
    if not selected<=4:
        print("Wrong choice.")
        input("Press Enter to go back.")
        main()
    else:
        exec("menu"+str(selected)+"()")

if __name__ == "__main__":
    main()