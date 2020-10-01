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


const calendar = document.querySelector("#app-calendar2");


//Check if day is a weekend
const isWeekend = day => {
    const date = new Date(year,month-1,day).getDay();
    if (date === 6 || date === 0){
        return true;
    }
}

//Get day name
const getDayName = day => {
    const date = new Date(year,month-1,day)
    const dayName = new Intl.DateTimeFormat("en-US",{weekday: "short"}).format(date)
    return dayName;
}

//Generating calendar
for (let day = 1; day <= daysInMonth; day++){
    const weekend = isWeekend(day)
    const dayName = getDayName(day);

    //Checking what day of week is first day of month
    if (day === 1 ){
        for(let i = 1; i <= nameOfFirstDay; i++){
            calendar.insertAdjacentHTML("beforeend",`
            <div class="hiddenday">
            </div>
        `)}}

    //Generating each day
    calendar.insertAdjacentHTML("beforeend",`
    <div id="${day}" class="day ${weekend ? "weekend":""}">
        <div class="name">
            ${dayName}
        </div>
        ${day}
    </div>
    `)
}

//Adding delegation days to calendar
for (let i of delegations){
    console.log(i.date__date);
    let day = (i.date__date.slice(8,10))[0] == 0 ? i.date__date.slice(9,10) : i.date__date.slice(8,10);
    let day_box = document.getElementById(day);
    day_box.classList.add('delegation')
    day_box.insertAdjacentHTML("beforeend",`
    <div class="delegation-day">
        <div >${i.destination__country} - ${i.destination__city}</div>
        <div >${i.company__company}</div>
    </div>
`)

}

//Adding selector for days in calendar
document.querySelectorAll('#app-calendar2 .day').forEach(day => {
    day.addEventListener("click",event =>{
        event.currentTarget.classList.toggle('selected')
    })
})


