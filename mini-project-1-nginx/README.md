# nginx-docker-webserver

This is a simple project that runs an NGINX web server inside a Docker container. It serves a custom `index.html` file.  
Perfect for learning how to create images and use Dockerfiles.

## Run it
```bash
docker build -t my-nginx-webserver .
docker run -d -p 8080:80 --name web1 my-nginx-webserver
