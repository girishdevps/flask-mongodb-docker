# 🏎️ DevOps Racer — Flask & MongoDB

A browser-based car racing game built using **Flask, JavaScript, HTML, CSS, MongoDB, and Docker Compose**. Players control a car, avoid traffic, track their score, and save scores to MongoDB through Flask REST APIs.

## 🚀 Features

- Interactive 2D car racing game.
- Keyboard controls (Left & Right arrow keys).
- Random enemy cars.
- Collision detection and Game Over.
- Score tracking.
- Player name input.
- Score persistence using MongoDB.
- REST APIs for score submission and leaderboard.
- Dockerized Flask application.
- Multi-container deployment using Docker Compose.
- Persistent MongoDB storage using Docker volumes.
- Container communication through a custom Docker network.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web application and REST API |
| MongoDB | Database for storing player scores |
| PyMongo | Python-MongoDB connectivity |
| HTML | Game structure |
| CSS | Styling |
| JavaScript | Game logic |
| Canvas API | Game rendering |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |

## 🏗️ Architecture

```text
                    Player Browser
                         |
                         v
                 Flask Application
                   Port 5000
                  (car_racer)
                         |
                         v
              Docker Network: flask-net
                         |
                         v
                    MongoDB
                   (mongofb)
                  Port 27017
                         |
                         v
                   car_vol
                (Docker Volume)
                         |
                         v
                  devops_project
                      Database
                         |
                         v
                     scores
                   Collection
```

## 📂 Project Structure

```text
car-game/
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Loads the game interface |
| `/score` | POST | Saves player score to MongoDB |
| `/leaderboard` | GET | Retrieves top 10 scores |

### Save Score

**Endpoint:** `POST /score`

Example JSON request:

```json
{
  "player": "Girish",
  "score": 350
}
```

Successful response:

```json
{
  "message": "Score saved"
}
```

### Leaderboard

**Endpoint:** `GET /leaderboard`

Returns the top 10 scores sorted in descending order.

## 🐳 Docker Compose Deployment

### 1. Clone the repository

```bash
git clone git@github.com:girishdevps/REPOSITORY-NAME.git
cd REPOSITORY-NAME
```

### 2. Build and start the containers

```bash
docker compose up -d --build
```

This command builds the Flask application image and starts both Flask and MongoDB containers.

### 3. Verify running containers

```bash
docker compose ps
```

### 4. View container logs

Flask logs:

```bash
docker compose logs -f flaskapp
```

MongoDB logs:

```bash
docker compose logs -f mongodb
```

### 5. Stop the application

```bash
docker compose down
```

Containers are stopped and removed, but MongoDB data remains stored in the named volume.

### 6. Rebuild the application

```bash
docker compose up -d --build
```

## 🌐 Access the Application

Open the application in your browser:

```text
http://localhost:5000
```

If deployed on an AWS EC2 instance:

```text
http://EC2-PUBLIC-IP:5000
```

Ensure the appropriate inbound rule is configured in the EC2 security group.

## 🗄️ MongoDB Configuration

MongoDB runs inside its own container and communicates with the Flask container through the custom Docker network `flask-net`.

**Connection URI:**

```text
mongodb://mongofb:27017/devops_project
```

| Configuration | Value |
|---|---|
| Container Name | `mongofb` |
| MongoDB Port | `27017` |
| Database | `devops_project` |
| Collection | `scores` |
| Docker Volume | `car_vol` |
| Mount Path | `/data/db` |
| Docker Network | `flask-net` |

### Verify stored scores

Enter the MongoDB container:

```bash
docker exec -it mongofb mongosh
```

Then execute:

```javascript
use devops_project
db.scores.find().pretty()
```

Count stored scores:

```javascript
db.scores.countDocuments()
```

## 🧪 Testing

- Start the application using Docker Compose.
- Open the game in a browser.
- Enter a player name.
- Play until collision.
- Verify that the score is submitted.
- Open `/leaderboard` to verify saved scores.
- Inspect MongoDB documents using `mongosh`.
- Check container logs using Docker Compose.

## 📌 Future Improvements

- CI/CD automation using GitHub Actions.
- AWS deployment.
- Improved game graphics and animations.
- Difficulty levels and increasing speed.
- Monitoring and logging.
- Leaderboard UI improvements.
- Container health checks.

---

**Built as a hands-on containerized application project to practice Flask, MongoDB, Docker, Docker Compose, container networking, persistent storage, API integration, and deployment workflows.**

