function commentTyped(id){

    let commentIcon = document.querySelector(`#news-comment-icon${id}`)
    let commentInput = document.querySelector(`#news-comment-input${id}`)
    console.log(commentInput.value, commentIcon, id)
    if(commentInput.value.length > 0) {
            commentIcon.style.visibility = "visible";
            window.innerWidth > 1200 ?
            commentInput.style.height = "16px":
            commentInput.style.height = "40px"
            commentInput.style.height = (commentInput.scrollHeight-16) + "px";
        }
        else {
            window.innerWidth > 1200 ?
            commentInput.style.height = "16px":
            commentInput.style.height = "40px"
            commentIcon.style.visibility = "hidden";
        }
}