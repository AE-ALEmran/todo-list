import functions
import time
now = time.strftime("%B %d-%m-%Y  %I::%M %p")
print("It is", now)

while True:
    user_choice = input("Enter show, add , Edit, exit, complete code :")
    user_choice = user_choice.strip()

    if user_choice.startswith('add'):
        todo = user_choice[4:]

        store = functions.get_store()                           # replace function

        store.append(todo + '\n')

        functions.write_store(store)
    elif user_choice.startswith('show'):

        store = functions.get_store()

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

            store = functions.get_store()

            new_todo=input("Enter the new Todo :")
            store[number]=new_todo + '\n'

            functions.write_store(store)
        except ValueError :
            print("Your comment is not valid.")
            continue

    elif user_choice.startswith('complete') :
        try :
            number = int(user_choice[9:])
            store = functions.get_store()
            index=number-1
            todo_to_remove=store[index].strip('\n')
            store.pop(index)                                       # here strip() use for remove line gap

            functions.write_store(store)

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

