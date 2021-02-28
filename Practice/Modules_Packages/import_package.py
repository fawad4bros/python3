from Packages.Car import Car
from Packages.calculate import planet_mass, planet_vol

Bugatti = Car('Divo',8.0 ,1961 ,1103) #Bugatti is instance of Car
Bugatti_mass = planet_mass(Bugatti.Engine, Bugatti.Kerb_weight)
Bugatti_vol = planet_vol(Bugatti.Kerb_weight)


print(f'Engine: {Bugatti.Engine}')
print(f'Kerb Weight: {Bugatti.Kerb_weight}')

print(f'{Bugatti.Name} Has the mass of {Bugatti_mass} and volume of {Bugatti_vol}')