# Suitcase by Ben Rothman
# python3 suitcase.py -<u|p|h> instructions_file.txt
import os
import re
import sys
import os.path
from time import sleep
import subprocess
from datetime import datetime

# define variables
today = datetime.now()
suitcase_path = os.path.dirname(os.path.abspath(__file__)) + "/suitcase/"
raw_directions = []
directions = []
options = sys.argv[1:]

# define color printing variables
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
OKCYAN = '\033[36m'
YELLOW = '\033[33m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def step(line):
    """Interperets and executes a command"""
    if (line.startswith('##')): ## line is a comment
        my_print( UNDERLINE + line[3 :] + ENDC)
        # Skip line
    elif (current_line.startswith('SKIP ')): # Skip the line
        print(FAIL + current_line[5:] + ' SKIPPED' + ENDC)
        sleep(1.0)
    elif (current_line.startswith('manual: ')):  # manual line (line calls for user execution based on written cue)
        my_print(YELLOW + BOLD + 'manual: ' + ENDC + line[8:] + ENDC)
        nun = input('Press Enter when complete.')
        print('')
    elif (current_line.startswith('$ ')): # execute shell command
        my_print(UNDERLINE + 'Execute: ' + line[2:] + ENDC)
        my_print(OKCYAN + '$ ' + line[2:] + ENDC)
        ## create subprocess for the command
        proc = subprocess.Popen(line[2:], stdout=subprocess.PIPE, shell=True)
        (output, err) = proc.communicate()
        ## Wait for date to terminate. Get return returncode ##
        p_status = proc.wait()
        if (p_status == 0):
            print(OKGREEN + 'Execution Successful ' + BOLD + '' + ENDC)
        else:
            print(FAIL + "Return: " + str(p_status) + "\n" + str(err) + ENDC)

# define 'my_print()
def my_print(words):
    """prints text with effect"""
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write("\n")






###### PROGRAM ######
# Clear the terminal
my_print(chr(27) + "[2J")
my_print('Welcome to Suitcase ' + str(today))

if (not os.path.exists('suitcase')):
    os.system('mkdir suitcase')


option = options[0]
instructions_file = options[1]

# Behave based on arguments
if (option == '-h' or option == '-help'): # help
    print('-----')
    print(UNDERLINE + '-h | help' + ENDC)
    my_print('This option my_prints out the different options that can be used to run the suitcase.')
    my_print('')
    my_print(UNDERLINE + '-p | pack' + ENDC)
    my_print('This option tells the script to pack the suitcase based on the packing list.')
    my_print('')
    my_print(UNDERLINE + '-u | unpack' + ENDC)
    my_print('This option unpacks the suitcase based on the unpacking list.')
    my_print('')
    print('-----')
elif (option == '-p'): # pack
    # read each line from the packing file put them in array $raw_directions
    with open(instructions_file) as my_file:
        for line in my_file:
            raw_directions.append(line)

    # Replace !!/ with suitcase directory in all lines of array $raw_directions and push them to array $directions
    for i in range(len(raw_directions)):
        directions.append(re.sub('!!\/', suitcase_path, raw_directions[i]))

    # my_print Header
    my_print(HEADER + UNDERLINE + 'PACKING LIST:' + ENDC + "\n")

    # Execute each line of array $directions
    for current_line in directions:
        step(current_line)

    my_print('Packing Complete.')
elif ('-u' in option): #unpack
    # Clear the terminal
    my_print(chr(27) + "[2J")

    # my_print Header
    my_print(HEADER + UNDERLINE + 'UNPACKING LIST:' + ENDC + "\n")

    # read each line from the unpacking file put them in array $raw_directions
    with open(instructions_file) as my_file:
        for line in my_file:
            raw_directions.append(line)

    # Replace !!/ with suitcase directory in all lines of array $raw_directions and push them to array $directions
    for i in range(len(raw_directions)):
        directions.append(re.sub('!!\/', suitcase_path, raw_directions[i]))

    # Execute each line of array $directions
    for current_line in directions:
        step(current_line)

    my_print('Unpacking Complete.')

##### END PROGRAM #####