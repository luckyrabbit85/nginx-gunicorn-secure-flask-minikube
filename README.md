# Project ML-Deploy-Docker-Nginx-Gunicorn-Flask
## Overview

This project exemplifies the setup of a web application stack using Docker, Nginx, Gunicorn, and Flask, tailored for deploying a machine learning application. It offers a blueprint for deploying a Flask-based machine learning application served by a Gunicorn server. Additionally, it integrates an Nginx reverse proxy for efficient management of HTTP and HTTPS requests.
    
    
![Architecture](https://lh6.googleusercontent.com/UQJjOnPSiafDTICrSyDzAA7civKZvIyVAwxJIFDAMaTqegYHGXzlaaFIVmUtS36vSQ5qqcMJrIWWUVydAgx0C6LfZKWEO0Lfn0T-c0Nb3S63BRhQ9T3r_Ti7N_5exNJ5pDN2CPIH4OHZ6W5AQaNyRn4)
    
    
## Project Components

The project includes the following fundamental components:

1. `Flask App`: An application built on Flask that specializes in predicting Iris flower classifications, serving as an example scenario for machine learning-based prediction. This web application is proficient in handling HTTP requests for this specific classification task.
2. `Nginx`:Serving as a web server, Nginx functions as a reverse proxy, directing requests to the Flask application, while also taking charge of HTTPS connections through SSL/TLS certificates.
3. `Gunicorn`: Utilized as a WSGI HTTP server, Gunicorn is responsible for running the Flask application.
4. `Docker Compose`: Docker Compose is employed to efficiently govern and orchestrate the Docker containers in the setup.


## Project Directory Layout
The project maintains the following directory structure:

```bash
|-- docker-compose.yml
|-- flask_app
|   |-- models
|   |   |-- SVM_20231027134419.pkl
|   |-- utilities
|   |   |-- app_logger.py
|   |   |-- error_handler.py
|   |   |-- iris_model.py
|   |-- Dockerfile
|   |-- main.py
|   |-- requirements.txt
|   |-- wsgi.py
|-- nginx
|   |-- Dockerfile
|   |-- nginx.conf
|   |-- project.conf
|-- run_docker.sh
|-- nginx-server.crt
|-- nginx-server.key
```
## Configuration and Deployment
1. Generating SSL Certificates (Optional)
If you desire HTTPS support, you have the option to generate self-signed SSL/TLS certificates using the following command:

```bash
openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes
```
2. Building Docker Containers 
To construct and launch Docker containers `docker-compose up --build -d` command from the project directory

```bash
docker-compose up --build -d
```
3.  Accessing the Application

Once the deployment is successful, the Flask application will be available at `http://localhost:8000`. Nginx will forward the HTTP requests to the Flask application.

For HTTPS access, you'll need to set up a DNS pointing to the server or add a record in your system file to map the domain used in the file to ./etc/hosts/nginx/project.conf for localhost.

4. Using Postman:

Open Postman and create a POST request to https://localhost/predict or https://yourdomain.com/predict, depending on your setup.
Ensure the request body is correctly formatted according to what your /predict endpoint expects (JSON, form data, etc.).
Send the request and examine the response.

4. Ending the Project
You can halt the Docker containers by using `docker-compose down` command.

```bash
docker-compose down
```

## Personalization

To personalize this project, follow these guidelines:

- `Flask Application`: Revise the code in the `flask_app` directory to develop your customized Flask application.
- `Nginx Configuration`: Customize the Nginx settings found in the `nginx/project.conf` file as necessary.
- `SSL/TLS Certificates`: Replace the current `nginx-server.crt` and `nginx-server.key` files with suitable certificates from a trusted certificate authority if you prefer to utilize SSL/TLS certificates.

## Conclusion
The project serves as a basic demonstration for constructing a secure web application stack with Docker, Nginx, Gunicorn, and Flask. It can be tailored to suit your specific requirements and serves as a foundational template for creating advanced and secure web applications. It's crucial to adhere to security best practices when deploying applications into a production environment.