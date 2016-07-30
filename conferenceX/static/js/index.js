$(document).ready(function(){
    $('.parallax').parallax();

    /* Adjust scrollto to compensate for the navbar */
    $('.scrollto').click(function(){
        var link = $(this).attr("href");
        $('html, body').animate({
            scrollTop: $(link).offset().top - $('#navbar').height()
        }, 200);
    });

    /* Move hamburger sideNav to right */
    $(".button-collapse").sideNav({
        edge: 'right', // Choose the horizontal origin
    });

    /* B&W effects */
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

    /* Prevent accidental google maps scrolling */
    $("#google-maps").click(function() {
        $("#google-maps iframe").css("pointer-events", "auto");
    });

    $("#google-maps").mouseleave(function() {
        $("#google-maps iframe").css("pointer-events", "none");
    });

    /* Fix scrolling when modals are opened */
    $.featherlight.defaults.afterOpen = function(event) {
        $("body").css("overflow", "hidden");
    };

    $.featherlight.defaults.afterClose = function(event) {
        $("body").css("overflow", "scroll");
    };
});

