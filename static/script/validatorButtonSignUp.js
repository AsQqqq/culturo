const nameInput = document.getElementsByName("name")[0];
const surnameInput = document.getElementsByName("surname")[0];
const loginInput = document.getElementsByName("login")[0];
const emailInput = document.getElementsByName("email")[0];
const passwordInput = document.getElementsByName("password")[0];
const rePasswordInput = document.getElementsByName("confirm_password")[0];
const buttonSignUp = document.getElementById("sign_up_button");


const checkConditions = () => {
  var count = (emailInput.value.match(/@/g) || []).length;
  const conditionName = nameInput.value.length > 1;
  const conditionSurname = surnameInput.value.length > 1;
  const conditionLogin = loginInput.value.length > 1;
  const conditionEmail = count == 1;
  const conditionPassword = passwordInput.value.length >= 8;
  const conditionRePassword = rePasswordInput.value == passwordInput.value;

  if (conditionName && conditionSurname && conditionLogin && conditionEmail && conditionPassword && conditionRePassword) {
    buttonSignUp.disabled = false;
    buttonSignUp.style.backgroundColor = "#333333";
    buttonSignUp.style.cursor = "pointer";
  } else {
    buttonSignUp.disabled = true;
    buttonSignUp.style.backgroundColor = "#999999";
    buttonSignUp.style.cursor = "not-allowed";
  }
};

nameInput.addEventListener("input", checkConditions);
surnameInput.addEventListener("input", checkConditions);
loginInput.addEventListener("input", checkConditions);
emailInput.addEventListener("input", checkConditions);
passwordInput.addEventListener("input", checkConditions);
rePasswordInput.addEventListener("input", checkConditions);
