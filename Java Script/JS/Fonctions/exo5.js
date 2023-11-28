let isLeap = function (year) {
    let isLeap = false;
    if (!(year % 400)) {
        isLeap = true;
    } else {
        if (!(year % 4) && (year % 100)) {
            isLeap = true;
        }
    }
    return isLeap;
}

let nbLeapYears = (date1, date2) => {
    let nbLeapYears = 0;
    for (let year=date1.getFullYear(); year<date2.getFullYear(); year++){
        if (isLeap(year)){
            nbLeapYears++;
        }
    }
    return(nbLeapYears);
};

let dateNow=new Date (Date.now());
let date2005Septembre22=new Date(2005, 12, 3);
console.log(nbLeapYears(date2005Septembre22, dateNow));