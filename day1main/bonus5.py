waiting_list=['sen','ben','jon']
waiting_list.sort()

for index , item in enumerate(waiting_list) :
    row=f"{index+1}.{item.capitalize()}"
    print(row)