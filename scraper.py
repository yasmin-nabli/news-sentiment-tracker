import newspaper
from newspaper import Config

class NewsScraper:
    def __init__(self, url):
        self.url = url
        # 🕵️ Add a User-Agent to pretend you are a real browser
        self.config = Config()
        self.config.browser_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        self.config.request_timeout = 15 # Wait longer for slow connections

    def fetch_articles(self, limit=5):
        try:
            # Build the paper with custom config
            paper = newspaper.build(self.url, config=self.config, memoize_articles=False)
            
            # Check if we actually found articles
            if not paper.articles:
                return "CONNECTION_ERROR"

            articles_data = []
            for article in paper.articles[:limit]:
                try:
                    article.download()
                    article.parse()
                    # Final safety check: ignore empty articles
                    if article.text and article.title:
                        articles_data.append({
                            'title': article.title,
                            'text': article.text,
                            'url': article.url
                        })
                except Exception:
                    continue 
            
            return articles_data if articles_data else "CONNECTION_ERROR"

        except Exception as e:
            # This catches the 'NoneType' error if build() fails
            return "CONNECTION_ERROR"