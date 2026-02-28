.📍 BarrierFree Navigator
📌 Project Description

BarrierFree Navigator is a community-driven web platform designed to help people with disabilities identify and share information about accessible public spaces.

Users can add locations, rate accessibility features such as ramps, elevators, and accessible restrooms, and leave comments to help others make informed decisions. The platform aims to promote inclusivity and support smart city accessibility initiatives.

🎯 Problem Statement

People with disabilities often struggle to determine whether a public place is accessible before visiting. Lack of centralized accessibility data leads to inconvenience, exclusion, and safety concerns.

💡 Our Solution

We built a web application that:

Allows users to add accessible places

Enables rating of accessibility features

Supports user comments and feedback

Displays accessibility information in an organized interface

The system uses a Django backend with a responsive frontend built using HTML, CSS, and JavaScript.

🚀 Features

✅ Add accessible locations

✅ Rate accessibility (1–5 scale)

✅ Add user comments

✅ View all submitted places

✅ Backend API endpoints (JSON responses)

✅ Clean and responsive UI

✅ Organized modular code structure

🛠 Tech Stack
Frontend

HTML

CSS

JavaScript

Backend

Python

Django

Database

SQLite3 (Default Django database)

Deployment

Render (HTTPS enabled)

⚙️ Installation Commands
1️⃣ Clone the Repository
git clone https://github.com/yourusername/accessibility_project.git
cd accessibility_project
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations
python manage.py migrate
▶️ Run the Project
python manage.py runserver

Open browser:

http://127.0.0.1:8000/
🌐 Live Deployment

🔗 Live Website: (Add your Render link here)

Hosted using Render

HTTPS enabled

No load errors

📷 Screenshots

<img width="1781" height="1079" alt="Screenshot 2026-02-28 084930" src="https://github.com/user-attachments/assets/030d48eb-f173-4fc1-bdb7-e8c17c883867" />
<img width="1823" height="1079" alt="Screenshot 2026-02-28 084903" src="https://github.com/user-attachments/assets/52d17800-3e10-4e87-bd76-ffec5035a859" />
<img width="1700" height="979" alt="Screenshot 2026-02-28 084830" src="https://github.com/user-attachments/assets/a58aed1c-2f52-42cd-b94a-3fe6ab6d8046" />
<img width="1492" height="1066" alt="Screenshot 2026-02-28 071007" src="https://github.com/user-attachments/assets/42e810f7-7729-4e95-96de-618f1f990c00" />


🎥 Demo Video

🔗 https://drive.google.com/file/d/1v4SMy1__qzZ5qRhC6V6i6PSwLbYEs2SD/view?usp=drivesdk



🏗 Architecture Diagram

(Add diagram inside docs/architecture.png)

Architecture Flow

User
⬇
Frontend (HTML/CSS/JS)
⬇
Django Views
⬇
Models
⬇
SQLite Database
⬇
JSON Response
⬇
Frontend Display

![Architecture Diagram](docs/architecture.png)
🔌 API Documentation
1️⃣ Add Place

Endpoint: /add_place/
Method: POST

Request Body (JSON):

{
  "name": "City Mall",
  "rating": 5,
  "comment": "Fully accessible with ramp and lift"
}

Response:

{
  "message": "Place added successfully"
}
2️⃣ Get All Places

Endpoint: /places/
Method: GET

Response Example:

[
  {
    "name": "City Mall",
    "rating": 4,
    "comment": "Ramp available"
  }
]
📂 Project Structure
accessibility_project/
│
├── accessibility_project/   # Django project settings
├── places/                  # Django app
├── static/                  # Static files (CSS/JS)
├── templates/               # HTML templates
├── docs/                    # Screenshots & diagrams
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
📁 Required Root Files

README.md

LICENSE

.gitignore

requirements.txt

👩‍💻 Team Members

Arshiya K N
P Devananda

🤖 AI Tools Used

This project used AI tools for:

README documentation generation

Code debugging assistance

Improving code structure

Generating documentation templates

AI prompts were used inside VS Code to generate structured documentation.

📜 License

This project is licensed under the MIT License.

See the LICENSE file for more details.


You’re honestly handling hackathon pressure like a champ. Let’s finish this strong 💪🔥
