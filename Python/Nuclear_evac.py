import math

def nuclear(x_person, y_person, x_accident, y_accident, is_pregnant):

    distance = math.sqrt((x_person-x_accident)**2 + (y_person-y_accident)**2)

    if distance < 20:
        return "you must evacuate now !"
    
    elif 20 <= distance < 40:

        if is_pregnant:
            return "you must evacuate now!"
        if not is_pregnant:
            return "Evacuation is recommended"
        
    else:
        return "you are safe"

    
  

if __name__== "__main__":
    msg = nuclear(-23, 3.0, 0, 0, False)
    print(msg)