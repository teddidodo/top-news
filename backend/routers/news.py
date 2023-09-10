from fastapi import APIRouter
import pygooglenews
import json

router = APIRouter()
news = []

@router.get('/')
def read_news(query: str):

    # Create a Google News client
    news_client = pygooglenews.GoogleNews(lang='en', country='US')

    # Search for news articles on a specific topic or query
    query = "Python programming"
    news_results = news_client.search(query)

    # Extract and print the top news articles
    for idx, article in enumerate(news_results['entries'], start=1):
        print(f"Article {idx}:")
        news.append(article)
    return news

@router.post('/', status_code=200)
def save_news(news_id: str):
    return news_id

@router.get('/queries', status_code=200)
def read_search_queries(user_id: str):
    return ['query1', 'query2']

@router.delete('/', status_code=200)
def unsave_news(news_id: str):
    return news_id
