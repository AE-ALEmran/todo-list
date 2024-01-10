from bonus.converter14 import convert
from bonus.persers14 import pers       # here is a problem folder must be one word not like "bonus code" class 14

feet_inches = input("Enter the feet and inches :")
parsed= pers(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} Feet and {parsed['inches']} Inches are convert to meters {result}")

if result < 1:
    print("The kid is too small.")
else:
    print("The kid can use the slide.")