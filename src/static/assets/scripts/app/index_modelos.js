/*
 |--------------------------------------------------------------------------
 | Shards Dashboards: Blog Overview Template
 |--------------------------------------------------------------------------
 */

d3.select("#vista_distribucion").on("click", function() {
    d3.select("#calendario_modelos").style("display", "block")
    d3.select("#calendario_estancia").style("display", "none")
    d3.select("#grupo_platillo").style("display", "none")
    d3.select("#grafica_mes").style("display", "block")
    d3.select("#grafica_semana").style("display", "block")
    d3.select("#grafica_tiempo").style("display", "block")
    d3.select("#grafica_tendencia").style("display", "none")
    d3.select("#grafica_tendencia_venta").style("display", "none")
    d3.select("#histograma").style("display", "none")
    d3.select("#vista_distribucion").style("opacity", "1")
    d3.select("#vista_tendencia").style("opacity", "0.3")
    d3.select("#vista_histograma").style("opacity", "0.3")

});

d3.select("#vista_tendencia").on("click", function() {
    d3.select("#grupo_platillo").style("display", "block")
    d3.select("#calendario_modelos").style("display", "none")
    d3.select("#calendario_estancia").style("display", "none")
    d3.select("#grafica_mes").style("display", "none")
    d3.select("#grafica_semana").style("display", "none")
    d3.select("#grafica_tiempo").style("display", "none")
    d3.select("#grafica_tendencia").style("display", "block")
    d3.select("#grafica_tendencia_venta").style("display", "block")
    d3.select("#histograma").style("display", "none")
    d3.select("#vista_distribucion").style("opacity", "0.3")
    d3.select("#vista_tendencia").style("opacity", "1")
    d3.select("#vista_histograma").style("opacity", "0.3")

});

d3.select("#vista_histograma").on("click", function() {
    d3.select("#grupo_platillo").style("display", "none")
    d3.select("#calendario_modelos").style("display", "none")
    d3.select("#calendario_estancia").style("display", "block")
    d3.select("#grafica_mes").style("display", "none")
    d3.select("#grafica_semana").style("display", "none")
    d3.select("#grafica_tiempo").style("display", "none")
    d3.select("#grafica_tendencia").style("display", "none")
    d3.select("#grafica_tendencia_venta").style("display", "none")
    d3.select("#histograma").style("display", "block")
    d3.select("#vista_distribucion").style("opacity", "0.3")
    d3.select("#vista_tendencia").style("opacity", "0.3")
    d3.select("#vista_histograma").style("opacity", "1")

});


