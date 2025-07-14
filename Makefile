IMAGE_NAME = myapp
CONTAINER_NAME = myapp_container
UPLOAD_DIR = C:/Users/benho/Pictures/images/uploads
PROCESSED_DIR = C:/Users/benho/Pictures/images/processed

.PHONY: build run stop logs test clean

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d --name $(CONTAINER_NAME) -p 8000:8000 \
		-v $(UPLOAD_DIR):/app/uploads \
		-v $(PROCESSED_DIR):/app/processed \
		$(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

logs:
	docker logs -f $(CONTAINER_NAME)

test:
	pytest tests/

clean: stop
	docker rmi $(IMAGE_NAME) || true
