let updateButtons = document.getElementsByClassName("edit");
for (let i=0;i<updateButtons.length;i++){
    updateButtons[i].addEventListener("click",function(){
       let task = document.getElementsByClassName("task");
       previous = task[i].innerText
       html = `<input type="text" class = "new-value" placeholder=${previous}>
       <button id = "confirm" type="submit" rel="tooltip" title="Edit Task" class="btn btn-success">
       <i class="fas fa-check"></i>
        </button>
       `
       task[i].innerHTML = html;
       let confirmButton = document.getElementById("confirm");
       confirmButton.addEventListener("click",function(){
          let form = document.getElementsByClassName("form-update");
          let child = document.createElement("input");
          child.setAttribute('type', 'hidden');
          child.setAttribute('name', 'update-value');
          let newValue = document.getElementsByClassName("new-value");
          child.setAttribute('value', newValue[0].value);
          form[i].appendChild(child)
          form[i].submit();

       })
    })
};
