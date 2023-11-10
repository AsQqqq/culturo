let mainBlock = document.getElementById("main-block");
let aboutBlock = document.getElementById("about-block");
let developersBlock = document.getElementById("developers-block");
let mainLink = document.getElementById("mainLink");
let aboutLink = document.getElementById("aboutLink");
let developersLink = document.getElementById("developersLink")



function switchContentMain () {
    aboutBlock.style.display = "none";
    developersBlock.style.display = "none";
    
    aboutLink.style.borderBottom = "none";
    developersLink.style.borderBottom = "none";

    mainLink.style.borderBottom = "1px solid";
    mainBlock.style.display = "flex";
}

function switchContentAbout () {
    mainBlock.style.display = "none";
    developersBlock.style.display = "none";
    
    mainLink.style.borderBottom = "none";
    developersLink.style.borderBottom = "none";

    aboutLink.style.borderBottom = "1px solid";
    aboutBlock.style.display = "flex";
}

function switchContentDevelopers () {
    aboutBlock.style.display = "none";
    mainBlock.style.display = "none";
    
    aboutLink.style.borderBottom = "none";
    mainLink.style.borderBottom = "none";

    developersLink.style.borderBottom = "1px solid";
    developersBlock.style.display = "flex";
}
