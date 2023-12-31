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

            with open('.idea/store.txt', 'w+') as file:
                file.writelines(store)
        case 'show' | 'display' :

            with open('.idea/store.txt', 'r') as file:
                store = file.readlines()

            new_store=[item.strip('\n') for item in store]

            for index , item in enumerate(new_store):
                item=item.title()
                index=index+1
                row=f"{index}.{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number You want to edit :"))
            number=number-1

            with open('.idea/store.txt', 'r') as file:  #edit er por jate full edit line ta jai txt file a class 8
                store = file.readlines()

            new_todo=input("Enter the new Todo :")
            store[number]=new_todo

            with open('.idea/store.txt', 'w+') as file: #txt file edit kora text ta add hobe , age hoto nah edit kora txt ta class 8
                file.writelines(store)
        case 'complete' :
            number = int(input("Enter the number You want to edit :"))
            with open('.idea/store.txt', 'r') as file:   # after complete file must be save in txt file class 8
                store = file.readlines()
            index=number-1
            todo_to_remove=store[index].strip('\n')                # store.pop() and massage ,,,, for use those 3 code class 8
            store.pop(index)                                       # here strip() use for remove line gap

            with open('.idea/store.txt', 'w+') as file:
                file.writelines(store)
            massage= f"Todo {todo_to_remove} was remove from the list !!!!!!"
            print(massage)
        case '_':
            print("Hey, Eneter the write variables!!!")
        case 'exit' :
            break

