import random


def binary_search(data, target, low, high):
    if low > high:
        return False
    
    mid = (low + high) // 2
    
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


def cycle_search(data, target):
    try:
        return data.index(target)
    except ValueError:
        return None


#Punto de ingreso
if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)] # Esto es un list comprehension

    data.sort()

    print(data)

    target = int(input('What number would you like to find? '))
    found = cycle_search(data, target)

    if found is not None:
        print('The number {target} was found in the position number {index}'.format(target = target, index = found + 1))
    else:
        print('The number {target} wasn\'t found in any position.'.format(target = target))
