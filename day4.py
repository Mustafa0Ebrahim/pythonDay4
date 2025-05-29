import math
import matplotlib.pyplot as plt
timeList = []
tempList = []
powerList = [] 
i = 0
choice = input("Type 1 For Getting The Reactor Data or 2 to Calculate The remaining Flux of Radioactive Element Or 3 to End it")
if choice == "1":
    try:
        with open ("reactorData.txt") as file:
            head = file.readline()
            for line in file:
                time, temp, power = line.strip().split(',')
                timeList.append(int(time))
                tempList.append(int(temp))
                powerList.append(int(power))
                print(f"At time {timeList[i]}, second the temperature becomes {tempList[i]} C and generates Power of {powerList[i]} MegaWatt")
                i = i+1
        maxTemp = max(tempList)
        maxTempTime = timeList[tempList.index(maxTemp)]
        maxPower = max(powerList)
        print(f"The reactor max temperature is {maxTemp} C at time {maxTempTime} Seconds")
        plt.figure(figsize=(10, 5))  
        plt.plot(timeList, tempList, 'r-o', label="Core Temp (°C)")  
        plt.xlabel("Time (seconds)")  
        plt.ylabel("Temperature (°C)")
        plt.title("Reactor Core Temperature Over Time")
        plt.grid(True)
        plt.legend()
        plt.show()
        with open("reactorReport" , "w") as report:
            report.write("***Reactor Report***\n")
            report.write(f"The Reactor Max Temperature Is {maxTemp} C at Time {maxTempTime} Seconds\n")
            report.write(f"The Reactor Max Generated Power is {maxPower}")
    except FileNotFoundError:
        print("File Not Found!")
elif choice == "2":
    try:
        initialFlux = input("Enter The Initial Flux")
        initialFlux = int(initialFlux.strip())
        time = input("Enter The Time")
        time = int(time.strip())
        halfLife = input("Enter The Element Half Life")
        halfLife = int(halfLife.strip())
        remainingFlux = initialFlux * math.exp(-0.693 * time / halfLife)
        print(f"remainingFlux is {remainingFlux}")
    except:
        print("Error! Please review the input Data")
elif choice == "3":
    print("Bye!")
else:
    print("Invalid Value")
