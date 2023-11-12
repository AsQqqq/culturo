var swipeElement = document.getElementById('swipe-container');
var startX, startY;

var cardDiv = document.getElementById("card");
var customAttributeValue = cardDiv.dataset.customAttribute;
var id_place = {
    idPlace: customAttributeValue
};

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
    fetch('/get_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify('confirm', id_place),
    })
}

function sendTrashResult() {
    fetch('/get_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify('trash', id_place),
    })
}

// Вызовите функцию обновления данных при загрузке страницы
updateData();

// Установите интервал для выполнения функции обновления каждую секунду
setInterval(updateData, 1000);

function darkenMainBlock() {
    var imageContainer = document.getElementById("main-block");
    imageContainer.classList.toggle("darken");
}

function unDarkenMainBlock() {
    var imageContainer = document.getElementById("main-block");
    imageContainer.classList.remove("darken");
    swipeElement.addEventListener("touchend", unDarkenMainBlock);
}

// Проверяем, является ли устройство мобильным
var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

if (isMobile) {
    // Если мобильное устройство, используем touch события
    swipeElement.addEventListener("touchstart", darkenMainBlock);
    swipeElement.addEventListener("touchend", unDarkenMainBlock);
} else {
    // Если не мобильное устройство, используем mouse события
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
        // Вычисляем разницу между начальными и конечными координатами
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
}