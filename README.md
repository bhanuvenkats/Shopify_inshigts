
# 🛍️ Shopify Store Insights-Fetcher

This project is a GenAI Developer Internship assignment designed to scrape public insights from Shopify-based stores without using the official Shopify API. It extracts business-critical information from the store’s frontend, persists the data in a MySQL database, and serves it via FastAPI endpoints.

---

## 🚀 Features

- 🔎 Scrapes public data from Shopify websites
- 📦 Extracts:
  - Product catalog
  - Hero/featured products
  - Store policies (refunds, shipping, etc.)
  - FAQs, About Us, and Contact details
  - Social media links
- 💾 Stores extracted data into a MySQL database
- ⚙️ API endpoints to trigger scraping and view data
- ✅ Follows clean architecture using FastAPI, SQLAlchemy

---

## 🛠️ Tech Stack

| Technology    | Purpose                        |
|---------------|--------------------------------|
| FastAPI       | Backend framework for REST API |
| BeautifulSoup | Web scraping                   |
| SQLAlchemy    | ORM to interact with MySQL     |
| Uvicorn       | ASGI server                    |
| MySQL         | Relational Database            |
| Pydantic      | Request data validation        |
| dotenv        | Environment variable handling  |

---

## 📁 Project Structure

shopify_insights/
├── app/
│ ├── main.py # FastAPI application entry point
│ ├── routers/
│ │ └── insights.py # API endpoint for scraping
│ ├── services/
│ │ └── scraper.py # Scraper logic using BeautifulSoup
│ ├── models/
│ │ └── brand_insights.py # SQLAlchemy data model
│ └── db/
│ ├── database.py # DB connection and session setup
│ └── init_db.py # Creates tables
├── .env # DB credentials and environment config
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/shopify_insights.git
cd shopify_insights
2. Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
# Activate (Windows)
.\venv\Scripts\activate
# OR (Mac/Linux)
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Setup .env File
Create a .env file in the root folder:

ini
Copy
Edit
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=shopify_db
5. Initialize the MySQL Database
Ensure MySQL is running, then:

bash
Copy
Edit
$env:PYTHONPATH = "."       # (Windows PowerShell only)
python app/db/init_db.py
This will create the brand_insights table.

▶️ Run the FastAPI App
bash
Copy
Edit
uvicorn app.main:app --reload
Visit Swagger Docs:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
📬 API Usage
POST /extract-insights
Trigger scraping and store results in the database.

Request body:

json
Copy
Edit
{
  "website_url": "https://examplestore.myshopify.com"
}
Response:

json
Copy
Edit
{
  "message": "Data scraped and saved successfully",
  "data": {
    "product_catalog": [...],
    "hero_products": [...],
    "about": "...",
    "policies": [...],
    ...
  }
}
💡 Example Insights Captured
Hero Products: Top-featured items on homepage

Product Catalog: List of all product names and prices

Policies: Return, refund, shipping pages

FAQs: Collapsible question-answer sections

Social Links: Facebook, Instagram, etc.

About & Contact: Text and email/phone info

📌 Improvements (Future Scope)
Add frontend UI (React/Vite)

Add user authentication

Enable background job queue (Celery + Redis)

Dockerize the app

Add Shopify store validity check

Add unit tests with pytest

✍️ Author
Bhanu Venkat Srikakulapu
Data Analyst | GenAI Developer Intern
