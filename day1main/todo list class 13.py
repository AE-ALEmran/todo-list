def get_store(filepath=".idea/store.txt"):
    with open(filepath, 'r') as file_local:
        store_local = file_local.readlines()
    return store_local

def write_store(store_arg , filepath =".idea/store.txt"):           #non-defolts parameter follows defolt parametters ,so store_arg is come 1st position class13
    with open(filepath, 'w') as file:
        file.writelines(store_arg)


while True:
    user_choice = input("Enter show, add , Edit, exit, complete code :")
    user_choice = user_choice.strip()

    if user_choice.startswith('add'):
        todo = user_choice[4:]

        store = get_store()                           # replace function

        store.append(todo + '\n')

        write_store(store)
    elif user_choice.startswith('show'):

        store = get_store()

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

            store = get_store()

            new_todo=input("Enter the new Todo :")
            store[number]=new_todo + '\n'

            write_store(store)
        except ValueError :
            print("Your comment is not valid.")
            continue

    elif user_choice.startswith('complete') :
        try :
            number = int(user_choice[9:])
            store = get_store()
            index=number-1
            todo_to_remove=store[index].strip('\n')
            store.pop(index)                                       # here strip() use for remove line gap

            write_store(store)

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

