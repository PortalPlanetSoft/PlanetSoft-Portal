// toast message that is displayed every time a successful/unsuccessful change is made
function showToast(result) {
    const toastContainer = document.getElementById("toast-container");
    const toastMessage = document.getElementById("toast-message");

    switch (result) {
        case ERROR_ACTION:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Neuspješno!";
            break;
        case DELETE_SUCCESSFUL:
            toastMessage.innerHTML = "Uspješno obrisano!";
            break;
        case INVALID_EMAIL_ERROR:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Molimo Vas unesite ispravan format e-mail adrese!";
            break;
        case INVALID_PHONE_ERROR:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Molimo Vas unesite ispravan format broja telefona!";
            break;
        case INVALID_VPN_ERROR:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Molimo Vas unesite ispravan format VPN telefona!";
            break;
        case INVALID_EMAILANDPHONE_ERROR:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Molimo Vas unesite ispravan format email adrese i broja telefona!";
            break;
        case INVALID_EMAILANDVPN_ERROR:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Molimo Vas unesite ispravan format email adrese i VPN telefona!";
            break;
        case INVALID_PHONEANDVPN_ERROR:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Molimo Vas unesite ispravan format broja privatnog i VPN telefona!";
            break;
        case INVALID_EMAIL_PHONE_VPN_ERROR:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Molimo Vas unesite ispravan format e-mail adrese kao i privatnog i VPN broja telefona!";
            break;
        case PASSWORD_VALIDATION_FAIL:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Molimo Vas unesite šifru u odgovarajućem formatu!";
            break;
        case PASSWORDS_MATCHING_ERROR:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Molimo Vas unesite istu šifru u oba polja!";
            break;
        case FIELDS_EMPTY:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Polja ne mogu biti prazna!";
            break;
        case FIRST_FIELD_EMPTY:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Polje ne moze biti prazno!";
            break;
        case SECOND_FIELD_EMPTY:
            toastContainer.style.backgroundColor = "var(--alert-light)";
            toastMessage.innerHTML = "Polje ne moze biti prazno!";
            break;
        default:
            toastMessage.innerHTML = "Uspješno sačuvano!";
            break;
    }
    toastContainer.className = "show";
    setTimeout(function () {
        toastContainer.className = toastContainer.className.replace("show", "");
    }, 3000);
}