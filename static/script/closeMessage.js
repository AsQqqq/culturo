// Закрытие всплывающего уведомления

function closePopup(element) {
    element.classList.remove("show");
}

document.addEventListener("DOMContentLoaded", function() {
    var popup = document.querySelector("#popupContainer .popup");
    setTimeout(function() {
        popup.classList.remove("show");
    }, 15000);
});
