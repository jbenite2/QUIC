import matplotlib.pyplot as plt

# Data
data_packets = range(1, 9)
time_sent = [1711431246.485677, 1711431246.73689, 1711431246.9882848, 1711431247.239805, 
             1711431247.491288, 1711431247.742762, 1711431247.994213, 1711431248.245524]
time_received = [1711431248.497519, 1711431248.4975228, 1711431248.497525, 1711431248.4975271, 
                 1711431248.497529, 1711431248.497531, 1711431248.4975328, 1711431248.4975848]

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

