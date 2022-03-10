const modalContent = document.getElementById("modal-content");
const modalContainer = document.getElementById("modal-container");
const urlAddress = 'http://127.0.0.1:8000';

const DEFAULT_TOAST = 6;
const ERROR_ACTION = 0;
const SUCCESSFUL_ACTION = 1;
const DELETE_SUCCESSFUL = 2;
// const INVALID_EMAIL_ERROR = ;
// const INVALID_PHONE_ERROR = ;

let result = DEFAULT_TOAST;

//pageOnLoad function that fetches action result from sessionStorage so the toast alert can be shown
$(function () {
    result = sessionStorage.getItem("result");
    if (result == SUCCESSFUL_ACTION) {
        showToast(1);
        sessionStorage.clear();
    } else if (result == ERROR_ACTION) {
        showToast(0);
        sessionStorage.clear();
    } else if (result == DELETE_SUCCESSFUL) {
        showToast(2);
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
            url: urlAddress + '/employees/' + id + '/',
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
            success: (data) => {
                console.log(data);
                modalContent.innerHTML = data
            },
            error : () => {
                console.log("neradi");
            }
        },
    );
}

//function that submits user's edited data
function submitEditUserForm(id) {
    let form = $("#edit-emp-form");
    let phoneNumber = document.getElementById("id_phone");
    let emailAddress = document.getElementById("id_email");

    let returnResult = validatorFunction(phoneNumber, emailAddress);

    if (returnResult == 11) {
        $.ajax({
                url: urlAddress + '/employees/' + id + '/',
                type: 'post',
                dataType: 'html',
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
                    modalContent.innerHTML = data.responseText;
                },
            },
        );
    } else {
        if (returnResult == 1) {
            emailAddress.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid email address.</li></ul>");
            showToast(3);
        } else if (returnResult == 10) {
            phoneNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid phone number.</li></ul>");
            showToast(4);
        } else {
            emailAddress.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid email address.</li></ul>");
            phoneNumber.insertAdjacentHTML("afterend", "<ul class=\"errorlist\"><li>Please enter a valid phone number.</li></ul>");
            showToast(5);
        }
    }
}

//function used for validation of email address and phone number
function validatorFunction(phoneNumber, emailAddress) {
    let regexNumber = /\+{0,1}\d{9,13}/;
    let regexMail = /^(([^<>()\\[\]\\.,;:\s@"]+(\.[^<>()\\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let emailValid = emailAddress.value.match(regexMail);
    let phoneValid = phoneNumber.value.match(regexNumber);
    let returnResult;
    if (emailValid && phoneValid) {
        returnResult = 11;
    } else if (emailValid && phoneValid == null) {
        returnResult = 10;
    } else if (emailValid == null && phoneValid) {
        returnResult = 1;
    } else {
        returnResult = 0;
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

//function that deletes user's data
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
                x
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
    if (result == 1) {
        toastMessage.innerHTML = "Uspješno sačuvano!";
    } else if (result == 0) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Neuspješno!";
    } else if (result == 2) {
        toastMessage.innerHTML = "Uspješno obrisano!";
    } else if (result == 3) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format e-mail adrese!";
    } else if (result == 4) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format broja telefona!";
    } else if (result == 5) {
        toastContainer.style.backgroundColor = "var(--alert-light)";
        toastMessage.innerHTML = "Molimo vas unesite ispravan format e-mail adrese i broja telefona!";
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
