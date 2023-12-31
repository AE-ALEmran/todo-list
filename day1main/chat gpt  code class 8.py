while True:
    user_action = input("Type add, edit, show, complete, or exit: ")
    user_action = user_action.strip()

    if user_action == 'add':
        todo = input("Enter a todo: ") + "\n"

        with open('todo.txt', 'a') as file:
            file.write(todo)

    elif user_action == 'show':
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos, start=1):
            item = item.strip('\n')
            row = f"{index}-{item}"
            print(row)

    elif user_action == 'edit':
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        if 0 <= number < len(todos):
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open('todo.txt', 'w') as file:
                file.writelines(todos)
        else:
            print("Invalid todo number")

    elif user_action == 'complete':
        number = int(input("Number of todo to complete: "))
        number = number - 1

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        if 0 <= number < len(todos):
            todos.pop(number)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)
        else:
            print("Invalid todo number")

    elif user_action == 'exit':
        print("Bye!!!")
        break

    else:
        print("Invalid action. Please type add, edit, show, complete, or exit.")
