const navToggleBtn = document.querySelector('#ov-nav-toggle');
const navigation = document.querySelector('#ov-navigation');

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

            console.log(e.target.result)
            console.log(document.getElementById('image-thumbnail').src)
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
