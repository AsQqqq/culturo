let headLink = document.getElementById("headLink");
let placesLink = document.getElementById("placesLink");

function switchContentHead() {
    placesLink.style.borderBottom = "none";
    headLink.style.borderBottom = "1px solid";
}

function switchContentPlaces() {
    headLink.style.borderBottom = "none";
    placesLink.style.borderBottom = "1px solid";
}

document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.userNameMain');

    links.forEach(function(link) {
      link.addEventListener('click', function() {
        const dropdown = this.nextElementSibling;
        dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
      });
    });

    // Закрывать меню, если клик вне меню
    document.addEventListener('click', function(event) {
      if (!event.target.matches('.userNameMain')) {
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

// Функция для выполнения запроса к серверу и обновления данных на странице
function updateData() {
    // AJAX-запрос к серверу для получения данных
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

updateData();

// Затемнение фона
function darkenMainBlock() {
    var imageContainer = document.getElementById("main-block");
    imageContainer.classList.toggle("darken");
}

// Возврат фона в исходную палитру
function unDarkenMainBlock() {
    var imageContainer = document.getElementById("main-block");
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
var hammer = new Hammer(swipeContainer);

hammer.on('swipeleft', function() {
    sendTrashResult();
});

hammer.on('swiperight', function() {
    sendConfirmResult();
});

swipeElement.addEventListener('mouseup', function () {
    isLeftButtonPressed = false;
    swipeElement.style.transform = 'rotate(0deg)';
});

swipeElement.addEventListener('mousemove', function (e) {
    if (isLeftButtonPressed) {
        // Выполнять действия только при зажатой левой кнопке

        // Получаем разницу между начальной и текущей координатами
        var deltaX = e.clientX - startX;

        // Определяем угол наклона (в данном случае, просто используем deltaX)
        var angle = deltaX / 10; // Подберите подходящий коэффициент

        // Применяем наклон к элементу
        swipeElement.style.transform = 'rotate(' + angle + 'deg)';

        // ... (ваш остальной код)
    }
});

document.addEventListener('mouseup', function (e) {
    if (isLeftButtonPressed) {
        if (!swipeElement.contains(e.target)) {
            // Курсор мыши находится вне swipeElement
            iconsToggle();  // Скрываем leftElement и rightElement
        }
        unDarkenMainBlock();
        isLeftButtonPressed = false;
        swipeElement.style.transform = 'rotate(0deg)';
    }
});

swipeElement.addEventListener('mouseup', function (e) {
    if (swipeElement.contains(e.target)) {
        // Курсор мыши находится вне swipeElement
        iconsToggle();  // Скрываем leftElement и rightElement
    }
    unDarkenMainBlock();
    isLeftButtonPressed = false;
    swipeElement.style.transform = 'rotate(0deg)';
});

// Проверяем, является ли устройство мобильным
var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

if (isMobile) {
    swipeElement.addEventListener("touchstart", darkenMainBlock);
    swipeElement.addEventListener("touchend", unDarkenMainBlock);
} else {
    swipeElement.addEventListener('mousedown', function (e) {
        isLeftButtonPressed = true;
        darkenMainBlock();
        iconsToggle();
        // Запоминаем начальные координаты при нажатии
        startX = e.clientX;
        startY = e.clientY;
    });

    swipeElement.addEventListener('mouseup', function (e) {
        // Вычисляем разницу между начальными и конечными координатами
        unDarkenMainBlock();

        var deltaX = e.clientX - startX;
        var deltaY = e.clientY - startY;

        // Проверяем, является ли свайп горизонтальным
        if (Math.abs(deltaX) > Math.abs(deltaY)) {
            // Горизонтальный свайп
            if (deltaX > 10000) {
                console.log('Свайп вправо');
                sendConfirmResult();
            } else if (deltaX < -10000) {
                console.log('Свайп влево');
                sendTrashResult();
            }
        } else {
            // Вертикальный свайп (здесь вы можете добавить необходимые действия или игнорировать)
            console.log('Нужный свайп не произошел');
        }
    });
}