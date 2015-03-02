def computegrade(score):
    if score >= 0.9:
        return "A"

    elif score >= 0.8:
        return "B"

    elif score >= 0.7:
        return "C"

    elif score >= 0.6:
        return "D"

    return "F"

inp = raw_input ("Enter score (between 0 and 1): ")

if inp == "":
    print "Error! Please enter score between 0 and 1!"
    quit()

score = float(inp)

if score < 0 or score > 1:
    print "Error! Please enter score between 0 and 1!"
    quit()

print "Grade:", computegrade(score)

# Version 0.2.0