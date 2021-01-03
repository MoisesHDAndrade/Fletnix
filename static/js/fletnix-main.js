let searchIcon = document.getElementById("search-icon")
let movieScraper = document.getElementById("movie-scraper")

searchIcon.addEventListener("click", function(){
    movieScraper.style.display = "block"
    movieScraper.style.visibility = "visible"
    movieScraper.style.width = "400px"
    movieScraper.style.transition = "0.5s"
    movieScraper.classList.add("hover-expand-input")
    })

searchIcon.addEventListener("mouseover", function(){
    movieScraper.style.display = "block" 
    movieScraper.classList.add("hover-expand-input")
    })

movieScraper.addEventListener("mouseout", function(){
    movieScraper.style.display = "none"
    movieScraper.style.visibility = "hidden"
    movieScraper.style.width = "0px"
    movieScraper.style.transition = "width 0.5s"
})