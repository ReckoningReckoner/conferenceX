$(document).ready(function(){
    $('.parallax').parallax();

    $('.scrollto').click(function(){
        var link = $(this).attr("href");
        $('html, body').animate({
            scrollTop: $(link).offset().top - $('#navbar').height()
        }, 200);
    });

    $(".button-collapse").sideNav({
        edge: 'right', // Choose the horizontal origin
    });
});

