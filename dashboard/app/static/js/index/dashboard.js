$(document).ready(function () {
    var trigger = $('.hamburger'),
        overlay = $('.overlay'),
        monitoringContent = $('.monitoring-content');
        isClosed = false;

    trigger.click(function () {
        hamburger_cross();
    });

    function hamburger_cross() {

        if (isClosed == true) {
            monitoringContent.removeClass('col-lg-10');
            monitoringContent.addClass('col-lg-12');
            trigger.removeClass('is-open');
            trigger.addClass('is-closed');
            isClosed = false;
        } else {
            monitoringContent.removeClass('col-lg-12');
            monitoringContent.addClass('col-lg-10');
            trigger.removeClass('is-closed');
            trigger.addClass('is-open');
            isClosed = true;
        }
    }

    $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
    });
});