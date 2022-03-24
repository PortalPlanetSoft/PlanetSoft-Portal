"use strict"
// toast message that is displayed every time a successful/unsuccessful change is made
function showToast(message, type) {
    const toastContainer = document.getElementById("toast-container");
    const toastMessage = document.getElementById("toast-message");
    switch (type) {
        case ERROR_ACTION:
            toastContainer.style.backgroundColor = "var(--alert-light)";
        default:
            toastMessage.innerHTML = message;
            break;
    }
    toastContainer.className = "show";
    setTimeout(function () {
        toastContainer.className = toastContainer.className.replace("show", "");
    }, 3000);
}