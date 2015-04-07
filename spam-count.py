# This script opens a file,
# searches through it for a specific line;
# then extracts the number from it
# and counts the average.

fname = raw_input("Enter file name: ")
fhandle = open(fname)

count = 0
spam = 0

try:

    for line in fhandle:
        if line.startswith("X-DSPAM-Confidence:"):
            count = count + 1
            colon = line.find(":")
            if spam == 0:
            spam = float(line[colon + 1:])
            else:
                spam = spam + float(line[colon + 1:])

except:
    print "Error! Bad input data!"
    quit()

avspam = spam / count
print "Average spam confidence:", avspam

# Version 0.1.1