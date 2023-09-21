import HTTP, { requestAPI } from './http_common'
import { return_authorization_header } from '@/utils/token'

export const postNewsAPI = async ({title, pubDate, link, description, creator, source_id, country, category, language, keywords, query}) => {
  const body = {
    title,
    published: pubDate,
    link,
    description,
    author: creator,
    publisher: source_id,
    country,
    category,
    language,
    keywords,
    query
  }

  try {
    const postNewsAPI = HTTP.post('/', body, { headers: return_authorization_header() })
    await requestAPI(postNewsAPI)
  } catch (error) {
    console.log(error);
  }
}

export const readNews = async (query) => {
  try {
    const newsPromise = HTTP.get('/news?query=' + query, { headers: return_authorization_header() })
    const data = await requestAPI(newsPromise)
    return data
  } catch (error) {
    console.log(error);
    return error
  }
}

export const readSavedNews = async () => {
  try {
    const savedNewsPromise = HTTP.get('/saved_news', { headers: return_authorization_header() })
    const data = await requestAPI(savedNewsPromise)
    return data
  } catch (error) {
    console.log(error);
    return error
  }
}

export const deleteQueryAPI = async (query) => {
  try {
    const deleteQueryPromise = HTTP.delete('/query?query=' + query, { headers: return_authorization_header() })
    await requestAPI(deleteQueryPromise)
  } catch (error) {
    console.log(error);
  }
}

export const postQueryAPI = async (query) => {
  try {
    const queryPromise = HTTP.post('/query', { query: query }, { headers: return_authorization_header() })
    await requestAPI(queryPromise)
  } catch (error) {
    console.log(error);
  }
}

export const getQueries = async () => {
  try {
    const queriesPromise = HTTP.get('/queries', { headers: return_authorization_header() })
    const data = await requestAPI(queriesPromise)
    return data
  } catch (error) {
    console.log(error);
    return error
  }
}

