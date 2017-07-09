# Kilometer Converter
# 7/1/2017
# CTI-110 M5T1_KilometerConverter
# Michael Winkler
#

def askUserForKilometers():
    userKilometers = float(input('Please enter the distance' + \
                                'in kilometers: ') )
    return userKilometers

def convertKilometersToMiles( userKilometers ):
    miles = userKilometers * 0.6214
    return miles

def main():
    userKilometersTyped = askUserForKilometers()
    convertedMiles = convertedKilometersToMiles( userKilometersTyped )

    print()

    print( userKilometersTyped, 'Kilometers converted to miles is', \
           format( convertedMiles, '.2f' ), 'miles')
main()
