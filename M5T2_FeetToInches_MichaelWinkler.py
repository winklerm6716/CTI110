def feetToInches( userFeet ):
    inches = ( userFeet / 1 ) * 12
    return inches

def main():
    userFeet = float( input('Please enter the number of feet: '))
    print()
    inches = feetToInches( userFeet )
    print(userFeet, 'Feet converted to inches is', format( inches, '.2f'), 'inches')

main()    
