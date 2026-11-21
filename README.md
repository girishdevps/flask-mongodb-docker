# 🏎️ DevOps Racer — Flask & MongoDB

A browser-based car racing game built using **Flask, JavaScript, HTML, CSS, MongoDB, and Docker**. Players control a car, avoid traffic, track their score, and save scores to MongoDB through Flask REST APIs.

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

## 🏗️ Architecture

```text
Player Browser
     |
     v
HTML + CSS + JavaScript
     |
     v
Flask Application (Docker)
     |
     v
MongoDB Container
     |
     v
devops_project Database
     |
     v
scores Collection
```

## 📂 Project Structure

```text
car-game/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Game interface |
| `/score` | POST | Save player score to MongoDB |
| `/leaderboard` | GET | Retrieve top 10 scores |

### Save Score

`POST /score`

Example JSON:

```json
{
  "player": "Girish",
  "score": 350
}
```

### Leaderboard

`GET /leaderboard`

Returns the top 10 scores sorted in descending order.

## 🐳 Docker Deployment

### 1. Build the image

```bash
docker build -t car-game:v3 .
```

### 2. Run the container

Ensure MongoDB container `mongofb` is running on the same Docker network.

```bash
docker run -d \
  --name car-game \
  --network dev-net \
  -p 5000:5000 \
  car-game:v3
```

### 3. Verify the container

```bash
docker ps
```

### 4. View container logs

```bash
docker logs car-game
```

## 🌐 Access the Application

```text
http://EC2-PUBLIC-IP:5000
```

## 🗄️ MongoDB Configuration

The application connects to MongoDB using the following connection string:

```python
mongodb://mongofb:27017/
```

Database:

```text
devops_project
```

Collection:

```text
scores
```

## 🧪 Testing

- Start the game in a browser.
- Enter a player name.
- Play until collision.
- Verify that the score is submitted.
- Open `/leaderboard` to verify saved scores.
- Check container logs using `docker logs car-game`.

## 📌 Future Improvements

- Docker Compose for multi-container deployment.
- CI/CD automation using GitHub Actions.
- AWS deployment.
- Improved game graphics and animations.
- Difficulty levels and increasing speed.
- Persistent MongoDB storage using Docker volumes.
- Leaderboard UI improvements.
- Monitoring and logging.

---

**Built as a hands-on containerized application project to practice Flask, MongoDB, Docker, API integration, and deployment workflows.**

