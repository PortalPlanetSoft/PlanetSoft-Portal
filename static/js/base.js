"use strict"

let maxDate;

// pageOnLoad function that fetches action result from sessionStorage so the toast alert can be shown
$(function () {
    let resultMessage;
    resultMessage = sessionStorage.getItem("message");
    switch (resultMessage) {
        case SUCCESSFUL_ACTION:
            sessionToastToggle(resultMessage, SUCCESSFUL_ACTION);
            break;
        case ERROR_ACTION:
            sessionToastToggle(resultMessage, ERROR_ACTION);
            break;
        case DELETE_SUCCESSFUL:
            sessionToastToggle(resultMessage, DELETE_SUCCESSFUL);
            break;
        default:
            resultMessage = DEFAULT_TOAST;
            sessionStorage.clear();
            break;
    }

    const TODAYS_DATE = new Date();

    let month = TODAYS_DATE.getMonth() + 1;
    let day = TODAYS_DATE.getDate();
    let year = TODAYS_DATE.getFullYear();

    if (month < 10)
        month = '0' + month.toString();
    if (day < 10)
        day = '0' + day.toString();

    maxDate = year + '-' + month + '-' + day;
    dateValidation();
});

function dateValidation() {
    $('#id_birth_date').attr('max', maxDate);
    $('#id_start_time_0').attr('min', maxDate);
    $('#id_end_time_0').attr('min', maxDate);
}

function sessionToastToggle(resultMessage, action) {
    showToast(resultMessage, action);
    sessionStorage.clear();
}

// Navigation hamburger menu
NAV_TOGGLE_BTN.addEventListener('click', (e) => {
    if (NAV_TOGGLE_BTN.firstChild.getAttribute('data-icon') === 'bars') {
        NAV_TOGGLE_BTN.firstChild.setAttribute('data-icon', 'xmark')
        NAV_TOGGLE_BTN.style.position = "fixed";
    } else {
        NAV_TOGGLE_BTN.firstChild.setAttribute('data-icon', 'bars');
        NAV_TOGGLE_BTN.style.position = "absolute";
    }
    toggleAnimation(NAVIGATION, 'showNav', 'hideNav');
});

function toggleAnimation(element, firstAnimName, secondAnimName) {
    if (
        element.style.animationName === '' ||
        element.style.animationName === secondAnimName
    ) {
        element.style.animationName = firstAnimName;
        return;
    }
    element.style.animationName = secondAnimName;
}

// function for showing chosen image preview on user settings page (/profile)
function changeThumbnail() {
    document.getElementById('id_profile_pic').addEventListener("change", function (e) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('photo-preview').src = e.target.result;
        };
        reader.readAsDataURL(this.files[0]);
    })
}

function docReady(fn) {
    if (document.readyState === "complete" || document === "interactive") {
        setTimeout(fn, 1);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}

docReady(changeThumbnail);

function submitFilterForm() {
    document.forms["userFilterForm"].submit();
}

function imageRemove() {
    let form = $("#avatar-delete-form");
    $.ajax({
            url: URL_ADDRESS + '/employees/remove-avatar/',
            type: 'POST',
            data: form.serialize(),
            success: function (data, textStatus, xhr) {
                requestSuccessful();
            },
            error: function (data, textStatus, xhr) {
                requestSuccessful();
            },
        },
    );
}

let ident;

function idKeeper(id) {
    ident = id;
    alert(id);
}

function imageRemoveNEWS(form_id) {
    let formData = new FormData($(form_id)[0]);
    alert(ident);
    $.ajax({
            url: DELETE_NEWS_PICTURE_URL + ident,
            type: 'POST',
            data: formData,
            success: function (data, textStatus, xhr) {
                requestSuccessful();
            },
            error: function (data, textStatus, xhr) {
                requestSuccessful();
            },
        },
    );
}

function genericSubmitCommentReaction(url, form_id, target_form_id, id, flag){
    let form = $(form_id);
    $.ajax({
            url: url,
            type: 'POST',
            data: form.serialize(),
            headers: flag,
            success: function (data, textStatus, xhr) {
                genericContentLoad(target_form_id, id);
            },
            error: function (data, textStatus, xhr) {
                requestUnsuccessful();
            },
        },
    );
}

function genericContentLoad(target_form_id, id){
    $.ajax({
        url: window.location.href,
        type: 'GET',
        data: {
            txtsearch: $(target_form_id + id).val()
        },
        dataType: 'html',
        success: function (data) {
            let result = $(target_form_id + id).append(data).find(target_form_id + id).html();
            $(target_form_id + id).html(result);
        },
    });
}

function reveal(field_id) {
    if (document.getElementById("box" + field_id).checked) {
        document.getElementById(field_id).type = 'text';
    } else
        document.getElementById(field_id).type = 'password';
}

function dateSet() {
    $.ajax({
        url: URL_ADDRESS + '/employees/previous-login/',
        type: 'GET',
    });
}

function showButtonsNewsImage(show) {
    const DELETE_IMAGE_BUTTON = document.getElementById("remove-image-button");
    const INPUT_FIELD_NEWS = document.getElementById("id_image");
    INPUT_FIELD_NEWS.classList.add("ov-form__btn--blue", "ov-form__btn");
    if (show == 0) {
        DELETE_IMAGE_BUTTON.style.visibility = "visible";
        INPUT_FIELD_NEWS.style.visibility = "visible";
    } else {
        DELETE_IMAGE_BUTTON.style.visibility = "hidden";
        INPUT_FIELD_NEWS.style.visibility = "hidden";
    }
}

function showButtonsAvatarImage(show) {
    INPUT_FIELD.classList.add("ov-form__btn--blue", "ov-form__btn");
    if (show == 0) {
        DELETE_AVATAR_BUTTON.style.visibility = "visible";
        INPUT_FIELD.style.visibility = "visible";
    } else {
        DELETE_AVATAR_BUTTON.style.visibility = "hidden";
        INPUT_FIELD.style.visibility = "hidden";
    }
}