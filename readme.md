<h1 align="center">Local Composer - By Ben Rothman
	<img src="https://img.shields.io/static/v1?ConciergeWPVersion=&message=v1.0.0&label=&color=999&style=flat-square"><br />
</h1>
<p align="center">
	(NOT affiliated with Symfony or Symfony Composer)
</p>

<p align="center">A program to migrate your files and settings to a new computer. First, run it on the old computer to automate the copying of your files and settings into a suitcase directory (pack). Then, you copy the local-composer directory onto the new computer and you run the program again in "unpacking mode" to unpack the suitcase directory and copy all of your old files and settings onto the new computer with the file and folder structures preserved (unpack).</p>
<p align="center">
	<br />
	<img src="https://img.shields.io/badge/python-v3.7-blue" alt="Python Version">
</p>

## Usage Overview
Create a directions txt file in the same directory as `local-composer.py` with one instruction per line (either shell commands to execute starting with a "$", or manual commands that cannot be executed by the shell ie: take a cell phone picture of X and just serve as reminders to the human operator to do a certain thing).

If the instruction is too complex for an instruction line and cannot be broken into multiple lines (for instance, download a program and run the installer and enter the registration key) you may start a line with "manual:", which will print out the entered line as a written prompt that you can do and Local Composer will not move to the next command until you press 'Enter', confirming that the manual command is done.

Note: As with all code, you can comment out a line so that it will not be run.  Commenting in the instructions file can be done by starting a line with '##'.

## How To Use
First you need to pack your old computer into a "suitcase".  Start by cloning the local-composer GitHub repo onto your old computer and creating the instructions file (example files can be found in the 'Sample Instructions' directory) in the same directory as the python file. You can then run the program with the following command to pack your old computer:

`python3 local-composer.py -p packing_filename.txt`

Once you have packed your old computer into a suitcase, you need to unpack the suitcase on your new computer preserving the files and settings.  Copy the whole 'local-composer' directory onto removable media from the old computer, then copy that folder from the removable media onto the new computer. Replace the packing instructions file you made with a new, similar unpacking instructions file (examples can be found in "Sample Instructions').  When the unpacking instructions file is in place, run Local Composer again but this time with the argument shown below to unpack the suitcase:

`python3 local-composer.py -u unpacking_filename.txt`

## Instruction File Notes:
- Use '$ ' before a command for it to be executed as a shell command.

- Use 'manual: ' before a command for it to be printed to the terminal and await a 'return' from the user before continuing.  Think of it like a reminder to do something yourself.

- Comment lines out or add lines as notes by adding '## ' to the start of a line

- Use '!!/' at the beginning of a path as a way to refer to the suitcase directory in the instructions file.  So for instance !!/desktop would refer to a directory named 'desktop' inside of the suitcase directory.

## FAQ
### The command is not finding my directions file, what should I do?
Make sure you did not use spaces in the filename and that the directions file is in the same folder as local-composer.py

### Is this program in any way associated with Symfony Composer?
No.  In no way.  Symfony's Composer was part of the inspiration for the idea but there is no commonality.

Enjoy!
