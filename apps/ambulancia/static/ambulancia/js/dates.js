function isLeapYear(year) {
    if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
        return true;
    }
    return false;
}

function getDaysInMonth(year, month) {
    var months = {0: 31, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31,
        8: 30, 9: 31, 10: 30, 11: 31};

    if (isLeapYear(year)) {
        months[1] = 29;
    }
    else {
        months[1] = 28;
    }

    return months[month];
}

function getWeekends(date) {
    var daysInMonth = getDaysInMonth(date.getFullYear(),
        date.getMonth());

    var weekends = [];

    for (var i = 1; i <= daysInMonth; i++) {
        var day = new Date(date.setDate(i));
        if (day.getDay() == 0 || day.getDay() == 6) {
            weekends.push(day);
        }
    }
    return weekends;
}

function getHolydays(year, month) {
    var holydays = {2014:
                        {1: [1],
                         2: [],
                         3: [3, 4, 24],
                         4: [2, 17, 18],
                         5: [1, 2, 25],
                         6: [20],
                         7: [9],
                         8: [18],
                         9: [],
                         10: [13],
                         11: [24],
                         12: [8, 25, 26]},
                    2015:
                        {1: [1],
                         2: [16, 17],
                         3: [23, 24],
                         4: [2, 3],
                         5: [1, 25],
                         6: [20],
                         7: [9],
                         8: [17],
                         9: [],
                         10: [12],
                         11: [23],
                         12: [7, 8, 25]}
                     };

    try {
        var days = holydays[year][month]
        return days.map(function(d) {
            return new Date(year + "," + month + "," + d);
            });
        }
    catch (TypeError) {
        return [];
    }
}

function selectHolydaysAndWeekends(date) {
    var days = getWeekends(date);
    var holydays = getHolydays(date.getFullYear(), date.getMonth() + 1);
    if (holydays.length !== 0) {
        days = days.concat(holydays);
    }
    return days;
}
