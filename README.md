# 📚 Online Learning Platform

A full-stack **Online Learning Platform** developed using **Django** that allows users to explore courses, enroll in courses, access lessons, watch learning videos, and take quizzes. The platform also provides an admin interface for managing courses, lessons, quizzes, and users.

## 🚀 Live Demo

🔗 **Live Website:** https://online-learning-platform-whg0.onrender.com/

## 💻 GitHub Repository

🔗 **Source Code:** https://github.com/Nsk-Narasimha/Online_Learning_platform

---

## ✨ Features

### 👤 User Features

* User registration and login
* Secure user authentication
* Browse available courses
* View course details
* Enroll in courses
* Access course lessons
* Watch uploaded course videos
* Access external learning resources
* Attempt quizzes
* Track learning progress
* User-friendly interface

### 🛠️ Admin Features

* Django Admin Dashboard
* Manage users
* Create and update courses
* Add and manage lessons
* Upload course thumbnails
* Upload lesson videos
* Create quizzes and questions
* Manage course content
* Monitor learning data

---

## 🏗️ Project Structure

```text
Online_Learning_platform/
│
├── courses/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── onlinelearning/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── media/
│   ├── thumbnails/
│   └── videos/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Django

### Database

* SQLite

### Deployment

* Render

### Development Tools

* Git
* GitHub
* Visual Studio Code

---

## 🗄️ Database Models

The application uses Django models to manage the learning platform data.

### Course

Stores information about available courses.

* Title
* Description
* Thumbnail
* Created By
* Learning Link

### Lesson

Stores individual lessons belonging to a course.

* Course
* Title
* Description
* Video
* External Link

### Quiz

Stores quizzes associated with courses or lessons.

### Question

Stores quiz questions and answer options.

### Progress

Tracks the learning progress of users.

---

## ⚙️ Installation and Setup

### 1. Clone the reposi
