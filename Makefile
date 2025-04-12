# Image name
IMAGE_NAME = darcounting-ask-service

# Docker build command
build:
	docker build -t $(IMAGE_NAME) .

# Docker run command
run:
	docker run -p 50051:50051 --env-file .env --add-host=host.docker.internal:host-gateway $(IMAGE_NAME)

# Clean up Docker images
clean:
	docker rmi $(IMAGE_NAME)

# Stop and remove running containers
stop:
	docker stop $(shell docker ps -q --filter ancestor=$(IMAGE_NAME))
	docker rm $(shell docker ps -a -q --filter ancestor=$(IMAGE_NAME))