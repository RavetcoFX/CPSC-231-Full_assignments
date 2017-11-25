import sys

input_file = open(sys.argv[1])
line = input_file.readline()
count = 1
while line:
       print("Line {}: {}".format(count, line.strip()))
       line = input_file.readline()
       count += 1

if len (sys.argv) != 2:
    print("error plz try again")
    sys.exit()