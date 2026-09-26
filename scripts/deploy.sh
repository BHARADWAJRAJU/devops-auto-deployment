#!/bin/bash

set -e

echo "Starting deployment..."

cd ~/devops-auto-deployment

echo "Pulling latest code..."
git pull origin main

echo "Building Docker image..."
sudo docker build -t devops-app:latest .

echo "Stopping old container..."
sudo docker stop devops-container || true

echo "Removing old container..."
sudo docker rm -f devops-container || true

echo "Waiting for port 5000 to be released..."
sleep 3

echo "Starting new container..."
sudo docker run -d \
  --name devops-container \
  -p 127.0.0.1:5000:5000 \
  devops-app:latest

echo "Checking application..."

sleep 5

curl -f http://127.0.0.1:5000/health

echo "Deployment successful!"
