
# 🚀 Sarv Suvidha - Backend Assignment

This project is developed as part of the backend API development assignment. It includes the implementation of two APIs using Django REST Framework and PostgreSQL.

---

## 📌 Project Overview

**Implemented APIs:**

1. **POST** `/api/forms/bogie-checksheet`
   → Submits a Bogie Checksheet form.

2. **GET** `/api/forms/wheel-specifications`
   → Retrieves filtered Wheel Specifications.

3. **POST** `/api/forms/wheel-specifications`
   → Submits a Wheel Specification form.

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Language:** Python 3.11+
* **Others:** Postman, SwaggerHub (Reference)

---

## ⚙️ Environment Configuration

Create a `.env` file in your project root and add:

```env
DB_NAME=sarv_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
```

---

## 🚀 Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/hs024/sarv_suvidha.git
cd sarv_suvidha
```

### 📦 2. Create and Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

### 📥 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🧠 4. Configure PostgreSQL

Create a PostgreSQL database and user as per `.env` values:

```sql
CREATE DATABASE sarv_db;
CREATE USER postgres WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE sarv_db TO postgres;
```

### 🔁 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 🚦 6. Run Development Server

```bash
python manage.py runserver
```

---

## 🔬 API Endpoints

### 1. Bogie Checksheet Form (POST)

* **URL:** `/api/forms/bogie-checksheet`
* **Method:** `POST`
* **Sample Request Body:**

```json
{
  "formNumber": "BCF001",
  "inspectionBy": "Inspector A",
  "inspectionDate": "2025-07-20",
  "status": "submitted"
}
```

---

### 2. Wheel Specifications Form (POST)

* **URL:** `/api/forms/wheel-specifications`
* **Method:** `POST`
* **Sample Request Body:**

```json
{
  "formNumber": "WS001",
  "submittedBy": "Technician X",
  "submittedDate": "2025-07-20",
  "status": "submitted"
}
```

---

### 3. Get Wheel Specifications (GET)

* **URL:** `/api/forms/wheel-specifications`
* **Method:** `GET`
* **Query Params (Optional):**

  * `formNumber`
  * `submittedBy`
  * `submittedDate`

**Example:**
`/api/forms/wheel-specifications?formNumber=WS001`

---

## ✅ Testing

Use **Postman** to test all endpoints. You can also import the provided `KPA_form data.postman_collection.json`.

---



## 💡 Notes

* PostgreSQL must be running locally on port `5432`.
* Make sure to include correct headers like `Content-Type: application/json` when testing POST requests.
* You can check inserted data via `psql` or any DB GUI tool like **pgAdmin**.

