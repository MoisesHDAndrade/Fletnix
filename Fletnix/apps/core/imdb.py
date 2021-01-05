from bs4 import BeautifulSoup as bs
import requests

# def get_cover(obj):
#     imagem = ''
#     res = dict()
#     headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
#     url = obj
#     page = requests.get(url, headers=headers)
#     soup = bs(page.text, 'html.parser')
#     title = ''
#     if soup.find(class_="title_wrapper",attrs="H1") != None:
#         title = soup.find(class_="title_wrapper",attrs="H1")
    
#     summary = ''
#     if soup.find(class_="summary_text") != None:
#         summary = soup.find(class_="summary_text").text
    
#     subtext = ''
#     if soup.find(class_="subtext") != None:
#         subtext = soup.find(class_="subtext")

#     genre = subtext.findChildren("a", recursive = False)

#     stars = ''
#     if soup.find('span', attrs = {'itemprop':'ratingValue'}) != None:
#         stars = soup.find('span', attrs = {'itemprop':'ratingValue'}).text
#     img = soup.find(class_="poster", attrs='img')
  
#     genre_list = []
#     for item in genre:
#         genre_list.append(item.text)
#     if img:
#         imagem = img.img.get('src')

#     res = {'title':title.h1.text, 'img': imagem, 'stars':stars, 'genre':genre_list[0:-1], 'summary':summary}
    
#     return res

# def search_imdb(search):
#     headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
#     url = f'https://www.imdb.com/find?q={search}&s=tt&ref_=fn_al_tt_mr'
#     page = requests.get(url, headers=headers)
#     soup = bs(page.text, 'html.parser')
#     td = soup.find_all(class_="result_text",attrs='href')
#     results = (item for item in td)

#     return results

def get_cover(obj):
    imagem = ''
    res = dict()
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    url = obj
    page = requests.get(url, headers=headers)
    soup = bs(page.text, 'html.parser')
    
    if soup.find(class_="13",attrs="h2") != None:
        pass
    title = soup.find("h2")

    year = ''
    if title.findChildren("span", recursive = False):
        year =  title.findChildren("span", recursive = False)[0].text
    
    people = soup.find(class_="people scroller")
    cards = ''
    
    try:
        cards = people.find_all(class_="card")
    except Exception as e:
        print(e)

    actors = []
    
    for item in cards:
        actors.append(item.p.text)
    

    trailer = ''
    if soup.find(class_="play_trailer"):
        trailer = soup.find(class_="play_trailer").get('data-id')

    
    summary = ''
    if soup.find(class_="overview") != None:
        summary = soup.find(class_="overview").text
    
    subtext = ''
    if soup.find(class_="facts") != None:
        subtext = soup.find(class_="facts")
    
    genre = subtext.find_all(class_="genres")
    
    genre_list = []
    for item in genre:
        genre_list.append(item.text)
    
    image_content = soup.find("div", class_="image_content")
    
    img = image_content.findChildren("img", recursive = False)
    
    
    if img:
        imagem = ''
        try:
            imagem = img[0].get('data-src')
            if requests.get(imagem).status_code != 200:
                imagem = f"https://www.themoviedb.org{img[0].get('data-src')}"
               

        except Exception as e:
           
            imagem = f"https://www.themoviedb.org{img[0].get('data-src')}"
        
        
       
        
    
    res = {
        'title':title.a.text, 
        'img': imagem, 
        'genre':genre_list, 
        'summary':summary, 
        'year':year,
        'trailer':trailer,
        'actors':actors}
    
    return res

def search_imdb(url_string):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
	url = f'https://www.themoviedb.org/search?query={url_string}'
	result = dict()
	page = requests.get(url, headers = headers)
	soup = bs(page.text, 'html.parser')
    
	result_div = soup.find_all(class_="card v4 tight")
	results = (item for item in result_div)
	# print(soup.find_all("img", class_="poster")[0].get('src'))
    
	return results
