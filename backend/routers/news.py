from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from newsdataapi import NewsDataApiClient
from sqlalchemy.orm import Session
from database import get_db
import model, schema, utils, jwt_auth
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

@router.get('/news', dependencies=[Depends(jwt_auth.JWTBearer())])
def read_news(query: str):

    if not query:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='A query is required to continue!'
        )

    api = NewsDataApiClient(apikey=os.environ.get('API_KEY'))

    response = api.news_api(q = query, size = 9)

    return response['results']

@router.get('/saved_news', dependencies=[Depends(jwt_auth.JWTBearer())])
def read_saved_news(request: Request, db: Session = Depends(get_db)):
    
    user_id = jwt_auth.return_user_id(request)
    news = []

    # if not query:
        # user_news_info = db.query(model.UserNews).filter(model.UserNews.user_id == user_id).all()
    # else:
    user_news_info = db.query(model.UserNews).filter(model.UserNews.user_id == user_id).all()

    for info in user_news_info:
        news.append(info.news)
    
    return news

@router.post('/', dependencies=[Depends(jwt_auth.JWTBearer())], status_code=200)
def save_news(news: schema.UserNewsSave, request: Request, db: Session = Depends(get_db)):

    if not news:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='News and/or query information should be provided to continue!'
        )
    
    news_dict = news.dict()
    news_dict['user_id'] = jwt_auth.return_user_id(request)
    query = news_dict.pop('query')

    # news_dict['published'] = utils.return_the_date(news_dict['published'])
    new_news = model.News(**news_dict)
    db.add(new_news)
    db.commit()
    db.refresh(new_news)

    user_id = jwt_auth.return_user_id(request)
    query_id = ''
    user_news = {}
    if query:
        query_id = db.query(model.Query.id).filter(model.Query.query == query).first()
        user_news = model.UserNews(user_id=user_id, news_id=new_news.id, query_id=query_id.id if query_id else None)
    else:
        user_news = model.UserNews(user_id=user_id, news_id=new_news)
    
    db.add(user_news)
    db.commit()
    db.refresh(user_news)

    return new_news


@router.delete('/', dependencies=[Depends(jwt_auth.JWTBearer())], status_code=200)
def unsave_news(news_id: str, request: Request, db: Session = Depends(get_db)):

    if not news_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='News ID is required to continue!'
        )
    
    user_id = jwt_auth.return_user_id(request)

    news_query = db.query(model.News).filter(model.News.id == news_id and model.News.user_id == user_id)
    news = news_query.first()

    if news == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No news with this ID!")
    
    if str(news.user_id) != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    news_query.delete(synchronize_session=False)
    db.commit()

    return news

@router.get('/queries', dependencies=[Depends(jwt_auth.JWTBearer())],  status_code=200)
def read_search_queries(request: Request, db: Session = Depends(get_db)):

    user_id = jwt_auth.return_user_id(request)

    queries = db.query(model.Query).filter(model.Query.user_id == user_id).all()

    return queries

@router.post('/query', dependencies=[Depends(jwt_auth.JWTBearer())], status_code=201)
def save_query(query: schema.QuerySchema, request: Request, db: Session = Depends(get_db)):

    if not query:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='A query is required to continue!'
        )
    user_id = jwt_auth.return_user_id(request)
    
    new_query = model.Query(query=query.query, user_id=user_id)
    db.add(new_query)
    db.commit()
    db.refresh(new_query)

    return new_query

@router.delete('/query', dependencies=[Depends(jwt_auth.JWTBearer())], status_code=200)
def delete_query(query: str, request: Request, db: Session = Depends(get_db)):

    if not query:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='A query is required to continue!'
        )
    
    user_id = jwt_auth.return_user_id(request)

    query_query = db.query(model.Query).filter(model.Query.query == query and model.Query.user_id == user_id)
    query = query_query.first()

    if query == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No news with this ID!")

    query_query.delete(synchronize_session=False)
    db.commit()

    return query
