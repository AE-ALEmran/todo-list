date=input("Enter today date :")
mood=input("How you rate your mood today from 1 to 10 !!!!!!")
journal=input("Let your through flow !!!!!\n")

with open(f"./file/{date}",'w') as file :
    file.write(mood+2*'\n')
    file.write(journal)
