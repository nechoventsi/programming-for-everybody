largest = None
smallest = None

while True:
    inp = raw_input("Enter a number (or 'done' if ready): ")

    if inp == "done":
        break

    try:
        num = float(inp)
        
    except:
        print "Invalid input"
        continue
    
    if largest is None and smallest is None:
            largest = num
            smallest = num
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num
    continue

print "Maximum is:", largest
print "Minimum is:", smallest

# Version 0.1.0