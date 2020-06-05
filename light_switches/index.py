#Jacob Banghart
#Last Editied: 6/5/2020
from math import floor
data = open("testdata.txt", "r")
output = []
for line in data:
    #read data and assign variables
    numbers = line.split()
    numberBaulbs = int(numbers[0])
    time = int(numbers[1])
    baulb = int(numbers[2])

    #remove repeated cycles
    newtime = time - (floor(time / numberBaulbs) * numberBaulbs)

    #determine on/off
    if newtime == 0:
        output.append("Off")
    elif newtime == 1:
        output.append("On")
    else:
        factors = []
        for i in range(1, baulb + 1):
            if(baulb % i == 0):
                factors.append(i)
            elif(i > newtime):
                break
        if len(factors) % 2 == 0:
            output.append("Off")
        else:
            output.append("On")

#close file and ouput results
data.close()
for i in range(0, len(output)):
    print("Case "+ str(i) + ": " + str(output[i]))