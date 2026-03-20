
#Palindrome assignment question: 

"""
Before writing a program, it is always pretty useful to write something called a "pseudocode". 
Pseudocode is basically a mind map of what you would need to do in order to achieve your goal. 
For this exercise, we know that a palindrome is a word that is read the same way from left to right and right to left. (ex: madam)
In our head, the logic is pretty obvious, simply look at the word and check to see if its the same from left to right and right to left. But,
when Coding, it is a bit more of a pain in the ass. You really have to exaggerate what our brain does and break down our thinking process into
little steps: 
"""
"""
And So here is what I mean when I said we really need to break down our thinking into little steps before writing it as a computer program: 

--> The pseudoCode:

Step 1: We want to iterate through the string from LEFT to RIGHT and also from RIGHT to LEFT. 

left = 0 
right = len(str_val) - 1 Note: len(str_val)-1 brings you to the back of the str_val. 

Step 2: create the logic to check whether or not the str_valing is a palindrome 
The best way to do this is by creating a loop. There are 2 kinds of loops: While loops and for loops (which you will learn later on). 
Long story short, The while loop is better to use in cases where you have an unknown number of iterations to do.
Whereas for a for loop, its best to use them when you have a fixed number of iterations. 

For this example, I will use a while loop primarily because I will be under the assumption that 
I don't necessarily know when the right and left variables will meet up. 
So the conditions for this loop (and the following logic) are as follows:

while left < right:  --> this means that this loop will do however many iterations UNTIL just before the left iteration is larger than the right one. 
    if str_val[left] != str_val[right]:
        return False --> Note, if we were to return true in here, the loop would immediately end if str_val[left] and str_val[right] are equivalent 
                            even though the word might not be a palindrome.
    left ++ 
    right --

return True --> Lastly, we return true once the entire loop has been executed and the compiler has found that the word is a palindrome

"""
str_val = "madam"
condition_is_met = False
left = 0
right = len(str_val) - 1

while left < right:

    if str_val[left] != str_val[right]:
        result = condition_is_met 
        print(f"the string is not a palindrome")
        exit(0)
        
    
    left+=1
    right-=1
    #Note: The +=, and -= and /= and *= operators are very useful in loops (throwback to when we spoke about this friday)
condition_is_met = True
result = condition_is_met
print(f"the stirng is a palindrome")

