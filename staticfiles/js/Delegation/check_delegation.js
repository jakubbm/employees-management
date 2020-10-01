let month = document.getElementById('month').textContent;
let year = document.getElementById('year').textContent;
let nameOfFirstDay = document.getElementById('name_of_first_day').textContent;
let daysInMonth = document.getElementById('days_in_month').textContent;
let delegations = document.getElementById('delegation_for_json').textContent;

month = JSON.parse(month);
year = JSON.parse(year);
nameOfFirstDay = JSON.parse(nameOfFirstDay);
daysInMonth = JSON.parse(daysInMonth);
delegations = JSON.parse(delegations);
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
            <div class="day-hiddenday">
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


for (let i of delegations){
    let day = (i.date__date.slice(8,10))[0] == 0 ? i.date__date.slice(9,10) : i.date__date.slice(8,10);
    let day_box = document.getElementById(day);
    let elements = day_box.querySelectorAll(".delegation-day").length
    day_box.insertAdjacentHTML("beforeend",`
        <div class="delegation-day ${elements % 2 == 0 ? "delegation" : "delegation2"}">
            <div>
                <b>
                ${i.employee__first_name} ${i.employee__last_name} 
                </b>
            </div>
            <div>
                ${i.destination__country} - ${i.destination__city}
            </div>
            <div>
                ${i.company__company}
            </div>
        </div>
    `)


}


document.querySelectorAll('#app-calendar .day').forEach(day => {
    day.addEventListener("click",event =>{
        event.currentTarget.classList.toggle('selected-day')
    })
})

