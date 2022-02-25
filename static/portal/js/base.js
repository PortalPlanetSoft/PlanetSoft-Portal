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
