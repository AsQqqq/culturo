// Функционал страницы с выбором города

let buttonContinue = document.getElementById("continueButton");

// Проверка условий для активности кнопки
function checkConditions () {
    let selectElement = document.getElementById("placeSelect");
    if (selectElement.value !== "Место проведения") {
        buttonContinue.disabled = false;
        buttonContinue.style.backgroundColor = "#333333";
        buttonContinue.style.cursor = "pointer";
    }
}

// Отключенная кнопка
const disableButton = () => {
    buttonContinue.disabled = true;
    buttonContinue.style.backgroundColor = "#999999";
    buttonContinue.style.cursor = "not-allowed";
}

// Фильтр кнопки при загрузке страницы
document.addEventListener("DOMContentLoaded", disableButton);

// Анимации dropdown-меню
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.userNamePreferences');

    // Отображение dropdown-меню
    links.forEach(function(link) {
      link.addEventListener('click', function() {
        const dropdown = this.nextElementSibling;
        dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
      });
    });

    // Сокрытие dropdown-меню
    document.addEventListener('click', function(event) {
      if (!event.target.matches('.userNamePreferences')) {
        const dropdowns = document.querySelectorAll('.dropdownPreferences');
        dropdowns.forEach(function(dropdown) {
          dropdown.style.display = 'none';
        });
      }
    });
  });