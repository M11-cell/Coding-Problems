
def count_unique_chars(s2):

    # todo: determine if the particular character in the string is unique to all elements. 
    seen_char = []
    char_counts = []
    unique_chars = 0

    #First we write a for loop that iterates thru every single character in the stwing. 
        #Visual Rep: 
            # for m in "mother"
    for char in s2:
        #Here we create a boolean value to keep track of what has been seen & what hasn't. 
        found = False
        #Here were creating another for loop, but this time its to iterate over the (For now empty seen_char) list. 
        #Over time this list will fill up ( [] to ['m', 'o', 't',  ... ]) and every time it fills up, more iterations will occur.
        #Basically, the logic below this loop is meant to STORE already seen characters, that way we can keep track of them. 
        # For i in range (0), then ... for i in range (1), then ... for i in range (4), ... etc
        for i in range(len(seen_char)):
            #Here we then kind of combine both loops together and say: if whatever character is in index i of seen_char and is equal to the current char that I am on.. 
            #compute the logic below. If not, continue. 
            # Ex: say seen_char now has characters: ['m', 'o', 't', 'h', '1', '3') and char is now equal to the second '3'.
            # NOTE: this for loop will actually iterate through the entire list of seen_chars before moving on to the next character in the string. 
            if seen_char[i] == char:
                #if a character stored in seen_char maches the current character, then the char_count will increment by 1, and found will become true (marking that two [or more]
                # of the same character has been found. 
                char_counts[i] += 1
                found = True
                break
            #If a character in seen char DOES NOT match the current character being evaluated in the very first for loop, then we will store that
            #character in the seen_char list to hold it and see if it comes back again. Additionally, char_counts will also increase by 1. 
        if not found:
            seen_char.append(char)
            char_counts.append(1)

    #Lastly, well create one last simple for loop which iterates over the entirety of the (now completed) seen_char string. 
    #and we will check if char_counts is == 1. Why? Because from the logic above, if a character has been seen more than once throughout the string, then char_counts
    # Will begin to tally it and the character count would increase by one every time it sees the same char. 
    for i in range(len(seen_char)):
        #Lastly we increment unique_char by one and return however many unique characters it counted. 
        if char_counts[i] == 1:
            unique_chars += 1

    return "There are: ", unique_chars, "In da Stwing"

def main():

    some_string ="hungover"
    msg = count_unique_chars(some_string)
    print(msg)

if __name__ == "__main__":
    main()
