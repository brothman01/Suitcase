<h1 align="center">Local Composer - By Ben Rothman
	<img src="https://img.shields.io/static/v1?ConciergeWPVersion=&message=v1.0.0&label=&color=999&style=flat-square">
</h1>

<p align="center">A program to run to migrate your files and settings to a new computer. First, run it on the old computer to automate the copying of your files and settings into a suitcase directory (pack). Then, you copy the suitcase directory onto the new computer and you run the program again in unpacking mode to unpack the suitcase directory and copy all of your old files and settings onto the new computer with the file and folder structures preserved (unpack).</p>
**NOT affiliated with Symfony or part of Symfony Composer**
<p align="center">
	<br />
	<img src="https://img.shields.io/badge/python-v3.7-blue" alt="Python Version">
</p>


## Usage Overview
Create a directions txt file in the same directory as the main file with one instruction per line (either shell commands to execute starting with a "$", or manual commands that cannot be executed by the shell ie: take a cell phone picture of X).  If the instruction is too complex for an instruction line and cannot be broken into multiple lines (for instance, download a program and run the installer and enter the registration key) you may start a line with "manual:", which will print out the entered line as a written prompt that you can do and Suitcase will not move to the next command until you press 'Enter'.

Note: As with all code, you can comment out a line during a run.  Commenting in the instructions file can be done by starting a line with '##'.

## How To Use
First you need to pack your old computer into the suitcase.  Start by cloning the Suitcase GitHub repo onto your old computer and create the instructions file (example files can be found in the 'Sample Instructions' directory) in the same directory as the python file. You can then run the program with the following command to pack your old computer:

`python3 suitcase.py -p packing_filename.txt`

Once you have packed your old computer into the suitcase, you need to unpack the suitcase on your new computer to preserve the files and settings.  Copy the whole 'Suitcase' directory onto removable media, then copy that directory from the removable media onto the new computer and replace the packing instructions file you made with a new, similar unpacking instructions file (examples can be found in the "Sample Instructions' directory).  When the unpacking instructions file is in place, run suitcase again but this time with the argument shown below to unpack the suitcase:

`python3 suitcase.py -u unpacking_filename.txt`

## Instruction File Notes:
- Use '$ ' before a command for it to be executed as a shell command.

- Use 'manual: ' before a command for it to be printed to the terminal and await a 'return' from the user before continuing.  Think of it like a reminder to do something yourself.

- Comment lines out or add lines as notes by adding '## ' to the start of a line

- Use '!!/' at the beginning of a path as a way to refer to the suitcase directory in the instructions file.  So for instance !!/desktop would refer to a directory named 'desktop' inside of the suitcase directory.

Enjoy!
