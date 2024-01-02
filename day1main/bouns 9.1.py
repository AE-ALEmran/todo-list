password=input("Enetr a new password :")

result={}                                    #dictinary function or mathod which not have append like list

if len(password)>=8 :                        #here we check the passw length use len function.
    result["lenth"]=True                     #store it in list and check true or false
else:
    result["lenth"]=False

digit=False                                 # for find disigt in the input passw.
for i in password :
    if i.isdigit() :
        digit=True
result["digits"] = digit

uppercase= False
for i in password :
    if i.isupper() :
        uppercase=True
result["upper-case"] = uppercase
print(result)
if all(result.values()) == True :                        # .values() just collect all value in dict data type
    print("Strong Password")
else:
    print("Weak Password")