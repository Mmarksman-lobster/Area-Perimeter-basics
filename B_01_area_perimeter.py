#ask user for width and loop
# until they enter a number more than 0
from Tools.demo.sortvisu import WIDTH


def num_check(question):

    error = "please enter a number that is more than 0\n"
    while True:

        try:
    #ask user for number
             response = float(input(question))

             #check number is more than 0
             if response > 0:
                return response
             else:
                 print(error)
        except ValueError:
            print (error)


#main program goes here

keep_going = ""
while keep_going == "":
    #get width and height
        width = num_check("Width: ")

        height = num_check("Height: ")


            #calculate area / perimeter
        Area = (width * height)

        perimeter = 2 * (width + height)

                            #display output
        print()
        print(f"area: {Area} units")
        print(f"perimeter: {perimeter} square units")
            #ask user if they want to keep going
        keep_going = input("press enter to keep going or any key to quit. ")
        print( )

print("thank you for using area / perimeter calculater")

