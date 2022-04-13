"use strict"

// function for displaying generic modal
async function displayModal(targetUrlAddress) {
    MODAL_CONTAINER.style.display = "flex";
    await $.ajax({
            url: targetUrlAddress,
            type: 'get',
            success: (data) => {
                MODAL_CONTENT.innerHTML = data;
                dateValidation();
            },
            error: (data) => {
                MODAL_CONTENT.innerHTML = data;
            },
        },
    )
}

async function newsDeletePicture(targetUrlAddress, id) {
    MODAL_CONTAINER.style.display = "flex";
    await $.ajax({
            url: targetUrlAddress,
            type: 'get',
            success: (data) => {
                MODAL_CONTENT.innerHTML = data;
                dateValidation();
                idKeeper(id);
            },
            error: (data) => {
                MODAL_CONTENT.innerHTML = data;
            },
        },
    )
}

// onclick function for opening of news edit modal
async function showNewsEditModal(id) {
    await displayModal(EDIT_NEWS_URL + id + '/').then(
        () => {
            addImagePreview("id_image", "photo-preview")
        }
    );
}

function addImagePreview(imageFeild_id, imagePreview_id) {
    document.getElementById(`${imageFeild_id}`).addEventListener("change", function (e) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById(`${imagePreview_id}`).src = e.target.result;
        };
        reader.readAsDataURL(this.files[0]);
    })
}

// function that submits user's password change request
function submitPasswordChangeForm() {
    let formErrors = passwordChangeValidation("id_old_password", "id_new_password1", "id_new_password2");
    if (formErrors) {
        genericValidationError(formErrors)
    } else {
        genericSubmitForm("password-change-form", PASSWORD_CHANGE_URL, SUCCESSFUL_ACTION)
    }
}

// function that validates the new password
function passwordChangeValidation(oldPassword_id, newPassword_id, newPasswordCompare_id) {
    let oldPassword = document.getElementById(oldPassword_id).value;
    let newPassword = document.getElementById(newPassword_id).value;
    let newPasswordCompare = document.getElementById(newPasswordCompare_id).value;
    let errors = {};

    if (!oldPassword) {
        errors[oldPassword_id] = FIRST_FIELD_EMPTY
    }
    if (!newPassword) {
        errors[newPassword_id] = FIRST_FIELD_EMPTY
    } else if (!newPassword.match(PASSWORD_REGEX)) {
        errors[newPassword_id] = PASSWORD_VALIDATION_FAIL
    }
    if (newPasswordCompare !== newPassword) {
        errors[newPasswordCompare_id] = PASSWORDS_MATCHING_ERROR
    }
    if (jQuery.isEmptyObject(errors)) {
        return 0;
    }
    return errors;
}

// function that submits user's edited data and displays error messages
function submitEditUserForm(id) {
    let formErrors = validatorFunction("id_email", "id_phone", "id_business_phone");
    if (formErrors) {
        genericValidationError(formErrors)
    } else {
        genericSubmitForm("edit-emp-form", VIEW_USER_URL + id + '/', SUCCESSFUL_ACTION)
    }
}

function genericSubmitForm(form_id, submit_url, success_message) {
    let form = $(`#${form_id}`);
    $.ajax({
        url: submit_url,
        type: 'POST',
        dataType: 'html',
        data: form.serialize(),
        success: function (data, textStatus, xhr) {
            sessionStorage.clear();
            sessionStorage.setItem("message", success_message);
            closeFunction();
        },
        error: function (data, xhr, textStatus) {
            requestUnsuccessful();
            MODAL_CONTENT.innerHTML = data.responseText;
        },
    });
}

function genericValidationError(errors) {
    for (const [errorLocation, message] of Object.entries(errors)) {
        document.getElementById(errorLocation).insertAdjacentHTML("afterend", `<ul class=\"errorlist\"><li>${message}</li></ul>`);
    }
}

function submitFormMultimediaData(targetUrlAddress, formData_id) {
    let formData = new FormData($(formData_id)[0]);
    $.ajax({
        url: targetUrlAddress,
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function (data, textStatus, xhr) {
            requestSuccessful();
        },
        error: function (data, xhr, textStatus) {
            requestUnsuccessful();
        },
    });
}

// function used for validation of email address and phone number
function validatorFunction(emailAddress, phoneNumber, vpnNumber) {
    let emailValid = document.getElementById(emailAddress).value.match(REGEX_MAIL);
    let phoneValid = document.getElementById(phoneNumber).value.match(REGEX_NUMBER);
    let vpnValid = document.getElementById(vpnNumber).value.match(REGEX_VPN_NUMBER);
    let errors = {};
    if (!emailValid) {
        errors[emailAddress] = INVALID_EMAIL_ERROR
    }
    if (!phoneValid) {
        errors[phoneNumber] = INVALID_PHONE_ERROR
    }
    if (!vpnValid) {
        errors[vpnNumber] = INVALID_VPN_ERROR
    }
    if (jQuery.isEmptyObject(errors)) {
        return 0;
    }
    return errors;
}

function requestSuccessful() {
    sessionStorage.clear();
    sessionStorage.setItem("message", SUCCESSFUL_ACTION);
    closeFunction();
}

function requestUnsuccessful() {
    sessionStorage.clear();
    sessionStorage.setItem("message", ERROR_ACTION);
    showToast(ERROR_ACTION, ERROR_ACTION);
    sessionStorage.clear();
}

// function that closes the modal if area outside of modal is clicked
window.onclick = function (event) {
    if (event.target === MODAL_CONTAINER) {
        MODAL_CONTAINER.style.display = "none";
        MODAL_CONTENT.innerHTML = "";
    }
}

// functions for modal closing on button press
function closeFunction() {
    MODAL_CONTAINER.style.display = "none";
    window.location.reload();
}

function modalClose() {
    MODAL_CONTAINER.style.display = "none";
}