#Sequence of charecters enclosed in single or double quotes.



#example: 

"Hello world" #encloised in double quotes.
'this is the python course'     #enclosed in single quotes.


"""she said,"hi" to me""" #here we have used multiple double quotes because if we would have used the single double quote it would have got occupied by "hi" and the remaining sentence would have given and error.

"she said, "hi to me #this will give an error.

#the outer double quote got paired with the double  quote of hi and left the remaining sentence out of string and it will be an error in programming.


#they are ordered sequences.

#0 1 2 3 4
#H E L L O

#we can use indexing to transverse across the string.

#index starts from 0.


#We can also use slicing on the string.
#slicing in the stringis something like grabbing the substring from the string by giving the starting and end indices.

sentence="Hello, My Name is Hanuman"

#Now here we will try to grab the new substring out of sentence from index 0 to 7

slice(sentence[0:7])

#slice is the keyword used for slicing
#slice takes in an argument and that is the variable name where the string is stored.
#the index is passed in the square bracket
#here 0 is the starting element of the string in this case it is H
#the stopping index is 7. 7th index will not be included in the output. 
#slicing doesn't take the stoping index but it slice the string to the one index less than that which is provided.

#output "Hello, "
#spaces are also counted

slice(sentence [5:7])
#this will start from index 5 and end at 6 so the output here will be ", " {comma and space after the word hello}


slice(sentence[::])

#This means start the string from zero and go all the way to the end.

slice(sentence[4:])

#this means that start the string from  4 and go all the way to the end.

slice(sentence[:9])

#this means start from the index 0 and end at the index 9-1 (index 9 will not be included in output)

#We can also jump while transversing the string. By giving the thrid argument.

slice(sentence[0::1])

#the thrid index tells us how many positions we need to jump.
#by default slicing jumps with the value 1

#here the output will be that the string will get printed from 0 all the way to end by jumping one position at a time.

#jumping from index 1 to 2 and then to 3 and so on.


slice(senternce[0::3])

#this means that the string will jump three positions at a time.
#now the slicing will jump on every third index starting from 0

#0-H
#2-l  #2 is the third element








#