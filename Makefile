.PHONY: all build run shell clean

all: clean build run

# Build Docker images
build:
	docker build -t image_backend ./backend
	docker build -t image_processor ./processor

# Run Docker containers
run:
	docker run -d --name backend_container -p 1234:8000 image_backend \
			-v $$HOME/Pictures/images/uploads:/app/upload \
            -v $$HOME/Pictures/images/uploads:/app/backup \

	docker run -d --name processor_container \
		-v $$HOME/Pictures/images/uploads:/app/upload \
		-v $$HOME/Pictures/images/processed:/app/processed \
		image_processor

clean:
	docker rm -f backend_container processor_container || true
	docker rmi -f image_backend image_processor || true
