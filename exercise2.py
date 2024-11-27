time = int(input("Enter the current time "))

if(time < 0):
    print("Please enter valid positive number")
elif(time >= 0):
    if(time < 12):
        print("Hey! Good Mornig and it is", time, "o'clock")
    elif(time > 12 & time< 17):
        print("Hey! Good Afternoon and it is", time, "o'clock")
    elif(time >= 20):
        print("Hey! Good evening and have a good nigth it is", time, "o'clock")
    else:
        print("Good Night Have a sweet dream")