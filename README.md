Keeps commands running in a loop.

You can change the delay in seconds between each command.

You can set the number of times the command runs.

### Usage: 

`looper date -d 3 -n 100.`

This runs 'date' every 3 seconds 100 times, then stops.

If n is left empty or 0 it will run indefinitely until interrupted.

Call looper with no arguments to enter the interactive mode.