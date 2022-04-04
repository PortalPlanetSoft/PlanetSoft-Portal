"use strict"
const MODAL_CONTENT = document.getElementById("modal-content");
const MODAL_CONTAINER = document.getElementById("modal-container");
const URL_ADDRESS = 'http://127.0.0.1:8000';

// error codes for displaying required fields and toast messages
const DEFAULT_TOAST = ""; // default message in the toast (empty - neutral)
const ERROR_ACTION = "Neuspješno!"; // action not completed successfully
const SUCCESSFUL_ACTION = "Uspješno sačuvano!"; // action completed successfully
const DELETE_SUCCESSFUL = "Uspješno obrisano!"; // delete action successful
const INVALID_EMAIL_ERROR = "Molimo Vas unesite ispravan format e-mail adrese!"; // input email not valid
const INVALID_PHONE_ERROR = "Molimo Vas unesite ispravan format broja telefona!"; // input phone number not valid
const INVALID_VPN_ERROR = "Molimo Vas unesite ispravan format VPN telefona!"; // input vpn number not valid

// validation codes to determine if validation was successful
const PASSWORD_VALIDATION_FAIL = "Molimo Vas unesite šifru u odgovarajućem formatu!"; // error that is triggered when new input password does not meet required format
const PASSWORDS_MATCHING_ERROR = "Molimo Vas unesite istu šifru u oba polja!"; // error that is triggered if the new password is not the same in both fields
const FIRST_FIELD_EMPTY = "Polje ne moze biti prazno!";

const PASSWORD_REGEX = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/; // minimum eight characters, at least one letter and one number
const REGEX_MAIL = /^(([^<>()\\[\]\\.,;:\s@"]+(\.[^<>()\\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
const REGEX_NUMBER = /^(\+387|00387|0)(66|65|61)[0-9]{6}$/;
const REGEX_VPN_NUMBER = /^[0-9]{3}$/;

const PASSWORD_CHANGE_URL = URL_ADDRESS + '/employees/password-change/';
const VIEW_USER_URL = URL_ADDRESS + '/employees/';
const DELETE_USER_URL = URL_ADDRESS + '/employees/delete/';
const ADD_USER_URL = URL_ADDRESS + '/employees/create/';
const ADD_NEWS_URL = URL_ADDRESS + '/news/create/';
const EDIT_NEWS_URL = URL_ADDRESS + '/news/';
const DELETE_NEWS_URL = URL_ADDRESS + '/news/delete/';
const VIEW_NEWS_URL = URL_ADDRESS + '/news/article/preview/';
const DELETE_AVATAR_URL = URL_ADDRESS + '/employees/remove-avatar/';

const CREATE_EVENT_URL = URL_ADDRESS + '/calendar/create/';
const DELETE_EVENT_URL = URL_ADDRESS + '/calendar/delete/';
const EDIT_EVENT_URL = URL_ADDRESS + '/calendar/';
const CALENDAR_EVENTS_URL = URL_ADDRESS + '/calendar/events/';
const EVENT_PREVIEW_URL = URL_ADDRESS + '/calendar/preview/';

const DELETE_AVATAR_BUTTON = document.getElementById("remove-avatar-button");
const DELETE_IMAGE_BUTTON = document.getElementById("remove-image-button");
const INPUT_FIELD = document.getElementById("id_profile_pic");
const INPUT_FIELD_NEWS = document.getElementById("id_image");
