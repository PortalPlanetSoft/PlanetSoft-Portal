const modalContent = document.getElementById("modal-content");
const modalContainer = document.getElementById("modal-container");
const urlAddress = 'http://127.0.0.1:8000';

// error codes for displaying required fields and toast messages
const DEFAULT_TOAST = 200; // default message in the toast (empty - neutral)
const ERROR_ACTION = 0; // action not completed successfully
const SUCCESSFUL_ACTION = 1; // action completed successfully
const DELETE_SUCCESSFUL = 2; // delete action successful
const INVALID_EMAIL_ERROR = 3; // input email not valid
const INVALID_PHONE_ERROR = 4; // input phone number not valid
const INVALID_VPN_ERROR = 5; // input vpn number not valid
const INVALID_EMAIL_PHONE_VPN_ERROR = 6; // input email, phone and vpn number - all not valid
const INVALID_EMAILANDPHONE_ERROR = 7; // input email and phone not valid
const INVALID_EMAILANDVPN_ERROR = 8; // input email and vpn number not valid
const INVALID_PHONEANDVPN_ERROR = 9; // input phone and vpn number not valid

// validation codes to determine if validation was successful
const VALIDATION_SUCCESS = 111; // validation of all elements successful
const PHONE_INVALID = 101; // phone number format not correct
const VPN_INVALID = 110; // vpn number format not correct
const EMAIL_INVALID = 11; // email format not correct
const EMAIL_PHONE_INVALID = 12; // email and phone number format not correct
const EMAIL_VPN_INVALID = 13; // email and vpn number format not correct
const PHONE_VPN_INVALID = 14; // phone and vpn number format not correct
const PASSWORD_VALIDATION_FAIL = 15; // error that is triggered when new input password does not meet required format
const PASSWORDS_MATCHING_ERROR = 16; // error that is triggered if the new password is not the same in both fields
const FIELDS_EMPTY = 17; // error that is triggered if both new password fields are empty
const FIRST_FIELD_EMPTY = 18;
const SECOND_FIELD_EMPTY = 19;
const VALIDATION_FAIL = 0; // validation of all elements unsuccessful

let result = DEFAULT_TOAST;

// pageOnLoad function that fetches action result from sessionStorage so the toast alert can be shown
$(function () {
    result = sessionStorage.getItem("result");
    if (result == SUCCESSFUL_ACTION) {
        showToast(result);
        sessionStorage.clear();
    } else if (result == ERROR_ACTION) {
        showToast(result);
        sessionStorage.clear();
    } else if (result == DELETE_SUCCESSFUL) {
        showToast(result);
        sessionStorage.clear();
    } else {
        result = DEFAULT_TOAST;
        sessionStorage.clear();
    }
});

// onclick function for opening of password change modal
function showPasswordChangeModal() {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/password-change/',
            type: 'get',
            success: (data) => modalContent.innerHTML = data,
        },
    );
}

// function that submits user's password change request
function submitPasswordChangeForm() {
    let form = $("#password-change-form");

    let oldPassword = document.getElementById("id_old_password");
    let newPassword = document.getElementById("id_new_password1");
    let newPasswordCompare = document.getElementById("id_new_password2");

    let validationResult = passwordChangeValidation(oldPassword, newPassword, newPasswordCompare);

    if (validationResult == FIELDS_EMPTY) {
        oldPassword.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>These fields cannot be empty.</li></ul>");
        newPassword.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>These fields cannot be empty.</li></ul>");
        newPasswordCompare.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>These fields cannot be empty.</li></ul>");
        showToast(FIELDS_EMPTY);
    } else if (validationResult == FIRST_FIELD_EMPTY) {
        newPassword.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>This field cannot be empty.</li></ul>");
        showToast(FIRST_FIELD_EMPTY);
    } else if (validationResult == SECOND_FIELD_EMPTY) {
        newPasswordCompare.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>This field cannot be empty.</li></ul>");
        showToast(SECOND_FIELD_EMPTY);
    } else if (validationResult == VALIDATION_SUCCESS) {
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
                    sessionStorage.clear();
                    sessionStorage.setItem("result", ERROR_ACTION);
                    oldPassword.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Current password is not correct.</li></ul>");
                    showToast(ERROR_ACTION);
                    sessionStorage.clear();
                },
            },
        );
    } else if (validationResult == PASSWORD_VALIDATION_FAIL) {
        newPassword.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Password does not meet required format.</li></ul>");
        showToast(PASSWORD_VALIDATION_FAIL);// password not matching format
    } else if (validationResult == PASSWORDS_MATCHING_ERROR) {
        newPasswordCompare.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>These passwords must match.</li></ul>");
        showToast(PASSWORDS_MATCHING_ERROR);// first and second entry of new password not matching
    }
}

