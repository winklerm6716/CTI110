# Body Mass Index
# 6/13/17
# CTI-110 - Body Mass Index
# Michael Winkler
#

userWeight = float( input('Please enter your weight: '))
userHeight = float( input('Please enter your height: '))
userBMI = ( userWeight * 703) / ( userHeight ** 2)

print()
if userBMI < 18.5:
    print('A person with a BMI of ' + format( userBMI, '.2f') + ' is underweight.')
elif userBMI < 26:
    print('A person with a BMI of ' + str( userBMI ) + ' has an optimal weight.')
else:
    print('A person with a BMI of ' + str( userBMI ) + ' is overweight')
