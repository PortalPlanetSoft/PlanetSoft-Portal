const navToggleBtn = document.querySelector('#ov-nav-toggle');
const navigation = document.querySelector('#ov-navigation');

navToggleBtn.addEventListener('click', (e) => {
  navToggleBtn.firstChild.getAttribute('data-icon') === 'bars'
    ? navToggleBtn.firstChild.setAttribute('data-icon', 'xmark')
    : navToggleBtn.firstChild.setAttribute('data-icon', 'bars');
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
