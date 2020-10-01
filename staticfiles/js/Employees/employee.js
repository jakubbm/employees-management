const successButtons = document.getElementsByClassName("finish-request")

function insertRow(employee, group){
return `
<tr class="table-secondary confirm-request">

<td>
    <h6 class="d-inline-block">Do you really want to finish request ? (Add emploee: ${employee} to group: ${group}) </h6>
</td>
<td>
    <div class="d-inline-block">
        <button type="button" rel="tooltip" title="Confirm" class="btn btn-success form-control confirm">
            <i class="fas fa-check-square"></i>
        </button>
    </div>
</td>
<td>
    <div class="d-inline-block">
        <button type="button" rel="tooltip" title="Cancel" class="btn btn-danger form-control cancel">
            <i class="fas fa-window-close"></i>
        </button>
    </div>
</td>
<td>
</td>
</tr>`}

for (success of successButtons){
    success.addEventListener("click",function(){
        if (this.classList.contains("active")){
            let confirmRow = document.getElementsByClassName("confirm-request")[0]
            confirmRow.innerHTML=""
            this.classList.remove("active")
        } else {
            this.classList.add("active")
            let employee = this.parentElement.parentElement.querySelector(".employee").innerHTML
            let group = this.parentElement.parentElement.querySelector(".group").innerHTML
            this.parentElement.parentElement.insertAdjacentHTML("afterend",insertRow(employee, group));
            let accept = document.getElementsByClassName("confirm")[0]
            let cancel = document.getElementsByClassName("cancel")[0]
            let confirmRow = document.getElementsByClassName("confirm-request")[0]
            accept.addEventListener("click",function(){
                success.getElementsByTagName("form")[0].submit();
            })
    
            cancel.addEventListener("click",function(){
                confirmRow.innerHTML=""
            })
        }

    })
}
