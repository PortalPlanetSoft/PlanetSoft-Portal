// function for displaying generic modal
function displayModal(targetUrlAddress) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: targetUrlAddress,
            type: 'get',
            success: (data) => modalContent.innerHTML = data,
        },
    );
}

// onclick function for opening of password change modal
function showPasswordChangeModal() {
    displayModal(passwordChangeUrl);
}

// onclick function for opening of user preview modal
function showUserPreviewModal(id) {
    displayModal(viewUserUrl + id + '/');
}

// onclick function for opening of user edit modal
function showUserEditModal(id) {
    displayModal(viewUserUrl + id + '/');
}

// onclick function for opening of user delete modal
function showUserDeleteModal(id) {
    displayModal(deleteUserUrl + id + '/');
}

// onclick function for opening of user add modal
function showUserAddModal() {
    displayModal(addUserUrl);
}

// onclick function for opening of news delete modal
function showNewsDeleteModal(id) {
    displayModal(deleteNewsUrl + id + '/');
}

// function for opening news add modal
function showNewsAddModal() {
    displayModal(addNewsUrl);
}

// onclick function for opening of news edit modal
function showNewsEditModal(id) {
    displayModal(editNewsUrl + id + '/');
}

// onclick function for opening news preview modal
function showNewsPreviewModal(id) {
    displayModal(viewNewsUrl + id);
}

