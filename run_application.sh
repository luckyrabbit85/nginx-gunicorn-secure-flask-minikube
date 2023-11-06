#!/bin/bash

# Start Minikube
minikube start

# Create ConfigMap
minikube kubectl -- create configmap nginx-config --from-file=nginx-config.conf