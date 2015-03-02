def computepay(hours, rate):
    if hours > 40:
        over_40 = hours - 40
        result = (40 * rate) + (over_40 * (rate * 1.5))

    else:
        result = hours * rate

    return result

try:
    inp_hr = raw_input ("Enter hours: ")
    hours = float(inp_hr)

    inp_rt = raw_input ("Enter rate: ")
    rate = float(inp_rt)

    pay = computepay(hours, rate)
    print pay

except:
    print "Error! Please enter numeric input!"
    quit()

# Version 0.4.0