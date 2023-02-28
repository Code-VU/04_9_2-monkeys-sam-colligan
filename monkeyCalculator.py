def calculateTime():
    
    # This first line is provided for you
    monkey_one = input("Is the first monkey smiling?:  ")
    monkey_two = input("Is the second monkey smiling?: ")

    if monkey_one.lower() == "y" and monkey_two.lower () == "y" :
        print("Uh Oh! We're in trouble!")
    elif monkey_one.lower() =="n" and monkey_two.lower() == "n" :
        print("Uh Oh! We're in trouble!")
    else:
        print("Yay! We're going to have a good day!")

        
if __name__ == "__main__":
    calculateTime()

    # end assignment


## If you want to test locally run > python monkeyCalculator.py

