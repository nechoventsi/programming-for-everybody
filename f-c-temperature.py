print "Welcome to temperature converter!"
print "What would you like to convert?"
print "1: Fahrenheit to Celsius"
print "2: Celsius to Fahrenheit"

inp = raw_input ("Please, enter '1' or '2':")

if inp == "1":
    F = raw_input ("Enter Fahrenheit temperature:\n")
    
    try:
        F = float(F)
        C = (F - 32) * 5/9
        print "Celsius temperature:", C

    except:
        print "Error! Please enter numeric input!"
    
elif inp == "2":
    C = raw_input ("Enter Celsius temperature:\n")

    try:    
        C = float(C)
        F = (C * 9/5) + 32
        print "Fahrenheit temperature:", F

    except:
        print "Error! Please enter numeric input!"

else:
    print "Error! Please enter '1' or '2'!"

# Version 0.4.0