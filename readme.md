<h1 align="center">Suitcase - By Ben Rothman
	<img src="https://img.shields.io/static/v1?ConciergeWPVersion=&message=v1.0.0&label=&color=999&style=flat-square">
</h1>

<p align="center">A program to run to migrate to a new computer by running it on the old computer before getting rid of it to automate the copying of your files and settings into a suitcase directory (pack). Then, you copy the suitcase directory onto the new computer and you run it to unpack the suitcase directory to copy all of your old files and settings onto the new computer with the file and folder structure preserved (unpack).</p>

<p align="center">
		<img src="https://img.shields.io/badge/python-v3.7-blue" alt="Python Version">
</p>


## Usage Overview
Create a directions txt file in the same directory as the main file with one instruction per line (either shell commands to execute starting with a "$", or manual commands that cannot be executed by the shell ie: take a cell phone picture of X).  If the instruction is too complex for an instruction line and cannot be broken into nultiple lines (for instance, download a program and run the installer and enter the registration key) you may start a line with "manual:", which will print out the entered line as a written prompt that you can do and Suitcase will not move to the next command until you press 'Enter'.

Note: As with all code, you can comment out a line during a run.  Commenting in the instructions file can be done by starting a line with '##'.

## How To Use
First you need to pack your old computer into the suitcase.  Clone the Suitcase repository from Github, then create the packing instructions text file in the same directory as the python file. You can then run the program with the following command to pack your old computer:

`python3 suitcase.py -p packing_filename.txt`

Once you have packed your old computer into the suitcase, you need to unpack the suitcase on your new computer to preserve the files and settings.  Copy the 'Suitcase' directory onto removable media, copy that directory from the removable media onto the new computer and run suitcase again, but this time with the argument shown below to unpack the suitcase:

`python3 suitcase.py -u unpacking_filename.txt`

Enjoy!