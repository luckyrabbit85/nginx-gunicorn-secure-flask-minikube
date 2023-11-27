@echo off
REM Start Minikube
minikube start

REM Expose the external IP directly to any program running on the host operating system
start cmd /k "minikube tunnel"

REM Create ConfigMap for Nginx and Slack configuration
kubectl create configmap nginx-configuration-map --from-file ssl-proxy-configuration=k8s/ssl-proxy.conf
kubectl create configmap slack-configuration-map --from-file slack-webhook-configuration=.env

REM Create TLS Secret for Nginx using provided certificates
kubectl create secret tls tls-certs-secret --cert=nginx-server.crt --key=nginx-server.key

REM Deploy Kubernetes Manifests for Iris app, services, and Nginx
kubectl apply -f k8s/iris-app.yaml -f k8s/iris-service.yaml -f k8s/nginx.yaml -f k8s/nginx-service.yaml

REM Wait for resources to become available
echo Waiting for Iris deployment...
kubectl wait --for=condition=Available --timeout=90s deployment.apps/iris-app

echo Waiting for Nginx deployment...
kubectl wait --for=condition=Available --timeout=90s deployment.apps/nginx

REM Display services available in the cluster
echo Services in the cluster:
kubectl get services
