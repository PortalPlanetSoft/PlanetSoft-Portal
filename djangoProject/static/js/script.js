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
    secondary.style.display = "none";
    primary.innerHTML = "PLANET SOFT je regionalna informatička grupacija koja posluje na teritoriji adrijatik regije. Primarni fokus kompanije su rješenja koja unaprijeđuju, optimizuju i automatizuju poslovne procese.";
}

function showhide() {
    // ' We are Planet Soft. <img id="logomaintitle" src="{%'static /images/logo/Planet_soft_logoonly_crop.png'%}">'

    // var content1 = 'We are Planet Soft. ';
    // var content2 = ' <img id="logomaintitle" ';
    // var content3 = ' src=" ';
    // var content4 = " {%' ";
    // var content5 = " static /images/logo/Planet_soft_logoonly_crop.png ";
    // var content6 = " ' ";
    // var content7 = ' %}"> ';

    //var result=content1.concat(content2).concat(content3).concat(content4).concat(content5).concat(content6).concat(content7);

    //document.getElementById("maintitle").innerHTML = `We are Planet Soft. <img id="logomaintitle" src="{%static '/images/logo/Planet_soft_logoonly_crop.png' %}">` ;
    secondary.style.display = "block";
    primary.innerHTML = "We are Planet Soft. ";

    // alert(content1.concat(content2));
}