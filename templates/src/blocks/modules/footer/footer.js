$(".navListCont").on({
    mouseenter: function () {
        $('.whiteBack').addClass("active");
        $('.navList').addClass("active");
    },
    mouseleave: function () {
        $('.whiteBack').removeClass("active");
        $('.navList').removeClass("active");
    }
});