// function that validates the new password
function passwordChangeValidation(oldPassword, newPassword, newPasswordCompare) {
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/; // minimum eight characters, at least one letter and one number
    if (newPassword.value == "" && newPasswordCompare.value == "" && oldPassword.value == "") {
        return FIELDS_EMPTY;
    } else if (newPassword.value == "" && newPasswordCompare.value) {
        return FIRST_FIELD_EMPTY;
    } else if (newPassword.value && newPasswordCompare.value == "") {
        return SECOND_FIELD_EMPTY;
    } else {
        if (newPassword.value == newPasswordCompare.value) {
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

// onclick function for opening of user preview modal
function showUserPreviewModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/' + id + '/',
            type: 'get',
            success: (data) => modalContent.innerHTML = data,
        },
    );
}

// onclick function for opening of user edit modal
function showUserEditModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/' + id + '/',
            type: 'get',
            success: (data) => modalContent.innerHTML = data,
        },
    );
}

// function that submits user's edited data and displays error messages
function submitEditUserForm(id) {
    let form = $("#edit-emp-form");
    let emailAddress = document.getElementById("id_email");
    let phoneNumber = document.getElementById("id_phone");
    let vpnNumber = document.getElementById("id_business_phone");

    const returnResult = validatorFunction(emailAddress, phoneNumber, vpnNumber);
    if (returnResult == VALIDATION_SUCCESS) {
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
                    sessionStorage.clear();
                    sessionStorage.setItem("result", ERROR_ACTION);
                    showToast(ERROR_ACTION);
                    sessionStorage.clear();
                    modalContent.innerHTML = data.responseText;
                },
            },
        );
    } else {
        if (returnResult == EMAIL_INVALID) {
            emailAddress.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid email address.</li></ul>");
            showToast(INVALID_EMAIL_ERROR);
        } else if (returnResult == PHONE_INVALID) {
            phoneNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid phone number.</li></ul>");
            showToast(INVALID_PHONE_ERROR);
        } else if (returnResult == VPN_INVALID) {
            vpnNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid VPN number.</li></ul>");
            showToast(INVALID_VPN_ERROR);
        } else if (returnResult == EMAIL_PHONE_INVALID) {
            emailAddress.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid email address.</li></ul>");
            phoneNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid phone number.</li></ul>");
            showToast(INVALID_EMAILANDPHONE_ERROR);
        } else if (returnResult == EMAIL_VPN_INVALID) {
            emailAddress.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid email address.</li></ul>");
            vpnNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid VPN number.</li></ul>");
            showToast(INVALID_EMAILANDVPN_ERROR);
        } else if (returnResult == PHONE_VPN_INVALID) {
            phoneNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid phone number.</li></ul>");
            vpnNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid VPN number.</li></ul>");
            showToast(INVALID_PHONEANDVPN_ERROR);
        } else if (returnResult == VALIDATION_FAIL) {
            emailAddress.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid email address.</li></ul>");
            phoneNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid phone number.</li></ul>");
            vpnNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid VPN number.</li></ul>");
            showToast(INVALID_EMAIL_PHONE_VPN_ERROR);
        }
    }
}

// function used for validation of email address and phone number
function validatorFunction(emailAddress, phoneNumber, vpnNumber) {
    let regexMail = /^(([^<>()\\[\]\\.,;:\s@"]+(\.[^<>()\\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let regexNumber = /\+{0,1}\d{9,13}/;
    let regexVpnNumber = /\+{0,1}\d{1,13}/;
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

// onclick function for opening of user delete modal
function showUserDeleteModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/delete/' + id + '/',
            type: 'get',
            success: (data) => modalContent.innerHTML = data,
        },
    );
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
                sessionStorage.clear();
                sessionStorage.setItem("result", ERROR_ACTION);
                showToast(ERROR_ACTION);
                sessionStorage.clear();
                modalContent.innerHTML = data.responseText;
            },
        },
    );
}

// onclick function for opening of user add modal
function showUserAddModal() {
    modalContainer.style.display = "flex";
    $.ajax({
        url: urlAddress + '/employees/create/',
        type: 'get',
        dataType: 'html',
        success: (data) => modalContent.innerHTML = data,
    });
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
            sessionStorage.clear();
            sessionStorage.setItem("result", SUCCESSFUL_ACTION);
            closeFunction();
            pageReload();
        },
        error: function (data, xhr, textStatus) {
            sessionStorage.clear();
            sessionStorage.setItem("result", ERROR_ACTION);
            showToast(ERROR_ACTION);
            sessionStorage.clear();
            modalContent.innerHTML = data.responseText;
        },
    });
}

