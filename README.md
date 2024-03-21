# UI gateway service
An intermediary component between Glaciation Frontend and Metadata Service. The service adapts user interface queries into a series of SPARQL requests to MetadataService and telemetry requests from Storage Service. The service also checking user permissions via oauth server and filters the KGs that a user is not allowed to access.

## Development
Work on the server and client is conducted in their respective directories: server and client, as the server-side and client-side parts have different dependencies, configurations, etc.

### Requirements
Python 3.10+

### Installation pre-commit hooks
```bash
pip install pre-commit
pre-commit install
```

### Working on a server
Go to the `/server` folder to install dependencies and work on the server application.  
Documentation on setting up the virtual environment, installing dependencies, and working with the server can be found [here](./server/README.md).

### Working on a client
Go to the `/client` folder to install dependencies and work on the client application.  
Documentation on setting up the virtual environment, installing dependencies, and working with the client can be found [here](./client/README.md).

### Release
The application version is specified in the VERSION file. The version should follow the format a.a.a, where 'a' is a number.  
To create a release, update the version in the VERSION file and add a tag in GIT.  
The release version for branches, pull requests, and tags will be generated based on the base version in the VERSION file.

### GitHub Actions
GitHub Actions triggers testing, builds, and application publishing for each release.  
https://docs.github.com/en/actions

During the build and publish process, a Docker image is built, a Helm chart is created, an openapi.yaml is generated.

**Initial setup**  
Create the branch gh-pages and use it as a GitHub page https://pages.github.com/.  
Set up secrets at `https://github.com/glaciation-heu/ui_gateway/settings/secrets/actions`:
1. DOCKER_IMAGE_NAME - The name of the Docker image for uploading to the repository.
2. DOCKER_USERNAME - The username for the Docker repository on https://hub.docker.com/.
3. DOCKER_PASSWORD - The password for the Docker repository.
4. PYPI_TOKEN - The secret token for PyPI. https://pypi.org/help/#apitoken

**After execution**  
The index.yaml file containing the list of Helm charts will be available at `https://glaciation-heu.github.io/ui_gateway/charts-repo/index.yaml`. You can this URL on https://artifacthub.io/.  
A package of the client will be available at pypi.org.

## Collaboration guidelines
HIRO uses and requires from its partners [GitFlow with Forks](https://hirodevops.notion.site/GitFlow-with-Forks-3b737784e4fc40eaa007f04aed49bb2e?pvs=4)
