import sys
import os
import subprocess

def init():
    pass

def case():
    pass

def testChal():
    pass

if __name__ == "__main__":
    ## Get Challenge File and Command
    '''groover.py challengeFilename --command
    
        commands
        --init          initializes challege set creates case folder
        --case          adds cases to challenge set
        --test          test challenge code against cases
        --submitted     closes challenge and removes cases

    '''

    if len(sys.argv) == 3:
        g, chalName, command = sys.argv
        print(f"Challenge:   {chalName}")
        print(f"Command:     {command}")
        if command == "--init" or command == "-i":
            pass
        elif command == '--case' or command == "-c":
            pass

        elif command == '--test' or command == "-t":
            pass
        else:
            print(f"--Unrecognisable Command: {command}--")
    else:
        print("--Impropper Number of Arguments--")

    ## For Test
    #subprocess.call()
    #s = subprocess.check_output(["echo", "Hello World!"])
    #print("s = " + str(s))

