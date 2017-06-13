# Age Classifier
# 6/13/17
# CTI-110 M3HW1 - Age Classifier
# Michael Winkler
#

userAge = int(input('Please enter your age: '))

if userAge <= 1:
        print('You are an infant.')
elif userAge < 13:
        print('You are a child.')
elif userAge < 20:
        print('You are a teenager.')
elif userAge >= 20:
        print('You are an adult.')
