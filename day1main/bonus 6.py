contant =["my ban is yhe car of our","opne al thr rabia didididi","fire in nthe sky ok my"]

filename=["file.txt","file 2678.txt","presentation.txt"]

for contant,filename in zip(contant , filename) :
    file=open(f"./file/{filename}",'w')
    file.write(contant)