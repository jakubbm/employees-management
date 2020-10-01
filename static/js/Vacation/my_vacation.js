let month = document.getElementById('month').textContent;
let year = document.getElementById('year').textContent;
let nameOfFirstDay = document.getElementById('name_of_first_day').textContent;
let daysInMonth = document.getElementById('days_in_month').textContent;
let vacations = document.getElementById('vacation_for_json').textContent;
let avaliable_vacation_days = document.getElementById('avaliable_vacation_days').textContent;
let total_days_vacations = document.getElementById('total_days_vacations').textContent;
let monthly_days_vacations = document.getElementById('monthly_days_vacations').textContent;


month = JSON.parse(month);
year = JSON.parse(year);
nameOfFirstDay = JSON.parse(nameOfFirstDay);
daysInMonth = JSON.parse(daysInMonth);
vacations = JSON.parse(vacations);
avaliable_vacation_days = JSON.parse(avaliable_vacation_days);
total_days_vacations = JSON.parse(total_days_vacations);
monthly_days_vacations = JSON.parse(monthly_days_vacations);

const calendar = document.querySelector("#app-calendar2");
const chart_monthly = document.querySelector("#monthly_chart");
const chart_annual = document.querySelector("#annual_chart");

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
            <div class="day-hidden">
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

//Adding booked vacation days to calendar
for (let i of vacations){
    console.log(i);
    let day = (i.date.slice(8,10))[0] == 0 ? i.date.slice(9,10) : i.date.slice(8,10);
    let day_box = document.getElementById(day);
    day_box.classList.add('booked')


}

//Adding selector for days in calendar
document.querySelectorAll('#app-calendar2 .day').forEach(day => {
    day.addEventListener("click",event =>{
        event.currentTarget.classList.toggle('selected')
    })
})


//Drawing chart: monthly hours
new Chart(chart_monthly, {
    type: 'pie',
    data: {
      labels: [`Booked days in a month: ${monthly_days_vacations}`, `Total avaliable vacation days in a year:${avaliable_vacation_days}`],
      datasets: [{
        backgroundColor: ["#D6BA73", "#003249"],
        data: [monthly_days_vacations,avaliable_vacation_days]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Monthly booked days'
      }
    }
});


//Drawing chart: annual hours
new Chart(chart_annual, {
    type: 'pie',
    data: {
      labels: [`Booked days in a whole year: ${total_days_vacations}`, `Total avaliable vacation days in a year: ${avaliable_vacation_days}`],
      datasets: [{
        backgroundColor: ["#D6BA73", "#003249"],
        data: [total_days_vacations,avaliable_vacation_days]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Annual booked days'
      }
    }
});