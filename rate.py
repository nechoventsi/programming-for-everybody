hours = raw_input ("Enter hours: ")
rate = raw_input ("Enter rate: ")

hrs_fl = float(hours)
rt_fl = float(rate)

if hrs_fl > 40:
    over_40 = hrs_fl - 40
    result = (40 * rt_fl) + (over_40 * (rt_fl * 1.5))
    print "Pay:", result

else:
    result = hrs_fl * rt_fl
    print "Pay:", result

# Version 0.3.1