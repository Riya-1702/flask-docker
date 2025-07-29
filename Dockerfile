FROM ubuntu:22.04
RUN apt update && \
    apt install -y python3 python3-pip && \
    apt clean
WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]
