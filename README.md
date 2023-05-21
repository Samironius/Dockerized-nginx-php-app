# Dockerized NGINX + PHP Application

This repository contains a Dockerized NGINX + PHP application that provides a convenient way to deploy and run your web applications using Docker containers.

## Prerequisites

Before running this application, ensure that you have the following dependencies installed on your machine:

- Docker
- Docker Compose

## Getting Started

To get started with this application, follow the steps below:

1. Clone this repository to your local machine:

   ```
   git clone <repository_url>
   ```

2. Navigate to the cloned repository:

   ```
   cd dockerized-nginx-php-app
   ```

3. Customize the NGINX and PHP configurations:

   - Edit the `nginx.conf` file in the `nginx` directory if needed. This file contains the NGINX server configuration.

   - Modify the `Dockerfile-php` and `Dockerfile-nginx` files if necessary. These files define the Docker images for PHP and NGINX respectively.

4. Place your PHP code in the `src` directory. This is where your PHP application files will be located.

5. Run the following command to start the Docker containers:

   ```
   docker-compose up -d
   ```

   This command will build the Docker images and start the NGINX and PHP containers in the background.

6. Access your application by opening a web browser and navigating to `http://localhost:8080`. You should see your PHP application being served by NGINX.

7. You can make changes to your PHP code in the `src` directory, and the changes will be automatically reflected in the running containers.

## Stopping and Cleanup

To stop the application and clean up the Docker containers and resources, run the following command:

```
docker-compose down --volumes
```

This command will stop the containers and remove any created volumes.

## Configuration

- The `docker-compose.yml` file defines the services and their configurations. You can modify the port mappings, container names, or other settings in this file.

- Additional environment variables, volume mounts, or network configurations can be added to the `docker-compose.yml` file as per your requirements.