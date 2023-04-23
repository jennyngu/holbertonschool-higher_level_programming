$.get("https://swapi-api.hbtn.io/api/people/5/?format=json", function(data) {
    var charName = data.name;
    $("#character").text(charName);
});