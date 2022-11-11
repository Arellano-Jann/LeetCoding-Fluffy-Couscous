COMPILER = python3
FLAGS = 
FILES = solution.py
FOLDER = 36ValidSudoku

all: main

main: $(FOLDER)/$(FILES)
	$(COMPILER) $(FLAGS) $^

clean:
	rm -rf __pycache__

.PHONY: clean all