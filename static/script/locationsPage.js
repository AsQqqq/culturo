function updateDataLiked() {
    fetch('/get_data')
        .then(response => response.json())
        .then(data => {
            // Действия на html-странице при получении карточки

        });
}

function updateDataAll() {
    fetch('/get_data')
        .then(response => response.json())
        .then(data => {
            // Действия на html-странице при получении карточки

        });
}

updateDataLiked()
updateDataAll()