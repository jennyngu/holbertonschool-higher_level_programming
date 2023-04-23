$(document).ready(function() {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
        var greeting = data.hello;
        console.log(greeting);
        $("#hello").text(greeting);
    });
});