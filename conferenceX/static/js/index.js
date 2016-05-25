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
            $(this).css("-webkit-filter", "grayscale(0%)");
            $(this).css("filter", "grayscale(0%)");
        },
        function(){
            $(this).css("-webkit-filter", "grayscale(100%)");
            $(this).css("filter", "grayscale(100%)");
        }
    );

    $("#google-maps").click(function() {
        $("#google-maps iframe").css("pointer-events", "auto");
    });

    $("#google-maps").mouseleave(function() {
        $("#google-maps iframe").css("pointer-events", "none");
    });
});

