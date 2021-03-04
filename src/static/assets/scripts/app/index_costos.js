/*
 |--------------------------------------------------------------------------
 | Shards Dashboards: Blog Overview Template
 |--------------------------------------------------------------------------
 */

var enviar_fecha = (fecha_menor, fecha_mayor) => {
    d3.json("/api/v1/indicadores/analisis_costos/costos", {
        method: "POST",
        body: JSON.stringify({ "fecha_menor": fecha_menor, "fecha_mayor": fecha_mayor }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }

    }).then(diccionario_datos => {


        // console.log(diccionario_datos.map(function(x) { return x['platos'].map(function(y) { return [y['nombre'], y['porcentaje']] }) }))
        // var grupos = diccionario_datos.map(function(x) { return [x['grupo'], x['porcentaje'].toFixed(2) + "%"] })
        // var platillos = diccionario_datos.map(function(x) { return x['platos'].map(function(y) { return [y['nombre'], y['porcentaje']] }) })
        console.log(diccionario_datos)
            // console.log(grupos)
            // console.log(platillos)

        d3.selectAll(".labels").remove()
        d3.selectAll(".hide").remove()

        for (var a in diccionario_datos) {
            d3.select("#tabla_costos").append("tbody").classed("labels", true).attr("id", "grupplat" + a).append("tr").attr("id", "tr" + a).append("td").attr("id", "td" + a).append("label").attr("for", "grupplatG" + a).text(diccionario_datos[a]['grupo'])
            d3.select("#td" + a).append("input").attr("type", "checkbox").attr("name", "grupplatG" + a).attr("id", "grupplatG" + a).attr("data-toggle", "toggle")
            d3.select("#tr" + a).append("td").attr("id", "tdP" + a).append("label").attr("for", "grupplatP" + a).text(diccionario_datos[a]['porcentaje'].toFixed(2) + "%")
            d3.select("#tdP" + a).append("input").attr("type", "checkbox").attr("name", "grupplatP" + a).attr("id", "grupplatP" + a).attr("data-toggle", "toggle")
            d3.select("#tabla_costos").append("tbody").classed("hide", true).attr("id", "num" + a).style("display", "none")


            for (var b in diccionario_datos[a]['platos']) {
                var c = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
                d3.select("#num" + a).append("tr").attr("id", c[b] + a).append("td").text(diccionario_datos[a]['platos'][b]['nombre'])
                d3.select("#" + (c[b] + a)).append("td").text(diccionario_datos[a]['platos'][b]['porcentaje'].toFixed(2) + "%")

            }
        }

        $(document).ready(function() {
            $('[data-toggle="toggle"]').change(function() {
                $(this).parents().next('.hide').toggle();
            });
        });

    });
};


// d3.select("#tabla_costos").insert("tbody").classed("labels", true).attr("id", "grupplat4").append("tr").attr("id", "tr4").append("td").attr("id", "td4").append("label").attr("for", "grupplat4G").text("Grupplat4")
// d3.select("#td4").append("input").attr("type", "checkbox").attr("name", "grupplat4G").attr("id", "grupplat4G").attr("data-toggle", "toggle")
// d3.select("#tr4").append("td").attr("id", "td42").append("label").attr("for", "grupplat4P").text("25.36%")
// d3.select("#td42").append("input").attr("type", "checkbox").attr("name", "grupplat4P").attr("id", "grupplat4P").attr("data-toggle", "toggle")


// d3.select("#tabla_costos").insert("tbody").classed("hide", true).style("display", "none").attr("id", "grupplat4P").append("tr").attr("id", "tr4P").append("td").attr("id", "td4P").text("Platillo1")
// d3.select("tr4P").append("td").text("25.36%")

// $(document).ready(function() {
//     $('[data-toggle="toggle"]').change(function() {
//         $(this).parents().next('.hide').toggle();
//     });
// });


//Escuchador fecha calendario
$('#reportrange').on('apply.daterangepicker', function(ev, picker) {
    var fecha_menor = picker.startDate.format('YYYY-MM-DD');
    var fecha_mayor = picker.endDate.format('YYYY-MM-DD')
    console.log(fecha_menor)
    console.log(fecha_mayor)
    enviar_fecha(fecha_menor, fecha_mayor)
    console.log("termina enviar fecha")
});








'use strict';

(function($) {
    $(document).ready(function() {



        //
        // Small Stats
        //

        // Datasets
        var boSmallStatsDatasets = [{
                backgroundColor: 'rgba(0, 184, 216, 0.1)',
                borderColor: 'rgb(0, 184, 216)',
                data: [10, 2, 1, 3, 5, 4, 10],
            },
            {
                backgroundColor: 'rgba(23,198,113,0.1)',
                borderColor: 'rgb(23,198,113)',
                data: [1, 2, 3, 3, 3, 4, 4]
            },

        ];

        // Options
        function boSmallStatsOptions(max) {
            return {
                maintainAspectRatio: true,
                responsive: true,
                // Uncomment the following line in order to disable the animations.
                // animation: false,
                legend: {
                    display: false
                },
                tooltips: {
                    enabled: false,
                    custom: false
                },
                elements: {
                    point: {
                        radius: 0
                    },
                    line: {
                        tension: 0.3
                    }
                },
                scales: {
                    xAxes: [{
                        gridLines: false,
                        scaleLabel: false,
                        ticks: {
                            display: false
                        }
                    }],
                    yAxes: [{
                        gridLines: false,
                        scaleLabel: false,
                        ticks: {
                            display: false,
                            // Avoid getting the graph line cut of at the top of the canvas.
                            // Chart.js bug link: https://github.com/chartjs/Chart.js/issues/4790
                            suggestedMax: max
                        }
                    }],
                },
            };
        }

        // Generate the small charts
        boSmallStatsDatasets.map(function(el, index) {

            var chartOptions = boSmallStatsOptions(Math.max.apply(Math, el.data) + 1);
            var ctx = document.getElementsByClassName('blog-overview-stats-small-' + (index + 1));
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5", "Label 6"],
                    datasets: [{
                        label: 'Today',
                        fill: 'start',
                        data: el.data,
                        backgroundColor: el.backgroundColor,
                        borderColor: el.borderColor,
                        borderWidth: 1.5,
                    }]
                },
                options: chartOptions
            });
        });
    });
})(jQuery);