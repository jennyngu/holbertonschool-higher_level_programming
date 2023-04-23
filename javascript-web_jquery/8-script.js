$.ajax({
    url: "https://swapi-api.hbtn.io/api/films/?format=json",
    method: "GET",
    dataType: "json",
    success: function(response) {
        var titles = [];
        for (let i = 0; i < response.results.length; i++) {
            const title = response.results[i].title;
            titles.push(title)
            $("#list_movies").append("<li>  "+ title +" </li>");
        }
    }
});