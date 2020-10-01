const startTime = document.getElementById("start_date");
const endTime = document.getElementById("end_date");
startTime.setAttribute("min",`${new Date(new Date().getTime() - new Date().getTimezoneOffset() * 60000).toISOString().split("T")[0]}`)
endTime.setAttribute("min",`${new Date(new Date().getTime() - new Date().getTimezoneOffset() * 60000).toISOString().split("T")[0]}`)

startTime.addEventListener('input', function(){
    endTime.setAttribute("min",`${this.value}`)
});

endTime.addEventListener('input', function(){
    startTime.setAttribute("max",`${this.value}`)
});