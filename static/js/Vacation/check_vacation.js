let month = document.getElementById('month').textContent;
let year = document.getElementById('year').textContent;
let nameOfFirstDay = document.getElementById('name_of_first_day').textContent;
let daysInMonth = document.getElementById('days_in_month').textContent;
let vacations = document.getElementById('vacation_for_json').textContent;

month = JSON.parse(month);
year = JSON.parse(year);
nameOfFirstDay = JSON.parse(nameOfFirstDay);
daysInMonth = JSON.parse(daysInMonth);
vacations = JSON.parse(vacations);

const calendar = document.querySelector("#app-calendar");


const isWeekend = day => {
    const date = new Date(year,month-1,day).getDay();
    if (date === 6 || date === 0){
        return true;
    }
}

const getDayName = day => {
    const date = new Date(year,month-1,day)
    const dayName = new Intl.DateTimeFormat("en-US",{weekday: "short"}).format(date)
    return dayName;
}

for (let day = 1; day <= daysInMonth; day++){
    const weekend = isWeekend(day)
    const dayName = getDayName(day);

    if (day === 1 ){
        for(let i = 1; i <= nameOfFirstDay; i++){
            calendar.insertAdjacentHTML("beforeend",`
            <div class="day-hidden">
            </div>
        `)}}

    calendar.insertAdjacentHTML("beforeend",`
    <div id="${day}" class="day ${weekend ? "weekend":""}">
        <div class="name">
            ${dayName}
        </div>
        ${day}
    </div>
    `)
}


for (let i of vacations){
    console.log(i);
    let day = (i.date.slice(8,10))[0] == 0 ? i.date.slice(9,10) : i.date.slice(8,10);
    let day_box = document.getElementById(day);
    let elements = day_box.getElementsByTagName("div").length
    day_box.insertAdjacentHTML("beforeend",`
        <div class="employee ${elements % 2 == 0 ? "vacation" : "vacation2"}">${i.employee__first_name} ${i.employee__last_name}</div>
    `)


}


document.querySelectorAll('#app-calendar .day').forEach(day => {
    day.addEventListener("click",event =>{
        event.currentTarget.classList.toggle('selected-day')
    })
})

