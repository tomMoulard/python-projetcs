all: run

run:
	date > test.txt
	./benchmark-compression.py --file test.txt > data.$(shell date +'%Y-%m-%d-%H-%M-%S').csv

clean:
	$(RM) -r test.txt*
	$(RM) -r data.*.csv
