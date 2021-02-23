#Series of {Key:Value} Pairs

# fourbros = {"Jawad":"MS(ML)","Saad":"MS(AI)","Hammad":"M.phil(pharmacology)","Fawad":"BS(CS)"}
# print(fourbros)
# print(fourbros['Hammad'])

#key in dictionary , check if a key exist in dictionary
#'Hammad' in fourbros


# print('Naeem' in fourbros)

# print('Saad' in fourbros)

# print(fourbros.keys())

# print(list(fourbros.keys()))

# print(fourbros.values())

# print(list(fourbros.values()))

# Values = list(fourbros.values())
# print(Values.count('BS(CS)'))
# print(Values.count('BS'))

# #Adding New Key:Value pair
# fourbros['Mr.Naeem'] = 'BS(EE)'
# print(fourbros)

# Youngest_Child = dict( name = "Fawad", age = 21 , height = 6.2)
# print(Youngest_Child)

def Pawri_Ho_Rahi_Hai(dictionary):
    for name,degree in dictionary.items():
        print(f'Yae Meri {degree} or main {name} hun or Yae Hamari Pawri Ho Rahi Hai ')

Jin_ke_Pawri_Ho_Rahi_Hai = {}

while True:
    name = input('Name: ')
    degree = input('Degree: ')
    Jin_ke_Pawri_Ho_Rahi_Hai[name] = degree
    another = input('Our Pawri Ho Rahi Hai ? (y/n) ')
    if another == 'y':
        continue
    else:
        break
Pawri_Ho_Rahi_Hai(Jin_ke_Pawri_Ho_Rahi_Hai)