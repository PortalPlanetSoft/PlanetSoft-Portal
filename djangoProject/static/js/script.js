var primary = document.getElementById("maintitle");

primary.addEventListener("mouseover", hideshow);
primary.addEventListener("mouseout", showhide);

function hideshow() {
    primary.innerHTML = "PLANET SOFT je regionalna informatička grupacija koja posluje na teritoriji adrijatik regije. Primarni fokus kompanije su rješenja koja unaprijeđuju, optimizuju i automatizuju poslovne procese.";
}

function showhide() {
    primary.innerHTML = "We are Planet Soft. ";
    primary.innerHTML += '<img class="logomaintitle" src="/static/images/logo/Planet_soft_logoonly_crop.png">';
}