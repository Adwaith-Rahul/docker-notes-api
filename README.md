# 🚀 Dockerized Flask Notes API

A simple REST API built with Flask and containerized using Docker.
Deployed on AWS EC2.

---

## 📌 Project Goal

Learn containerization fundamentals:

- Build a REST API
- Write a Dockerfile
- Build Docker image
- Run container
- Use persistent storage
- Deploy on AWS EC2

---

## 🛠 Tech Stack

- Python 3
- Flask
- Docker
- AWS EC2
- Ubuntu Linux

---

## 📂 Project Structure
project-a/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md

---

## ⚙️ API Endpoints

### GET /

Returns API status.

### GET /notes

Returns all saved notes.

### POST /notes

Add a note.

Example:
curl -X POST http://<server-ip>:5000/notes
-H "Content-Type: application/json"
-d '{"title":"Learn Docker"}'

---

## 🐳 Docker Instructions

### Build Image
docker build -t notes-api .


### Run Container



docker run -d -p 5000:5000 notes-api


---

## 💾 Persistent Storage

Using Docker Volume:



docker volume create notes-volume

docker run -d -p 5000:5000
-v notes-volume:/data
notes-api


---

## ☁️ Deployment

Deployed on AWS EC2 (Ubuntu 22.04).

Security group allows:
- SSH (22)
- HTTP (80)
- Custom TCP (5000)

---

## 🎯 Skills Learned

- Docker image building
- Container lifecycle management
- Port mapping
- Persistent storage (volumes)
- Linux server setup
- AWS EC2 deployment

---

## 👨‍💻 Author

Adwaith Rahul


Save:

CTRL + X → Y → Enter

🚀 STEP 2 — Commit README
git add README.md
git commit -m "Added professional README"
git push

