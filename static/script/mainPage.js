// Функционал страницы со свайпами

let headLink = document.getElementById("headLink");
let placesLink = document.getElementById("placesLink");

// Анимация для переключения на страницу "Главная"
function switchContentHead() {
    placesLink.style.borderBottom = "none";
    headLink.style.borderBottom = "1px solid";
}

// Анимация для переключения на страницу "Места"
function switchContentPlaces() {
    headLink.style.borderBottom = "none";
    placesLink.style.borderBottom = "1px solid";
}

// Управление dropdown-меню
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.dropdown-selector');

    // Отображение элементов меню
    links.forEach(function(link) {
      link.addEventListener('click', function() {
        const dropdown = this.nextElementSibling;
        dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
      });
    });

    // Сокрытие элементов меню
    document.addEventListener('click', function(event) {
      if (!event.target.matches('.dropdown-selector')) {
        const dropdowns = document.querySelectorAll('.dropdownMain');
        dropdowns.forEach(function(dropdown) {
          dropdown.style.display = 'none';
        });
      }
    });
  });

var swipeElement = document.getElementById('swipe-container');
var startX, startY;
isLeftButtonPressed = false;

// Выполнение запроса к севреру и возвращение данных обратно на страницу
function updateData() {
    fetch('/get_data')
        .then(response => response.json())
        .then(data => {
            var swipeCard = document.getElementById('card');
            swipeCard.style.backgroundImage = `url(/static/images/cards/${data[0]})`;
            var header = document.getElementById('innerInfoCard');
            header.innerHTML = data[1];
            var description = document.getElementById('innerDescriptionCard');
            description.innerHTML = data[2];
        });
}

// Отправка информации о свайпе вправо
function sendConfirmResult() {
    fetch('/get_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify('confirm'),
    })
    updateData();
}


// Отправка информации о свайпе влево
function sendTrashResult() {
    fetch('/get_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify('trash'),
    })
    updateData();
}

// Вызов запроса к серверу при обновлении страницы
updateData();

// Затемнение фона
function darkenMainBlock() {
    var imageContainer = document.getElementById("content-block-main");
    imageContainer.classList.toggle("darken");
}

// Возврат фона в исходную палитру
function unDarkenMainBlock() {
    var imageContainer = document.getElementById("content-block-main");
    imageContainer.classList.remove("darken");
    swipeElement.addEventListener("touchend", unDarkenMainBlock);
}

// Появление иконок
function iconsToggle() {
    var leftElement = document.getElementById('trash-icon');
    var rightElement = document.getElementById('confirm-icon');
    leftElement.classList.toggle('hidden');
    leftElement.classList.toggle('trash-icon');

    rightElement.classList.toggle('hidden');
    rightElement.classList.toggle('confirm-icon');
}

var swipeContainer = document.getElementById('swipe-container');
// Подключение библиотеки Hammer для орбработки свайпов
var hammer = new Hammer(swipeContainer);

// Отправка информации о свайпе влево на мобильной версии сайта
hammer.on('swipeleft', function() {
    sendTrashResult();
});

// Отправка информации о свайпе вправо на мобильной версии сайта
hammer.on('swiperight', function() {
    sendConfirmResult();
});

// Анимация наклона карточки, взависимости от действий пользователя
swipeElement.addEventListener('mousemove', function (e) {
    if (isLeftButtonPressed) {
        var deltaX = e.clientX - startX;
        var angle = deltaX / 10;
        swipeElement.style.transform = 'rotate(' + angle + 'deg)';
    }
});

// Анимация возврата карточки в исходное положение
swipeElement.addEventListener('mouseup', function () {
    isLeftButtonPressed = false;
    swipeElement.style.transform = 'rotate(0deg)';
});

let isTouchActive = false;
let startXM = 0;

swipeElement.addEventListener('touchstart', function (e) {
    isTouchActive = true;
    startXM = e.touches[0].clientX;
});

swipeElement.addEventListener('touchmove', function (e) {
    if (isTouchActive) {
        let deltaX = e.touches[0].clientX - startXM;
        let angle = deltaX / 10;
        swipeElement.style.transform = 'rotate(' + angle + 'deg)';
    }
});

swipeElement.addEventListener('touchend', function () {
    isTouchActive = false;
    swipeElement.style.transform = 'rotate(0deg)';
});

// Анимации в случае отмены ЛКМ (на странице)
document.addEventListener('mouseup', function (e) {
    if (isLeftButtonPressed) {
        if (!swipeElement.contains(e.target)) {
            iconsToggle();
        }
        unDarkenMainBlock();
        isLeftButtonPressed = false;
        swipeElement.style.transform = 'rotate(0deg)';
    }
});

// Анимации в случае отмены ЛКМ (на карточке)
swipeElement.addEventListener('mouseup', function (e) {
    if (swipeElement.contains(e.target)) {
        iconsToggle();
    }
    unDarkenMainBlock();
    isLeftButtonPressed = false;
    swipeElement.style.transform = 'rotate(0deg)';
});

// Проверка устройства
var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

if (isMobile) {
    // Старт анимаций при нажатии на карточку (мобильная версия)
    swipeElement.addEventListener("touchstart", darkenMainBlock);
    swipeElement.addEventListener("touchstart", iconsToggle);
    swipeElement.addEventListener("touchend", unDarkenMainBlock);
    swipeElement.addEventListener("touchend", iconsToggle);
    document.addEventListener("touchend", iconsToggle);
} else {
    // Старт анимаций при нажатии на карточку
    swipeElement.addEventListener('mousedown', function (e) {
        isLeftButtonPressed = true;
        darkenMainBlock();
        iconsToggle();
        startX = e.clientX;
        startY = e.clientY;
    });

    // Обработка действий после отмены ЛКМ на карточке
    swipeElement.addEventListener('mouseup', function (e) {
        unDarkenMainBlock();

        var deltaX = e.clientX - startX;
        var deltaY = e.clientY - startY;

        if (Math.abs(deltaX) > Math.abs(deltaY)) {
            // Действия при свайпе влево
            if (deltaX > 10000) {
                sendConfirmResult();
            // Действия при свайпе вправо
            } else if (deltaX < -10000) {
                sendTrashResult();
            }
        } else {
            // Обработка в случае непредвиденных действий
            console.log('Исключение!');
        }
    });
}

// Переключение контента на карточке

var detailsCard = document.getElementById('details-container');
detailsCard.style.display = 'none';

function showDetailsCard() {
    detailsCard.style.display = 'flex';
    swipeContainer.style.display = 'none';
}

function hideDetailsCard() {
    detailsCard.style.display = 'none';
    swipeContainer.style.display = 'flex';
}