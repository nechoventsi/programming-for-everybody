print "Welcome to temperature converter!"
print "What would you like to convert?"
print "1: Fahrenheit to Celsius"
print "2: Celsius to Fahrenheit"

inp = raw_input ("Please, enter '1' or '2':\n")

if inp == "1":
    F = raw_input ("Enter Fahrenheit temperature:\n")
    F = float(F)
    C = (F - 32) * 5/9
    print "Celsius temperature:", C

elif inp == "2":
    C = raw_input ("Enter Celsius temperature:\n")
    C = float(C)
    F = (C * 9/5) + 32
    print "Fahrenheit temperature:", F

else:
    print "Error! Please enter '1' or '2'!"

# Version 0.3.0