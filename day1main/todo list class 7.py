while True :
    user_choice=input("Enter show, add , Edit, exit, complete code :")
    user_choice=user_choice.strip()
    match user_choice :
        case 'add' :
            todo=input("Enter todo data:") + "\n"

            file=open('.idea/store.txt','r')
            store=file.readlines()
            file.close()

            store.append(todo)

            file=open('.idea/store.txt', 'w+')
            file.writelines(store)
            file.close()
        case 'show' | 'display' :
            file = open('.idea/store.txt', 'r')  # file ta read korbe and etr jorno store=[] ata lagbe nah
            store = file.readlines()
            file.close()

           # new_store=[]                         #define new store

           # for item in store:                   #here we use new_store to remove gap class7
            #    new_item=item.strip('\n')
             #   new_store.append(new_item)
            new_store=[item.strip('\n') for item in store]  #up 4 line combine line here

            for index , item in enumerate(new_store):
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

