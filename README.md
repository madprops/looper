Keeps commands running in a loop.

You can change the delay in seconds between each command.

You can set the number of times the command runs.

### Usage: 

`python3 looper.py -d 1 -n 3 date`

This runs 'date' every second 3 times, then stops.

If n is left empty or 0 it will run indefinitely until interrupted.

Call looper with no arguments to enter the interactive mode.