# UI gateway service
Use this template for developing a web service.

The template includes an example server application in Python with tests, automatically generated OpenAPI file, and an automatically generated client for accessing the server API from third-party applications.

Upon committing and pushing, pre-commit triggers code checks, OpenAPI file generation, and client generation.

Upon pushing the commit to GitHub, workflows are initiated, which:
- Check the code formatting of the server and client;
- Execute server and client tests;
- Create a Docker image of the server, Helm chart, and deploy the application to a Kubernetes cluster.
- Build the client package and push it to [pypi.org](https://pypi.org/)

Work on the server and client is conducted in their respective directories: server and client, as the server-side and client-side parts have different dependencies, configurations, etc.

## Requirements
Python 3.10+

## Installation
```bash
pip install pre-commit
pre-commit install
```

## Working on a server
Go to the `/server` folder to install dependencies and work on the server application.  
Documentation on setting up the virtual environment, installing dependencies, and working with the server can be found [here](./server/README.md).

## Working on a client
Go to the `/client` folder to install dependencies and work on the client application.  
Documentation on setting up the virtual environment, installing dependencies, and working with the client can be found [here](./client/README.md).

## Release
The application version is specified in the VERSION file. The version should follow the format a.a.a, where 'a' is a number.  
To create a release, update the version in the VERSION file and add a tag in GIT.  
The release version for branches, pull requests, and tags will be generated based on the base version in the VERSION file.

## GitHub Actions
GitHub Actions triggers testing, builds, and application publishing for each release.  
https://docs.github.com/en/actions  

You can set up automatic testing in GitHub Actions for different versions of Python. To do this, you need to specify the set of versions in the `.github/workflows/client.yaml` or `.github/workflows/server.yaml file`. For example:
```yaml
strategy:
  matrix:
    python-version: ["3.10", "3.11", "3.12"]
```

During the build and publish process, a Docker image is built, a Helm chart is created, an openapi.yaml is generated, and the web service is deployed to a Kubernetes cluster.

**Initial setup**  
Create the branch gh-pages and use it as a GitHub page https://pages.github.com/.  
Set up secrets at `https://github.com/<workspace>/<project>/settings/secrets/actions`:
1. DOCKER_IMAGE_NAME - The name of the Docker image for uploading to the repository.
2. DOCKER_USERNAME - The username for the Docker repository on https://hub.docker.com/.
3. DOCKER_PASSWORD - The password for the Docker repository.
4. AWS_ACCESS_KEY_ID - AWS Access Key ID. https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html
5. AWS_SECRET_ACCESS_KEY - AWS Secret Access Key
6. AWS_REGION - AWS region. https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
7. EKS_CLUSTER_ROLE_ARN - The IAM role's ARN in AWS, providing permissions for managing an Amazon EKS Kubernetes cluster.
8. EKS_CLUSTER_NAME - Amazon EKS Kubernetes cluster name.
9. EKS_CLUSTER_NAMESPACE - Amazon EKS Kubernetes cluster namespace.
10. HELM_REPO_URL - `https://<workspace>.github.io/<project>/charts-repo/`
11. PYPI_TOKEN - The secret token for PyPI. https://pypi.org/help/#apitoken

**After execution**  
The index.yaml file containing the list of Helm charts will be available at `https://<workspace>.github.io/<project>/charts-repo/index.yaml`. You can this URL on https://artifacthub.io/.  
A package of the client will be available at pypi.org. 

## Act
You can run your GitHub Actions locally using https://github.com/nektos/act. 

Usage example:
```bash
act push -j test_and_build_client --secret-file my.secrets
```

# Collaboration guidelines
HIRO uses and requires from its partners [GitFlow with Forks](https://hirodevops.notion.site/GitFlow-with-Forks-3b737784e4fc40eaa007f04aed49bb2e?pvs=4)
