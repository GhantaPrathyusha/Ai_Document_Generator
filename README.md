AI Document Generator (DOCX + PPTX) – FastAPI + Gemini + HTML/JS Frontend

A full-stack web application that allows users to:
✅ Register & Login
✅ Generate AI-powered content using Google Gemini
✅ Export content as DOCX or PPTX
✅ Download generated files
✅ Secure endpoints using JWT authentication

🚀 Features
Authentication (Register/Login using JWT)
Google Gemini text generation
DOCX export using python-docx
PPTX export using python-pptx
Fully working frontend (HTML + CSS + JS)
Secured backend with FastAPI
MySQL database support
Environment variables support (.env)

📌 Project Structure
AI_DOC_GENERATOR/
│
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   ├── content/
│   │   ├── documents/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── deps.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── style.css
│   ├── script.js
│
└── README.md
└── .gitignore

🔧 Backend Setup Instructions (FastAPI)
1️⃣ Create a virtual environment
python -m venv venv

2️⃣ Activate environment
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

🔐 Environment Variables (.env)
⚠️ This file must NOT be committed to GitHub.
(Already handled in .gitignore)

Create backend/.env:

DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=ai_doc_generator

JWT_SECRET=your_jwt_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

GOOGLE_API_KEY=your_google_ai_studio_api_key
GEMINI_MODEL=models/gemini-2.5-flash

▶️ Run the Backend

Inside backend/:
uvicorn app.main:app --reload

Backend runs at:
http://127.0.0.1:8000

Swagger Docs:
http://127.0.0.1:8000/docs

🌐 Frontend Setup (HTML + JS)
No installation needed.
Run using VS Code Live Server or open directly:

frontend/index.html
frontend/login.html
frontend/register.html

If using Live Server:
http://127.0.0.1:5500/frontend/login.html

🧪 Usage Guide
1️⃣ Register
Go to register.html
Create username & password
Automatically saved in MySQL

2️⃣ Login
Returns JWT token
Stored in localStorage

3️⃣ Generate Document
Enter a prompt
Choose DOCX or PPTX
AI generates content → exported → file downloaded

📝 API Endpoints
Authentication:
POST /auth/register
POST /auth/login

Generate Document:
POST /documents/generate
Authorization: Bearer <token>

📦 Example Prompts
“Explain AI in education in slide format”
“Write a research-style summary about Machine Learning”
“Give bullet points for a business pitch deck”

🚀 Deployment Options

⭐ Deploy Backend
Render.com
Railway.app
AWS EC2

⭐ Deploy Frontend
GitHub Pages
Netlify
Vercel

❤️ Contributions
Pull requests are welcome!

📧 Contact
For questions or support, feel free to ask on GitHub or directly.