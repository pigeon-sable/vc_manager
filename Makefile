PYTHON	= python
PYDOC	= pydoc
PYCS	= $(shell find . -name "*.pyc")
PYCACHE	= $(shell find . -name "__pycache__")
TARGET	= Example.py
MODULE	= Example
ARCHIVE	= $(shell basename `pwd`)
WORKDIR	= ./
PYLINT	= pylint
LINTRCF	= .pylintrc
LINTRST	= pylintresult.txt

all:
	@:

wipe: clean
	(cd ../ ; rm -f ./$(ARCHIVE).zip)

clean:
	@for each in ${PYCS} ; do echo "rm -f $${each}" ; rm -f $${each} ; done
	@for each in ${PYCACHE} ; do echo "rm -f $${each}" ; rm -rf $${each} ; done
	@if [ -e $(LINTRST) ] ; then echo "rm -f $(LINTRST)" ; rm -f $(LINTRST) ; fi
	@find . -name ".DS_Store" -exec rm {} ";" -exec echo rm -f {} ";"
	@xattr -cr ./

run:
	$(PYTHON) ./$(TARGET)

doc:
	$(PYDOC) ./$(TARGET)

zip: wipe
	(cd ../ ; zip -r ./$(ARCHIVE).zip ./$(ARCHIVE)/ --exclude='*/.svn/*')

pydoc:
	(sleep 3 ; open http://localhost:9999/$(MODULE).html) & $(PYDOC) -p 9999

lint: pylint clean
	@if [ ! -e $(LINTRCF) ] ; then $(PYLINT) --generate-rcfile > $(LINTRCF) 2> /dev/null ; fi
	pylint --rcfile=$(LINTRCF) `find . -name "*.py"` > $(LINTRST) ; less $(LINTRST)

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
# Pylint is a tool that checks for errors in Python code,
# tries to enforce a coding standard and looks for code smells.
#
pylint:
	@if [ -z `pip list --format=freeze | grep pylint` ]; \
	then \
		(cd $(WORKDIR); sudo -H pip install pylint); \
	fi

#
# List of the required packages
#
list: pip
	@(pip list --format=freeze | grep pip)
	@(pip list --format=freeze | grep pylint)

prepare: pip pylint

update: pip pylint