// function for opening news add modal
function showNewsAddModal() {
    $.ajax({
        url: urlAddress + '/news/create/',
        type: 'get',
        dataType: 'html',
        success: (data) => {
            modalContent.innerHTML = data;
            modalContainer.style.display = "flex";
        },
    });
}

// function that submits newly created news article
function submitNewsAddForm() {
    let formData = new FormData($("#create-news-form")[0]);
    $.ajax({
        url: urlAddress + '/news/create/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function (data, textStatus, xhr) {
            sessionStorage.clear();
            sessionStorage.setItem("result", SUCCESSFUL_ACTION);
            closeFunction();
            pageReload();
        },
        error: function (data, xhr, textStatus) {
            sessionStorage.clear();
            sessionStorage.setItem("result", ERROR_ACTION);
            showToast(ERROR_ACTION);
            sessionStorage.clear();
        },
    });
}

// onclick function for opening of news edit modal
function showNewsEditModal(id) {
    $.ajax({
            url: urlAddress + '/news/' + id + '/',
            type: 'get',
            success: (data) => {
                modalContent.innerHTML = data;
                modalContainer.style.display = "flex";
            },
        },
    );
}

// function that submits edited article data
function submitNewsEditForm(id) {
    let formData = new FormData($("#edit-news-form")[0]);
    $.ajax({
        url: urlAddress + '/news/' + id + '/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function (data, textStatus, xhr) {
            sessionStorage.clear();
            sessionStorage.setItem("result", SUCCESSFUL_ACTION);
            closeFunction();
            pageReload();
        },
        error: function (data, xhr, textStatus) {
            sessionStorage.clear();
            sessionStorage.setItem("result", ERROR_ACTION);
            showToast(ERROR_ACTION);
            sessionStorage.clear();
        },
    });
}

// onclick function for opening of news delete modal
function showNewsDeleteModal(id) {
    $.ajax({
            url: urlAddress + '/news/delete/' + id + '/',
            type: 'get',
            success: (data) => {
                modalContent.innerHTML = data;
                modalContainer.style.display = "flex";
            },
        },
    );
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
                sessionStorage.clear();
                sessionStorage.setItem("result", ERROR_ACTION);
                showToast(ERROR_ACTION);
                sessionStorage.clear();
            },
        },
    );
}

// toast message that is displayed every time a successful/unsuccessful change is made
function showToast(result) {
    const toastContainer = document.getElementById("toast-container");
    const toastMessage = document.getElementById("toast-message");
    if (result == SUCCESSFUL_ACTION) {
        toastMessage.innerHTML = "Uspješno sačuvano!";
    } else if (result == ERROR_ACTION) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Neuspješno!";
    } else if (result == DELETE_SUCCESSFUL) {
        toastMessage.innerHTML = "Uspješno obrisano!";
    } else if (result == INVALID_EMAIL_ERROR) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format e-mail adrese!";
    } else if (result == INVALID_PHONE_ERROR) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format broja telefona!";
    } else if (result == INVALID_VPN_ERROR) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format VPN telefona!";
    } else if (result == INVALID_EMAILANDPHONE_ERROR) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format email adrese i broja telefona!";
    } else if (result == INVALID_EMAILANDVPN_ERROR) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format email adrese i VPN telefona!";
    } else if (result == INVALID_PHONEANDVPN_ERROR) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format broja privatnog i VPN telefona!";
    } else if (result == INVALID_EMAIL_PHONE_VPN_ERROR) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format e-mail adrese kao i privatnog i VPN broja telefona!";
    } else if (result == PASSWORD_VALIDATION_FAIL) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite šifru u odgovarajućem formatu!";
    } else if (result == PASSWORDS_MATCHING_ERROR) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite istu šifru u oba polja!";
    } else if (result == FIELDS_EMPTY) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Polja ne mogu biti prazna!";
    } else if (result == FIRST_FIELD_EMPTY) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Polje ne moze biti prazno!";
    } else if (result == SECOND_FIELD_EMPTY) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Polje ne moze biti prazno!";
    }
    toastContainer.className = "show";
    setTimeout(function () {
        toastContainer.className = toastContainer.className.replace("show", "");
    }, 3000);
}

// function that closes the modal if area outside of modal is clicked
window.onclick = function (event) {
    if (event.target == modalContainer) {
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

// function that reloads to target page so that up-to-date results (post edit) can be shown
function pageReload() {
    window.location.reload();
}

function log(obj) {
    console.log(obj);
}

function submitFilterForm() {
    document.forms["userFilterForm"].submit();
}
