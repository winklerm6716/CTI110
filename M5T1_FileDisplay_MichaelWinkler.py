def main():
    numberFile = open("numbers.txt", "r")

    line = numbersFile.readline()

    while line !='':
        print( line )
        line = numbersFile.readline()

main()
