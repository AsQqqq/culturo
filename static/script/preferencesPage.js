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