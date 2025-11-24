**AI Document Generator (DOCX + PPTX) – FastAPI + Gemini + HTML/JS Frontend**

**Project Structure**
<img width="338" height="831" alt="image" src="https://github.com/user-attachments/assets/2141425c-dbd2-4de6-bbaf-4c2b8b7e7447" />

**Web Screenshots** 
<img width="1431" height="652" alt="image" src="https://github.com/user-attachments/assets/bb45ef4d-e773-4d2c-ac33-4041f51fd284" />
<img width="898" height="549" alt="image" src="https://github.com/user-attachments/assets/7dd30764-8ebe-48bf-b62b-fdc8f8aff7ab" />


**A full-stack web application that allows users to:**
  -> Register & Login
  -> Generate AI-powered content using Google Gemini
  -> Export content as DOCX or PPTX
  ->Download generated files
  -> Secure endpoints using JWT authentication

**Features**
   Authentication (Register/Login using JWT),
   Google Gemini text generation,
   DOCX export using python-docx,
   PPTX export using python-pptx,
   Fully working frontend (HTML + CSS + JS),
   Secured backend with FastAPI,
   MySQL database support,
   Environment variables support (.env)

**Backend Setup Instructions (FastAPI)**
1️. Create and activate virtual environment
   python -m venv venv
   Windows:
    venv\Scripts\activate
   Mac/Linux:
    source venv/bin/activate

2. Install dependencies
  pip install -r requirements.txt

3. Database Setup (MySQL)
   Create the database
   Log into MySQL:
   mysql -u root -p
   
   Run:
   CREATE DATABASE ai_doc_generator;

**Create Environment Variables (.env)**
 This file must NOT be committed to GitHub.
   Create backend/.env:
   
   DB_USER=root
   DB_PASSWORD=yourpassword
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=ai_doc_generator
   JWT_SECRET=your_jwt_secret_key
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=60
   GOOGLE_API_KEY=your_google_ai_studio_api_key
   GEMINI_MODEL=models/gemini-2.5-flash
   
   Run the Backend
   Inside backend/:
     uvicorn app.main:app --reload
   
   Backend runs at:
    http://127.0.0.1:8000
   
   Swagger Docs:
    http://127.0.0.1:8000/docs

**Frontend Setup (HTML + JS)**
  No installation needed.
  Run using VS Code Live Server or open directly:
  
  frontend/index.html
  frontend/login.html
  frontend/register.html
  
  If using Live Server:
    http://127.0.0.1:5500/frontend/login.html

**Usage Guide**
  1️. Register
    Go to register.html
    Create username & password
    Automatically saved in MySQL
  
  2️. Login
    Returns JWT token
    Stored in localStorage
  
  3️. Generate Document
    Enter a prompt
    Choose DOCX or PPTX
    AI generates content → exported → file downloaded

**Example Prompts**
  “Explain AI in education in slide format”
  “Generate a formal, well-structured PPT outline on the topic Artificial Intelligence in Healthcare. Create 6–8 slides, each with a clear title and 3–5 concise bullet points. Focus on definition, applications, benefits, challenges, and future scope.”

**Contributions**
  Pull requests are welcome!

**Contact**
  For questions or support, feel free to ask on GitHub or directly.
