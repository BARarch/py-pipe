import sys
import os
import subprocess
import shutil

pa = os.getcwd()

def init(chal):
    subprocess.call(f'mkdir {chal}Input')
    subprocess.call(f'touch {chal}.py')

def case():
    pass

def testChal(chal):
    
    ## Get cases from challenge folder
    ##print(list(map(case_name, os.listdir(f'{pa}\{chal}Input'))))
    #testCases = ['input000', 'input006', 'input001']

    testCases = map(case_name, os.listdir(f'{pa}\{chal}Input'))

    for testCase in testCases:
        caseStream = open(f'{pa}\{chal}Input\{testCase}.txt')
        #caseStream = open(f'{os.getcwd()}\{chal}Input\input000.txt')
        #subprocess.call("python restaurantMath.py", stdin="caseStream", shell=True)
        subprocess.call(f"python {chal}.py", stdin=caseStream)
        caseStream.close()

        ## Print Output
        show_results(testCase)
        
    return

def case_name(fileName):
    return fileName[:-4]

def show_results(testCase):
    print(f'--Results for: {testCase}--')
    subprocess.call(f"cat {os.environ['OUTPUT_PATH']}")
    print()

def clear_results():
    resultsBuffer = open(os.environ['OUTPUT_PATH'], 'w')
    resultsBuffer.close()

def submitted(chal):
    ## Delete TestCase Folder
    shutil.rmtree(f'{pa}\{chal}Input')
    ## Move project file
    shutil.move(f'{pa}\{chal}.py',f'..\{chal}.py')




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
            init(chalName)
        elif command == '--case' or command == "-c":
            pass
        elif command == '--test' or command == "-t":
            clear_results()
            testChal(chalName)
        elif command == '--submitted' or command == "-s":
            clear_results()
            submitted(chalName)

        else:
            print(f"--Unrecognisable Command: {command}--")
    else:
        print("--Impropper Number of Arguments--")

    ## For Test
    #subprocess.call()
    #s = subprocess.check_output(["echo", "Hello World!"])
    #print("s = " + str(s))

