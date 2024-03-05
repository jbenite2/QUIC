import json
from collections import defaultdict

def parse_text_to_json(input_file, output_file):
    data = defaultdict(dict)
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines, start=1):
            if i % 7 != 0:
                match i % 7:
                    case 1: #Packet Number
                        packetNumber = line.strip().split(': ')[1]  # Change ':' to your delimiter
                    case 2: #Interval
                        interval = line.strip().split(': ')[1]  # Change ':' to your delimiter
                        data[packetNumber]["interval"]= interval.strip()
                    case 3: #Server Send
                        value = line.strip().split(':')[2]  # Change ':' to your delimiter
                        data[packetNumber]["serverSend"]= value.strip()
                    case 4: #Client Request Time
                        value = line.strip().split(':')[2]  # Change ':' to your delimiter
                        data[packetNumber]["clientSend"]= value.strip()
                    case 5: #Client Received Time
                        value = line.strip().split(':')[2]  # Change ':' to your delimiter
                        data[packetNumber]["clientReceived"]= value.strip()
                    case 6: #Client RTT
                        value = line.strip().split(':')[2]  # Change ':' to your delimiter
                        data[packetNumber]["clientRTT"]= value.strip()
                 
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    input_file = "output.txt"  # Replace with your input file path
    output_file = "output.json"  # Replace with your output file path
    parse_text_to_json(input_file, output_file)

