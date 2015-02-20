try:
    inp = raw_input ("Enter hours: ")
    hours = float(inp)
    inp = raw_input ("Enter rate: ")
    rate = float(inp)

except:
    print "Error! Please enter numeric input!"
    quit()

if hours > 40:
    over_40 = hours - 40
    result = (40 * rate) + (over_40 * (rate * 1.5))
    print "Pay:", result

else:
    result = hours * rate
    print "Pay:", result

# Version 0.3.2