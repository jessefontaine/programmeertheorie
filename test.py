def swap(list, a, b):
    """
    Swap elements in a list
    """
    list[a], list[b] = list[b], list[a]

lijst = [5, 6, 7, 8]
swap(lijst, 1, 3)
print(lijst)