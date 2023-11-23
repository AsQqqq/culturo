let logoutButton = document.getElementById('logout-from-profile');
let uploadImageButton = document.getElementById('upload-user-image-button');
let sendCriteriaButton = document.getElementById('upload-criteria-user-button');
let messageInput = document.getElementsByName("communication-with-developers")[0];


document.addEventListener('DOMContentLoaded', function () {
    setButtonInactive(uploadImageButton);
    checkConditions(); // Вызываем функцию для проверки условий при загрузке страницы
});


logoutButton.style.backgroundColor = "#a52a2a";

function setButtonInactive(button) {
    button.style.backgroundColor = "gray";
    button.style.cursor = "not-allowed";
}

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