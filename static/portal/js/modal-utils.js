let genericForm = document.getElementById("generic-form");
let editForm = document.getElementById("edit-emp-form");
let modalContainer = document.getElementById("modal-container");
let modalContent = document.getElementById("modal-content");
const urlAddress = 'http://127.0.0.1:8000';

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
            //dataType: 'html',
            success: (data) => modalContent.innerHTML = data,
        },
    ).then(res=>{
          $('a#submitForm').on('click', e=>{
        e.preventDefault();
        e.stopPropagation();
        console.log('Link clicked')
              const mm = $("#edit-emp-form");
        $.ajax({
               url: urlAddress + '/employees/' + id + '/',
               type: 'post',
               dataType: 'html',
               data: mm.serialize(),
               success: function (data, textStatus, xhr) {
                   console.log(data, textStatus, xhr);
                   closeFunction();
                   pageReload();
               },
               error: function (data, xhr, textStatus) {
                   console.log("Status code edit: " + xhr.status);
               }
           },
       );
    })

    });


}

//onclick function for user deleting modal
function showUserDeleteModal(id) {
    modalContainer.style.display = "flex";
    $.ajax({
            url: urlAddress + '/employees/delete/' + id + '/',
            type: 'get',
            success: (data) => modalContent.innerHTML = data,
        },
    ).then(res=>{
        $("a#submitForm").on("click", (e) => {
        e.preventDefault();
        e.stopPropagation()
        const mm = $("#delete-emp-form");
        $.ajax({
                url: urlAddress + '/employees/delete/' + id + '/',
                type: 'POST',
                data: mm.serialize(),
                success:function(data){pageReload()},
            },

        );
        closeFunction();

    })

    });


}


//onclick function for user adding modal
function showUserAddModal() {
    modalContainer.style.display = "flex";
    $.ajax({
        url: urlAddress + '/employees/create/',
        type: 'get',
        dataType: 'html',
        success: (data) => modalContent.innerHTML = data,
    }).then(res=>{
        $("a#submitForm").on("click", (e) => {
        e.preventDefault();
        const mm = $("#create-emp-form");
        $.ajax({
            url: urlAddress + '/employees/create/',
            type: 'post',
            dataType: 'html',
            data: mm.serialize(),
            success: function (data, textStatus, xhr) {
                closeFunction();
                pageReload();
            },
            error: function (data, xhr, textStatus) {
                console.log("Status code: " + xhr.status);

            }
        });
    })

    })


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
    //window.open("http://127.0.0.1:8000/employees/", "_self");
}


//function that reloads to target page so that up-to-date results (post edit) can be shown
function pageReload() {
    console.log('nesto');
      setTimeout(() => {window.open("http://127.0.0.1:8000/employees/", "_self");}, 1000);

    //window.open("http://127.0.0.1:8000/employees/", "_self");
}
function log(obj){
    console.log(obj);
}
