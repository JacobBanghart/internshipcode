#Jacob Banghart
#Last edited 6/5/2020
askedAverage = 1
cases = []
while(askedAverage > 0):
    askedAverage = int(input(""))
    if(askedAverage >= 0):
        totalTests = int(input(""))
        weights = []
        currentGrades = []
        currentWeight = 0
        for i in range(0, totalTests):
            weights.append(int(input("")))
        for i in range(0, totalTests - 1):
            currentGrades.append(float(input("")))
            currentWeight += weights[i] * (currentGrades[i] / 100)
        neededWeight = askedAverage - currentWeight
        if(neededWeight > weights[len(weights) - 1]):
            cases.append("Impossible")
        else:
            cases.append((neededWeight/weights[len(weights) - 1]) * 100)
print("\n")
for i in range(0, len(cases)):
    print("Case "+ str(i) + ": " + str(cases[i]))