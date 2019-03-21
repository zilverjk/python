import sys


clients = ['Pablo', 'Ricardo']


def create_client(client_name):
    global clients  # <--"global" coge la variable local para añadirlo dentro de a función

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already exsits')


def list_clients():
    for index, client in enumerate(clients):
        print('{}: {}'.format(index, client))


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        _get_validation()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        _get_validation()


def search_client(client_name):

    for client in clients:
        if client != client_name:
            continue #<----Continue es para que continue a la sieguiente iteración
        else:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_name():
    client_name = None #<-- None significa que no hay ningun valor (como null)

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_validation():
    return print('Client is not in the list')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if (command == 'C'):
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the list')
        else:
            print('The client {} is NOT in the list'.format(client_name))
    else:
        print('Invalid command')