let genericForm = document.getElementById("generic-form");
let modalContainer = document.getElementById("modal-container");
let urladdress = 'http://127.0.0.1:8000';

window.onload = function () {
    genericForm.onsubmit = setTimeout(function () {
    }, 10);
}

//onclick function for user editing modal
function showUserEditModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urladdress + '/employees/' + id + '/',
            type: 'get',
            //dataType: 'html',
            success: (data) => genericForm.innerHTML = data,
        },
    );

    $("#generic-form").on("submit", (e) => {
        e.preventDefault();
        const mm = $("#generic-form");
        $.ajax({
                url: urladdress + '/employees/' + id + '/',
                type: 'post',
                dataType: 'html',
                data: mm.serialize(),
            },
        );
        closeFunction();
        pageReload();
    })
}

//onclick function for user deleting modal
function showUserDeleteModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urladdress + '/employees/delete/' + id + '/',
            type: 'get',
            success: (data) => genericForm.innerHTML = data,
        },
    );

    $("#generic-form").on("submit", (e) => {
        e.preventDefault();
        const mm = $("#generic-form");
        $.ajax({
                url: urladdress + '/employees/delete/' + id + '/',
                type: 'POST',
                data: mm.serialize(),
            },
        );
        closeFunction();
        pageReload();
    })
}


//onclick function for user adding modal
function showUserAddModal() {
    modalContainer.style.display = "flex";
    $.ajax({
        url: urladdress + '/employees/create/',
        type: 'get',
        dataType: 'html',
        success: (data) => genericForm.innerHTML = data,
    })

    $("#generic-form").on("submit", (e) => {
        e.preventDefault();
        const mm = $("#generic-form");
        $.ajax({
            url: urladdress + '/employees/create/',
            type: 'post',
            dataType: 'html',
            data: mm.serialize(),
            success: function (data, textStatus, xhr) {
                alert("Status code: " + xhr.status);
            },
            error: function (data,xhr, textStatus) {
                alert("Status code: " + xhr.status);
            }
        });
    })
}

//function that closes the modal if area outside of modal is clicked
window.onclick = function (event) {
    if (event.target == modalContainer) {
        modalContainer.style.display = "none";
    }
}

/*function for modal closing on button press
function closeFunction() {
    modalContainer.style.display = "none";
    //window.open("http://127.0.0.1:8000/employees/", "_self");
}

*/
///function that reloads to target page so that up-to-date results (post edit) can be shown
/*function pageReload() {
    window.open("http://127.0.0.1:8000/employees/", "_self");
}*/

