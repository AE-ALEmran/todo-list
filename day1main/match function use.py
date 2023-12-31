store=[]

while True :
    user_choice=input("Enter show, add , Edit, exit, complete code :")
    user_choice=user_choice.strip()
    match user_choice : #here use a match function which help to match input string.
        case 'add' :
            todo=input("Enter todo data:") + "\n"
            store.append(todo)                    #append arrange string in serial in list.
            file=open('.idea/store.txt', 'w+')
            file.writelines(store)
        case 'show' | 'display' :
            for index , item in enumerate(store):
                item=item.title()
                index=index+1
                row=f"{index}.{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number You want to edit :"))
            number=number-1
            new_todo=input("Enter the new Todo :")
            store[number]=new_todo
        case 'complete' :
            number = int(input("Enter the number You want to edit :"))
            store.pop(number-1)
        case '_':
            print("Hey, Eneter the write variables!!!")
        case 'exit' :
            break

