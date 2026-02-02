🌐 Global News Sentiment Tracker
An automated end-to-end data pipeline designed to scrape real-time news articles, perform NLP-based sentiment analysis, and visualize public mood trends via a web dashboard.

🚀 Overview
This project demonstrates a complete data engineering lifecycle:

Extraction: Automated scraping of news sources using newspaper4k with custom User-Agents.

Processing: Text cleaning and Sentiment Analysis using NLTK (VADER).

Storage: Structured data persistence using SQLAlchemy and SQLite.

Visualization: Real-time interactive dashboard built with Streamlit, featuring automated refresh cycles.

🐳 Quick Start with Docker (Recommended)
The easiest way to run this project is using Docker. This ensures all dependencies (Python, NLTK lexicons, and system libraries) are pre-configured in an isolated environment.

Ensure you have Docker Desktop installed and running.

Clone the repository:

Bash
git clone https://github.com/yourusername/news-sentiment-tracker.git
cd news-sentiment-tracker
Run the application:

Bash
docker-compose up --build
Access the dashboard: Open your browser and navigate to: http://localhost:8501

🛠️ Tech Stack
Language: Python 3.11

Containerization: Docker & Docker Compose

Data Engineering: Pandas, SQLAlchemy (SQLite)

Web Scraping: Newspaper4k

NLP: NLTK (SentimentIntensityAnalyzer)

Frontend: Streamlit

📂 Project Structure
app.py: Entry point for the Streamlit dashboard and UI logic.

scraper.py: Modular scraping engine with robust connection error handling.

database.py: Database schema and SQLite session management.

utils.py: Natural Language Processing (Sentiment) logic.

Dockerfile & docker-compose.yml: Containerization and volume mapping configuration.

data/: Persistent storage directory for the SQLite database (mounted as a volume).

⚙️ Configuration
You can customize the application behavior via the .env file without touching the code:

APP_TITLE: Change the dashboard heading.

SCRAPE_INTERVAL: Set the frequency of automated scans (default: 60s).

DB_PATH: Define the internal database connection string.

🛡️ Key Features
Auto-Monitoring: Toggle the "Live" mode to refresh data every minute automatically.

Sentiment Metrics: Real-time calculation of "Current Mood" and historical trend lines.

Connection Resilience: Built-in detection for internet interruptions or site blocking with professional UI alerts.

Data Persistence: The database is mapped to your local machine, so your history is never lost even if the container is deleted.

Clean UI: Professional dashboard styling with hidden deployment menus for a standalone app feel.

🔧 Manual Installation (Alternative)
If you prefer to run it without Docker:

Install dependencies:

Bash
pip install -r requirements.txt
Download NLTK Lexicon:

Bash
python -m nltk.downloader vader_lexicon
Run the application:

Bash
streamlit run app.py
👨‍💻 Developed by Yasmine Nabli
