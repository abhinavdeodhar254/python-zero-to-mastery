#Used to concat strings in a dynamic way
# here is the syntax as given below

print("string here {} then also {}".format('something 1','something 2'))

# "something1" and "something 2" will get entered in those curly braces.
#Make sure that we terminate the string entered before the .format() 
# the dot(.) in dot format is touching the string 

print("this is the string {}".format("Inserted"))

#We can also insert the string depending on the index count of the literals 
# inserted in the .format section

print("this are the first three campions {}, {}, {}!!".format("Sam","pam","Jim"))

# so by deafult the first literal entered in the .format section will occupy the first curly braces.
# We can also give them the index and then they can enter in the respective curly braces as well

print('The {1} {2} {0}'.format('fox','quick','brown')) 
# here inside the format section quick is at 1 index and brown is at 2 index and fox is at zero index.  

print('The {q} {b} {f}'.format(f='fox',q='quick',b='brown'))
#we can also add them the key value pair.

#here using the key value pair will make it easy to understand what is the position of the values.


#we can also work with the decimal number.
# the syntax here is that print("your statement{r:width.number of decimal places}".fomat(r='result))

result=1.3453464374789345
print("this is my result in decimal: {r:1.5}".format(r=result))

##if the last digit after using formating is greater than or equal to  5 then itwill also round it off.



#three is one other way to use dotformating and that is f string it is the upgraded feature which comes in pyhton version3 and above.

name='Abhinav'
age=23
print(f"hello! my name is {name} and i am {age} years old")



