#!/bin/bash
TIME_IMAGE_VERSION=`cat ./docker/version.txt`
eval $(minikube docker-env)
docker build -t time-service:${TIME_IMAGE_VERSION} -f docker/Dockerfile .