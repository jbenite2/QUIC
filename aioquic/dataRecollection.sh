#!/bin/bash

# Interval incrementation
for ((i=0; i<1; i=i+0.080))
do
	python examples/http3_server.py --certificate tests/ssl_cert.pem --private-key tests/ssl_key.pem -interval $i -size 1024
	server_pid=$!  # Get the PID of the server process
	python examples/http3_client.py --ca-certs tests/pycacert.pem  https://localhost:4433/
	kill $server_pid  # Kill the server process
done



