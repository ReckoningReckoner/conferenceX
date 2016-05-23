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

    $(".featured-image").hover(
        function(){
            $(this).css("filter", "grayscale(0%)");
        },
        function(){
            $(this).css("filter", "grayscale(100%)");
        }
    );

});

