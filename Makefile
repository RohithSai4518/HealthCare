# HealthSphere Automation Makefile

.PHONY: help install build run test cli seed docker-build docker-run clean

help:
	@echo "HealthSphere Management Commands:"
	@echo "  make install      - Install project dependencies into virtualenv"
	@echo "  make build        - Build python package distribution artifacts"
	@echo "  make run          - Launch the RESTful API Server and Web Dashboard"
	@echo "  make test         - Execute the complete automated unit and integration test suite"
	@echo "  make cli          - Launch the interactive clinical terminal dashboard"
	@echo "  make seed         - Seed 10 synthetic patient records and export FHIR bundle"
	@echo "  make docker-build - Build the Docker container image"
	@echo "  make docker-run   - Run the Docker container on port 8000"
	@echo "  make clean        - Clean up bytecode cache and build artifacts"

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .

build:
	python setup.py sdist bdist_wheel

run:
	python main.py --serve --port 8000

test:
	python main.py --test

cli:
	python main.py

seed:
	python main.py --seed 10

docker-build:
	docker build -t healthsphere:latest .

docker-run:
	docker run -p 8000:8000 healthsphere:latest

clean:
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .coverage __pycache__ */__pycache__
