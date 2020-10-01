Chart.defaults.global.legend.display = false;

const data = document.getElementById('chart-data').textContent;
const dataJson = JSON.parse(data);
const ctx = document.getElementById('hours_chart').getContext('2d');
const [labelsValues,dataValues] = getData(dataJson);





var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labelsValues,
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: dataValues
        }]
    },
    options: {
        scales: {
            yAxes: [{
                display: true,
                ticks: {
                    min: 0,
                    max: 16,
                    stepSize: 1
                }
            }]
        }
    }
});

function getData(jsondata){
    let labels = [];
    let data = [];
    let results=[];
    for (let i of jsondata){
        labels.push(i['date__date']);
        data.push(i['hours_in_day']);
    }
    results.push(labels,data)
    return results;
}


