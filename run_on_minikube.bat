@echo off
REM Start Minikube
minikube start

REM Expose the external IP directly to any program running on the host operating system
start cmd /k "minikube tunnel"

REM Create ConfigMap for Nginx configuration
kubectl create configmap nginx-config-map --from-file=nginx-config.conf

REM Create TLS Secret for Nginx using provided certificates
kubectl create secret tls tls-certs-secret --cert=nginx-server.crt --key=nginx-server.key

REM Deploy Kubernetes Manifests for Iris app, services, and Nginx
kubectl apply -f iris-app.yaml -f iris-service.yaml -f nginx.yaml -f nginx-service.yaml

REM Wait for resources to become available
echo Waiting for Iris deployment...
kubectl wait --for=condition=Available --timeout=90s deployment.apps/iris

echo Waiting for Nginx deployment...
kubectl wait --for=condition=Available --timeout=90s deployment.apps/nginx

REM Display services available in the cluster
echo Services in the cluster:
kubectl get services
