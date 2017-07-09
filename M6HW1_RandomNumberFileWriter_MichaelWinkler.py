# File Writer
# 7/3
# CTI-110 M6HW1 - Random Number File Writer
# Michael Winkler
#
def main():
    
    random_numbers = open('Random.txt', 'w')
    
    qty_numbers =  6 #int(input('Input how many random numbers should be written to the file: '))
    print('Your list of random numbers are: ')
   
    for count in range (qty_numbers):
        number = random.randint(1,500)
        
        print(number)
        
        random_numbers.write(str(number)+ '\n')
    
    random_numbers.close()
    
    print('Your list of random numbers have been written to the file named')
    print('ran_numbers.txt')

main()
