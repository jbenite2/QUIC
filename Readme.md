# Notre Dame Computer Networks Research: QUIC Findings

During the course of the spring semester of 2024. I realized a series of experiments, leveraging two main QUIC open source libraries: Aioquic and Quiche. 

## Aioquic
- I started by forking this repo:
```bash
git clone https://github.com/aiortc/aioquic
```

- The files that I specifically modified are the following:
-- aioquic/examples/http3_client.py 
-- aioquic/examples/http3_server.py
-- aioquic/dataRecollection.sh
-- aioquic/output.json
-- aioquic/output.txt
-- aioquic/setup.py
-- aioquic/parseTextToJson.py
-- aioquic/Makefile
-- aioquic/createGraph.py


- The code is originally structured so client sends data to the server. I had to switch this logic so that the client send a GET request to the server and it responds with the data. 
- The code was also modified so the user could add interval, size, and count as arguments. 

- This is how to run the example server and client:
```bash
    python examples/http3_server.py --certificate tests/ssl_cert.pem --private-key tests/ssl_key.pem -interval 0.250 -size 100 -count
    python examples/http3_client.py --ca-certs tests/pycacert.pem https://localhost:4433/
```
- By running make, the scripts will run in order. Type this command to see the results in a graph format:
```bash
    python createGraph.py
```

- Key findings:
    - Aioquic's asynchronous logic doesn't allow for packet separation upon reception. 
        - All the packets, even though they were sent out individually, were bundled together and delivered at the same time as shown by this graph. 
        ![image](aioquic_graph.png)









