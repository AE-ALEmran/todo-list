password=input("Enetr a new password :")

result=[]

if len(password)>=8 :                        #here we check the passw length use len function.
    result.append(True)                      #store it in list and check true or false
else:
    result.append(False)

digit=False                                 # for find disigt in the input passw.
for i in password :
    if i.isdigit() :
        digit=True
result.append(digit)

uppercase= False
for i in password :
    if i.isupper() :
        uppercase=True
result.append(uppercase)
print(result)
if all(result) == True :
    print("Strong Password")
else:
    print("Weak Password")