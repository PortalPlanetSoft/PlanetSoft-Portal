"use strict"

const navToggleBtn = document.querySelector('#ov-nav-toggle');
const navigation = document.querySelector('#ov-navigation');

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

    const todaysDate = new Date();

    let month = todaysDate.getMonth() + 1;
    let day = todaysDate.getDate();
    let year = todaysDate.getFullYear();

    if (month < 10)
        month = '0' + month.toString();
    if (day < 10)
        day = '0' + day.toString();

    let maxDate = year + '-' + month + '-' + day;
    $('#id_birth_date').attr('max', maxDate);
});

function sessionToastToggle(resultMessage, action) {
    showToast(resultMessage, action);
    sessionStorage.clear();
}

// Navigation hamburger menu
navToggleBtn.addEventListener('click', (e) => {
    if (navToggleBtn.firstChild.getAttribute('data-icon') === 'bars') {
        navToggleBtn.firstChild.setAttribute('data-icon', 'xmark')
        navToggleBtn.style.position = "fixed";
    } else {
        navToggleBtn.firstChild.setAttribute('data-icon', 'bars');
        navToggleBtn.style.position = "absolute";
    }
    toggleAnimation(navigation, 'showNav', 'hideNav');
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

// function that reloads to target page so that up-to-date results (post edit) can be shown
function pageReload() {
    window.location.reload();
}

function submitFilterForm() {
    document.forms["userFilterForm"].submit();
}

function imageRemove() {
    let form = $("#avatar-delete-form");
    $.ajax({
            url: urlAddress + '/employees/remove-avatar/',
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

function submitLikeButton(id) {
    let form = $("#news-like-form");
    alert("radi");
    $.ajax({
            url: urlAddress + '/news/react/' + id + '/',
            type: 'POST',
            data: form.serialize(),
            success: function (data, textStatus, xhr) {
                $("#comment-like-section").load(location.href + "#comment-like-section");
                requestSuccessful();
            },
            error: function (data, textStatus, xhr) {
                requestUnsuccessful();
            },
        },
    );
}

function submitDislikeButton(id) {
    let form = $("#news-dislike-form");


    /*
    $.ajax({
            url: urlAddress + '/news/react/' + id + '/',
            type: 'POST',
            data: form.serialize(),
            success: function (data, textStatus, xhr) {
                requestSuccessful();
            },
            error: function (data, textStatus, xhr) {
                requestUnsuccessful();
            },
        },
    );*/
}