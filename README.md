# Multasko-Backend
  
## Getting this respository
```bash
git clone https://github.com/clement0010/multasko-backend
```

## Requirements
- [Python 3.7](https://www.python.org/downloads/release/python-370/) or above
- [Docker](https://docs.docker.com/get-docker/) or [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/)
    to host the various servers required in a hassle free manner.

## Using Venv
1. Ensure you have `virtualenv` installed.
    - Follow this [guide](https://www.c-sharpcorner.com/article/steps-to-set-up-a-virtual-environment-for-python-development/) if necessary and you're on a Windows machine.
    - If you're on a mac e.g. [OS X](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html).
2. Ensure you have GNU make installed (Windows only) (Optional).
    - Install chocolatey from [here](https://chocolatey.org/install).
    - Then, `choco install make`.
3. You can create your `virtualenv`. The steps for Windows look something like as follows:

   ```bash
   make venv 
   ```
   
   This will also install all dependencies as listed in the `requirements.txt` file.
4. You can activate your `virtualenv`. This is not required for using `make` commands. The steps for Windows look something like as follows:
    
   ```bash
   venv\Scripts\activate 
   ```
    
   You should see a `(venv)` in front of the prompt on your console/terminal/command prompt.
   This shows your virtual environment is active.

   
## Make commands

These commands are to be executed in the base directory of this repo.

Execute them by typing a `make` in front of them. For example:

```bash
make venv 
```

- Venv Helpers
    - venv             
        - Install dependencies
    - clean-venv
        - Delete the venv folder

- Server  
    - runserver
        - Runs the server at http://localhost:5000


## Not Using Venv

### 1. Ensure that you have install the packages required
Install the pip packages (i)
```bash
pip install -r requirements.txt
```

### 2. Start the flask server
You can start the flask server using the command below
```bash
python main.py
```
And now you can visit the site with the URL http://localhost:5000

### Containerise the app

#### 1. Build the image
You can build the image using the command below
```bash
docker build -t multasko-backend:latest .
```

#### 2. Run container
You can Run container in background using the command below
```bash
docker run -dp 5000:5000 multasko-backend
```
And now you can visit the site with the URL http://localhost:5000
