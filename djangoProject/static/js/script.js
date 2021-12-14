$(document).ready(function () {
    $('li').on('click', function () {
        let gdje = $(this).attr('rel');
        if (gdje == 'infotable') {
            let hash = '#';
            let result = hash.concat(gdje);
            $('html, body').animate({
                scrollTop: $(result).offset().top - 130,
                behavior: "smooth"
            }, 200);
        } else if (gdje == 'contact') {
            let hash = '#';
            let result = hash.concat(gdje);
            $('html, body').animate({
                scrollTop: $(result).offset().top + 70,
                behavior: "smooth"
            }, 200);
        } else {
            $('html, body').animate({
                scrollTop: 0,
                behavior: "smooth"
            }, 200);
        }
    });
    $('ul.nav.navbar-nav > li')
        .click(function (e) {
            $('ul.nav.navbar-nav > li')
                .removeClass('active');
            $(this).addClass('active');
        });
});

var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1
    }

    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 2000);
}

var primary = document.getElementById("maintitle");
var secondary = document.getElementById("logomaintitle");
primary.addEventListener("mouseover", hideshow);
primary.addEventListener("mouseout", showhide);

function hideshow() {
    primary.innerHTML = "PLANET SOFT je regionalna informatička grupacija koja posluje na teritoriji adrijatik regije. Primarni fokus kompanije su rješenja koja unaprijeđuju, optimizuju i automatizuju poslovne procese.";
}

function showhide() {
    primary.innerHTML = "We are Planet Soft. ";
    primary.innerHTML += '<img class="logomaintitle" src="/static/images/logo/Planet_soft_logoonly_crop.png">';
}