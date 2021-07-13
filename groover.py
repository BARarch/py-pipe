import sys
import os
import subprocess

def init():
    pass

def case():
    pass

def testChal(chal):
    testCases = ['input000', 'input006', 'input001']

    for testCase in testCases:
        caseStream = open(f'{os.getcwd()}\{chal}Input\{testCase}.txt')
        #caseStream = open(f'{os.getcwd()}\{chal}Input\input000.txt')
        #subprocess.call("python restaurantMath.py", stdin="caseStream", shell=True)
        subprocess.call(f"python {chal}.py", stdin=caseStream)
        caseStream.close()

    
        ## Print Output
        showResults(testCase)
        

    return

def showResults(testCase):
    print(f'--Results for: {testCase}--')
    subprocess.call(f"cat {os.environ['OUTPUT_PATH']}")
    print()

def clearResults():
    resultsBuffer = open(os.environ['OUTPUT_PATH'], 'w')
    resultsBuffer.close()



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
        #print(f"Challenge:   {chalName}")
        #print(f"Command:     {command}")
        if command == "--init" or command == "-i":
            pass
        elif command == '--case' or command == "-c":
            pass

        elif command == '--test' or command == "-t":
            clearResults()
            testChal(chalName)
        else:
            print(f"--Unrecognisable Command: {command}--")
    else:
        print("--Impropper Number of Arguments--")

    ## For Test
    #subprocess.call()
    #s = subprocess.check_output(["echo", "Hello World!"])
    #print("s = " + str(s))

