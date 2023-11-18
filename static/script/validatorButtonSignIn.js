// Функционал кнопки на странице входа

const loginInput = document.getElementsByName("login")[0];
const passwordInput = document.getElementsByName("password")[0];
const buttonSignIn = document.getElementById("sign_in_button");

// Проверка условий
const checkConditions = () => {
    const conditionLogin = loginInput.value.length > 1;
    const conditionPassword = passwordInput.value.length >= 8;

    if (conditionLogin && conditionPassword) {
        buttonSignIn.disabled = false;
        buttonSignIn.style.backgroundColor = "#333333";
        buttonSignIn.style.cursor = "pointer";
        console.log('false')
    } else {
        buttonSignIn.disabled = true;
        buttonSignIn.style.backgroundColor = "#999999";
        buttonSignIn.style.cursor = "not-allowed";
    }
}


loginInput.addEventListener("input", checkConditions);
passwordInput.addEventListener("input", checkConditions);
document.addEventListener('DOMContentLoaded', checkConditions);