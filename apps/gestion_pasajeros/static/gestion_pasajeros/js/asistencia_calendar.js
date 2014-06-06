$( "#datepicker" ).multiDatesPicker({
    inline: true,
    altField: '#id_dates',
    dateFormat: "d/m/yy",
    changeMonth: true,
    changeYear: true,
    addDates: selectHolydaysAndWeekends(new Date()),
    onChangeMonthYear: function(year, month) {
        $('#datepicker').multiDatesPicker('resetDates', 'picked');
        $('#datepicker').multiDatesPicker('addDates',
            selectHolydaysAndWeekends(new Date(year, month - 1, 1)));
        $('#id_date').val($('#datepicker').multiDatesPicker('getDates'));
    }
});