const navToggleBtn = document.querySelector('#ov-nav-toggle');
const navigation = document.querySelector('#ov-navigation');
const newsCommentInput = document.querySelector("#news-comment-input");
const commentIcon = document.querySelector("#comment-icon");

console.log(window.innerWidth);

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

// Navigation hamburger menu
navToggleBtn.addEventListener('click', (e) => {
    if (navToggleBtn.firstChild.getAttribute('data-icon') === 'bars') {
        navToggleBtn.firstChild.setAttribute('data-icon', 'xmark')
        navToggleBtn.style.position = "fixed";
    } else {
        navToggleBtn.firstChild.setAttribute('data-icon', 'bars');
        navToggleBtn.style.position = "absolute";
    }
    toggleAnimation(navigation, 'showNav', 'hideNav');
});

function toggleAnimation(element, firstAnimName, secondAnimName) {
    if (
        element.style.animationName === '' ||
        element.style.animationName === secondAnimName
    ) {
        element.style.animationName = firstAnimName;
        return;
    }
    element.style.animationName = secondAnimName;
}

//function for showing chosen image preview on user settings page (/profile)

function changeThumbnail() {
    document.getElementById('id_profile_pic').addEventListener("change", function (e) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('photo-preview').src = e.target.result;
        };
        reader.readAsDataURL(this.files[0]);
    })
}

function docReady(fn) {
    if (document.readyState === "complete" || document === "interactive") {
        setTimeout(fn, 1);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}

docReady(changeThumbnail);
