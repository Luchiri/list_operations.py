#create an empty list
my_list = []

#append eleemnts 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert 15 at the second position (index 1)
my_list.insert(1, 15)

#extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

#remove the last element
my_list.pop()

#sort the list in ascending order
my_list.sort()

#find and print the index of 30
index_of_30 = my_list.index(30)
print("Index of 30: ", index_of_30)

#print final list
print("Final List: ", my_list)