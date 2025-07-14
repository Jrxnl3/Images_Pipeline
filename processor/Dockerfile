FROM ubuntu:latest

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
      python3 \
      python3-pip \
      darktable \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

EXPOSE 8000

CMD ["python3", "app.py"]
