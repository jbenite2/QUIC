all: run

run: 
	python examples/http3_client.py --ca-certs tests/pycacert.pem  https://localhost:4433/ -d "TESTING1"
	python examples/http3_client.py --ca-certs tests/pycacert.pem  https://localhost:4433/ -d "TESTING2"
	python examples/http3_client.py --ca-certs tests/pycacert.pem  https://localhost:4433/ -d "TESTING3"
	python3 receive_times.py

clean:
	rm -f output.txt
