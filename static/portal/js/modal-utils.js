const updateForm = document.getElementById("update-form");
const modalContainer = document.getElementById("modal-container");


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


}

window.onclick = function (event) {
    if (event.target == modalContainer) {
        modalContainer.style.display = "none";
    }
}

let span = document.getElementById("close-button");

span.onclick = function () {
    modalContainer.style.display = "none";
}
