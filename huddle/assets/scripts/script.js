$(document).on("scroll", function () {
    var pageTop = $(document).scrollTop();
    var pageBottom = pageTop + $(window).height();
    var infos = $(".info, .info1");

    for (var i = 0; i < infos.length; i++) {
        var info = infos[i];

        if ($(info).position().top < pageBottom) {
            $(info).addClass("visible");
        } else {
            $(info).removeClass("visible");
        }
    }
});