var enviar_fecha = (fecha_menor_distribucion, fecha_mayor_distribucion) => {
    d3.json("/api/v1/indicadores/modelos/distribucion_demanda", {
        method: "POST",
        body: JSON.stringify({ "fecha_menor": fecha_menor_distribucion, "fecha_mayor": fecha_mayor_distribucion }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }

    }).then(diccionario_datos => {

        if (diccionario_datos == "Error") {
            d3.select("#grafica_distribucion_demanda_mes").text("No existen datos para las fechas seleccionadas")
            d3.select("#grafica_distribucion_demanda_semana").text("No existen datos para las fechas seleccionadas")
            d3.select("#grafica_distribucion_demanda_tiempo").text("No existen datos para las fechas seleccionadas")
        } else {
            d3.select("#grafica_distribucion_demanda_mes").text("")
            d3.select("#grafica_distribucion_demanda_semana").text("")
            d3.select("#grafica_distribucion_demanda_tiempo").text("")
                // Grafica Distribucion Demanda por Mes
            var Venta_Alimentos_Mes = {
                x: diccionario_datos.mes.dia,
                y: diccionario_datos.mes.alimentos,
                type: 'bar',
                name: 'Alimentos',
                marker: { color: 'rgb(87, 117, 144)' }
            };

            var Venta_Bebidas_No_Alcoholicas_Mes = {
                x: diccionario_datos.mes.dia,
                y: diccionario_datos.mes.bebidas_no_alcoholicas,
                type: 'bar',
                name: 'Bebidas No Alcoholicas',
                marker: { color: 'rgb(67, 170, 139)' }
            };

            var Venta_Postres_Mes = {
                x: diccionario_datos.mes.dia,
                y: diccionario_datos.mes.postres,
                type: 'bar',
                name: 'Postres',
                marker: { color: 'rgb(144, 190, 109)' }
            };

            var Venta_Vinos_Mes = {
                x: diccionario_datos.mes.dia,
                y: diccionario_datos.mes.vinos,
                type: 'bar',
                name: 'Vinos',
                marker: { color: 'rgb(249, 199, 79)' }
            };

            var Venta_Cafe_Mes = {
                x: diccionario_datos.mes.dia,
                y: diccionario_datos.mes.cafe,
                type: 'bar',
                name: 'Café',
                marker: { color: 'rgb(248, 150, 30)' }
            };

            var Venta_Alcohol_Mes = {
                x: diccionario_datos.mes.dia,
                y: diccionario_datos.mes.alcohol,
                type: 'bar',
                name: 'Alcohol',
                marker: { color: 'rgb(243, 114, 44)' }
            };

            var layout_venta_mes = {
                font: { size: 10 },
                xaxis: { tick0: 0, dtick: 1, title: { text: 'Día del mes' } },
                yaxis: { autorange: true, type: 'linear', title: { text: 'Cantidad Vendido' } },
                barmode: 'stack',
                autosize: true
            };

            var config = { responsive: true };

            var data_distribucion_mes = [Venta_Alimentos_Mes, Venta_Bebidas_No_Alcoholicas_Mes, Venta_Postres_Mes, Venta_Cafe_Mes, Venta_Alcohol_Mes, Venta_Vinos_Mes];

            Plotly.newPlot('grafica_distribucion_demanda_mes', data_distribucion_mes, layout_venta_mes, config);


            // Grafica Distribucion Demanda por Semana
            var Venta_Alimentos_Semana = {
                x: diccionario_datos.semana.dia,
                y: diccionario_datos.semana.alimentos,
                type: 'bar',
                name: 'Alimentos',
                marker: { color: 'rgb(87, 117, 144)' }
            };


            var Venta_Bebidas_No_Alcoholicas_Semana = {
                x: diccionario_datos.semana.dia,
                y: diccionario_datos.semana.bebidas_no_alcoholicas,
                type: 'bar',
                name: 'Bebidas No Alcoholicas',
                marker: { color: 'rgb(67, 170, 139)' }
            };

            var Venta_Postres_Semana = {
                x: diccionario_datos.semana.dia,
                y: diccionario_datos.semana.postres,
                type: 'bar',
                name: 'Postres',
                marker: { color: 'rgb(144, 190, 109)' }
            };

            var Venta_Vinos_Semana = {
                x: diccionario_datos.semana.dia,
                y: diccionario_datos.semana.vinos,
                type: 'bar',
                name: 'Vinos',
                marker: { color: 'rgb(249, 199, 79)' }
            };

            var Venta_Cafe_Semana = {
                x: diccionario_datos.semana.dia,
                y: diccionario_datos.semana.cafe,
                type: 'bar',
                name: 'Café',
                marker: { color: 'rgb(248, 150, 30)' }
            };

            var Venta_Alcohol_Semana = {
                x: diccionario_datos.semana.dia,
                y: diccionario_datos.semana.alcohol,
                type: 'bar',
                name: 'Alcohol',
                marker: { color: 'rgb(243, 114, 44)' }
            };

            var layout_venta_semana = {
                font: { size: 10 },
                xaxis: { tick0: 0, dtick: 1, title: { text: 'Día de la semana' } },
                yaxis: { autorange: true, type: 'linear', title: { text: 'Cantidad Vendido' } },
                barmode: 'stack',
                autosize: true
            };

            var config = { responsive: true };

            var data_distribucion_semana = [Venta_Alimentos_Semana, Venta_Bebidas_No_Alcoholicas_Semana, Venta_Postres_Semana, Venta_Cafe_Semana, Venta_Alcohol_Semana, Venta_Vinos_Semana];

            Plotly.newPlot('grafica_distribucion_demanda_semana', data_distribucion_semana, layout_venta_semana, config);


            // Grafica Distribucion Demanda por Tiempo
            var Venta_Alimentos_Tiempo = {
                x: diccionario_datos.tiempo.dia,
                y: diccionario_datos.tiempo.alimentos,
                type: 'bar',
                name: 'Alimentos',
                marker: { color: 'rgb(87, 117, 144)' }
            };


            var Venta_Bebidas_No_Alcoholicas_Tiempo = {
                x: diccionario_datos.tiempo.dia,
                y: diccionario_datos.tiempo.bebidas_no_alcoholicas,
                type: 'bar',
                name: 'Bebidas No Alcoholicas',
                marker: { color: 'rgb(67, 170, 139)' }
            };

            var Venta_Postres_Tiempo = {
                x: diccionario_datos.tiempo.dia,
                y: diccionario_datos.tiempo.postres,
                type: 'bar',
                name: 'Postres',
                marker: { color: 'rgb(144, 190, 109)' }
            };

            var Venta_Vinos_Tiempo = {
                x: diccionario_datos.tiempo.dia,
                y: diccionario_datos.tiempo.vinos,
                type: 'bar',
                name: 'Vinos',
                marker: { color: 'rgb(249, 199, 79)' }
            };

            var Venta_Cafe_Tiempo = {
                x: diccionario_datos.tiempo.dia,
                y: diccionario_datos.tiempo.cafe,
                type: 'bar',
                name: 'Café',
                marker: { color: 'rgb(248, 150, 30)' }
            };

            var Venta_Alcohol_Tiempo = {
                x: diccionario_datos.tiempo.dia,
                y: diccionario_datos.tiempo.alcohol,
                type: 'bar',
                name: 'Alcohol',
                marker: { color: 'rgb(243, 114, 44)' }
            };

            var layout_venta_tiempo = {
                font: { size: 10 },
                xaxis: { title: { text: 'Tiempo de estancia' } },
                yaxis: { autorange: true, type: 'linear', title: { text: 'Cantidad Vendido' } },
                barmode: 'stack',
                autosize: true
            };

            var config = { responsive: true };

            var data_distribucion_tiempo = [Venta_Alimentos_Tiempo, Venta_Bebidas_No_Alcoholicas_Tiempo, Venta_Postres_Tiempo, Venta_Cafe_Tiempo, Venta_Alcohol_Tiempo, Venta_Vinos_Tiempo];

            Plotly.newPlot('grafica_distribucion_demanda_tiempo', data_distribucion_tiempo, layout_venta_tiempo, config);

        };

    });
};

