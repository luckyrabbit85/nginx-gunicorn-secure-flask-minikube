# Crafting a Secure Flask App: Deploying with Nginx and Gunicorn on Minikube for Maximum Protection
## Overview

This project details a comprehensive strategy for building a resilient web application setup utilizing Kubernetes, Docker, Nginx, Gunicorn, and Flask, specially designed for deploying machine learning applications. It provides a structured guideline for deploying a Gunicorn-served Flask-based machine learning application, including an Nginx reverse proxy for efficient HTTP and HTTPS request management. With a primary focus on deploying and rigorously testing a secure Flask web application within a Minikube cluster, the project underscores the importance of adhering to security best practices. This encompasses not only utilizing non-root user configurations in Dockerfiles, optimizing image sizes, and implementing essential SSL/TLS encryption but also includes measures to prevent the leakage of sensitive information, ensuring a robust and secure deployment environment.
    
    
![Architecture](https://lh6.googleusercontent.com/UQJjOnPSiafDTICrSyDzAA7civKZvIyVAwxJIFDAMaTqegYHGXzlaaFIVmUtS36vSQ5qqcMJrIWWUVydAgx0C6LfZKWEO0Lfn0T-c0Nb3S63BRhQ9T3r_Ti7N_5exNJ5pDN2CPIH4OHZ6W5AQaNyRn4)
    
    
## Project Components

The project includes the following fundamental components:

1. `Flask App`: An application built on Flask that specializes in predicting Iris flower classifications, serving as an example scenario for machine learning-based prediction. This web application is proficient in handling HTTP requests for this specific classification task.
2. `Gunicorn`: Utilized as a WSGI HTTP server, Gunicorn is responsible for running the Flask application.
3. `Nginx`: Serving as a web server, Nginx functions as a reverse proxy, directing requests to the Flask application, while also taking charge of HTTPS connections through SSL/TLS certificates.
4. `Docker`: Docker Compose is employed to efficiently govern and orchestrate the Docker containers in the setup.
5. `Minikube`: The Minikube setup ensures a micro-scale Kubernetes environment, ideal for local development and testing also ensuring compatibility and readiness for larger-scale deployments.

## Salient Features
1. Integrated custom error module and configured logging for immediate Slack notifications in case of errors.
2. Utilizing Nginx as a reverse proxy to bolster security by concealing backend server information.
3. Specification of SSL certificate and private key for secure communication, alongside HTTP to HTTPS redirection ensuring encrypted and secure traffic.
4. Minimizing image size by selectively copying essential files, avoiding unnecessary Python bytecode generation, and executing the application with non-root user permissions.
5. Implementing rate limiting and connection limiting zones to regulate client access rates, preventing misuse and ensuring equitable usage.
6. Employing config mapping and secret utilization for secure and efficient management of application configurations and sensitive data.

## Project Directory Layout
The project maintains the following directory structure:

```bash
|-- flask_app
|   |-- .env # SLACK_WEBHOOK_URL
|   |-- Dockerfile
|   |-- main.py
|   |-- requirements.txt
|   |-- wsgi.py
|   |-- __init__.py
|   |-- models
|   |   |-- SVM_20231027134419.pkl
|   |-- utilities
|   |   |-- app_logger.py
|   |   |-- error_handler.py
|   |   |-- iris_model.py
|   |   |-- __init__.py
|-- k8s
|   |-- iris-app.yaml
|   |-- iris-service.yaml
|   |-- nginx-config.conf
|   |-- nginx-service.yaml
|   |-- nginx.yaml
|-- ml_develop
|   |-- Iris Classification.ipynb
|   |-- SVM_20231027134419.pkl
|-- nginx
|   |-- Dockerfile
|   |-- nginx.conf
|   |-- project.conf
|
|-- .gitignore
|-- docker-compose.yaml
|-- LICENSE
|-- nginx-server.crt # CERTIFICATE
|-- nginx-server.key # PRIVATE KEY
|-- README.md
|-- run_on_docker.bat
|-- run_on_minikube.bat
```

## Rolling out deployments

1. Generating SSL Certificates (Optional)
If you desire HTTPS support, you have the option to generate self-signed SSL/TLS certificates using the following command:

```bash
openssl req -x509 -newkey rsa:4096 -keyout nginx-server.key -out nginx-server.crt -days 365 -nodes
```
2. Running Docker Containers 
To construct and launch Docker containers use `run_on_docker.bat` from the project directory.

```bash
run_on_docker.bat
```
3. Accessing the Application
Once the deployment is successful, Nginx will forward the HTTP requests to the Flask application at `https://localhost/`. 

4. Using Postman:
Open Postman and create a POST request to https://localhost/predict, depending on your setup. Ensure the request body is correctly formatted according to what your /predict endpoint expects (JSON, form data, etc.)
Send the request and examine the response.

```json
{
    "iris_dimensions": [3.4, 5.6, 4.5, 1.3]
}
```
5. Running on minikube
Make sure you have docker and minikube installed and running, then you can use `run_on_minkube` from the project directory.

```bash
run_on_minikube.bat
```


## Personalization

To personalize this project, follow these guidelines:

- `Flask Application`: Revise the code in the `flask_app` directory to develop your customized Flask application.
- `Nginx Configuration`: Customize the Nginx settings found in the `nginx/project.conf` file as necessary.
- `SSL/TLS Certificates`: Replace the current `nginx-server.crt` and `nginx-server.key` files with suitable certificates from a trusted certificate authority if you prefer to utilize SSL/TLS certificates.

## Conclusion
The project serves as a basic demonstration for constructing a secure web application stack with Minikube, Docker, Nginx, Gunicorn, and Flask. It can be tailored to suit your specific requirements and serves as a foundational template for creating advanced and secure web applications. It's crucial to adhere to security best practices when deploying applications into a production environment.