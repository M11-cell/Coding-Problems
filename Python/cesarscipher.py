
#todo: if ascii number reaches 42 on one hand and 126 on the other, then the code must be wrapped back to the other end. 
# => 123 + 5 = 128, thus the ascii number will simply start back at 42 and add remaining number to give final ASCII code of 43. 

def encrypt(word, rotation):
    
    encrypted_word = "" #here we are simply declaring the encrypted_word variable which is what the function will return at the very end. 

    #todo: Check if string is not greater than 5 characters:
    if len(word) != 5: 
        return "Invalid input"
    
    #todo: check is ASCII characters are greater than 126 or less than 42:
    for char in word: 
            
            wrap = wrapper(char, rotation) 
            """
                here we are calling the helper function.
                The entire goal of a helper function is to 1. make your code easier to read and also make your functions neater 
                and 2. to break up tasks into even smaller ones to simplify the problem. 
                So in this case, we call the wrapper function which takes in char (the current character being evaluated in the loop)
                and the rotation number. 
            """
            encrypted_word += wrap

            """
                last but not least, we create a new string "encrypted_word" and we add the encrypted character into the string and then we return it. 
            """
    
    return encrypted_word
    

def decrypt(scrambled_werd, rotation):  
    

    if len(scrambled_werd) != 5: 
        return "Invalid input"
    
    #todo: reverse the rotation that was done in the encrypt. 
    """

        decryption here is pretty straightforward since its basically the same thing as encryption
        BUT REVERSED, therefor, all you would need is a REVERSED ROTATION NUMBER (aka. make the rotation negative !)
    """
    return encrypt(scrambled_werd, -rotation)



def wrapper(character, rotation_num):
    
    """
        Now this is the wrapper function: takes in 2 parameters. a single character and the rotation number 

        The first thing it does is create a variable that takes in the current character the encrypt function was evaluating and converts it to its ascii number. 
        Now, why did I create this variable? Just for simplicity and legibilities sake. I could have directly plugged ord(character) into the new_ascoo = ascii_val + rotation_num.
        all the ascii_val is doing is creating a placeholder for the characters ascii value. Nothing more nothing less. 

        then we have the logic itsef: 

        if new_ascii > 126, we know that we want to revert it back to 42, and then add the remaining amount to 42. 
        Therefor, to do thatttt ... we will assume that we start at 42 ... hence the "42 + ..." THEN, we will do new_ascii - 127.

        picture this: 

        imagine that new_ascii = ascii_val + rotation_num = 130. SO,

        under the if statement new_ascii > 126:

        we will now reassign new_ascii to the wrapped value which is now: 42 + (130 - 127) = 45 ! Get it ... ? :D

        n0w we'll do the same thing with similar logic if the ascii value is less than 42. 

        and then well return the character value of the new_ascii number BACK to the encrypted function. 

        Note: chr() is the same as ord(). But instead of converitng a character to an ascii number, itll convert an ascii number into a character !. 
    """

    ascii_val = ord(character)

    new_ascii = ascii_val + rotation_num

    if new_ascii > 126:

        new_ascii = 42 + (new_ascii - 127)

    elif new_ascii < 42:

        new_ascii = 126 - (41 - new_ascii)


    return chr(new_ascii) 

def check_cipher(s1, s2, rot):
    
    """
    Docstring for check_cipher
    
    :param s1: decripted string
    :param s2: encripted string
    :param rot: rotation number
    """

    check_decrip = decrypt(s2, rot)

    if check_decrip != s1:
        return False
    
    return True


#todo: if stirng is not 5 characters long, resturn invalid input and DO NOT attempt to encode/decode message.

def main():
    
    msg_encrypt = encrypt('Hello', 200)
    print(msg_encrypt)

if __name__ == "__main__":
    main()