import sys, os, time, argparse

def split():
    print("----------")

def clear():
    os.system("clear")

def translate(cmd):
    cmds=split(cmd," ")
    if cmds[0]=="exit":
        exit(0)
    elif cmds[0]=="range":
        rangeONum=[int(cmds[2]),int(cmds[3])]
        rangeONum=sorted(rangeONum)
        exec(cmds[1]+"=0")
        exec(cmds[1]+"range=["+string(rangeONum[0])+","+string(rangeONum[1])+"]")
    elif cmds[0]=="for":
        pass
    else:
        pass

def commandLine():
    while True:
        cmd=input("> ")
        translate(cmd)

def compile():
    scadd=input("Source Code Location: ")
    if not scadd[-4:]==".rdg":
        print("Fatal Error: No standard rdg code is given.")
        exit(1)
    if exist(scadd):
        filepointer=open(scadd,"r")
        pass
    else:
        print("Fatal Error: File does not exist.")
        exit(1)

def exist(filenm):
    return os.path.exists(filenm)

def showHelp():
    content='''
    RandomDataGenerator ver1.0
    Usage: RandomDataGenerator [-c|-h|-r|-v] (No additional Arguments needed)
        -h: (--help)            Show this page then exit.
        -c: (--cmd | --command) Run application in command line mode.
        -r: (--run)             Translate a .rdg source code (if not existed) and run once.
        -v: (--version)         Show version then exit.
    '''
def version():
    print("RandomDataGenerator ver1.0")
    print("Author: iwtywai")
    print("Copyright 2019-2020 iwtywai all rights reserved")

def select(arg,*conds):
    listconds=list(conds)
    for i in range(len(listconds)-1):
        if arg==listconds[i]:
            return i
    else:
        return -1

args=sys.argv[1:]
if len(args)>1:
    print("Fatal Error: Too many arguments.")
    exit(1)
else:
    ans=select(args,"--commands","--cmd","-c","-r","--run","-h","--help","-v","--version")
    if ans>=0 and ans<=2:
        commandLine()
    elif ans>=3 and ans<=4:
        compile()
    elif ans>=5 and ans<=6:
        showHelp()
    elif ans>=7 and ans<=8:
        version()
    else:
        print("Fatal Error: Argument(s) invalid.")
        exit(1)