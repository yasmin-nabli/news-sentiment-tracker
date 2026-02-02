# 🌐 Global News Sentiment Tracker

An automated end-to-end data pipeline designed to scrape real-time news articles, perform NLP-based sentiment analysis, and visualize public mood trends via a web dashboard.

## 🚀 Overview
This project demonstrates a complete data engineering lifecycle:
1. **Extraction:** Automated scraping of news sources using `newspaper4k`.
2. **Processing:** Text cleaning and Sentiment Analysis using `NLTK (VADER)`.
3. **Storage:** Structured data persistence using `SQLAlchemy` and `SQLite`.
4. **Visualization:** Real-time interactive dashboard built with `Streamlit`.



## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Data Engineering:** Pandas, SQLAlchemy
- **Web Scraping:** Newspaper4k
- **NLP:** NLTK (SentimentIntensityAnalyzer)
- **Frontend:** Streamlit

## 📂 Project Structure
- `app.py`: The entry point for the Streamlit dashboard.
- `scraper.py`: Modular scraping engine designed for scalability.
- `database.py`: Database schema and session management.
- `utils.py`: Natural Language Processing logic.

## 🔧 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/news-sentiment-tracker.git](https://github.com/yourusername/news-sentiment-tracker.git)
   cd news-sentiment-tracker