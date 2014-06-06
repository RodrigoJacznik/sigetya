$( "#fecha_emision" ).datepicker({
    inline: true,
    altField: "#id_fecha_emision",
    dateFormat: "d/m/yy",
});

$( "#mes_inicio" ).datepicker({
    inline: true,
    altField: "#id_mes_inicio",
    dateFormat: "d/m/yy",
    onSelect: function(selectedDate) {
        $("#mes_fin").datepicker("option", "minDate", selectedDate)
    }
});

$( "#mes_fin" ).datepicker({
    inline: true,
    altField: "#id_mes_fin",
    dateFormat: "d/m/yy",
    onSelect: function(selectedDate) {
        $("#mes_inicio").datepicker("option", "maxDate", selectedDate)
    }
});
