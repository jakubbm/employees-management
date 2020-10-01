//Hamburger Menu
const menu = document.getElementById("hamburger-menu");
const sidebar = document.querySelector(".sidebar")
const mainContent = document.querySelector(".main")
const time = document.getElementById("time")


menu.addEventListener("click", function(){
    menu.classList.toggle("rotate");
    sidebar.classList.toggle("sidebar-hidden");
    mainContent.classList.toggle("hidden");
})

//Time
function getTime(){
    return new Date();
}

setInterval(function(){
time.innerHTML = getTime();
},1000)

