function validate() {
    var checkBox = document.getElementById('chkbx1');
    var submitButton = document.getElementById('b1');

    if (checkBox && checkBox.checked) {
        if (submitButton) {
            submitButton.disabled = false;
        }
    } else {
        if (submitButton) {
            submitButton.disabled = true;
        }
    }
}

$('.niceInputs').jvFloat();

$(document).ready(function() {
    validate();
});

$(function() {
    $('[data-toggle="tooltip"]').tooltip()
});

$('.modals form').focusin(function() {
    $('.modals input.form-control').tooltip('hide');
});

$('.forgetPass').click(function() {
    $('#signin').modal('hide');
    $('#recoverPass').modal('show');
});

$('.resendConfirmationToken').click(function() {
    $('#signin').modal('hide');
    $('#resend_confirmation_token').modal('show');
});
/*фикс модалок для IOS*/
$(document).ready(function() {
    // Detect ios 11_x_x affected
    // NEED TO BE UPDATED if new versions are affected
    var ua = navigator.userAgent,
        iOS = /iPad|iPhone|iPod/.test(ua);
    // ios 11 bug caret position
    if(iOS){
        // Add CSS class to body
        $("body").addClass("iosBugFixCaret");
    }
});

$(document).ready(function() {
    var anchor = window.location.hash;
    if (anchor == "#signin") {
        $('button.signin').trigger('click');
    } else if (anchor == "#signup") {
        $('button.signup').trigger('click');
    }

});


$(document).ready(function() {
    $('.modal').on('shown.bs.modal', function() {
        $(this).find("input:visible").eq(0).trigger("focus");
    })
});

$(document).ready(function() {

    $('form#login-form').on('beforeSubmit', function (event) {
        if(yaCounter23673460!=undefined) yaCounter23673460.reachGoal('signin');
        if(typeof gtag==="function"){
            gtag("event","signin");
        }else{
            if(ga!=undefined) ga("send","signin");
        }
    });

    $('form#registration-form').on('beforeSubmit', function (event) {
        if(yaCounter23673460!=undefined) yaCounter23673460.reachGoal('reg_web');
        if(typeof gtag==="function"){
            gtag("event","reg_web");
        }else{
            if(ga!=undefined) ga("send","reg_web");
        }
    });

    $('form#registration-advert').on('beforeSubmit', function (event) {
        if(yaCounter23673460!=undefined) yaCounter23673460.reachGoal('reg_advert');
        if(typeof gtag==="function"){
            gtag("event","reg_advert");
        }else{
            if(ga!=undefined) ga("send","reg_advert");
        }
    });


    $('.vk_sign').on('click', function (event) {
        if(yaCounter23673460!=undefined) yaCounter23673460.reachGoal('vk_reg');
        if(typeof gtag==="function"){
            gtag("event","vk_reg_ga");
        }else{
            if(ga!=undefined) ga("send","vk_reg_ga");
        }
    });

    $('.fb_sign').on('click', function (event) {
        if(yaCounter23673460!=undefined) yaCounter23673460.reachGoal('fb_reg');
        if(typeof gtag==="function"){
            gtag("event","fb_reg_ga");
        }else{
            if(ga!=undefined) ga("send","fb_reg_ga");
        }
    });

    $('.gp_sign').on('click', function (event) {
        if(yaCounter23673460!=undefined) yaCounter23673460.reachGoal('google_reg');
        if(typeof gtag==="function"){
            gtag("event","google_reg_ga");
        }else{
            if(ga!=undefined) ga("send","google_reg_ga");
        }
    });

});

$(document).ready(function() {
    var query = document.location.search.replace(/(^\?)/,'').split("&").map(function(n){return n = n.split("="),this[n[0]] = n[1],this}.bind({}))[0];
    if (query.action === 'connect') {
        $('#connectAccount').modal('show');
    }
});
