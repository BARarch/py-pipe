import sys
import os
import subprocess
import shutil
import cs_utils
from datetime import datetime


pa = os.getcwd()

def init(chal):
    ## Create Challenge Input Folder
    subprocess.call(f'mkdir {chal}Input')
    ## Create Challenge File
    subprocess.call(f'touch {chal}.py')

def initCsStub(chal):
    date = datetime.now().strftime('%y%m%d')
    init(chal)
    subprocess.call(f'echo ...initializing codesignal stub for {chal}')
    subprocess.call('echo Enter challenge function stub below:')
    subprocess.call(f'echo #Date Started: {date} >> {chal}.py', shell=True)
    subprocess.call(f'cat testEnvironmentHeader.py >> {chal}.py', shell=True)
    subprocess.call(f'cat {chal}.py', shell=True)
    subprocess.call(f'cat >> {chal}.py', shell=True)
    subprocess.call(f'cat testEnvironmentFooter_CS.py >> {chal}.py', shell=True)

def initHrStub(chal):
    date = datetime.now().strftime('%y%m%d')
    init(chal)
    subprocess.call(f'echo ...initializing codesignal stub for {chal}')
    subprocess.call('echo Enter code stub below:')
    subprocess.call(f'echo #Date Started: {date} >> {chal}.py', shell=True)
    subprocess.call(f'cat testEnvironmentHeader.py >> {chal}.py', shell=True)
    subprocess.call(f'cat {chal}.py', shell=True)
    subprocess.call(f'cat >> {chal}.py', shell=True)

def case(chal):
    ## Create Text file for tesk case in the challenge input folder
    digit = len(os.listdir(f'{pa}\{chal}Input'))
    caseName = f'{chal}Input/input{str(digit).rjust(3, "0")}'
    subprocess.call(f'touch {caseName}.txt')
    subprocess.call('echo Paste testcase text:')
    subprocess.call(f'cat >> {caseName}.txt', shell=True)


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
    helpMode = False
    comStr = tuple(sys.argv)
    ## Helpmode Setup Code
    if comStr[-1] == '-h' or comStr[-1] == '--help':
        helpMode = True
        ## Chop off the help command from the command string
        ## Proceed with the helpmode flag up
        comStr = comStr[:-1]

    if len(comStr) >= 3:
        g, chalName, command = comStr[:3]
        #comStr = comStr[3:]
        #print(f"Challenge:   {chalName}")
        #print(f"Command:     {command}")
        if command == "--init" or command == "-i":
            comStr = comStr[3:]
            if comStr and (comStr[0] == '--codesignal' or comStr[0] == '-cs'):
                initCsStub(chalName)
            elif comStr and (comStr[0] == '--hackerrank' or comStr[0] == '-hr'):
                initHrStub(chalName)
            else:
                init(chalName)
        elif command == '--case' or command == "-c":
            case(chalName)

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