//Escuchador fecha calendario
$('#reportrange').on('apply.daterangepicker', function(ev, picker) {
    var fecha_menor_distribucion = picker.startDate.format('YYYY-MM-DD');
    var fecha_mayor_distribucion = picker.endDate.format('YYYY-MM-DD')
    enviar_fecha(fecha_menor_distribucion, fecha_mayor_distribucion)
});

var tendencia_venta = (grupo_platillo) => {
    d3.json("/api/v1/indicadores/modelos/tendencia_venta", {
        method: "POST",
        body: JSON.stringify({ "grupplat": grupo_platillo }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }

    }).then(diccionario_datos => {

        var tendencia_2016 = {
            x: diccionario_datos.venta_platillos_2016.mes,
            y: diccionario_datos.venta_platillos_2016.cantidad,
            type: 'scatter',
            name: 'Tendencia de Venta 2016',
            marker: { color: 'rgb(244, 96, 54)' }
        };
        var tendencia_2017 = {
            x: diccionario_datos.venta_platillos_2017.mes,
            y: diccionario_datos.venta_platillos_2017.cantidad,
            type: 'scatter',
            name: 'Tendencia de Venta 2017',
            marker: { color: 'rgb(46, 41, 78)' }
        };

        var tendencia_2018 = {
            x: diccionario_datos.venta_platillos_2018.mes,
            y: diccionario_datos.venta_platillos_2018.cantidad,
            type: 'scatter',
            name: 'Tendencia de Venta 2018',
            marker: { color: 'rgb(27, 153, 139)' }
        };

        var tendencia_2019 = {
            x: diccionario_datos.venta_platillos_2019.mes,
            y: diccionario_datos.venta_platillos_2019.cantidad,
            type: 'scatter',
            name: 'Tendencia de Venta 2019',
            marker: { color: 'rgb(231, 29, 54)' }
        };

        var tendencia_2020 = {
            x: diccionario_datos.venta_platillos_2020.mes,
            y: diccionario_datos.venta_platillos_2020.cantidad,
            type: 'scatter',
            name: 'Tendencia de Venta 2020',
            marker: { color: 'rgb(197, 216, 109)' }
        };

        var layout_tendencia = {
            font: { size: 10 },
            xaxis: { tick0: 0, dtick: 1, title: { text: 'Mes' } },
            yaxis: { autorange: true, type: 'linear', title: { text: 'Cantidad' } },
            autosize: true,
            title: d3.select("#grupos option:checked").text()
        };

        var config = { responsive: true };

        var data_tendencia = [tendencia_2016, tendencia_2017, tendencia_2018, tendencia_2019, tendencia_2020];

        Plotly.newPlot('grafica_tendencia', data_tendencia, layout_tendencia, config);



    });
};
//Escuchador Grupo Platillo Tendencia de venta
d3.select("#grupos").on("change", function() {

    var grupo_platillo = d3.select("#grupos option:checked").text()
    if (grupo_platillo == "Platillos") {
        grupo_platillo = 'A%%'
    } else if (grupo_platillo == "Bebidas") {
        grupo_platillo = 'B%%'
    } else if (grupo_platillo == "Vinos") {
        grupo_platillo = 'V%%'
    }
    tendencia_venta(grupo_platillo)
});



