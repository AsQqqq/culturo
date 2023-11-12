var swipeElement = document.getElementById('swipe-container');
var startX, startY;

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
// Вызовите функцию обновления данных при загрузке страницы
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

var swipeContainer = document.getElementById('swipe-container');
var hammer = new Hammer(swipeContainer);

hammer.on('swipeleft', function() {
    sendTrashResult();
});

hammer.on('swiperight', function() {
    sendConfirmResult();
});

// Проверяем, является ли устройство мобильным
var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

if (isMobile) {
    swipeElement.addEventListener("touchstart", darkenMainBlock);
    swipeElement.addEventListener("touchend", unDarkenMainBlock);
} else {
    swipeElement.addEventListener('mousedown', function (e) {
        darkenMainBlock();

        var leftElement = document.getElementById('trash-icon');
        var rightElement = document.getElementById('confirm-icon');
        leftElement.classList.toggle('hidden');
        leftElement.classList.toggle('trash-icon');

        rightElement.classList.toggle('hidden');
        rightElement.classList.toggle('confirm-icon');

        // Запоминаем начальные координаты при нажатии
        startX = e.clientX;
        startY = e.clientY;
    });

    swipeElement.addEventListener('mouseup', function (e) {
        // Вычисляем разницу между начальными и конечными координатами
        unDarkenMainBlock();

        var leftElement = document.getElementById('trash-icon');
        var rightElement = document.getElementById('confirm-icon');

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
            console.log('Нужный свайп не произошел');
        }
    });
}