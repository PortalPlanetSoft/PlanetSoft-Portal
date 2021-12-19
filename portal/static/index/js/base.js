const navToggleBtn = document.querySelector('#nav-toggle-btn');
const navigation = document.querySelector('#navigation');

navToggleBtn.addEventListener('click', (e) => {
  e.preventDefault();
  toggleNav(navigation);
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
