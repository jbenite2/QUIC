all: run

run: clean 
	sh dataRecollection.sh
	python3 parseTextToJson.py


clean:
	rm -f output.txt
