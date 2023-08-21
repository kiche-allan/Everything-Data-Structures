# a three dimensional array is an array of arrays of arrays. it stores elements in a cube-like format where each element can be accessed by its layer, row and column indices

#declare and initialize the array with student grades

grades = [[[90, 58, 34], [56, 78, 23], [23, 67, 90], [45, 67, 89]], [[90, 58, 34], [56, 78, 23], [23, 67, 90], [45, 67, 89]], [[90, 58, 34], [56, 78, 23], [23, 67, 90], [45, 67, 89]]]

print(grades)

# print grade of student in first class, second roww and third column

print(grades[0][1][2])

#update the grade of the student in the second class  in the 3rd row and first column

grades[1][2][0] = 85
print(grades)


# get the number of layers in the array

print(len(grades))

#get the number of rows in the array
print(len(grades[0]))

# get the number of columns in the array

print(len(grades[0][0]))


# In this example, we first declare and initialize a three-dimensional array named "grades" with the grades of students in multiple classes. Each innermost array represents the grades of a student, each middle array represents the class, and the outermost array represents the number of classes. We then use the square brackets notation to access and manipulate the elements in the array. We can use the print statement to display the entire array, a specific element in the array, the number of layers, rows, and columns in the array.