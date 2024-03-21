# Server application

## Requirements
Python 3.10+

## Installation
<details>
<summary>Install Python (3.12) if it is not available in your package manager</summary>

These instructions are for Ubuntu 22.04. If you're on a different distribution,
or - God forbid! - Windows, you should adjust these accordingly.

Also, these instructions are about using Poetry with Pyenv-managed (non-system) Python.
 
### Step 1: Update and Install Dependencies
Before we install pyenv, we need to update our package lists for upgrades and new package installations. We also need to install dependencies for pyenv. 

Open your terminal and type:
```bash
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils \
tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

### Step 2: Install Pyenv
We will clone pyenv from the official GitHub repository and add it to our system path.
```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec "$SHELL"
```

### Step 3: Install Python 3.12
Now that pyenv is installed, we can install different Python versions. To install Python 3.12, use the following command:
```bash
pyenv install 3.12
```

### Step 4: Connect Poetry to it
Do this in the template dir. Pycharm will automatically connect to it later
```bash
poetry env use ~/.pyenv/versions/3.12.1/bin/python
```
(change the version number accordingly to what is installed)

Finally, verify that Poetry indeed is connected to the proper version:
```bash
poetry enf info
```
</details>  

1. If you don't have `Poetry` installed run:
```bash
pip install poetry
```

2. Install dependencies:
```bash
poetry config virtualenvs.in-project true
poetry install --no-root --with dev,test
```

3. Launch the project:
```bash
poetry run uvicorn app.api.main:app [--reload]
```

1. Running tests:
```bash
poetry run pytest
```

## Manual build and deployment on minikube
1. Install [minikube](https://minikube.sigs.k8s.io/docs/start/).
2. Start minikube:
```bash
minikube start
```
3. Build a docker image:
```bash
docker build . -t ui-gateway:latest
```
4. Upload the docker image to minikube:
```bash
minikube image load ui-gateway:latest
```
5. Deploy the service:
```bash
helm upgrade --install ui-gateway-dep ./charts/server --set image.repository=ui-gateway --set image.tag=latest --version 0.1.0
```

## Prometheus metrics
The application includes prometheus-fastapi-instrumentator for monitoring performance and analyzing its operation. It automatically adds an endpoint `/metrics` where you can access application metrics for Prometheus. These metrics include information about request counts, request execution times, and other important indicators of application performance.
More on that at (Prometheus FastAPI Instrumentator)[https://github.com/trallnag/prometheus-fastapi-instrumentator]
