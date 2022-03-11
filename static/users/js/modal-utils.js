const modalContent = document.getElementById("modal-content");
const modalContainer = document.getElementById("modal-container");
const urlAddress = 'http://127.0.0.1:8000';

const DEFAULT_TOAST = 200;
const ERROR_ACTION = 0;
const SUCCESSFUL_ACTION = 1;
const DELETE_SUCCESSFUL = 2;
const INVALID_EMAIL_ERROR = 3;
const INVALID_PHONE_ERROR = 4;
const INVALID_VPN_ERROR = 5;
const INVALID_EMAIL_PHONE_VPN_ERROR = 6;

const VALIDATION_SUCCESS = 111;
const PHONE_INVALID = 101;
const VPN_INVALID = 110;
const EMAIL_INVALID = 11;
const VALIDATION_FAIL = 0;

let result = DEFAULT_TOAST;

//pageOnLoad function that fetches action result from sessionStorage so the toast alert can be shown
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

//onclick function for opening of password change modal
function showPasswordChangeModal() {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/password-change/',
            type: 'get',
            success: (data) => modalContent.innerHTML = data,
        },
    );
}

//function that submits user's password change request
function submitPasswordChangeForm() {
    let form = $("#password-change-form");
    $.ajax({
            url: urlAddress + '/password-change/',
            type: 'POST',
            data: form.serialize(),
            success: function (data, textStatus, xhr) {
                sessionStorage.clear();
                sessionStorage.setItem("result", 1);
                closeFunction();
            },
            error: function (data, xhr, textStatus) {
                sessionStorage.clear();
                sessionStorage.setItem("result", 0);
                showToast(0);
                sessionStorage.clear();
            },
        },
    );
}

//onclick function for opening of user preview modal
function showUserPreviewModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/preview/' + id + '/',
            type: 'get',
            success: (data) => modalContent.innerHTML = data,
        },
    );
}

//onclick function for opening of user edit modal
function showUserEditModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/' + id + '/',
            type: 'get',
            success: (data) => modalContent.innerHTML = data,
        },
    );
}

//function that submits user's edited data
function submitEditUserForm(id) {
    let form = $("#edit-emp-form");
    let emailAddress = document.getElementById("id_email");
    let phoneNumber = document.getElementById("id_phone");
    let vpnNumber = document.getElementById("id_business_phone");

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
                console.log(data);
                sessionStorage.clear();
                sessionStorage.setItem("result", ERROR_ACTION);
                showToast(ERROR_ACTION);
                sessionStorage.clear();
                modalContent.innerHTML = data.responseText;
            },
        },
    );

    // const returnResult = validatorFunction(emailAddress, phoneNumber, vpnNumber);
    // if (returnResult === VALIDATION_SUCCESS) {
    //     $.ajax({
    //             url: urlAddress + '/employees/' + id + '/',
    //             type: 'POST',
    //             dataType: 'html',
    //             data: form.serialize(),
    //             success: function (data, textStatus, xhr) {
    //                 sessionStorage.clear();
    //                 sessionStorage.setItem("result", SUCCESSFUL_ACTION);
    //                 closeFunction();
    //             },
    //             error: function (data, xhr, textStatus) {
    //                 console.log(data);
    //                 sessionStorage.clear();
    //                 sessionStorage.setItem("result", ERROR_ACTION);
    //                 showToast(ERROR_ACTION);
    //                 sessionStorage.clear();
    //                 modalContent.innerHTML = data.responseText;
    //             },
    //         },
    //     );
    // } else {
    //     if (returnResult === 1) {
    //         emailAddress.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid email address.</li></ul>");
    //         showToast(INVALID_EMAIL_ERROR);
    //     } else if (returnResult === PHONE_INVALID) {
    //         phoneNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid phone number.</li></ul>");
    //         showToast(INVALID_PHONE_ERROR);
    //     } else if (returnResult === VPN_INVALID) {
    //         vpnNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid VPN number.</li></ul>");
    //         showToast(INVALID_VPN_ERROR);
    //     } else if (returnResult === VALIDATION_FAIL) {
    //         emailAddress.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid email address.</li></ul>");
    //         phoneNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid phone number.</li></ul>");
    //         vpnNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid VPN number.</li></ul>");
    //         showToast(INVALID_EMAIL_PHONE_VPN_ERROR);
    //     }
    // }
}

//function used for validation of email address and phone number
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
        alert("top");
    } else if (emailValid == null && phoneValid && vpnValid) {
        returnResult = EMAIL_INVALID;
        alert("mail");
    } else if (emailValid && phoneValid == null && vpnValid) {
        returnResult = PHONE_INVALID;
        alert("tel");
    } else if (emailValid && phoneValid && vpnValid == null) {
        returnResult = VPN_INVALID;
        alert("vpn");
    } else {
        returnResult = VALIDATION_FAIL;
        alert("sve");
    }
    return returnResult;
}

//onclick function for opening of user delete modal
function showUserDeleteModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/delete/' + id + '/',
            type: 'get',
            success: (data) => modalContent.innerHTML = data,
        },
    );
}

//function that deletes the user
function submitUserDeleteForm(id) {
    let form = $("#delete-emp-form");
    $.ajax({
            url: urlAddress + '/employees/delete/' + id + '/',
            type: 'POST',
            data: form.serialize(),
            success: function (data, textStatus, xhr) {
                sessionStorage.clear();
                sessionStorage.setItem("result", 2);
                closeFunction();
                pageReload();
            },
            error: function (data, xhr, textStatus) {
                sessionStorage.clear();
                sessionStorage.setItem("result", 0);
                showToast(0);
                sessionStorage.clear();
                modalContent.innerHTML = data.responseText;
            },
        },
    );
}

//onclick function for opening of user add modal
function showUserAddModal() {
    modalContainer.style.display = "flex";
    $.ajax({
        url: urlAddress + '/employees/create/',
        type: 'get',
        dataType: 'html',
        success: (data) => modalContent.innerHTML = data,
    });
}

//function that submits newly created user's data
function submitCreateUserForm() {
    let form = $("#create-emp-form");
    $.ajax({
        url: urlAddress + '/employees/create/',
        type: 'post',
        dataType: 'html',
        data: form.serialize(),
        success: function (data, textStatus, xhr) {
            sessionStorage.clear();
            sessionStorage.setItem("result", 1);
            closeFunction();
            pageReload();
        },
        error: function (data, xhr, textStatus) {
            sessionStorage.clear();
            sessionStorage.setItem("result", 0);
            showToast(0);
            sessionStorage.clear();
            modalContent.innerHTML = data.responseText;
        },
    });
}

//toast message that is displayed every time a successful/unsuccessful change is made
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
    } else if (result == INVALID_EMAIL_PHONE_VPN_ERROR) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format e-mail adrese kao i privatnog i VPN broja telefona!";
    }
    toastContainer.className = "show";
    setTimeout(function () {
        toastContainer.className = toastContainer.className.replace("show", "");
    }, 3000);
}


//function that closes the modal if area outside of modal is clicked
window.onclick = function (event) {
    if (event.target == modalContainer) {
        modalContainer.style.display = "none";
    }
}

//function for modal closing on button press
function closeFunction() {
    modalContainer.style.display = "none";
    window.location.reload();
}

function modalClose() {
    modalContainer.style.display = "none";
}


//function that reloads to target page so that up-to-date results (post edit) can be shown
function pageReload() {
    window.location.reload();
}

function log(obj) {
    console.log(obj);
}

function submitFilterForm() {
    document.forms["userFilterForm"].submit();
}
