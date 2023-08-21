#creating a dictionary
phone_book = {'John': 123456789, 'Jack': 987654321, 'Jill': 456789123}

#accessing the value for a key
print(phone_book['John'])

#adding a new key-value pair
phone_book['Jack'] = '555-333'

#updating a value for a key
phone_book['Jill'] = '555-2468'

#removing a key-value pair
del phone_book['John']

#checking if a key exists in the dictionary

if 'Jack' in phone_book:
    print("Jack's phone number is ", phone_book['Jack'])
    
#iterating over a dictionary

for name in phone_book:
    print(name, phone_book[name])
    
    #update/ add an elemet to the dictionary
    myDict = {'a': 1, 'b': 2, 'c': 3}
    myDict['a'] = 5
    print(myDict)
    myDict['c'] = 4
    print(myDict)
    
    #traverse through the dictionary
    myDict2 = {'name': 'John', 'age': 26, 'salary': 5000}
    
    def traverseDict(dict):
        for key in dict:
            print(key, dict[key])
    traverseDict(myDict2)
    
    #searching an element in a dictionary
    
    def searchDict(dict, value):
        for key in dict:
            if dict[key] == value:
                return key, value
            return 'The value does not exist in the dictionary'
        
    print(searchDict(myDict2, 26))
    
    #removing an element fro a dictionary
    
    myDict3 = {'name': 'Kiche', 'age': 26, 'address': 'Nairobi', 'education': 'bachelors'}
    
    print(myDict3.pop('name'))
    
    print(myDict3)
    
    # or use clear method
    
    myDict3.clear()
    print(myDict3)
    
    #copying a dictionary
    myDict4 = {'name': 'Kiche', 'age': 26, 'address': 'Nairobi', 'education': 'bachelors', 'salary': 5000, 'phone': 123456789}
    
    dict = myDict4.copy()
    print(myDict4) 
    print(dict)
    
    #get a method. it taes 2 parameters - 
    