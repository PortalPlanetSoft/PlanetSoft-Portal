// Navigation
const navToggleBtn = document.querySelector('#nav-toggle-btn');
const navigation = document.querySelector('#navigation');

// Dark Mode
const darkToggleBtn = document.querySelector('#dark-toggle-btn');

navToggleBtn.addEventListener('click', (e) => {
  e.preventDefault();
  navToggleBtn.firstChild.classList.toggle('fa-times');
  toggleAnimation(navigation, 'showNav', 'hideNav');
});
darkToggleBtn.addEventListener('click', (e) => {
  e.preventDefault();
  toggleDark();
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

function toggleDark() {
  document.documentElement.classList.toggle('dark');

  toggleAnimation(darkToggleBtn, 'btnIconToRight', 'btnIconToLeft');

  darkToggleBtn.firstChild.className === 'fas fa-sun'
    ? (darkToggleBtn.firstChild.className = 'fas fa-moon')
    : (darkToggleBtn.firstChild.className = 'fas fa-sun');
}
