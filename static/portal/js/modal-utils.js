let genericForm = document.getElementById("generic-form");
let modalContainer = document.getElementById("modal-container");
let urladdress = 'http://127.0.0.1:8000';

$(function () {
    $.ajaxSetup({})
});

function showUserEditModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urladdress + '/employees/' + id + '/',
            type: 'get',
            dataType: 'html',
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
    })
}

function showUserDeleteModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urladdress + '/employees/delete/' + id + '/',
            type: 'get',
            dataType: 'html',
            success: (data) => genericForm.innerHTML = data,
        },
    );
    console.log(id);

    $("#general-form").on("submit", (e) => {
        $.ajax({
            url: urladdress + '/employees/delete/' + id + '/',
            headers: {
                "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
            },
            method: "POST",
            dataType: 'JSON',
            success: function (data) {
                console.log(data);
            }
        })
    })
}

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
            },
        );
    })
}

window.onclick = function (event) {
    if (event.target == modalContainer) {
        modalContainer.style.display = "none";
    }
}


