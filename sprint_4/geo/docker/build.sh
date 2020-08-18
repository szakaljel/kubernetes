#!/bin/bash
GEO_IMAGE_VERSION=`cat ./docker/version.txt`
eval $(minikube docker-env)
docker build -t geo-service:${GEO_IMAGE_VERSION} -f docker/Dockerfile .