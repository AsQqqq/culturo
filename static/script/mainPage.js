var swipeElement = document.getElementById('swipe-container');
var startX, startY;

// Функция для выполнения запроса к серверу и обновления данных на странице
function updateData() {
    // Выполните AJAX-запрос к серверу для получения данных
    fetch('/get_data')
        .then(response => response.json())
        .then(data => {
            // Очистите текущие данные на странице
            document.getElementById('data-list').innerHTML = '';

            // Обновите данные на странице
            data.forEach(record => {
                const listItem = document.createElement('li');
                listItem.textContent = record.field_name;  // Замените на соответствующее поле
                document.getElementById('data-list').appendChild(listItem);
            });
        });
}

function sendConfirmResult() {
    fetch('/confirmCard', {
        method: 'POST',
    })
}

function sendTrashResult() {
    fetch('/trashCard', {
        method: 'POST',
    })
}


// Вызовите функцию обновления данных при загрузке страницы
updateData();

// Настройте WebSocket для мгновенного обновления данных
const socket = new WebSocket('ws://localhost:5000/socket');

socket.addEventListener('message', function (event) {
    // При получении сообщения от сервера, обновите данные на странице
    updateData();
});

// Установите интервал для выполнения функции обновления каждую секунду
setInterval(updateData, 10000);

function darkenMainBlock () {
    var imageContainer = document.getElementById("main-block");
    imageContainer.classList.toggle("darken");
}

function unDarkenMainBlock () {
    var imageContainer = document.getElementById("main-block");
    imageContainer.classList.remove("darken");
    swipeElement.addEventListener("touchend", unDarkenMainBlock);
}

swipeElement.addEventListener("touchstart", darkenMainBlock);

swipeElement.addEventListener('mousedown', function (e) {
    darkenMainBlock();
    // Запоминаем начальные координаты при нажатии
    startX = e.clientX;
    startY = e.clientY;
    var leftElement = document.getElementById('trash-icon');
    var rightElement = document.getElementById('confirm-icon');

    // Добавляем/удаляем классы для запуска анимации
    leftElement.classList.toggle('hidden');
    leftElement.classList.toggle('trash-icon');

    rightElement.classList.toggle('hidden');
    rightElement.classList.toggle('confirm-icon');
});

swipeElement.addEventListener('mouseup', function (e) {
    // Вычисляем разницу между начальными и конечными координатамиё
    unDarkenMainBlock();
    var leftElement = document.getElementById('trash-icon');
    var rightElement = document.getElementById('confirm-icon');

    // Добавляем/удаляем классы для запуска анимации
    leftElement.classList.toggle('hidden');
    leftElement.classList.toggle('trash-icon');

    rightElement.classList.toggle('hidden');
    rightElement.classList.toggle('confirm-icon');

    var deltaX = e.clientX - startX;
    var deltaY = e.clientY - startY;

    // Проверяем, является ли свайп горизонтальным
    if (Math.abs(deltaX) > Math.abs(deltaY)) {
        // Горизонтальный свайп
        if (deltaX > 0) {
            console.log('Свайп вправо');
            sendConfirmResult();
        } else {
            console.log('Свайп влево');
            sendTrashResult();
        }
    } else {
        // Вертикальный свайп (здесь вы можете добавить необходимые действия или игнорировать)
        console.log('Вертикальный свайп');
    }
});