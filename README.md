# 🛡️ API Rate Limiter

A backend Django application that implements a simple IP-based API rate limiting mechanism using a fixed time window strategy. This protects APIs from abuse or spam by throttling excessive requests from the same IP.

---

## 🚀 Features

- Tracks API requests per IP address
- Allows configurable request limits and time windows
- Blocks requests exceeding the limit
- Sends meaningful error responses to the client
- Logs and stores request data in a SQLite database
- Unit tested using `pytest`
- Easily testable with Postman

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Django, Django REST Framework (DRF)
- **Database:** SQLite
- **Testing:** Pytest
- **Client Testing Tool:** Postman
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

rate_limiter_project/
│
├── limiter/ # Django app
│ ├── models.py # IPRequestLog model for tracking
│ ├── views.py # Main API view with rate limiter logic
│ ├── tests.py # Unit tests
│ ├── urls.py # API route
│ └── ...
├── rate_limiter_project/
│ └── settings.py
├── db.sqlite3 # SQLite database
├── manage.py
└── README.md




---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Set Up Virtual Environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Migrations
python manage.py migrate

5. Run Development Server
python manage.py runserver
The API will be available at: http://127.0.0.1:8000/api/

🧪 Running Tests

Make sure pytest is installed:

pip install pytest
Then run tests:

pytest
🧪 API Endpoint Example

POST /api/limit/
Use Postman or curl to make repeated requests. After 5 requests (default limit), further requests from the same IP will be blocked temporarily.

📌 How It Works

The user sends a request to the /api/limit/ endpoint.
The app checks how many requests this IP has made in the last N seconds.
If it's within the allowed limit, it logs the request and sends a success response.
If the limit is exceeded, it returns 429 Too Many Requests.
🧠 Concepts Used

Custom DRF views
Request throttling logic (manual)
IP extraction from headers
Query filtering with timestamps
Unit testing API views
SQLite ORM models
Serializers to control output
📄 Requirements

If you're creating requirements.txt, here’s a minimal version:

Django>=4.0
djangorestframework
pytest
👩‍💻 Author

Sri Kaaviya
GitHub: @srikaaviya

📜 License

This project is licensed under the MIT License.

