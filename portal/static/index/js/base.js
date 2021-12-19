// Navigation
const navToggleBtn = document.querySelector('#nav-toggle-btn');
const navigation = document.querySelector('#navigation');

// Dark Mode
const darkToggleBtn = document.querySelector('#dark-toggle-btn');

navToggleBtn.addEventListener('click', (e) => {
  e.preventDefault();
  toggleNav(navigation);
});
darkToggleBtn.addEventListener('click', (e) => {
  e.preventDefault();
  toggleDark();
});

function toggleNav(navigation) {
  navToggleBtn.firstChild.classList.toggle('fa-times');
  if (
    navigation.style.animationName === '' ||
    navigation.style.animationName === 'hideNav'
  ) {
    navigation.style.animationName = 'showNav';
    return;
  }
  navigation.style.animationName = 'hideNav';
}

function toggleDark() {
  document.documentElement.classList.toggle('dark');

  darkToggleBtn.classList.toggle('btn--toggle-right');

  darkToggleBtn.firstChild.className === 'fas fa-sun'
    ? (darkToggleBtn.firstChild.className = 'fas fa-moon')
    : (darkToggleBtn.firstChild.className = 'fas fa-sun');
}
