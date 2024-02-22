<h1 align="center">Local Composer 2 - By Ben Rothman
	<img src="https://img.shields.io/static/v1?ConciergeWPVersion=&message=v2.0.0&label=&color=999&style=flat-square"><br />
</h1>
<p align="center">
	(NOT affiliated with Symfony or Symfony Composer)
</p>

<p align="center">A program to migrate your files and settings to a new computer. First, run it on the old computer to automate the copying of your files and settings into a suitcase directory (pack). Then, you copy the local-composer directory onto the new computer and you run the program again in "unpacking mode" to unpack the suitcase directory and copy all of your old files and settings onto the new computer with the file and folder structures preserved (unpack).</p>
<p align="center">
	<br />
	<img src="https://img.shields.io/badge/python-v3.7-blue" alt="Python Version">
</p>

## Usage Overview - V1 TO V2 UNDER CONSTRUCTION
Enter create mode and choose things you want to install from our library and instructions to install those things will be added to a directions file in the same directory as `local-composer.py`. The file will have one instruction per line.  You can customize the directions file and add your own commands in addition to the library commands.

Note: As with most code, you can comment out a line so that it will not be run.  Commenting in the instructions file can be done by starting a line with '##'.

## How To Use
local-composer is a migration tool for when you get a new computer and you have to set it up by copying things from your old computer and you have to install things from the internet.

### On the old computer:
1. Execute `python3 local-composer.py create packing {filename}` to create an instructions file for local-composer.
2. You will be shown a menu where you can choose to copy common files from your original computer so make your selections based on what you want to save.
3. When you are done building the packing list, you can start the packing with the command: `python3 local-composer.py -p {filename}` and your suitcase will be created with copies of your important files.
4. Copy the whole 'local-composer' directory onto removable media from the old computer.

### On the new comoputer:
1. Copy the local-composer directory from the removable media onto the new computer.
2. Execute `python3 local-compooser.py -u {filename}` to unpack your suitcase.

## Instruction File Documentation (How to read or add manual steps):
- Start a line with '$ '  for it to be executed as a shell command.

- Start a line with 'manual: ' for it to be printed to the terminal awaiting a 'return' from the user before continuing to prompt them to do a manual task such as registering software or calling someone.

- Comment lines out or add lines as notes by adding '## ' to the start of a line

- Use '!!/' at the beginning of a path as a way to refer to the suitcase directory from within the instructions file.  So for instance !!/desktop would refer to a directory named 'desktop' inside of the suitcase directory.

## FAQ
### The command is not finding my directions file, what should I do?
Make sure you did not use spaces in the filename and that the directions file is in the same folder as local-composer.py

### Is this program in any way associated with Symfony Composer?
No.  In no way.  Symfony's Composer was part of the inspiration for the idea because that is a very nice piece of software but there is no relation.

Enjoy!
