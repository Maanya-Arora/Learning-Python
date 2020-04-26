import sys
if (sys.argv[1]) =="1":
    water =int (sys.argv[2]) * 1.33
elif (sys.argv[1]) == "2":
    water =int (sys.argv[2]) * 2
elif (sys.argv[1]) == "3":
    water= int(sys.argv[2]) * 1.25
elif (sys.argv[1]) == "4":
    water=int(sys.argv[2]) * 1.5
elif (sys.argv[1]) == "h" or (sys.agrv[1]) == "H":
    print("this is the help manual-")
    print("in the command line, enter the rice you are cooking & the number of cups you plan to cook to find out how much water you will need")
    print("enter 1 for JASMINE RICE")
    print("enter 2 for BASMATI RICE")
    print("enter 3 for LONG GRAIN BROWN RICE")
    print("enter 4 for SHORT GRAIN BROWN RICE")
    water = 0
print (water)

