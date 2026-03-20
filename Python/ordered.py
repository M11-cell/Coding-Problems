#Ordered ASCII Strings Problem

"""
Docstring for ordered

And finally, we have reached... THE LAST AND FINAL EXERCISEEEE!! DUN DUN DUNNNNNN

So let get straight into the pseudocode queen: 

Step 1: Declare the needed variables 

str_val = "A]4."
is_decreasing = True

Step 2: Now comes the pain in the ass part, which is the logic.
What we want to do here is iterate through each character in the string and determine if the following character is greater than the previous one.
If it is greater than the previous one, then the loop ends and we know that the string is not in decreasing order. 

for i in range(len(str_val) - 1): --> Note: this time we are using a variation of a for loop to iterate through our string
    if ord(str_val[i]) < ord(str_val[i+1]):
        is_decreasing = False
        print("This stirng is not in order!")
        break:

"""

def main():
    
    str_val = "A]4."

    for i in range(len(str_val) - 1): #Note: We use, str_val - 1 to prevent any out of range errors when evaluating the current 
                                        #character with the previous one
        if ord(str_val[i]) < ord(str_val[i+1]): 
            print(f" This string is not in decreasing order !")
            return False
    print(f" This string is in decreasing order !")
main()