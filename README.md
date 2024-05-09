# Kubernetes-Multi-Service-App
Local Kubernetes Multi-Service Application with Ingress for API Gateway and database integration.

## Docker images
-  Front-End: front-end-service
-  Back-End: back-end-service

## Docker Hub Image Link
You can find the Docker images on Docker Hub at the following link:
- https://hub.docker.com/r/nestallum/back-end
- https://hub.docker.com/r/nestallum/front-end

## Docker App run command
To run this Python application in a browser, you can use the following command:

- **Running the application via Ingress :**
    ```bash
    minikube addons enable ingress-dns
    minikube tunnel
    ```
    Click [here](https://github.com/Nestallum/docker-python-app/blob/main/screenshots/ingress.png) to view the execution of the application using Ingress.

