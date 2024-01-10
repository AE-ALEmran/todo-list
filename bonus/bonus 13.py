feet_inches = input("Enter the feet and inches :")

def pers(feet_inches) :
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
parsed=pers(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} Feet and {parsed['inches']} Inches are convert to meters {result}")

if result < 1:
    print("The kid is too small.")
else:
    print("The kid can use the slide.")