/*
 |--------------------------------------------------------------------------
 | Shards Dashboards: Blog Overview Template
 |--------------------------------------------------------------------------
 */

var enviar_fecha = (fecha_menor, fecha_mayor) => {
    d3.json("/api/v1/indicadores/productos/productos_consulta", {
        method: "POST",
        body: JSON.stringify({ "fecha_menor": fecha_menor, "fecha_mayor": fecha_mayor }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }

    }).then(diccionario_datos => {


        function borrar_tabla(div) {
            d3.selectAll(div).remove()

        };
        if (diccionario_datos == "Error") {
            d3.select("#venta_platillos").text("No existen datos para las fechas seleccionadas")
            d3.select("#venta_bebidas").text("No existen datos para las fechas seleccionadas")
            d3.select("#venta_vino").text("No existen datos para las fechas seleccionadas")

            borrar_tabla(".nuevos")

        } else {

            d3.select("#venta_platillos").text("")
            d3.select("#venta_bebidas").text("")
            d3.select("#venta_vino").text("")
            borrar_tabla(".nuevos")

            var platillos_array = diccionario_datos.producto_mas_vendido_platillos.sort((a, b) => parseFloat(b['cantidad_platillos']) - parseFloat(a['cantidad_platillos']));
            var bebidas_array = diccionario_datos.producto_mas_vendido_bebidas.sort((a, b) => parseFloat(b['cantidad_bebidas']) - parseFloat(a['cantidad_bebidas']));
            var vinos_array = diccionario_datos.producto_mas_vendido_vinos.sort((a, b) => parseFloat(b['cantidad_vinos']) - parseFloat(a['cantidad_vinos']));
            var datos_platillos = platillos_array.map(x => { return { "Fecha": x.fecha, "Descripción": x.nombre, "Cantidad": x.cantidad_platillos, "Grupo de Platillos": x.grupo_platillo } })
            var datos_bebidas = bebidas_array.map(x => { return { "Fecha": x.fecha, "Descripción": x.nombre, "Cantidad": x.cantidad_bebidas, "Grupo de Platillos": x.grupo_platillo } })
            var datos_vinos = vinos_array.map(x => { return { "Fecha": x.fecha, "Descripción": x.nombre, "Cantidad": x.cantidad_vinos, "Grupo de Platillos": x.grupo_platillo } })


            d3.select("#venta_platillos").text(platillos_array[0]['nombre'])
            d3.select("#venta_bebidas").text(bebidas_array[0]['nombre'])
            d3.select("#venta_vino").text(vinos_array[0]['nombre'])

            d3.select("#vista_bebidas").style("display", "none")
            d3.select("#vista_vinos").style("display", "none")


            function crear_tabla(div, datos) {
                var tr = d3.select(div)
                    .selectAll("tr").data(datos).enter().append("tr").classed("nuevos", true);

                var td = tr.selectAll("td")
                    .data(function(d, i) { return Object.values(d); })
                    .enter().append("td")
                    .text(function(d) { return d; });
            };




            crear_tabla("#tabla_platillos tbody", datos_platillos)

            d3.select("#platillos_click").on("click", function() {
                d3.select("#vista_platillos").style("display", "block")
                d3.select("#vista_bebidas").style("display", "none")
                d3.select("#vista_vinos").style("display", "none")
                d3.select("#platillos_click").style("opacity", "1")
                d3.select("#bebidas_click").style("opacity", "0.3")
                d3.select("#vinos_click").style("opacity", "0.3")

                // datos_platillos = platillos_array.map(x => { return { "Fecha": x.fecha, "Descripción": x.nombre, "Cantidad": x.cantidad_platillos, "Grupo de Platillos": x.grupo_platillo } })
                crear_tabla("#tabla_platillos tbody", datos_platillos)
            });

            crear_tabla("#tabla_bebidas tbody", datos_bebidas)

            d3.select("#bebidas_click").on("click", function() {
                d3.select("#vista_platillos").style("display", "none")
                d3.select("#vista_bebidas").style("display", "block")
                d3.select("#vista_vinos").style("display", "none")
                d3.select("#platillos_click").style("opacity", "0.3")
                d3.select("#bebidas_click").style("opacity", "1")
                d3.select("#vinos_click").style("opacity", "0.3")


                crear_tabla("#tabla_bebidas tbody", datos_bebidas)

            });
            crear_tabla("#tabla_vinos tbody", datos_vinos)
            d3.select("#vinos_click").on("click", function() {
                d3.select("#vista_platillos").style("display", "none")
                d3.select("#vista_bebidas").style("display", "none")
                d3.select("#vista_vinos").style("display", "block")
                d3.select("#platillos_click").style("opacity", "0.3")
                d3.select("#bebidas_click").style("opacity", "0.3")
                d3.select("#vinos_click").style("opacity", "1")

                crear_tabla("#tabla_vinos tbody", datos_vinos)
            });



        };
    });
};

//Escuchador fecha calendario
$('#reportrange').on('apply.daterangepicker', function(ev, picker) {
    var fecha_menor = picker.startDate.format('YYYY-MM-DD');
    var fecha_mayor = picker.endDate.format('YYYY-MM-DD')
    console.log(fecha_menor)
    console.log(fecha_mayor)
    enviar_fecha(fecha_menor, fecha_mayor)
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
                    labels: ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5", "Label 6", "Label 7"],
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