#They are the ordered sequesnce that can hold the variety of object types.

#they are enclosedin the square brackets and the elements are seperated by commas.
# they also support slicing and indexing like strings


my_list=[1,2,3,4,5,6]

# We can also create the list of mixed object types.
# # they are very flexible with the data type that they can hold

my_list_two=[1,22.3,"hello"]

#thid is still a very valid list.

len(my_list_two)

# len() is the method which is used to get the length of the string

# slicing and indexing also works in the list.

print(my_list_two[2])

print(my_list[1:4])

#We can also concatinate two lists


my_list=["one","two","three","four"]
my_list_two=["five","six","seven","eight","nine"]
my_concatinated_list=my_list+my_list_two
print(my_concatinated_list)

#list are mutable we can change the list elements.

my_concatinated_list[0]="ONE"

print(my_concatinated_list)

# so see we can change thelist element

# we can also add the elements to the end of the list
# append(0) method is used to add the element to the end of the list.

my_concatinated_list.append("I am  the new item")
print(my_concatinated_list)

#output: ['ONE', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'I am  the new item']

# # we can also remvoe the items from the list
# pop() method is used to remove the element from the list.
# # Everytime we use this method only the last element is going to get popped out of the list

my_concatinated_list.pop()
print(my_concatinated_list)

#output: ['ONE', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

my_concatinated_list.pop(3)
print(my_concatinated_list)

#output: ['ONE', 'two', 'three', 'five', 'six', 'seven', 'eight', 'nine']

# So if we give the index number to the pop function then that respective element will also get removed.
# here four was at the index 3 so it got removed


my_concatinated_list.pop()

# output:
# 'nine'


#Here we can see that it has also returned the element that it  has popped out.
# lets save the results into the new list of popped items

popped_item_list=my_concatinated_list.pop()
print(popped_item_list)
# output: seven

# # so here i have executed the block twice and is observed that is previously the "eight" element was popped but 
# when i rerun the same code thinking that it will now two popped elements in the popped item list 
# but no its not the case. 
# Everytime we run it a empty listis assigned with the popped element.

list1=['a','h','y','u','i','o','v']
list2=[5,6,8,2,4,0,45,54]
list1.sort()

print(list1)
#output:
# ['a', 'h', 'i', 'o', 'u', 'v', 'y']


# we cant assign the new  list to the sorted opertaion performed on the other list.
newlist=list1.sort()
print(type(newlist))

# <class 'NoneType'> --->output

# it will say thatit is the none type

# what we can do is first sort the list and then assign it to the new list.

list2.sort()

mysorted_list=list2
print(mysorted_list)


# [0, 2, 4, 5, 6, 8, 45, 54] : output

#here we go

#we can also reverse the list using the reverse method.
list1.reverse()
print(list1)
# ['y', 'v', 'u', 'o', 'i', 'h', 'a']: output
