shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

#accessing the elements in the list
print(shoppingList[0])
print(shoppingList[4])
print(shoppingList[-3])

#check if an elemt is in the list
print("banana" in shoppingList)


#traversing the elements in the list using a loop

for i in shoppingList:
    print(i)

    #traverse in reverse order
    for i in shoppingList[::-1]:
        print(i)
        
#traverse using the range and len function
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "!"
    print(shoppingList[i])
    
#empty list
emptyList = []
for i in emptyList:
    print("This is not going to happen")

#uupdating an element in the list
myList = [1, 2, 3, 4, 5]
print(myList)
myList[2] = 33
myList[0] = 11
print(myList)

# time complexity of the list
# 0(1)

#space complexity of the list
# 0(1)

#inserting an element in the list
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList)

#insering an element to the beginning of list

myList.insert(0, 33)
myList.insert(5, 78)
#it has an o(n) time complexity
print(myList)

#inserting an elemnt to any given place in the list
#inserting an element to the end of the list

myList.append(100)
#has an o(1) time complexity
#has an o(1) space complexity
print(myList)

#adding another list to the list
newList = [11, 22, 33, 44, 55]
myList.extend(newList)
#time complexity depends on the length of the list and size of the list

print(myList)

#deleting an element in the list
myList2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(myList2)

#slicing a list
print(myList2[0:2])
print(myList2[2:])
print(myList2[:5])
print(myList2[:])

#delete an element from the list
#list methods for deletion

# - pop()
myList2.pop(3)
print(myList2)

# - delete()

del myList2[6]
print(myList2)

del myList2[0:3]
print(myList2)

# del myList2[:]
# print(myList2)

del myList2[5:]
#takes 0(n) time complexity 
print(myList2)
# - remove()

#delete a specific element in the list
myList2.remove('g')
#takes 0(n) time complexity
print(myList2)

#pop function
myList2.pop(3)
#takes 0(1) time complexity
print(myList2)

# list operations / functions

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

c = a + b
print(c)

a = [0, 1]
a = a*4
print(a)

a = [0, 1, 2, 3, 4, 5, 6]
print(max(a))
print(min(a))
print(sum(a)/len(a))


#searching for an elemnt in the List
myList3 = [10,20,30,40,50,60,70,80,90,100]
#use an in operator
if 20 in myList3:
    print(myList3.index(20))
    
else:
    print('The value does not exist in the list')
    
    
#use of a searchList
def searchingList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
        return "the value does not exist in the list"
print(searchingList(myList3, 50))


