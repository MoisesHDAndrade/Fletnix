# Fletnix 

**Fletnix** is a site where allow anyone inside your localhost watch your saved movies from your browser
---

## About
Fletnix use Django as a backend and scrape all the informations with python requests and BeatifulSoup4 libs from [TMDB](https://www.themoviedb.org/)
Javascript Vanilla to manipulate the DOM and Bootstrap 5 
(Planning to integrate VueJS)

## Features
* Work with MP4 files and Youtube links
* Display summary, cover and cast
* Template inspirate by Netflix
* API available, but you can change whatever you want to

## How it Works
### Linux
##### In your host computer
* Clone the project
* Create a Virtual env
* Run pip install -r requirements.txt
* Run python manage.py migrate
* Run python manage.py runserver 0.0.0.0:8000
* Run ifconfig to know what it is your local ip address  exxample:*192.168.1.12*
* Add your local ip address on ALLOWED_HOSTS in settings.py
* Install Apache
* Go to your Apache folder '/var/www/'
* Give admin permissions to your a Apache folder
* Create a new folder inside like '/var/www/movies'

#### Now the best part
* Add your movies to library on menu "actions"
* Search by the name of movie that you want add
* Pick it up one of that those
* Add a URL using the follow address
  - your machine local ip address 
  - followed by the folder where it is your file *like http://192.168.1.12/movies/my_movie.mp4*

---
If you are not sure where it is your files, bur you already installed Apache
just type your local ip address your browser + your movie folder like this *http://192.168.1.12/movies/*

### Important
Do not use for commercial purpose

## Screenshots
![alt text](https://github.com/FuryAndRage/Fletnix/blob/main/images/index.png "Index") 
![](https://github.com/FuryAndRage/Fletnix/blob/main/images/scraping_movie.png "Scraping")
![](https://github.com/FuryAndRage/Fletnix/blob/main/images/movie_info_scraping.png "Scraping Movie info")
![](https://github.com/FuryAndRage/Fletnix/blob/main/images/movie_detail.png "Detail")
