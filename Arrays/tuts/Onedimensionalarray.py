#declare and initialize the array with student grades

grades = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

#print the entire array

print(grades)

#print the grade of the student at index 3

print(grades[3])


#update the grade of the studet at index 3

grades[3] = 456

print(grades)


# Time and space complexity in one dimensional array

# Operation ---------------------------------- Time Complexity ------------------------------ Space Complexity
# Creating an empty array -------------------- O(1) ----------------------------------------- O(n)
# Insering a value in an array ------------------- O(n)/0(n) ----------------------------------------- O(1)
# Traversing a given array ----------------------0(n) --------------------------------------------0(1)
# Accessing a given cell ------------------------0(1)---------------------------------------------0(1)
# Searching a given value -----------------------0(n)---------------------------------------------0(1)
# Deleting a given value ------------------------0(n)/0(n)---------------------------------------------0(1)
