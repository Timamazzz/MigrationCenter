if (document.referrer.indexOf(window.location.origin) != -1) {
    $('.modalCoocke').addClass("active");
    $('.modalCoocke_content').addClass("active");
    $('html, body').css({
        overflow: 'hidden'
    });
}
else {
    console.log("from external site");
}

$('.modalCoockee_btn').on('click', function () {
    $('.modalCoocke').removeClass("active");
    $('.modalCoocke_content').removeClass("active");
    $('html, body').css({
        overflow: 'auto',
    });
})

$('.docsOpen').on('click', function () {
    $('.modalDocs').addClass("active");
    $('.modalDocs_content').addClass("active");
    $('html, body').css({
        overflow: 'hidden',
    });
})

$('.docsClose').on('click', function () {
    $('.modalDocs').removeClass("active");
    $('.modalDocs_content').removeClass("active");
    $('html, body').css({
        overflow: 'auto',
    });
})

$('.langOpen').on('click', function () {
    $('.modalLAng').addClass("active");
    $('.modalLang_content').addClass("active");
    $('html, body').css({
        overflow: 'hidden',
    });
})

$('.langClose').on('click', function () {
    $('.modalLAng').removeClass("active");
    $('.modalLang_content').removeClass("active");
    $('html, body').css({
        overflow: 'auto',
    });
})

$('.userInfo').on('click', function () {
    $('.userInfoModal').addClass("active");
    $('.modalUserBg').addClass("active");
    $('html, body').css({
        overflow: 'hidden',
    });
})

$('.modalUserBg').on('click', function () {
    $('.userInfoModal').removeClass("active");
    $('.modalUserBg').removeClass("active");
    $('html, body').css({
        overflow: 'auto',
    });
})




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