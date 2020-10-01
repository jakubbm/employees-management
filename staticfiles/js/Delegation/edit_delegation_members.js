let rows = document.getElementsByClassName("row-amount");


function insertedHtml(employeeName,functionality,gramar){
    return `
     <h6>Do you really want to ${functionality} : <strong>${employeeName}</strong> ${gramar} delegation ?</h6>
     </div>
     <div class="col-md-12 text-center">
     <div class="d-inline-block">
         <button type="button" rel="tooltip" title="Confirm" class="btn btn-success form-control confirm">
             <i class="fas fa-check-square"></i>
         </button>
     </div>
     <div class="d-inline-block">
         <button type="button" rel="tooltip" title="Cancel" class="btn btn-danger form-control cancel">
             <i class="fas fa-window-close"></i>
         </button>
     </div>`
 };


for (let i = 0;i < rows.length; i++){
    let employeesAdd = rows[i].getElementsByClassName("employee-add");
    let employeesRemove = rows[i].getElementsByClassName("employee-remove");
    for (employee of employeesAdd){
        employee.addEventListener("click",function(){
            let employeeName = this.querySelector("div");
            let form = this.querySelector("form");
            let confirmRow = rows[i].querySelector(".toggle-confirm-row")
            confirmRow.innerHTML="";
            confirmRow.insertAdjacentHTML("afterbegin",insertedHtml(employeeName.innerHTML, "add", "to"));
            confirmRow.querySelector(".confirm").addEventListener("click",function(){
                form.submit();
            });
            confirmRow.querySelector(".cancel").addEventListener("click",function(){
                confirmRow.innerHTML="";
            });
    })}

    for (employee of employeesRemove){
        employee.addEventListener("click",function(){
            let employeeName = this.querySelector("div");
            let form = this.querySelector("form");
            let confirmRow = rows[i].querySelector(".toggle-confirm-row")
            confirmRow.innerHTML="";
            confirmRow.insertAdjacentHTML("afterbegin",insertedHtml(employeeName.innerHTML, "remove", "from"));
            confirmRow.querySelector(".confirm").addEventListener("click",function(){
                form.submit();
            });
            confirmRow.querySelector(".cancel").addEventListener("click",function(){
                confirmRow.innerHTML="";
            });
    })}
}

