.PHONY: all build run shell clean

all: clean build run

# Build Docker images
build:
	docker build -t image_backend ./backend
	docker build -t image_processor ./processor

# Run Docker containers
run:
	docker run -d --name backend_container \
		-p 1234:8000 \
		-v $$HOME/Pictures/images/upload:/app/upload \
		-v $$HOME/Pictures/images/backup:/app/backup \
		image_backend

	docker run -d --name processor_container \
		-v $$HOME/Pictures/images/uploads:/app/upload \
		-v $$HOME/Pictures/images/processed:/app/processed \
		image_processor

# Stop and remove containers/images
clean:
	-docker rm -f backend_container processor_container
	-docker rmi -f image_backend image_processor