var enviar_fecha_estancia = (fecha_menor, fecha_mayor) => {
    d3.json("/api/v1/indicadores/modelos/estancia", {
        method: "POST",
        body: JSON.stringify({ "fecha_menor": fecha_menor, "fecha_mayor": fecha_mayor }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }

    }).then(diccionario_datos => {
        console.log(diccionario_datos)
        if (diccionario_datos == "Error") {
            d3.select("#grafica_histograma").text("No existen datos para las fechas seleccionadas")
        } else {
            d3.select("#grafica_histograma").text("")
            var trace_histograma = {
                x: diccionario_datos.tiempo,
                type: 'histogram',
                marker: { color: 'rgb(120, 161, 187' }
            };
            var data_histograma = [trace_histograma];

            var layout_histograma = {
                font: { size: 10 },
                xaxis: { title: { text: 'Tiempo de Estancia' } },
                yaxis: { autorange: true, type: 'linear', title: { text: 'Cantidad' } },
                autosize: true,
            }

            var config = { responsive: true };
            Plotly.newPlot('grafica_histograma', data_histograma, layout_histograma, config)
        };
    });

};

$('#reportrange_estancia').on('apply.daterangepicker', function(ev, picker) {
    var fecha_menor = picker.startDate.format('YYYY-MM-DD');
    var fecha_mayor = picker.endDate.format('YYYY-MM-DD')
    enviar_fecha_estancia(fecha_menor, fecha_mayor)

});


'use strict';

(function($) {
    $(document).ready(function() {

        // Blog overview date range init.
        $('#blog-overview-date-range').datepicker({});

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
            {
                backgroundColor: 'rgba(255,180,0,0.1)',
                borderColor: 'rgb(255,180,0)',
                data: [2, 3, 3, 3, 4, 3, 3]
            },
            // {
            //     backgroundColor: 'rgba(255,65,105,0.1)',
            //     borderColor: 'rgb(255,65,105)',
            //     data: [1, 7, 1, 3, 1, 4, 8]
            // },
            // {
            //     backgroundColor: 'rgb(0,123,255,0.1)',
            //     borderColor: 'rgb(0,123,255)',
            //     data: [3, 2, 3, 2, 4, 5, 4]
            // }
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
                    labels: ["Label 1", "Label 2", "Label 3"],
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