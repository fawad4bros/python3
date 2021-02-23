# def Greet(Name,Time):
#     print(f" It's {Time} {Name}, Hope you are Learning if not F**k you !")

# Name = input('Enter Your Name:')
# Time = input('Time at the moment:')
# Greet(Name,Time)

#***************************************************************************
# def area(radius):
#     return 3.142 * radius * radius

# def vol(area,length):
#     return area * length

# radius = int(input('Enter a Radius: '))
# length = int(input('Enter a Length: '))

# calculatedArea = area(radius)

# calculatedVolume = vol(calculatedArea, length)

# print(f'Calculated Volume is: {calculatedVolume}')

#***************************************************************************

#Passing Function to function
def area(radius):
    return 3.142 * radius * radius

def vol(area,length):
    return area * length

Radius = int(input('Enter Radius: '))
Length = int(input('Enter Length: '))

calculatedVolume = vol(area(Radius),Length)

print(f'Calculated Volume is: {calculatedVolume}')
