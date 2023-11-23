let buttonContinue = document.getElementById("continueButton");


function checkConditions () {
    let selectElement = document.getElementById("placeSelect");
    if (selectElement.value !== "Место проведения") {
        buttonContinue.disabled = false;
        buttonContinue.style.backgroundColor = "#333333";
        buttonContinue.style.cursor = "pointer";
    }
}

const disableButton = () => {
    buttonContinue.disabled = true;
    buttonContinue.style.backgroundColor = "#999999";
    buttonContinue.style.cursor = "not-allowed";
}


document.addEventListener("DOMContentLoaded", disableButton);

document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.userNamePreferences');

    links.forEach(function(link) {
      link.addEventListener('click', function() {
        const dropdown = this.nextElementSibling;
        dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
      });
    });

    // Закрывать меню, если клик вне меню
    document.addEventListener('click', function(event) {
      if (!event.target.matches('.userNamePreferences')) {
        const dropdowns = document.querySelectorAll('.dropdownPreferences');
        dropdowns.forEach(function(dropdown) {
          dropdown.style.display = 'none';
        });
      }
    });
  });