from sqlalchemy import create_engine, Column, String, Float, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    url = Column(String, unique=True)
    sentiment = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class DBManager:
    def __init__(self):
        self.engine = create_engine('sqlite:///data/news_data.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_article(self, title,text, url, sentiment):
        session = self.Session()
        try:
            new_article = Article(title=title, text=text,url=url, sentiment=sentiment)
            session.add(new_article)
            session.commit()
        except:
            session.rollback()
        finally:
            session.close()