// function that submits user's password change request
function submitPasswordChangeForm() {
    let form = $("#password-change-form");

    let oldPassword = document.getElementById("id_old_password");
    let newPassword = document.getElementById("id_new_password1");
    let newPasswordCompare = document.getElementById("id_new_password2");

    let validationResult = passwordChangeValidation(oldPassword, newPassword, newPasswordCompare);

    switch (validationResult) {
        case FIELDS_EMPTY:
            oldPasswordValidationError(oldPassword);
            newPasswordValidationError(newPassword);
            newPasswordCompareValidationError(newPasswordCompare);
            showToast(FIELDS_EMPTY);
            break;
        case FIRST_FIELD_EMPTY:
            newPasswordValidationError(newPassword);
            showToast(FIRST_FIELD_EMPTY);
            break;
        case SECOND_FIELD_EMPTY:
            newPasswordCompareValidationError(newPasswordCompare);
            showToast(SECOND_FIELD_EMPTY);
            break;
        case PASSWORD_VALIDATION_FAIL:
            newPassword.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Šifra ne odgovara zahtijevanom formatu (najmanje 8 znakova, velika i mala slova, kao i brojevi.</li></ul>");
            showToast(PASSWORD_VALIDATION_FAIL);// password not matching format
            break;
        case PASSWORDS_MATCHING_ERROR:
            newPasswordCompare.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Lozinke moraju biti jednake.</li></ul>");
            showToast(PASSWORDS_MATCHING_ERROR);// first and second entry of new password not matching
            break;
        default:
            $.ajax({
                    url: urlAddress + '/employees/password-change/',
                    type: 'POST',
                    data: form.serialize(),
                    success: function (data, textStatus, xhr) {
                        sessionStorage.clear();
                        sessionStorage.setItem("result", SUCCESSFUL_ACTION);
                        closeFunction();
                    },
                    error: function (data, xhr, textStatus) {
                        requestUnsuccessful();
                        oldPassword.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Trenutka lozinka nije ispravna.</li></ul>");
                    },
                },
            );
            break;
    }
}

// function that validates the new password
function passwordChangeValidation(oldPassword, newPassword, newPasswordCompare) {
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/; // minimum eight characters, at least one letter and one number
    if (newPassword.value === "" && newPasswordCompare.value === "" && oldPassword.value === "") {
        return FIELDS_EMPTY;
    } else if (newPassword.value === "" && newPasswordCompare.value) {
        return FIRST_FIELD_EMPTY;
    } else if (newPassword.value && newPasswordCompare.value === "") {
        return SECOND_FIELD_EMPTY;
    } else {
        if (newPassword.value === newPasswordCompare.value) {
            let passwordValid = newPassword.value.match(passwordRegex);
            if (passwordValid) {
                return VALIDATION_SUCCESS;
            } else {
                return PASSWORD_VALIDATION_FAIL;
            }
        } else {
            return PASSWORDS_MATCHING_ERROR;
        }
    }
}

// function that submits user's edited data and displays error messages
function submitEditUserForm(id) {
    let form = $("#edit-emp-form");

    let emailAddress = document.getElementById("id_email");
    let phoneNumber = document.getElementById("id_phone");
    let vpnNumber = document.getElementById("id_business_phone");

    let returnResult = validatorFunction(emailAddress, phoneNumber, vpnNumber);

    switch (returnResult) {
        case EMAIL_INVALID:
            emailValidationInvalidError(emailAddress);
            showToast(INVALID_EMAIL_ERROR);
            break;
        case PHONE_INVALID:
            phoneValidationInvalidError(phoneNumber);
            showToast(INVALID_PHONE_ERROR);
            break;
        case VPN_INVALID:
            vpnPhoneValidationInvalidError(vpnNumber);
            showToast(INVALID_VPN_ERROR);
            break;
        case EMAIL_PHONE_INVALID:
            emailValidationInvalidError(emailAddress);
            phoneValidationInvalidError(phoneNumber);
            showToast(INVALID_EMAILANDPHONE_ERROR);
            break;
        case EMAIL_VPN_INVALID:
            emailValidationInvalidError(emailAddress);
            vpnPhoneValidationInvalidError(vpnNumber);
            showToast(INVALID_EMAILANDVPN_ERROR);
            break;
        case PHONE_VPN_INVALID:
            phoneValidationInvalidError(phoneNumber);
            vpnPhoneValidationInvalidError(vpnNumber);
            showToast(INVALID_PHONEANDVPN_ERROR);
            break;
        case VALIDATION_FAIL:
            emailValidationInvalidError(emailAddress);
            phoneValidationInvalidError(phoneNumber);
            vpnPhoneValidationInvalidError(vpnNumber);
            showToast(INVALID_EMAIL_PHONE_VPN_ERROR);
            break;
        default:
            $.ajax({
                    url: urlAddress + '/employees/' + id + '/',
                    type: 'POST',
                    dataType: 'html',
                    data: form.serialize(),
                    success: function (data, textStatus, xhr) {
                        sessionStorage.clear();
                        sessionStorage.setItem("result", SUCCESSFUL_ACTION);
                        closeFunction();
                    },
                    error: function (data, xhr, textStatus) {
                        requestUnsuccessful();
                        modalContent.innerHTML = data.responseText;
                    },
                },
            );
            break;
    }
}

function emailValidationInvalidError(emailAddress) {
    emailAddress.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Molimo Vas da unesete odgovarajuću email adresu.</li></ul>");
}

function phoneValidationInvalidError(phoneNumber) {
    phoneNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Molimo Vas unesite ispravan broj telefona.</li></ul>");
}

function vpnPhoneValidationInvalidError(vpnNumber) {
    vpnNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Molimo Vas unesite ispravan broj VPN telefona.</li></ul>");
}

function oldPasswordValidationError(oldPassword) {
    oldPassword.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Ovo polje ne može biti prazno.</li></ul>");
}

function newPasswordValidationError(newPassword) {
    newPassword.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Ovo polje ne može biti prazno.</li></ul>");
}

function newPasswordCompareValidationError(newPasswordCompare) {
    newPasswordCompare.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Ovo polje ne može biti prazno.</li></ul>");
}

// function used for validation of email address and phone number
function validatorFunction(emailAddress, phoneNumber, vpnNumber) {
    let regexMail = /^(([^<>()\\[\]\\.,;:\s@"]+(\.[^<>()\\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let regexNumber = /^(\+387|00387|0)(66|65|61)[0-9]{6}$/;
    let regexVpnNumber = /^[0-9]{3}$/;
    let emailValid = emailAddress.value.match(regexMail);
    let phoneValid = phoneNumber.value.match(regexNumber);
    let vpnValid = vpnNumber.value.match(regexVpnNumber);
    let returnResult;

    if (emailValid && phoneValid && vpnValid) {
        returnResult = VALIDATION_SUCCESS;
    } else if (emailValid == null && phoneValid && vpnValid) {
        returnResult = EMAIL_INVALID;
    } else if (emailValid && phoneValid == null && vpnValid) {
        returnResult = PHONE_INVALID;
    } else if (emailValid && phoneValid && vpnValid == null) {
        returnResult = VPN_INVALID;
    } else if (emailValid == null && phoneValid == null && vpnValid) {
        returnResult = EMAIL_PHONE_INVALID;
    } else if (emailValid == null && phoneValid && vpnValid == null) {
        returnResult = EMAIL_VPN_INVALID;
    } else if (emailValid && phoneValid == null && vpnValid == null) {
        returnResult = PHONE_VPN_INVALID;
    } else {
        returnResult = VALIDATION_FAIL;
    }
    return returnResult;
}

// function that deletes the user
function submitUserDeleteForm(id) {
    let form = $("#delete-emp-form");
    $.ajax({
            url: urlAddress + '/employees/delete/' + id + '/',
            type: 'POST',
            data: form.serialize(),
            success: function (data, textStatus, xhr) {
                sessionStorage.clear();
                sessionStorage.setItem("result", DELETE_SUCCESSFUL);
                closeFunction();
                pageReload();
            },
            error: function (data, xhr, textStatus) {
                requestUnsuccessful();
                modalContent.innerHTML = data.responseText;
            },
        },
    );
}

// function that submits newly created user's data
function submitCreateUserForm() {
    let form = $("#create-emp-form");
    $.ajax({
        url: urlAddress + '/employees/create/',
        type: 'post',
        dataType: 'html',
        data: form.serialize(),
        success: function (data, textStatus, xhr) {
            requestSuccessful();
        },
        error: function (data, xhr, textStatus) {
            requestUnsuccessful();
            modalContent.innerHTML = data.responseText;
        },
    });
}

function submitFormMultimediaData(targetUrlAddress, formData) {
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

// function that submits newly created news article
function submitNewsAddForm() {
    let formData = new FormData($("#create-news-form")[0]);
    submitFormMultimediaData(addNewsUrl, formData);
}

// function that submits edited article data
function submitNewsEditForm(id) {
    let formData = new FormData($("#edit-news-form")[0]);
    submitFormMultimediaData(editNewsUrl + id + '/', formData);
}

// function that deletes selected article
function submitNewsDeleteForm(id) {
    let form = $("#delete-news-form");
    $.ajax({
            url: urlAddress + '/news/delete/' + id + '/',
            type: 'POST',
            data: form.serialize(),
            success: function (data, textStatus, xhr) {
                sessionStorage.clear();
                sessionStorage.setItem("result", DELETE_SUCCESSFUL);
                closeFunction();
                pageReload();
            },
            error: function (data, xhr, textStatus) {
                requestUnsuccessful();
            },
        },
    );
}

function requestSuccessful() {
    sessionStorage.clear();
    sessionStorage.setItem("result", SUCCESSFUL_ACTION);
    closeFunction();
    pageReload();
}

function requestUnsuccessful() {
    sessionStorage.clear();
    sessionStorage.setItem("result", ERROR_ACTION);
    showToast(ERROR_ACTION);
    sessionStorage.clear();
}

// function that closes the modal if area outside of modal is clicked
window.onclick = function (event) {
    if (event.target === modalContainer) {
        modalContainer.style.display = "none";
        modalContent.innerHTML = "";
    }
}

// functions for modal closing on button press
function closeFunction() {
    modalContainer.style.display = "none";
    window.location.reload();
}

function modalClose() {
    modalContainer.style.display = "none";
}