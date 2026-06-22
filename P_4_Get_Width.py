#ask user for width and loop
# until they enter a number more than 0


error = "please enter a number that is more than 0\n"
while True:

    try:
#ask user for number
         width = float(input("width: "))

         #check number is more than 0
         if width > 0:
            break
         else:
             print(error)
    except ValueError:
        print (error)