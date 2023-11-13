let logoutButton = document.getElementById('logout-from-profile');
let uploadImageButton = document.getElementById('upload-user-image-button');
let sendCriteriaButton = document.getElementById('upload-criteria-user-button');

logoutButton.style.backgroundColor = "#a52a2a";

function setButtonInactive(button) {
    button.style.backgroundColor = "gray";
    button.style.cursor = "not-allowed";
}

document.addEventListener('DOMContentLoaded', setButtonInactive(uploadImageButton));
document.addEventListener('DOMContentLoaded', setButtonInactive(sendCriteriaButton));




