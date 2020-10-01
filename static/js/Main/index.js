let timeButton = document.getElementsByClassName('time-button');
let confirmRow = document.getElementsByClassName("toggle-time-row");
let cancelButton = document.getElementsByClassName("cancel");

function confirmRowToggle(i){
    confirmRow[i].classList.toggle('hide-show')
};

for(let i=0;timeButton.length;i++){
    timeButton[i].addEventListener("click",confirmRowToggle.bind(null, i), false);
    cancelButton[i].addEventListener("click",confirmRowToggle.bind(null, i), false);
};

