from requests import get
from bs4 import BeautifulSoup


def scrape_movie(movie_name):
    ##### For Fetching Link of First Title From Results ######
    url = "https://www.imdb.com/find?q="+movie_name+"&ref_=nv_sr_sm"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    result = html_soup.find('td', class_='result_text')

    ##### For Scraping Movie Info ######
    #####print(result.a['href'])

    movie_url = 'https://www.imdb.com'+result.a['href']+'?ref_=fn_al_tt_1'
    response = get(movie_url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    movieInfo = {'title': '', 'rating': '', 'categories': [], 'summary': '',
                 'directors': [], 'stars': []}
    ##### For Scraping Title ######

    title = html_soup.find('h1', class_ = 'TitleHeader__TitleText-sc-1wu6n3d-0 dxSWFG').text
    movieInfo['title'] = title.replace('\xa0', ' ')
    ###print(movieInfo['title'])
    ##### For Scraping Rating ######

    rating = html_soup.find('span', class_='AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV').text
    ##print(rating)
    movieInfo['rating'] = rating+"/10"

    plot = html_soup.find('div', class_='ipc-html-content ipc-html-content--base').find_all('div')

    summary = plot[0].text.strip()

    ##print(summary)
    movieInfo['summary'] = summary

    ##### For Scraping Category ######

    categories_data = html_soup.find('div', class_='ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL').find_all('a')
    categories_data.pop()
    categories = []
    for category in categories_data:
        ###print(category.text)
        categories.append(category.text)

    movieInfo['categories'] = categories

    ##### For Scraping Summary ######

    

    ##### For Scraping List of Directors ######

    directors_data = html_soup.find('li', class_ = 'ipc-metadata-list__item').find_all('div')
    
    directors = []
    for director in directors_data:
        ###print(director.text)
        directors.append(director.text)
    directors.pop();
    movieInfo['directors'] = directors

    ##### For Scraping List of Writers ######

    #### For Scraping List of Stars ######
    stars_data = html_soup.find('div', class_ = 'ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l title-cast__grid').find_all('div',class_ = 'StyledComponents__CastItemWrapper-y9ygcu-7 hTEaNu')
    stars = []
    for star in stars_data:
        ##print(star.find_all('div', class_= 'StyledComponents__CastItemSummary-y9ygcu-9 fBAofn')[0].a.text)
        stars.append(star.find_all('div', class_= 'StyledComponents__CastItemSummary-y9ygcu-9 fBAofn')[0].a.text)

    movieInfo['stars'] = stars


    ########## FINAL RESULT ###########
    return movieInfo
  
