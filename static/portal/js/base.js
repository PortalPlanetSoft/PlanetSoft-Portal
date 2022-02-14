const navToggleBtn = document.querySelector('#ov-nav-toggle');
const navigation = document.querySelector('#ov-navigation');

const modal = document.querySelector('#ov-modal');
const btnshowModal = document.querySelector('#ov-btnShowModal');
const btncloseModal = document.querySelector('#ov-btnCloseModal');


if (btnshowModal !== null) {
  btnshowModal.addEventListener('click', (e) => {
    e.preventDefault();
    modal.style.display = "flex";
  });
}

if(btncloseModal !== null) {
  btncloseModal.addEventListener('click', e => {
    e.preventDefault();
    modal.style.display = "none";
  })
}



// Navigation hamburger menu
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
