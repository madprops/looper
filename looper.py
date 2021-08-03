import os
import sys
import time
import argparse
from typing import Tuple

class Info:
	@staticmethod
	def defaults() -> Tuple[str, int, int]:
		return ("", 1, 0)

	def __init__(self, command: str, delay: int, counter: int) -> None:
		self.command = command
		self.delay = delay
		self.counter = counter
		self.infinite = counter <= 0
	
	def iteration(self) -> bool:
		self.counter -= 1
		return self.counter == 0

def main() -> None:
	try:
		if len(sys.argv) < 2:
			info = get_input()
		else:
			info = parse_arguments()
		run(info)
	except KeyboardInterrupt:
		pass

def get_input() -> Info:
	command, delay, counter = Info.defaults()

	try:
		command = input("Command: ").strip()
		if not command: exit(1)

		idelay = input("Delay (seconds): ").strip()
		if idelay: delay = int(idelay)

		icounter= input("Iterations (Default: infinite): ").strip()
		if icounter: counter = int(icounter)
	except:
		exit(1)
		
	return Info(command, delay, counter)

def parse_arguments() -> Info:
	command, delay, counter = Info.defaults()

	parser = argparse.ArgumentParser()
	parser.add_argument("command", type=str)
	parser.add_argument("-d", help="Delay in seconds")
	parser.add_argument("-n", help="Number of counter")
	args = parser.parse_args()

	try:
		if args.command != None:
			command = str(args.command)
		if args.d != None:
			delay = int(args.d)
		if args.n != None:
			counter = int(args.n)
	except:
		exit(1)
	
	return Info(command, delay, counter)

def run(info: Info) -> None:
	while True:
		os.system(info.command)
		if not info.infinite: 
			if info.iteration(): break
		time.sleep(info.delay)

if __name__ == "__main__": main()