const modalContent = document.getElementById("modal-content");
const modalContainer = document.getElementById("modal-container");
const urlAddress = 'http://127.0.0.1:8000';

// error codes for displaying required fields and toast messages
const DEFAULT_TOAST = 200; // default message in the toast (empty - neutral)
const ERROR_ACTION = 0; // action not completed successfully
const SUCCESSFUL_ACTION = 1; // action completed successfully
const DELETE_SUCCESSFUL = 2; // delete action successful
const INVALID_EMAIL_ERROR = 3; // input email not valid
const INVALID_PHONE_ERROR = 4; // input phone number not valid
const INVALID_VPN_ERROR = 5; // input vpn number not valid
const INVALID_EMAIL_PHONE_VPN_ERROR = 6; // input email, phone and vpn number - all not valid
const INVALID_EMAILANDPHONE_ERROR = 7; // input email and phone not valid
const INVALID_EMAILANDVPN_ERROR = 8; // input email and vpn number not valid
const INVALID_PHONEANDVPN_ERROR = 9; // input phone and vpn number not valid

// validation codes to determine if validation was successful
const VALIDATION_SUCCESS = 111; // validation of all elements successful
const PHONE_INVALID = 101; // phone number format not correct
const VPN_INVALID = 110; // vpn number format not correct
const EMAIL_INVALID = 11; // email format not correct
const EMAIL_PHONE_INVALID = 12; // email and phone number format not correct
const EMAIL_VPN_INVALID = 13; // email and vpn number format not correct
const PHONE_VPN_INVALID = 14; // phone and vpn number format not correct
const PASSWORD_VALIDATION_FAIL = 15; // error that is triggered when new input password does not meet required format
const PASSWORDS_MATCHING_ERROR = 16; // error that is triggered if the new password is not the same in both fields
const FIELDS_EMPTY = 17; // error that is triggered if both new password fields are empty
const FIRST_FIELD_EMPTY = 18;
const SECOND_FIELD_EMPTY = 19;
const VALIDATION_FAIL = 0; // validation of all elements unsuccessful

let result = DEFAULT_TOAST;

const passwordChangeUrl = urlAddress + '/employees/password-change/';
const viewUserUrl = urlAddress + '/employees/';
const deleteUserUrl = urlAddress + '/employees/delete/';
const addUserUrl = urlAddress + '/employees/create/';
const addNewsUrl = urlAddress + '/news/create/';
const editNewsUrl = urlAddress + '/news/';
const deleteNewsUrl = urlAddress + '/news/delete/';
const viewNewsUrl = urlAddress + '/news/article/';
