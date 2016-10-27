mass = float(input('What is the mass of the object? '))
height = float(input('What is the height of the object? '))
velocity = float(input('What is the velocity of the object? '))
gravity = 9.8
Joule = ('kg*m2/sec2')
PE = (mass * height * gravity)
KE = (.5 * mass * velocity**2)
TotalE = PE + KE
print('The total energy is ', TotalE, Joule)
