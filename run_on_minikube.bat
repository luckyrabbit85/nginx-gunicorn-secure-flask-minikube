@echo off
REM Start Minikube
minikube start

REM Create ConfigMap
kubectl create configmap nginx-config-map --from-file=nginx-config.conf

REM Create TLS Secret
kubectl create secret tls tls-certs-secret --cert=nginx-server.crt --key=nginx-server.key

REM Deploy Manifests
kubectl apply -f iris-app.yaml -f iris-service.yaml -f nginx.yaml -f nginx-service.yaml

REM Wait for the resources to become available
echo Waiting for Iris deployment...
kubectl wait --for=condition=Available --timeout=60s deployment.apps/iris

echo Waiting for Nginx deployment...
kubectl wait --for=condition=Available --timeout=60s deployment.apps/nginx

REM Check services
echo Services in the cluster:
kubectl get services
