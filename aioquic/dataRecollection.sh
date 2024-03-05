#!/bin/bash

# Interval incrementation
for ((i=0; i<10; i++))
do
    interval=$(echo "scale=3; $i * 0.080" | bc)
	echo "Packet Number: $((i+1))" >> output.txt
    echo "Interval: $interval" >> output.txt
    
    # Start the server in the background
    python examples/http3_server.py --certificate tests/ssl_cert.pem --private-key tests/ssl_key.pem -interval $interval -size 1024 &
    
    # Capture the PID of the server process
    server_pid=$!
    echo "Server started with PID: $server_pid"
    
    # Start the client
    python examples/http3_client.py --ca-certs tests/pycacert.pem  https://localhost:4433/
    echo "Client started"
    
    # Kill the server process
    echo "Killing server with PID: $server_pid"
    kill $server_pid
    
    # Wait for the server to shut down
    sleep 1
done

