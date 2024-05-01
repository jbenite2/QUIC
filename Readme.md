# Notre Dame Computer Networks Research: QUIC Findings

During the course of the spring semester in 2024, I conducted a series of experiments using two main QUIC open-source libraries: Aioquic and Quiche.

## Aioquic
- Started by forking this repo:
    ```bash
    git clone https://github.com/aiortc/aioquic
    ```
- To find the functions modified by me command find jbenite2.
- The files that I specifically modified are the following:
    - [aioquic/examples/http3_client.py](https://github.com/jbenite2/QUIC/blob/main/aioquic/examples/http3_client.py) 
       - The function perfor_http_request was modified to log received packets.
    - [aioquic/examples/http3_server.py](https://github.com/jbenite2/QUIC/blob/main/aioquic/examples/http3_server.py)
       - Flags were added to main to adapt to the size, interval, and count of the data that is returned after the GET request is sent. 
       - HTTP_event_received was modified to account for the flags that were added and also dynamically return an input of a given size at specified intervals. 
    - [aioquic/dataRecollection.sh](https://github.com/jbenite2/QUIC/blob/main/aioquic/dataRecollection.sh)
       - This script starts the client and the server by running using a for loop. 
    - [aioquic/output.json](https://github.com/jbenite2/QUIC/blob/main/aioquic/output.json)
       - Contains the results of the server and the client after processing. 
    - [aioquic/output.txt](https://github.com/jbenite2/QUIC/blob/main/aioquic/output.txt)
       - Contains the results of the server and the client before processing. 
    - aioquic/parseTextToJson.py
    - [aioquic/parseTextToJson.py](https://github.com/jbenite2/QUIC/blob/main/aioquic/parseTextToJson.py)
       - Parses the txt file and organizes it in a way that is suitable for graphing.  
    - [aioquic/Makefile](https://github.com/jbenite2/QUIC/blob/main/aioquic/Makefile)
    - [aioquic/createGraph.py](https://github.com/jbenite2/QUIC/blob/main/aioquic/createGraph.py)
       -Leverages pyplot to make a graph of the results


> The code is originally structured so client sends data to the server. I had to switch this logic so that the client send a GET request to the server and it responds with the data. 
> The code was also modified so the user could add interval, size, and count as arguments. 

- This is how to run the example server and client:
    ```bash
        python examples/http3_server.py --certificate tests/ssl_cert.pem --private-key tests/ssl_key.pem -interval 0.250 -size 100 -count
        python examples/http3_client.py --ca-certs tests/pycacert.pem https://localhost:4433/
    ```
- By running "make", the scripts will run in order. Type this command after the "make" to see the results in a graph format:
    ```bash
        python createGraph.py
    ```

- Key findings:
    - Aioquic's asynchronous logic doesn't allow for packet separation upon reception. 
        - All the packets, even though they were sent out individually, were bundled together and delivered at the same time as shown by this graph. 
        ![image](aioquic_graph.png)
        - The graph above shows how I sent packages out at a certain interval and QUIC bundled them together on the client side so they all seem to be coming in at the same time. 
        - The main idea was to have the packets come in individually. However, I couldn't find a way to do this in Aioquic. After much trying I looked for another way to achieve this goal: QUICHE. 


## Quiche
- Started by forking this repository.
```bash
https://github.com/cloudflare/quiche
```

- This project uses RUST. I ran it using a Macbook Pro and had to download several dependencies including cargo. 

- The files that I specifically modified:
    - quiche/apps/src/bin/quiche-client.rs
        - This file references the actual client which is the one below.
    - quiche/apps/src/bin/quiche-server.rs
    - quiche/apps/bin/args.rs
        - Modified common args in an attempt to modify the size of the data sent and the intervals.
    - quiche/apps/bin/client.rs
        - Added stopwatch logic to record send time. 
    - quiche/examples/server.rs

- To run this:
```bash
cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key
cargo run --bin quiche-client -- --no-verify https://127.0.0.1:4433/
```
   - This will send a couple of packet from the client to the server. 
   - Before my research was over I was trying to figure out how to have the server send the message to the client and modify the existing flags found in args.rs to modify the size of the packets and the gaps between them. 
    - I'd recommend starting from here moving forward. Once the behavior described in Aioquic can be replicated in Rust, we'll find out if the Quiche allows for packet division upon reception. This link proved to be quite helpful: [Beginner Issue Section Help](https://github.com/cloudflare/quiche/issues/1518)


- Shifting over to a Rust based project was a good learning experience. Here are some of the resources I used to aid my learning process:
    - [Rust for the impatient](https://www.youtube.com/watch?v=br3GIIQeefY&t=242s)
    - [5 things I wish I knew before learning Rust](https://www.youtube.com/watch?v=EYCBm0xAWow)
    - [Rust tutorial full course](https://www.youtube.com/watch?v=ygL_xcavzQ4)

















