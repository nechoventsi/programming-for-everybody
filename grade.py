inp = raw_input ("Enter score (between 0 and 1): ")

if inp == "":
    print "Error! Please enter score between 0 and 1!"
    quit()

score = float(inp)

if score < 0 or score > 1:
    print "Error! Please enter score between 0 and 1!"
    quit()

else:
    if score >= 0.9:
        print "Grade: A"

    elif score >= 0.8:
        print "Grade: B"

    elif score >= 0.7:
        print "Grade: C"

    elif score >= 0.6:
        print "Grade: D"

    else:
        print "Grade: F"