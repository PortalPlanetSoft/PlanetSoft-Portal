const genericForm = document.getElementById("generic-form");
const modalContainer = document.getElementById("modal-container");
const urlAddress = 'http://127.0.0.1:8000';
let result = 3;

//pageOnLoad function that fetches action result from sessionStorage so the toast alert can be shown
$(function () {
    result = sessionStorage.getItem("result");
    if (result == 1) {
        showToast(1);
        sessionStorage.clear();
    } else if (result == 0) {
        showToast(0);
        sessionStorage.clear();
    } else if (result == 2) {
        showToast(2);
        sessionStorage.clear();
    } else {
        result = 3;
        sessionStorage.clear();
    }
});

//pageOnLoad function that creates timeout so edited data can be loaded
window.onload = function () {
    genericForm.onsubmit = setTimeout(function () {
    }, 10);
}

//onclick function for user editing modal
function showUserEditModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/' + id + '/',
            type: 'get',
            success: (data) => genericForm.innerHTML = data,
        },
    );

    $("#generic-form").on("submit", (e) => {
        e.preventDefault();
        const mm = $("#generic-form");
        $.ajax({
                url: urlAddress + '/employees/' + id + '/',
                type: 'post',
                dataType: 'html',
                data: mm.serialize(),
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
    })
}

//onclick function for user deleting modal
function showUserDeleteModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/delete/' + id + '/',
            type: 'get',
            success: (data) => genericForm.innerHTML = data,
        },
    );

    $("#generic-form").on("submit", (e) => {
        e.preventDefault();
        const mm = $("#generic-form");
        $.ajax({
                url: urlAddress + '/employees/delete/' + id + '/',
                type: 'POST',
                data: mm.serialize(),
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
                },
            },
        );
    })
}


//onclick function for user adding modal
function showUserAddModal() {
    modalContainer.style.display = "flex";
    $.ajax({
        url: urlAddress + '/employees/create/',
        type: 'get',
        dataType: 'html',
        success: (data) => genericForm.innerHTML = data,
    })

    $("#generic-form").on("submit", (e) => {
        e.preventDefault();
        const mm = $("#generic-form");
        $.ajax({
            url: urlAddress + '/employees/create/',
            type: 'post',
            dataType: 'html',
            data: mm.serialize(),
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
            },
        });
    })
}

//toast message that is displayed every time a successful/unsuccessful change is made
function showToast(result) {
    const toastContainer = document.getElementById("toast-container");
    const toastMessage = document.getElementById("toast-message");
    if (result == 1) {
        toastMessage.innerHTML = "Uspješno sačuvano!";
    } else if (result == 0) {
        toastMessage.innerHTML = "Neuspješno!";
    } else if (result == 2) {
        toastMessage.innerHTML = "Uspješno obrisano!";
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
};


//function that reloads to target page so that up-to-date results (post edit) can be shown
function pageReload() {
    window.location.reload();
}

