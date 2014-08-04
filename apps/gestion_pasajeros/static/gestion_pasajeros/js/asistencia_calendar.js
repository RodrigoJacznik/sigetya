$( "#datepicker" ).multiDatesPicker({
    inline: true,
    altField: '#id_dates',
    dateFormat: "d/m/yy",
    changeMonth: true,
    changeYear: true,
    addDates: selectHolydaysAndWeekends(new Date()),
    onChangeMonthYear: function(year, month) {
        var date = new Date(year, month - 1, 1);
        $(this).multiDatesPicker('resetDates', 'picked');
        $(this).multiDatesPicker('addDates',
            selectHolydaysAndWeekends(date));
        document.getElementById('id_dates').value = $(this).multiDatesPicker('getDates');
    }
});
