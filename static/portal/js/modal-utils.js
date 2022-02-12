const modalContainer = document.getElementById("modal-container");

function showUserEditModal(id){
    console.log(id);
    $.ajax({
        url:'http://127.0.0.1:8000/employees/'+id,
        type:'get',
        dataType:'html',
        success: (data) => modalContainer.innerHTML=data
        },
    );
    modalContainer.style.display = "flex";
    // window.location.replace('http://127.0.0.1:8000/employees/'+id);
    // modalContainer.innerHTML="testtest1223";
}
