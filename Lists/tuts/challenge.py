# total = 0
# count = 0
myList = list()
while(True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    # total = total + value
    # count = count + 1
    myList.append(value)
    average = sum(myList)/ len(myList)
    
print('Average:', average)