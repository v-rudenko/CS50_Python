import sys

if len(sys.argv) < 2:
    print("To few arguments")
    sys.exit()

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)
