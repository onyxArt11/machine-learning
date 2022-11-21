from pymatgen.io.cif import CifParser # this help us query the MP database
from urllib.request import urlopen # this helps us read or open a website 
from pymatgen.ext.matproj import MPRester
from pymatgen.ext.matproj import MPRestError
m = MPRester("Jbm6FXHA5AyIqvS1ZXJ2bxmEPMhRBed5")


#GETTING AND CONVERTING OUR FILE

request = urlopen('https://github.com/sheriftawfikabbas/crystalfeatures/blob/master/Li10Ge(PS6)2_mp-696128_computed.cif') #this helps us open the website our file is in, in the code
cifFile = request.read().decode('utf-8')# this reads the file
parser = CifParser.from_string(cifFile)# this converts the file into a String data


#METHODS FOR ACCESING SOME UNIQUE FEATURES OF OUR STRUCTURE

structure = parser.get_structures() # returns list of structure objects

print(structure[0])

structure = structure[0]

print(structure.lattice)
print(structure.species)
print(structure.charge)
print(structure.cart_coords)
print(structure.atomic_numbers)
print(structure.distance_matrix)
