const tableEmployees = document.getElementsByClassName("tohide");
const showButton = document.getElementsByClassName("show-button");

for(let i =0; i < showButton.length; i++){
    showButton[i].addEventListener("click",function(){
        tableEmployees[i].classList.toggle("hide-show-table");
    })
}

