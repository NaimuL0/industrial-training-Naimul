import datetime
from requests_html import HTMLSession
from .database import SessionLocal
from .crud import create_news
from .schemas import NewsCreate, News
from sqlalchemy.orm import Session
import logging

def single_news_scraper(url: str):
    session = HTMLSession()
    try:
        response = session.get(url)
        # response.html.render()  # This will download Chromium if not found

        publisher_website = url.split('/')[2]
        publisher = publisher_website.split('.')[-2]
        title = response.html.find('.h1', first=True).text
        reporter = response.html.find('.author-name', first=True).text
        datetime_element = response.html.find('.date', first=True)
        # news_datetime = datetime_element.attrs['datetime']
        category = response.html.find('h2', first=True).text
        content = '\n'.join([p.text for p in response.html.find('.rtejustify')])
        # img_tags = response.html.find('img')
        # images = [img.attrs['src'] for img in img_tags if 'src' in img.attrs]
        img_tags = response.html.find('.section-media')
        images = [img.attrs['data-src'] for img in img_tags if 'data-src' in img.attrs]
        news_datetime = datetime.datetime.now()

        print(f"Scraped news from {url}")
        print(f"Title: {title}")
        print(f"Reporter: {reporter}")
        print(f"Date: {news_datetime}")
        print(f"Category: {category}")
        print(f"Images: {images}")
        print(f"News Body: {content}")


        return NewsCreate(
            publisher_website=publisher_website,
            news_publisher=publisher,
            title=title,
            news_reporter=reporter,
            datetime=news_datetime,
            link=url,
            news_category=category,
            body=content,
            images=images,
        )
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def scrape_and_store_news(url: str, db: Session):
    news_data = single_news_scraper(url)
    if news_data is None:
        logging.error(f"Failed to scrape news from {url}")
        return None
    
    try:
        inserted_news = create_news(db=db, news=news_data)
        return inserted_news
    except Exception as e:
        logging.error(f"An error occurred while storing news to the database: {e}")
        return None

