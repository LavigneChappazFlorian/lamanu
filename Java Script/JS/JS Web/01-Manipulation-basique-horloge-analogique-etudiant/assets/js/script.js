

let clocks = [
    {city: 'paris'},
    {city: 'london'},
    {city: 'newyork'},
    {city: 'tokyo'}
];

for (clock of clocks) {
    clock.p=document.querySelector('.'+clock.city+' p');
    clock.timezoneOffset=document.querySelector('.'+clock.city).dataset.timezone;
}

function updateClocks() {
    for (clock of clocks) {
        clocks.pop.innerText=getTime(clock.timezoneOffset);
    }
    setTimeout(updateClocks, 1000);
}

function getTime(timezoneOffset) {
    now = new Date();
    hours = (now.getUTChours() + Number(timezoneOffset))%24;
    minutes = String(now.getUTCMinutes()).padStart(2, '0');
    seconds = String(now.getUTCSeconds()).padStart(2, '0');
    return `${hours}:${minutes}:${seconds}`;
}
