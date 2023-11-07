function setDefaultColor (element) {
  element.style.color = "#333333";
  element.style.borderColor = "#333333";
}

function setErrorColor (element) {
  let button = document.getElementById("sign_up_button");
  element.style.color = "#a52a2a";
  element.style.borderColor = "#a52a2a";
}

function validateName () {
  let nameInput = document.getElementsByName("name")[0];
  let nameValue = nameInput.value;
  
  if (nameValue.length > 1) {
    setDefaultColor(nameInput);
  } else {
    setErrorColor(nameInput);
  }
}

function validateSurname () {
  let surnameInput = document.getElementsByName("surname")[0];
  let surnameValue = surnameInput.value;
  
  if (surnameValue.length > 1) {
    setDefaultColor(surnameInput);
  } else {
    setErrorColor(surnameInput);
  }
}

function validateLogin () {
  let loginInput = document.getElementsByName("login")[0];
  let loginValue = loginInput.value;

  var reg = /[а-яА-ЯёЁ]/g; 
  if (loginInput.value.search(reg) != -1) {
    loginInput.value = loginInput.value.replace(reg, '');
  }
  
  if (loginValue.length >= 2) {
    setDefaultColor(loginInput);
  } else {
    setErrorColor(loginInput);
  }
}

function validateEmail () {
  let emailInput = document.getElementsByName("email")[0];
  let emailValue = emailInput.value;
  var count = (emailValue.match(/@/g) || []).length;

  if (count > 1 || count < 1) {
    setErrorColor(emailInput);
  } else {
    setDefaultColor(emailInput);
  }
}

function validatePassword () {
  let passwordInput = document.getElementsByName("password")[0];
  let passwordValue = passwordInput.value;
  let passwordLength = passwordValue.length;

  var reg = /[а-яА-ЯёЁ]/g;

  if (passwordValue.search(reg) != -1) {
    passwordValue = passwordValue.replace(reg, '');
  }

  if (passwordLength < 8) {
    setErrorColor(passwordInput);
  } else {
    setDefaultColor(passwordInput);
  }
}

function validateRePassword () {
  let passwordInput = document.getElementsByName("password")[0];
  let passwordValue = passwordInput.value;
  let rePasswordInput = document.getElementsByName("confirm_password")[0];
  let rePasswordValue = rePasswordInput.value

  var reg = /[а-яА-ЯёЁ]/g; 

  if (rePasswordValue.search(reg) != -1) {
    rePasswordValue = rePasswordValue.replace(reg, '');
  }

  if (rePasswordValue != passwordValue) {
    setErrorColor(rePasswordInput);
    setErrorColor(passwordInput);
  } else {
    setDefaultColor(rePasswordInput);
    setDefaultColor(passwordInput);
  }
}

