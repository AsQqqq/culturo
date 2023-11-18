// Валидация полей на странице входа

// Валидация поля "Логин"
function validateLogin () {
    let loginInput = document.getElementsByName("login")[0];
    
    var reg = /[а-яА-ЯёЁ]/g; 
    if (loginInput.value.search(reg) != -1) {
      loginInput.value = loginInput.value.replace(reg, '');
    }
}