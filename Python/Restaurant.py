

class Restaurant:

    def __init__(self, name, cuisineType, isOpen = False):
        self.restaurantName = name
        self.cuisineType = cuisineType
        self.is_open = isOpen 


    def descirbe_restaurant(self): 
        
        print(self.restaurantName + " is a new 5 star restaurant offereing the best " + self.cuisineType + " food in town!") 

    def isOpen(self):
        
        res = "Open" if self.is_open else "closed"
        print("Restaurant is " + res)

        
    def setAttributes(self):
        input_name = input("What is the restaurant name? ").strip()
        if input_name:
            self.restaurantName = input_name

        input_cuisineType = input("What is the cuisine type? ").strip()
        if input_cuisineType:
            self.cuisineType = input_cuisineType

        while True:
            input_is_open = input("Is the restaurant open? (true/false): ").strip().lower()
            if input_is_open in ("true", "t", "yes", "y", "1"):
                self.is_open = True
                break
            if input_is_open in ("false", "f", "no", "n", "0"):
                self.is_open = False
                break
            print("Please enter true/false (or yes/no, y/n, 1/0).")

        return self
    
    def differentRestaurants(self):
        
        restaurants = [
            
            Restaurant("Devs", "Indian", True),
            Restaurant("Poulet Rouge", "Arab", True),
            Restaurant("AlTaiib", "Arabic", False),
            Restaurant("Chef Istanbul", "Turkish", True)
        ]

        print("\n here are some other open restaurants! \n")
        for r in restaurants:
            if r.is_open == True:
                print(r.restaurantName)
            



def main(): 

    restaurant = Restaurant("LaBodega", "Latin American", False)
    restaurant.setAttributes()
    restaurant.descirbe_restaurant()
    restaurant.isOpen()
    restaurant.differentRestaurants()

if __name__ == "__main__":
    main()

