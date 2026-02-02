import streamlit as st
import pandas as pd
import time
from datetime import datetime
from scraper import NewsScraper
from utils import SentimentEngine
from database import DBManager


@st.cache_resource # This keeps it in memory so it only checks once
def load_nltk():
    import nltk
    nltk.download('vader_lexicon', quiet=True) # 'quiet' hides the "Downloading..." text

load_nltk()
st.set_page_config(page_title="Live Sentiment Tracker", layout="wide")

# Custom CSS to brand the app and hide Streamlit UI elements
st.markdown("""
    <style>
    .stAppDeployButton { display: none !important; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .status-card { padding: 20px; border-radius: 10px; background-color: #f0f2f6; }
    </style>
""", unsafe_allow_html=True)

# Initialize Backend Components
db = DBManager()
engine = SentimentEngine()

# --- 2. HELPER FUNCTIONS ---

def show_connection_error():
    """Displays a professional error message when scraping fails."""
    st.error("Connection Failed", icon="📡")
    st.warning("The news site is blocking the request or the internet is down.")

def run_analysis_cycle(url, limit):
    """Handles the core logic of scraping, analyzing, and saving data."""
    scraper = NewsScraper(url)
    articles = scraper.fetch_articles(limit=limit)
    
    if articles == "CONNECTION_ERROR":
        return False
    
    for art in articles:
        score = engine.analyze(art['text'])
        db.save_article(art['title'], art['text'], art['url'], score)
    return True

# --- 3. SIDEBAR UI ---

st.sidebar.title("⚙️ Control Panel")
news_url = st.sidebar.text_input("Target News URL", "https://www.bbc.com/news")
fetch_limit = st.sidebar.slider("Articles per cycle", 1, 10, 3)

manual_run = st.sidebar.button("🔍 Run Analysis Manually")
auto_mode = st.sidebar.toggle("🚀 Enable Auto-Monitoring", value=False)
refresh_interval = 60 

# --- 4. MAIN DASHBOARD UI ---

st.title("🌐 Global News Sentiment Tracker")
st.markdown(f"**System Status:** {'🟢 Auto-Scanning' if auto_mode else '⚪ Idle'}")

# Execution Logic
if manual_run or auto_mode:
    with st.spinner('Processing latest news...'):
        success = run_analysis_cycle(news_url, fetch_limit)
        
        if success:
            st.toast(f"Updated at {datetime.now().strftime('%H:%M:%S')}", icon="✅")
            if manual_run:
                st.success("Manual Scrape Completed!")
        else:
            show_connection_error()
            if auto_mode:
                st.info("Retrying in 1 minute...")
                time.sleep(refresh_interval)
                st.rerun()

# --- 5. DATA VISUALIZATION ---

# Load data from SQLite
df = pd.read_sql("SELECT * FROM articles ORDER BY timestamp DESC", db.engine)

if not df.empty:
    # Top Metrics Row
    avg_sent = df['sentiment'].head(10).mean()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Mood", "Positive" if avg_sent > 0 else "Negative")
    with col2:
        st.metric("Avg Sentiment Score", f"{round(avg_sent, 2)}")
    with col3:
        st.metric("Total Articles", len(df))

    # Charts & Tables
    st.subheader("📈 Sentiment Trend")
    st.line_chart(df.set_index('timestamp')['sentiment'])

    st.subheader("📑 Recent Articles")
    st.dataframe(
        df[['timestamp', 'title', 'sentiment', 'url']], 
        use_container_width=True,
        column_config={"url": st.column_config.LinkColumn("Article Link")}
    )
else:
    st.info("No data found. Please run a scan to begin.")

# --- 6. AUTOMATION LOOP ---
if auto_mode:
    time.sleep(refresh_interval)
    st.rerun()