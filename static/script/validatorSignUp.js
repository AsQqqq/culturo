var reg = /[а-яА-ЯёЁ]/g;

function setDefaultColor(element) {
  element.style.color = "#333333";
  element.style.borderColor = "#333333";
}

function setErrorColor(element) {
  element.style.color = "#a52a2a";
  element.style.borderColor = "#a52a2a";
}

function validateName() {
  let nameInput = document.getElementsByName("name")[0];
  let nameValue = nameInput.value;

  if (nameValue.length > 1) {
    setDefaultColor(nameInput);
  } else {
    setErrorColor(nameInput);
  }
}

function validateSurname() {
  let surnameInput = document.getElementsByName("surname")[0];
  let surnameValue = surnameInput.value;

  if (surnameValue.length > 1) {
    setDefaultColor(surnameInput);
  } else {
    setErrorColor(surnameInput);
  }
}

function validateLogin() {
  let loginInput = document.getElementsByName("login")[0];
  let loginValue = loginInput.value;

  if (loginValue.search(reg) != -1) {
    loginInput.value = loginValue.replace(reg, '');
  }

  if (loginValue.length >= 2) {
    setDefaultColor(loginInput);
  } else {
    setErrorColor(loginInput);
  }
}

function validateEmail() {
  let emailInput = document.getElementsByName("email")[0];
  let emailValue = emailInput.value;
  var count = (emailValue.match(/@/g) || []).length;

  if (count > 1 || count < 1) {
    setErrorColor(emailInput);
  } else {
    setDefaultColor(emailInput);
  }
}

function validatePassword() {
  let passwordInput = document.getElementsByName("password")[0];
  let passwordValue = passwordInput.value;
  let passwordLength = passwordValue.length;
  let rePasswordInput = document.getElementsByName("confirm_password")[0];
  let rePasswordValue = rePasswordInput.value;

  if (passwordLength < 8) {
    setErrorColor(passwordInput);
  } else {
    setDefaultColor(passwordInput);
  }
}

function validateRePassword() {
  let passwordInput = document.getElementsByName("password")[0];
  let passwordValue = passwordInput.value;
  let rePasswordInput = document.getElementsByName("confirm_password")[0];
  let rePasswordValue = rePasswordInput.value;

  if (rePasswordValue != passwordValue) {
    setErrorColor(rePasswordInput);
    setErrorColor(passwordInput);
  } else {
    setDefaultColor(rePasswordInput);
    setDefaultColor(passwordInput);
  }
}

function filterPassword() {
  let passwordValue = document.getElementsByName("password")[0].value;
  if (passwordValue.search(reg) != -1) 
    passwordValue = passwordValue.replace(reg, '');
}

function filterRePassword() {
  let rePasswordValue = document.getElementsByName("confirm_password")[0].value;
  if (rePasswordValue.search(reg) != -1) 
    rePasswordValue = rePasswordValue.replace(reg, '');
}

let passwordInput = document.getElementsByName("password")[0];
let rePasswordInput = document.getElementsByName("confirm_password")[0];
passwordInput.addEventListener('input', filterPassword);
rePasswordInput.addEventListener('input', filterRePassword);