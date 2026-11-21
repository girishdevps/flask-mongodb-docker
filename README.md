# Flask + MongoDB Docker Project

A containerized Flask application integrated with MongoDB using Docker.

## Architecture

Flask Application → MongoDB

Both services run inside Docker containers and communicate through a Docker network.

## Tech Stack

- Python (Flask)
- MongoDB
- Docker
- Docker Networking
- Docker Volumes
- Git & GitHub

## Features

- Flask application connected to MongoDB
- REST API to add and retrieve users
- Dockerized Flask application
- MongoDB running inside a container
- Persistent MongoDB storage using Docker volumes
- Container-to-container communication using Docker networking

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application status |
| GET | `/users` | Retrieve users |
| POST | `/users` | Add a user |

## Docker Components

- Flask container: Application service
- MongoDB container: Database service
- Docker network: Container communication
- Docker volume: Persistent database storage

## Learning Objectives

- Containerize a Python application
- Connect an application to a database inside Docker
- Understand Docker networking
- Understand Docker volumes
- Practice Git and GitHub version control

## Author

Girish

GitHub: https://github.com/girishdevps
