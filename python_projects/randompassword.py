import string
from random import *


characters = string.ascii_letters + string.punctuation + string.digits

password = "".join(choice(characters)for i in range(randint(7,14)))

print("Olusturulan parolaniz :" , password)

#print(string.ascii_letters) #harfler buyuk kucuk
#print(string.digits) #rakamlar
#print(string.punctuation) #semboller
