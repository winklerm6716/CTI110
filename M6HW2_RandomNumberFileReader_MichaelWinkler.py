# File Reader
# 7/3
# CTI-110 M6HW2 - Random Number File Reader
# Michael Winkler
#

afile = open("Random.txt", "r" )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 500))
    afile.write(line+str("\n")) 
    print(line)

afile.close()

print("\nReading the file now." )
afile = open("Random.txt", "r")

print(afile.read())
afile.close()
