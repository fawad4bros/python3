cars = ['Aston Martin','Audi','BMW','Cadillac','Chevrolet']

for car in cars:
    print(car)

for car in cars[1:3]:
    print(car)

for car in cars:
    if car == 'Aston Martin':
        print(f'{car} - The name Aston Martin is derived partly from the name of its founder, Lionel Martin, and partly for a stretch of road in Hertfordshire, England, used for racing, called the Aston Hillclimb.')
    elif car == 'Audi':
        print(f'{car} - German Engineer August Horch founded the company August Horch & Cie. Motorwagenwerke AG, in 1899. Due to misunderstandings among partners, Horch left the company and formed a new company, August Horch Automobilwerke GmbH in 1909.')
    elif car == 'BMW':
        print(f'{car} - BMW started its operation in 1912 and was formed by the merger of three German companies.')
    elif car == 'Cadillac':
        print(f'{car} - Cadillac was named after the great French explorer Antoine Laumet de La Mothe, Sieur de Cadillac, who founded Detroit, Michigan in 1701. ')
        break
    else:
        print(car)