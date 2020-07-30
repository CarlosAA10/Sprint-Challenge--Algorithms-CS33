# list_1 = [1,2,4]
# list_2 = [1,3,5]


# list_1.extend(list_2)

# combined = list(set(list_1))

# print(combined)

# class Parent(object):
#     def fun(self):

#         print('Hi')

# p = Parent()

# # print(p.fun())
# p.fun()

# class Child(Parent):
#     def fun(self):
#         print('Bye')

# c = Child()

# # print(c.fun())
# c.fun()


# Python program for implementation of Insertion Sort 

# Function to do insertion sort 
def insertionSort(arr): 

	# Traverse through 1 to len(arr) 
	for i in range(1, len(arr)): 

		key = arr[i] 

		# Move elements of arr[0..i-1], that are 
		# greater than key, to one position ahead 
		# of their current position 
		j = i-1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
		arr[j + 1] = key 


# Driver code to test above 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
	print ("% d" % arr[i]) 

# This code is contributed by Mohit Kumra 
