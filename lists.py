my_list = [1, 2, 3]
my_list2 = [1, 2, 3, 2.65 , 'string']
var = 1

print(my_list2[3])
print(my_list2[-2])
print(my_list + my_list2)

my_list3 = my_list + my_list2

print(my_list3)

print(my_list3*10)

print(len(my_list3))

my_list3.append('mais um')
print(my_list3)

my_list3.pop()
print(my_list3)

my_list3.pop(0)
print(my_list3)

my_list3.reverse()
print(my_list3)
print(my_list3[::-1])

my_list3.sort()
print(my_list3)

arr1 = [1,2,3]
arr2 = [4,5,6]
arr3 = [7,8,9]

matrix = [arr1, arr2, arr3]

print(matrix)
print(matrix[1][1])

first_col = [row[0] for row in matrix]
print(first_col)