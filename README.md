# Kubernetes-Multi-Service-App
Local Kubernetes Multi-Service Application with Ingress for API Gateway and database integration.
This repository houses a Dockerized multi-service web application featuring both a backend and a frontend component. The backend, built with Flask, interacts with a local MySQL database to fetch data, while the frontend serves as the user interface, making requests to the backend and displaying retrieved data.

## Docker images
-  Front-End: front-end-service
-  Back-End: back-end-service

## Docker Hub Image Link
You can find the Docker images on Docker Hub at the following link:
- https://hub.docker.com/r/nestallum/back-end
- https://hub.docker.com/r/nestallum/front-end

## Application Flow

1. **Frontend Interaction:** Users interact with the frontend interface, which sends requests to the backend to fetch data.
2. **Backend Processing:** The backend service processes incoming requests, querying the MySQL database to retrieve the requested data.
3. **Data Retrieval:** Upon receiving data from the database, the backend service sends it back to the frontend in response to the original request.
4. **Data Presentation:** The frontend receives the data from the backend and renders it within the user interface for users to view and interact with.

## Service Communication

- **Frontend to Backend:** Communication between the frontend and backend occurs via HTTP requests, with the frontend initiating requests for data retrieval.
- **Backend to Database:** The backend service connects to the MySQL database using database drivers (e.g., mysql.connector) to execute queries and retrieve data.

## Usage

1. Clone this repository to your local environment.
2. Ensure you have Docker installed on your system.
3. Use the provided Dockerfile to build the Docker image for the application.
4. Start the Docker container to run the multi-service web application.
5. Access the application through your web browser to interact with the frontend and view data retrieved from the backend.

## Repository Structure

- `backend/`: Contains the code for the backend service, including Flask application files and database connection setup.
- `frontend/`: Contains the code for the frontend service, including HTML, CSS, and JavaScript files for the user interface.
- `database/`: Includes database schema files and scripts for initializing and managing the MySQL database.

## Docker App run command
To run this Python application in a browser, you can use the following command:

**Running the application via Ingress :**


        minikube addons enable ingress-dns
        minikube tunnel

Click [here](https://github.com/Nestallum/Kubernetes-Multi-Service-App/blob/main/Screenshots/ingress.png) to view the execution of the application using Ingress.

## Authors
- LATTAB Nassim
- AZZAOUI Mohamed

