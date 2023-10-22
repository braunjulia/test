import cowsay
import sys
if len(sys.argv) == 2:
    print(sys.argv)
    cowsay.cow("Hello, " + sys.argv[1])

cowsay.trex("Hello")
