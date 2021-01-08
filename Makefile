export

VENV_NAME?=venv
PIP_REQUIREMENTS := requirements.txt

# is Windows_NT on XP, 2000, 7, Vista, 10...
ifeq ($(OS),Windows_NT)   
	ROOT_DIR:=$(shell cd)
	TOUCH:=copy NUL 
	REMOVE_DIR:=rd /s /q 
	REMOVE_FILE:=del /F /Q
	PYTHON=$(ROOT_DIR)\\$(VENV_NAME)\\Scripts\\python.exe
	VENV_ACTIVATE := $(VENV_NAME)\\Scripts\\activate
	MAKE_VENV_IF_NOT_EXIST := IF NOT EXIST $(VENV_NAME)/ virtualenv $(VENV_NAME)
else
	ROOT_DIR:=$(shell pwd)
	TOUCH:=touch
	REMOVE_DIR:=rm -rf
	REMOVE_FILE:=rm -f
	PYTHON=$(ROOT_DIR)/$(VENV_NAME)/bin/python3
	VENV_ACTIVATE := $(VENV_NAME)/bin/activate
	MAKE_VENV_IF_NOT_EXIST := test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
endif

export PYTHONPATH += $(ROOT_DIR);

.DEFAULT: help

help:
	@echo xxxxxxxxxxxxxxxxxx  Venv Helpers  xxxxxxxxxxxxxxxxxx
	@echo venv:               Install dependencies
	@echo clean-venv:         Delete the venv folder
	@echo.
	@echo xxxxxxxxxxxxxxxxxx  Server  xxxxxxxxxxxxxxxxxx
	@echo runserver:          Runs the server
	@echo.
	@echo xxxxxxxxxxxxxxxxxx  Containerise the app in Docker  xxxxxxxxxxxxxxxxxx
	@echo docker-setup:       Build the image
	@echo docker-start:       Run container
.PHONY: help

# Requirements are in requirements.txt, so whenever requirements.txt is changed, re-run installation of dependencies.
venv: $(VENV_ACTIVATE)
$(VENV_ACTIVATE): $(PIP_REQUIREMENTS)
	$(MAKE_VENV_IF_NOT_EXIST)
	$(PYTHON) -m pip install -r $(PIP_REQUIREMENTS) 
	$(TOUCH) $(VENV_ACTIVATE)

clean-venv:
	$(REMOVE_DIR) $(VENV_NAME)
.PHONY: clean-venv

runserver:
	$(PYTHON) main.py

docker-setup:
	-docker build -t multasko-backend:latest .
.PHONY: docker-setup

docker-start:
	-docker run -dp 5000:5000 multasko-backend
.PHONY: docker-start
