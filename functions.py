def get_store(filepath=".idea/store.txt"):
    with open(filepath, 'r') as file_local:
        store_local = file_local.readlines()
    return store_local

def write_store(store_arg , filepath =".idea/store.txt"):           #non-defolts parameter follows defolt parametters ,so store_arg is come 1st position class13
    with open(filepath, 'w') as file:
        file.writelines(store_arg)

