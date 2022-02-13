const updateForm = document.getElementById("update-form");
const modalContainer = document.getElementById("modal-container");

let span = document.getElementsByClassName("close-button")[0];

function showUserEditModal(id) {
    console.log(id);
    $.ajax({
            url: 'http://127.0.0.1:8000/employees/' + id + '/',
            type: 'get',
            dataType: 'html',
            success: (data) => updateForm.innerHTML = data,
        },
    );
    modalContainer.style.display = "flex";

    $("#update-form").on("submit", (e) => {
        e.preventDefault();
        const mm = $("#update-form");
        $.ajax({
                url: 'http://127.0.0.1:8000/employees/' + id + '/',
                type: 'post',
                dataType: 'html',
                data: mm.serialize(),
            },
        );
    })

    span.onclick = function () {
        modalContainer.style.display = "none";
    }
}

