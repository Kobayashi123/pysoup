PYTHON	= python
PYDOC	= pydoc
PYCS	= $(shell find src -name "*.pyc")
PYCACHE	= $(shell find src -name "__pycache__")
TARGET_DIR	= src/pysoup
TARGET	= $(TARGET_DIR)/*.py
MODULE	= src/pysoup
ARCHIVE	= $(shell basename `pwd`)
WORKDIR	= ./

all:
	@:

wipe: clean
	@find . -name ".DS_Store" -exec rm {} ";" -exec echo rm -f {} ";"
	(cd ../ ; rm -f ./$(ARCHIVE).zip)

clean:
	@for each in ${PYCS} ; do echo "rm -f $${each}" ; rm -f $${each} ; done
	@for each in ${PYCACHE} ; do echo "rm -f $${each}" ; rm -rf $${each} ; done
	@if [ -e $(LINTRST) ] ; then echo "rm -f $(LINTRST)" ; rm -f $(LINTRST) ; fi
	@find . -name ".DS_Store" -exec rm {} ";" -exec echo rm -f {} ";"
	@find output -name "*.html" -exec rm {} ";" -exec echo rm -f {} ";"

run:
	$(PYTHON) ./$(TARGET)

doc:
	$(PYDOC) ./$(TARGET)

zip: wipe
	(cd ../ ; zip -r ./$(ARCHIVE).zip ./$(ARCHIVE)/ --exclude='*/.git/*')

pydoc:
	(sleep 3 ; open http://localhost:9999/$(MODULE).html) & $(PYDOC) -p 9999

lint: flake8 isort black
	flake8 $(TARGET_DIR)
	isort --check --diff $(TARGET_DIR)
	black --check $(TARGET_DIR)

format: isort black
	isort $(TARGET_DIR)
	black $(TARGET_DIR)

#
# pip is the PyPA recommended tool for installing Python packages.
#
pip:
	@if [ -z `which pip` ]; \
	then \
		(cd $(WORKDIR); curl -O https://bootstrap.pypa.io/get-pip.py); \
		(cd $(WORKDIR); sudo -H python get-pip.py); \
		(cd $(WORKDIR); rm -r get-pip.py); \
	else \
		(cd $(WORKDIR); sudo -H pip install -U pip); \
	fi

#
# Flake8 is a tool that checks for errors in Python code,
# tries to enforce a coding standard and looks for code smells.
#
flake8:
	@if [ -z `pip list --format=freeze | grep flake8` ]; \
	then \
		(cd $(WORKDIR); sudo -H pip install flake8); \
	fi

#
# black is a tool that checks for errors in Python code,
# tries to enforce a coding standard and looks for code smells.
#
black:
	@if [ -z `pip list --format=freeze | grep black` ]; \
	then \
		(cd $(WORKDIR); sudo -H pip install black); \
	fi

#
# isort is a tool that checks for errors in Python code,
# tries to enforce a coding standard and looks for code smells.
#

isort:
	@if [ -z `pip list --format=freeze | grep isort` ]; \
	then \
		(cd $(WORKDIR); sudo -H pip install isort); \
	fi

#
# mypy is a tool that checks for errors in Python code,
# tries to enforce a coding standard and looks for code smells.
#

mypy:
	@if [ -z `pip list --format=freeze | grep mypy` ]; \
	then \
		(cd $(WORKDIR); sudo -H pip install mypy); \
	fi

#
# List of the required packages
#
list: pip
	@(pip list --format=freeze | grep pip)
	@(pip list --format=freeze | grep flake8)
	@(pip list --format=freeze | grep black)
	@(pip list --format=freeze | grep isort)
	@(pip list --format=freeze | grep mypy)

prepare: pip flake8 black isort mypy

update: pip flake8 black isort mypy
