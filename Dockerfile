# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Install system dependencies needed for lxml and newspaper4k
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. PRE-DOWNLOAD NLTK DATA TO AVOID RUNTIME ISSUES
RUN python -m nltk.downloader vader_lexicon

# 6. Copy the rest of the application
COPY . .

# 7. Expose the port Streamlit runs on
EXPOSE 8501

# 8. Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]