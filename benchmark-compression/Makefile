all: run

run:
	./benchmark-compression.py -c 3 --file test.txt > data.$(shell date +'%Y-%m-%d-%H-%M-%S').csv

clean:
	$(RM) -r test.txt*
	$(RM) -r data.*.csv
