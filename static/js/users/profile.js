
addImagePreview("id_profile_pic", "photo-preview" );
 console.log("Tu smo negde");

function addImagePreview(imageFeild_id, imagePreview_id) {
    document.getElementById(`${imageFeild_id}`).addEventListener("change", function (e) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById(`${imagePreview_id}`).src = e.target.result;
        };
        reader.readAsDataURL(this.files[0]);
    });
}