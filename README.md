## Project summary
This project is a calculator with 10 digits.

It is a demonstration of a Python Flask web app put in a Docker image.

## Project files explained

#### Flask files:
- main.py:                Python file to run to start the Flask app
- templates:              Directory for HTML files used by the Flask app
- templates/index.html:   HTML file which contains the GUI of the calculator


#### Python files:
- calculator.py:          The code for the calculator
- requirements.txt:       List of Python packages necessary to install before the Python app can run (i.e. the Flask package)

#### Docker files:
- Dockerfile:             Configuration file for creating the Docker image

#### Git files:
- .gitignore:             Tells Git to ignore `__pycache__` directory
- README.md:              This README file which describes the project


## Docker commands

These commands have been tested with Docker Desktop for Windows.

They require Docker Desktop to be running and are to be typed in a terminal window (e.g. Command Prompt or PowerShell).

#### Build image and container:

1. Build Docker image (terminal must be in root directory of project):

    `docker build --tag calculator_image .`

2. Create Docker container from image and tell it to use port 5001:

    `docker create --name calculator_container -p 5001:5001 calculator_image`

#### Start/stop container:

1. Start Docker container:

    `docker start calculator_container`

2. Open a browser to use the Flask app:

        "http://localhost:5001" or "http://127.0.0.1:5001"

3. Stop Docker container:

    `docker stop calculator_container`

#### Save/load image from tar file:

- Save Docker image to tar file (terminal must be in directory where file should be saved):

    `docker save -o calculator_image.tar calculator_image`

- Load Docker image from tar file (terminal must be in directory where file is located):
    
    `docker load -i calculator_image.tar`