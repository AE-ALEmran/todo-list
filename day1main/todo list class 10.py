while True :
    user_choice=input("Enter show, add , Edit, exit, complete code :")
    user_choice=user_choice.strip()

    if user_choice.startswith('add') :             #if use for input string can be acces and if string contain add then program come to thos section class 9
        todo=user_choice[4:]                                      # [4:] use for not enclude add  for user input "add fix the computer" class 9

        with open('.idea/store.txt', 'r') as file:
            store = file.readlines()

        store.append(todo+ '\n')

        with open('.idea/store.txt', 'w') as file:
            file.writelines(store)
    elif user_choice.startswith('show'):                                 #elif use for excute one section only not all the section class 9.1

        with open('.idea/store.txt', 'r') as file:
            store = file.readlines()

        new_store=[item.strip('\n') for item in store]

        for index , item in enumerate(new_store):
            item=item.title()
            index=index+1
            row=f"{index}.{item}"
            print(row)
    elif user_choice.startswith('edit'):
        try :
            number = int(user_choice[5:])
            print(number)
            number=number-1

            with open('.idea/store.txt', 'r') as file:              #edit er por jate full edit line ta jai txt file a class 8
                store = file.readlines()

            new_todo=input("Enter the new Todo :")
            store[number]=new_todo + '\n'

            with open('.idea/store.txt', 'w+') as file:            #txt file edit kora text ta add hobe , age hoto nah edit kora txt ta class 8
                file.writelines(store)
        except ValueError :
            print("Your comment is not valid.")
            continue

    elif user_choice.startswith('complete') :
        try :
            number = int(user_choice[9:])
            with open('.idea/store.txt', 'r') as file:   # after complete file must be save in txt file class 8
                store = file.readlines()
            index=number-1
            todo_to_remove=store[index].strip('\n')                # store.pop() and massage ,,,, for use those 3 code class 8
            store.pop(index)                                       # here strip() use for remove line gap

            with open('.idea/store.txt', 'w+') as file:
                file.writelines(store)
            massage= f"Todo {todo_to_remove} was remove from the list !!!!!!"
            print(massage)
        except IndexError :
            print("Your enter number is out of the range .")
            continue

    elif '_' in user_choice:
        print("Hey, Eneter the write variables!!!")
    elif user_choice.startswith('exit') :
        break
    else:
        print("Commend is not valid")

