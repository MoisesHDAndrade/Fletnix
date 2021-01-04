
Vue.component('navbar',{
    props:[''],
    template: `<div id="nav-app">
    <nav class="navbar navbar-expand-lg navbar-dark  sticky-top" style="background-color:rgba(0,0,0,0.3)">
      <div class="container-fluid">
        <a class="navbar-brand" style="color:#cc5353" href="#"> <img style="height:35px;width: 100px;"src="{%static 'img/logo.png'%}" alt=""> </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="{% url 'movies:index' %}">Home</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownCategories" role="button" data-toggle="dropdown" aria-expanded="false">
                Categories
              </a>
              <ul class="dropdown-menu p-0 bg-dark bg-gradient" aria-labelledby="navbarDropdownCategories">
                <li><a class="dropdown-item  bg-transparent text-light" href="#">Action</a></li>
                <li><a class="dropdown-item  bg-transparent  text-light" href="#">Another action</a></li>
                <li><a class="dropdown-item bg-transparent  text-light" href="#">Something else here</a></li>
              </ul>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownActions" role="button" data-toggle="dropdown" aria-expanded="false">
                Actions
              </a>
              <ul class="dropdown-menu p-0 bg-dark bg-gradient" aria-labelledby="navbarDropdownActions">
                <li><a class="dropdown-item  bg-transparent text-light" href="{% url 'movies:searcher' %}">Add a new movie to library</a></li>
              </ul>
            </li>
          </ul>
          <form class="d-flex" method="GET" action="{% url 'movies:library_search' %}">
             
            <input id="movie-scraper" class="form-control mr-2 text-white"  type="search" style="background-color:#18191c;" 
            name="search" autocomplete="off" placeholder="Search" aria-label="Search"><span><i  id="search-icon" class="fa fa-search mr-2 fa-2x" ></i></span>
            <button class="btn text-white" style="background-color:#cc5353"type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
  </div>`})

new Vue({
    el: "#nav-app",
    data: {

    },
    methods:{

    },
    created(){

    }
})