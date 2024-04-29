import matplotlib.pyplot as plt

# Read data from output.txt
time_sent = []
time_received = []
with open("output.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        parts = line.split(":")
        if parts[0] == "SERVER":
            time_sent.append(float(parts[2]))
        elif parts[0] == "CLIENT":
            time_received.append(float(parts[2]))

# Data packets
data_packets = range(1, len(time_sent) + 1)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(data_packets, time_sent, marker='o', label='Time Sent')
plt.plot(data_packets, time_received, marker='o', label='Time Received')
plt.title('Time Sent vs Time Received')
plt.xlabel('Data Packet')
plt.ylabel('Time')
plt.legend()
plt.grid(True)
plt.show()

