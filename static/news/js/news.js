const newsCommentInput = document.querySelector("#news-comment-input");
const commentIcon = document.querySelector("#comment-icon");

if(newsCommentInput!== undefined) {
    newsCommentInput.addEventListener('input', () => {
        if(newsCommentInput.value.length > 0) {
            commentIcon.style.visibility = "visible";
            window.innerWidth > 1200 ?
            newsCommentInput.style.height = "16px":
            newsCommentInput.style.height = "40px"
            newsCommentInput.style.height = (newsCommentInput.scrollHeight) + "px";
        }
        else {
            window.innerWidth > 1200 ?
            newsCommentInput.style.height = "16px":
            newsCommentInput.style.height = "40px"
            commentIcon.style.visibility = "hidden"; 
        }

    })
}