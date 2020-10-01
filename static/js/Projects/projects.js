let rows = document.getElementsByClassName("row-amount-removing");
let activity;
let gramar;


function insertedHtml(employeeName,functionality,gramar,position){
    return `
     <h6>Do you really want to ${functionality} ${position}: <strong>${employeeName}</strong> ${gramar} project ?</h6>
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



if (rows.length != 0){
    activity = "remove";
    gramar = "from";

} else {
    rows = document.getElementsByClassName("row-amount-adding")
    activity = "add";
    gramar = "to";
}




for (let i = 0;i < rows.length; i++){
    let employees = rows[i].getElementsByClassName("emplo");
    let teamleads = rows[i].getElementsByClassName("teamld");
    for (employee of employees){
        employee.addEventListener("click",function(){
            let employeeName = this.querySelector("div");
            let form = this.querySelector("form");

            let confirmRow = rows[i].querySelector(".toggle-confirm-row")
            confirmRow.innerHTML="";
            confirmRow.insertAdjacentHTML("afterbegin",insertedHtml(employeeName.innerHTML,activity,gramar,"employee"));
            confirmRow.querySelector(".confirm").addEventListener("click",function(){
                form.submit();
            });
            confirmRow.querySelector(".cancel").addEventListener("click",function(){
                confirmRow.innerHTML="";
            });
    })}
    
    for (teamlead of teamleads){
        teamlead.addEventListener("click",function(){
            let employeeName = this.querySelector("div");
            let form = this.querySelector("form");

            let confirmRow = rows[i].querySelector(".toggle-confirm-row")
            confirmRow.innerHTML="";
            confirmRow.insertAdjacentHTML("afterbegin",insertedHtml(employeeName.innerHTML,activity,gramar,"teamleader"));
            confirmRow.querySelector(".confirm").addEventListener("click",function(){
                form.submit();
            });
            confirmRow.querySelector(".cancel").addEventListener("click",function(){
                confirmRow.innerHTML="";
            });
    })}

}

