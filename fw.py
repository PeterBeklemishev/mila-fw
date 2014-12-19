#!/usr/bin/python
#
#	-p <port>
#	-e #erase before flashing
#	-f <file_to_flash>
#	-v #verify
#	-r #run after flashing
#	-V #verbose output
#
#


import sys, getopt
port = ''
inputfile = ''
verbose = False

def start(self):
	print("lol")

def erase():
	'''
	'''
	print ("erasing...")

def verify():
	'''
	'''
	print ("verifying...")

def program():
	'''
	'''
	print (port,inputfile,"flashing...")

def run():
	'''
	'''
	print ("running...")


def main(argv):
	acts = []
	try:
		opts, args = getopt.getopt(argv,"p:Vef:vr")
	except getopt.GetoptError:
		print('test.py -p <inputfile> -i <outputfile> -v -e')
		sys.exit(2)

	for opt, arg in opts:
		if opt == "-p":
			global port 
			port = arg
		elif opt == "-V":
			global verbose 
			verbose = True

		elif opt == "-e":
			acts.append("erase")

		elif opt == "-f":
			global inputfile 
			inputfile = arg
			acts.append("flash")
		
		elif opt == "-v":
			acts.append("verify")
		
		elif opt == "-r":
			acts.append("run")
	return acts
	


if __name__ == "__main__":
	acts = main(sys.argv[1:])

	#do the thing!s
	if "erase" in acts:
		erase()
		print("done")
	if "flash" in acts:
		program()
		print("done")
	if "verify" in acts:
		verify()
		print("done")	
	if "run" in acts:
		run()
		print("done")