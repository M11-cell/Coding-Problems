#intermediate value theorem problem

"""
Docstring for ivt

Coolsies, now we have finally made it to the next exercise!

Now that we've read da exercise, lets get straight into the pseudocode queen. 

step 1: initialize all the needed variables.

a = 0
b = 2


step 2: here we gotta figure out (aka: come up with some logic) that will input a and b into the function, and sum the computed values 
        together so we can determine wether or not its a positive or a negative.

    lower_bound = a^5 - 2a^3 - 2
    upper_bound = b^5 - 2b^3 - 2

    if lower_bound < 0 and upper_bound > 0:
        print("This polynomial has a root")
        return True
    
    return False --> returns false if it supposidely does not have a root

"""


def main():
    
    a = 0
    b = 2
    lower_bound = a**5 - 2*(a**3) - 2
    upper_bound = b**5 - 2*(b**3) - 2

    if lower_bound < 0 and upper_bound > 0:
        print(f"This function has a root")
        return False

    print(f"This function does not have a root")
    




main()