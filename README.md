# findMe development Workspace 🤖

## Quick Access Links

- [wiki](https://github.com/uzh-ase-fs24/workspace/wiki)
- [findme-backend](https://github.com/uzh-ase-fs24/backend)
- [findme-frontend](https://github.com/uzh-ase-fs24/frontend)
- [findme-shared](https://github.com/uzh-ase-fs24/shared)

## Overview

The development workspace is configured as a pycharm project. It is intended to be used as the project folder.
Each repository used for development will be cloned inside this workspace.

```yaml
workspace
-- .idea # pycharm project configuration
-- scripts # configuration / commit scripts
  # findme repositories
-- backend
-- frontend
-- shared
-- workspace.wiki # findme wiki
docker-compose.yml # to run application locally
```

## Setup

### Prerequisites

- python3.12
- [pre-commit](https://pre-commit.com/#installation)
- [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli)
- check each repository for their prerequisites

### Initialization

After cloning this repository run `python scripts/initialize_project.py` this will:

- configure your git config
- clone all necessary repositories
- initialize pre-commit checks in each repository (you can do it manually by running `pre-commit install` in each
  repository)

## Running the application

The findMe application is designed and built as a cloud native application. To run the application locally we use docker
and docker compose.
By running `docker compose up --build` from the root directory of this workspace the application will be started
locally. After the initial build you can use `docker compose up` to start the application.
However, this will not include any changes made to the backend repository since the last build.

Our docker compose defines the following services:

```yaml
  - localstack-main # emulates AWS services for local development
  - serverless # used to deploy the AWS services to localstack (shuts down after successful execution)
  - frontend # mounted frontend code, serves the frontend on localhost:8100
```

After the serverless container has stopped the application is ready and accessible on http://localhost:8100, use chrome
and its mobile view that can be activated in the dev tools to simulate a mobile device.