
#Helper function for removing common letters 
def rmCommonLetters(a, b):
    
    for i in range(len(a)):
        for j in range(len(b)):

            if a[i] == b[j]:
                c = a[i]
                a.remove(c)
                b.remove(c)
                #print(a + ["*"] + b)
                return [a + ["*"] + b, True]
    return [a + ["*"] + b, False]




if __name__ == "__main__":
    """
        Write your name and someone else's on a piece of paper.
        Cross out all common letters appearing in both names.
        Count up the number of remaining letters (that aren't shared) in both names.
        Count through the letters of “FLAME” up to the number of leftover letters.
        Use the letter that you land on to predict the future of your relationship.
    
    """

    p1 = list(input("Player 1 name: ").lower().replace(" ", ""))
    p2 = list(input("Player 2 name: ").lower().replace(" ", ""))

    cont = True
    while cont: 

        tmp = rmCommonLetters(p1, p2)

        lst, cont = tmp[0], tmp[1]

        index = lst.index("*")
        n1 = lst[:index] # getting items of list up until *
        n2 = lst[index + 1:] # getting items after * starting from * + 1

    count = len(n1) + len(n2)
    result = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]

    while len(result) > 1:
        
        #Counting through letters of FLAME:

        sidx = (count % len(result)) - 1

        if sidx >= 0:
            result = result[sidx + 1:] + result[:sidx]
        else:
            result = result[:len(result) - 1]

    print("Relationship Status: ", result[0])
        

         

        
    
