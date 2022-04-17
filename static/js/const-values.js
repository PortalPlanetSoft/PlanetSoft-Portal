"use strict"

let MODAL_CONTENT = document.getElementById("modal-content");
let MODAL_CONTAINER = document.getElementById("modal-container");
let NOTIFICATIONS;
const URL_ADDRESS = 'http://127.0.0.1:8000';

const NAV_TOGGLE_BTN = document.querySelector('#ov-nav-toggle');
const NAVIGATION = document.querySelector('#ov-navigation');

const DEFAULT_TOAST = "";
const ERROR_ACTION = "Neuspješno!";
const SUCCESSFUL_ACTION = "Uspješno sačuvano!";
const DELETE_SUCCESSFUL = "Uspješno obrisano!";
const INVALID_EMAIL_ERROR = "Molimo Vas unesite ispravan format e-mail adrese!";
const INVALID_PHONE_ERROR = "Molimo Vas unesite ispravan format broja telefona!";
const INVALID_VPN_ERROR = "Molimo Vas unesite ispravan format VPN telefona!";

const PASSWORD_VALIDATION_FAIL = "Molimo Vas unesite šifru u odgovarajućem formatu! (Minimalno 8 znakova, od kojih obavezno jedno slovo i jedan broj.)";
const PASSWORDS_MATCHING_ERROR = "Molimo Vas unesite istu šifru u oba polja!";
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
const DELETE_NEWS_PICTURE_URL = URL_ADDRESS + '/news/remove-photo/';

const CREATE_EVENT_URL = URL_ADDRESS + '/calendar/create/';
const DELETE_EVENT_URL = URL_ADDRESS + '/calendar/delete/';
const EDIT_EVENT_URL = URL_ADDRESS + '/calendar/';
const EVENT_PREVIEW_URL = URL_ADDRESS + '/calendar/preview/';
const CALENDAR_EVENTS_URL = URL_ADDRESS + '/calendar/events/';

const DELETE_AVATAR_BUTTON = document.getElementById("remove-avatar-button");
const INPUT_FIELD = document.getElementById("id_profile_pic");

const REACT_COMMENT_URL = URL_ADDRESS + '/news/likes_dislikes_comment/';
const SUBMIT_COMMENT_URL = URL_ADDRESS + '/news/comment/';
const REACT_ARTICLE_URL = URL_ADDRESS + '/news/react/';
const RANDOM = URL_ADDRESS + '/news/article';

