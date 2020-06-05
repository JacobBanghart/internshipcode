#Jacob Banghart
#Last edited 6/5/2020
askedAverage = 1
cases = []
while(askedAverage > 0):
    askedAverage = int(input("What is the Percentage you want in the class?"))
    if(askedAverage >= 0):
        totalTests = int(input("Input the total number of tests including the final:"))
        weights = []
        currentGrades = []
        currentWeight = 0
        print("What is the weight for each test(insert separately)")
        for i in range(0, totalTests):
            weights.append(int(input(":")))

        print("Please insert the grades as a percentage for each test excluding the final")
        for i in range(0, totalTests - 1):
            currentGrades.append(float(input(":")))
            currentWeight += weights[i] * (currentGrades[i] / 100)
        neededWeight = askedAverage - currentWeight
        if(neededWeight > weights[len(weights) - 1]):
            cases.append("Impossible")
        else:
            cases.append((neededWeight/weights[len(weights) - 1]) * 100)
print("\n")
for i in range(0, len(cases)):
    print("Case "+ str(i) + ": " + str(cases[i]))