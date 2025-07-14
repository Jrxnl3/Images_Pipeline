CONTAINER_NAME = myapp_container
PROCESSED_DIR = C:/Users/benho/Pictures/images/processed

.PHONY: build run stop logs test clean

build:
	docker build -t image_backend ./image_backend
	docker build -t image_processor ./image_processor

run-processor:
	docker run -d image_processor \
		-v ~/uploads:/app/uploads \
		-v ~/processed:/app/processed