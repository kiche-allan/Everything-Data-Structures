from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1, 3, 1.5, 1.6])


#inserting an element in the end of an array
arr1.insert(6, 7)

#inserting an element in the beginning of an array
arr1.insert(2, 9)

# print(arr1)

#traversing arrays
def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)

#accessing an element
def accessElement(array, index):
    if index > len(array):
        print('There is not any element in this index')
    else:
        print(array[index])
        
accessElement(arr1, 7)

#searching an element in an array


def searchArray(arr, value):
    for i in array:
        if i == value:
            return arr.index(value)
        return "The element does not exist in this array"

    print(searchInArray(arr1, 7))
    
#deleting an element from an array

arr1.remove(6)
print(arr1)


