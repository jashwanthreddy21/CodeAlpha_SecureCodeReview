# 🛡️ Secure Code Review - SSRF Protection Demo

## 🧠 Project Objective
This is a **Flask web application** developed as part of CodeAlpha's Internship Task 3. It demonstrates **how to protect a web service against Server-Side Request Forgery (SSRF)** using secure Python code.

---

## 🚀 How it works

### Endpoint:

GET /ping?host=
### ✅ Features:

- Accepts safe, validated URLs
- Returns HTTP status code of requested resource
- Prevents open SSRF abuse by validating the target host

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repo:

git clone https://github.com/yourusername/CodeAlpha_SecureCodeReview.git

cd CodeAlpha_SecureCodeReview



2️⃣ Set up virtual environment

python3 -m venv venv

source venv/bin/activate



3️⃣ Install dependencies

pip install -r requirements.txt



4️⃣ Run the app

python app.py



🧪 Example Test


curl "http://127.0.0.1:5000/ping?host=https://google.com"



Expected response:


{
  "host": "https://google.com",
  "response_code": 200,
  "status": "success"
}
