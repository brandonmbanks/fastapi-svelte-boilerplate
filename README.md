# fastapi-svelte-template
The goal of this repo is to get some of the initial boilerplate code out of the way.
* Containerized simple but functional apps
* Connection between frontend and backend
* Simple user with email, name, password
* Authentication with OAuth2 and JWT

## Pre-Req
[Docker](https://docs.docker.com/get-docker/) is required to use this template

## Setup
1. Clone the repo
2. Copy the backend `.env.example` file with
```
cp app/.env.example app/.env
```
3. Start the docker containers
```
make up
```

## Tests
Make sure docker containers are running. This will include the backend FastAPI app, the frontend Svelte app, and Postgres DB.

```bash
docker-compose up -d
```

### Backend tests
[Pytest](https://docs.pytest.org/en/stable/) is used as the runner.

1. Exec into the app container: `docker-compose exec app bash`
2. Run `pytest`


**Pytest Rules**
* Each test file name must start with `test_`
* Each test function name must start with `test_`
* If grouping tests in a class, the class name must start with `Test`
* Pytest will capture stdout and stderr to control the output. You can use `pytest -s` to disable the capture.
