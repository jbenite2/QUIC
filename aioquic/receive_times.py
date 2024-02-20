receiveTimes = []
timeDiff = []

#Open the file where time stamps are recorded and parse it
with open('output.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        timestamp = float(line.split(': ')[1].split('}')[0])
        receiveTimes.append(timestamp)

#Save the time differences into an array
for i in range(1, len(receiveTimes), 2):
    timeDiff.append((receiveTimes[i-1] - receiveTimes[i]) * 1000)

#Print to std::out
for i, time_diff in enumerate(timeDiff):
    print(i, "Time difference (ms):", time_diff)

