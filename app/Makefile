# POETRY COMMANDS

.PHONY: pinstall pbuild requirements black pytest black

pinstall:
	poetry install

pbuild: install
	poetry build

requirements:
	poetry export -f requirements.txt --without-hashes -o requirements.txt

black:
	poetry run black .

pytest:
	poetry run pytest --cov=./tests --black -rAP 

black:
	isort .
	black .


# DOCKER / CONTAINER REGISTRY COMMANDS
CONTAINER_NAME=template
PROJECT_ID=kavi-dummy-project-123

.PHONY: build run push attach

build:
	docker build -t gcr.io/$(PROJECT_ID)/$(CONTAINER_NAME) .

run: build
	docker run -it --name ${CONTAINER_NAME} gcr.io/$(PROJECT_ID)/$(CONTAINER_NAME)

push: build
	docker push gcr.io/$(PROJECT_ID)/$(CONTAINER_NAME)

attach:
	docker exec -it $(CONTAINER_NAME) /bin/bash