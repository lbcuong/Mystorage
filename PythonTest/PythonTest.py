
a = [1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def intersection(lst1, lst2):  #value can appear more than 1 time if lis1 have 2 more same element
    list = []
    for value in lst1:
        if value in lst2:
            list.append(value)
    print(list)

def commonList(a, b):          #set() method used to sort sequence and non-repeat element
    list = (set(a) & set(b))
    print(list)

def fillterMethod(a, b):
    list = [(filter(lambda number: number in a, c)) for c in b]
    print(list)

intersection(a, b)
commonList(a, b)
fillterMethod(a, b)