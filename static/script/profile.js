// Функционал страницы профиля

let logoutButton = document.getElementById('logout-from-profile');
let uploadImageButton = document.getElementById('upload-user-image-button');
let sendCriteriaButton = document.getElementById('upload-criteria-user-button');
let messageInput = document.getElementsByName("communication-with-developers")[0];

// Стартовые действия при обновлении страницы
document.addEventListener('DOMContentLoaded', function () {
    setButtonInactive(uploadImageButton);
    checkConditions();
});

logoutButton.style.backgroundColor = "#a52a2a";

// Установка кнопки неактивной
function setButtonInactive(button) {
    button.style.backgroundColor = "gray";
    button.style.cursor = "not-allowed";
}

// Ограничение письма разработчикам
const checkConditions = () => {
    const conditionMessage = messageInput.value.length > 4;
  
    if (conditionMessage) {
        sendCriteriaButton.disabled = false;
        sendCriteriaButton.style.backgroundColor = "#333333";
        sendCriteriaButton.style.cursor = "pointer";
    } else {
        sendCriteriaButton.disabled = true;
        sendCriteriaButton.style.backgroundColor = "#999999";
        sendCriteriaButton.style.cursor = "not-allowed";
    }
};

messageInput.addEventListener("input", checkConditions);
document.addEventListener('DOMContentLoaded', setButtonInactive(uploadImageButton));