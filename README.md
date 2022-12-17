# demo-predictive-model-apis

Serving a classification model via FastAPI.


### Quick Start

```bash
make start
```

Once the docker finishes setting up database, cache, and api in the compose file. You can access the API at http://localhost:8080 and the documentation can be accessed at http://localhost:8080/docs.


### Local Development

```bash
make startup_db

cd app
poetry shell
make uvicorn
```

### Sample Request

The documentation will provide your example curl request to interact with your api.

```bash
# Post data to the api.
curl -X 'POST' \
  'http://localhost/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "string",
  "password": "string"
}'
```

And to fetch results back.

```bash
# Fetch results from the API.
curl -X 'GET' \
  'http://localhost/users/?skip=0&limit=100' \
  -H 'accept: application/json'
```