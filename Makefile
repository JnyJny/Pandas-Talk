# Pandas Talk Makefile

PYTHON3= python3
VENV= .venv
PIP=  $(PYTHON3) -m pip
UPDATE_PIP= $(PIP) install -U pip
INSTALL_REQUIREMENTS= $(PIP) install -Ur requirements.txt
ACTIVATE= . $(VENV)/bin/activate

all:
	@echo
	@echo '-- Pandas Talk Makefile Targets --'
	@echo
	@echo 'install - Install Notebook Dependencies '
	@echo 'start   - Start the Jupyter Notebook Server.'
	@echo

	@echo

$(VENV):
	$(PYTHON3) -m venv --prompt Pandas $(VENV)

install: $(VENV)
	$(ACTIVATE) && $(UPDATE_PIP) && $(INSTALL_REQUIREMENTS)

start:
	$(ACTIVATE) && jupyter-notebook >& jupyter.log 
