


def highest_grade(grades: list[tuple]) ->str: 

    #iterate through list
    #Scan which name has the highest grade 
    # Retrun name w/ highest grade

    highest_grade = ""
    fake_max = 0.0000001
    for g in grades:
        
        if g[1] > fake_max:
            fake_max = g[1]
            highest_grade = g[0]
        
    print(highest_grade)
            
    return highest_grade




def main():

    highest_avg_grade = [('Finn', 20), ('Jason', 74), ('Jason', 79), ('Finn', 87), ('Marceline', 100)]

    highest_grade(highest_avg_grade)

if __name__ == "__main__":
    main()