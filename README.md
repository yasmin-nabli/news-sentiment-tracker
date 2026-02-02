# 🌐 Global News Sentiment Tracker

An automated end-to-end data pipeline designed to scrape real-time news articles, perform NLP-based sentiment analysis, and visualize public mood trends via a professional web dashboard.

## 🚀 Overview
This project demonstrates a complete data engineering lifecycle:
1. **Extraction:** Automated scraping of news sources using `newspaper4k` with custom User-Agents to bypass basic bot detection.
2. **Processing:** Text cleaning and Sentiment Analysis using `NLTK (VADER)`.
3. **Storage:** Structured data persistence using `SQLAlchemy` and `SQLite`.
4. **Visualization:** Real-time interactive dashboard built with `Streamlit`, featuring automated refresh cycles.



---

## 🐳 Quick Start with Docker (Recommended)
The easiest way to run this project is using Docker. This ensures all dependencies (Python, NLTK lexicons, and system libraries) are pre-configured in an isolated environment.

1. **Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.**
2. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/news-sentiment-tracker.git](https://github.com/yourusername/news-sentiment-tracker.git)
   cd news-sentiment-tracker
3. **Run the application:**
   ```bash
   docker-compose up --build
4. **Access the dashboard:** Open your browser and navigate to: http://localhost:8501

## 🛠️ Tech Stack
- Language: Python 3.11
- Containerization: Docker & Docker Compose
- Data Engineering: Pandas, SQLAlchemy (SQLite)
- Web Scraping: Newspaper4k
- NLP: NLTK (SentimentIntensityAnalyzer)
- Frontend: Streamlit
##📂 Project Structure
- **app.py:** Entry point for the Streamlit dashboard and UI logic.
- **scraper.py:** Modular scraping engine with robust connection error handling.
- **database.py:** Database schema and SQLite session management.
- **utils.py:** Natural Language Processing (Sentiment) logic.
- **Dockerfile & docker-compose.yml:** Containerization and volume mapping configuration.
- **data/:** Persistent storage directory for the SQLite database (mounted as a volume).

## **👨‍💻 Developed by Yasmine Nabli**
