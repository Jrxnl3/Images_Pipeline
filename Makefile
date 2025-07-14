.PHONY: all build run shell clean

all: build run

# Build Docker images
build:
	docker build -t image_backend ./image_backend
	docker build -t image_processor ./image_processor

# Run Docker containers
run:
	docker run -d --name backend_container -p 8000:8000 image_backend
	docker run -d --name processor_container \
		-v $$HOME/Pictures/images/uploads:/app/uploads \
		-v $$HOME/Pictures/images/processed:/app/processed \
		image_processor