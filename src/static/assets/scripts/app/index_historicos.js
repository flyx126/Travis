/*
 |--------------------------------------------------------------------------
 | Shards Dashboards: Blog Overview Template
 |--------------------------------------------------------------------------
 */

var enviar_fecha = (fecha_menor, fecha_mayor) => {
    d3.json("/api/v1/indicadores/historicos/historico_dia", {
        method: "POST",
        body: JSON.stringify({ "fecha_menor": fecha_menor, "fecha_mayor": fecha_mayor }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }

    }).then(diccionario_datos => {

        console.log(diccionario_datos)

        d3.select("#venta_del_dia").text("$" + diccionario_datos.monto_volumen[0]['monto'])
        d3.select("#costo_del_dia").text("$" + diccionario_datos.monto_volumen[0]['costo'])
        d3.select("#utilidad_del_dia").text("$" + diccionario_datos.monto_volumen[0]['utilidad'])
        d3.select('#mayor_venta_mesero').text("$" + diccionario_datos.mesero[1])
        d3.select("#cheque_promedio").text("$" + (diccionario_datos.monto_volumen[0]['venta'] / diccionario_datos.monto_volumen[0]['personas']).toFixed(2))

        d3.select("#costo").style("display", "none")
        d3.select("#utilidad").style("display", "none")
        d3.select("#mesero").style("display", "none")



        d3.select("#cheque_click").on("click", function() {
            d3.select("#costo").style("display", "none")
            d3.select("#monto_venta").style("display", "none")
            d3.select("#volumen_venta").style("display", "none")
            d3.select("#utilidad").style("display", "none")
            d3.select("#mesero").style("display", "none")
            d3.select("#costo_dia_click").style("opacity", "0.3")
            d3.select("#venta_dia_click").style("opacity", "0.3")
            d3.select("#utilidad_dia_click").style("opacity", "0.3")
            d3.select("#mesero_click").style("opacity", "0.3")
            d3.select("#cheque_click").style("opacity", "1")
            Plotly.purge('grafica_monto_venta_hora');
            Plotly.purge('grafica_volumen_venta_hora');
            Plotly.purge('grafica_costo_hora');
            Plotly.purge('grafica_utilidad_hora');
            Plotly.purge('grafica_mesero');
            Plotly.purge('grafica_monto_mesero');
        });

        // Grafica Monto de venta por hora

        var Venta_Total_Por_Hora = {
            x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),

            y: diccionario_datos.venta_por_hora.map(function(x) { return x['dinero'] }),
            type: 'scatter',
            line: { shape: 'spline' },
            name: 'Venta Total por hora',
            marker: { color: 'rgb(29, 53, 87)' }
        };

        var Venta_Bebidas_Por_Hora = {
            x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
            y: diccionario_datos.venta_por_hora.map(function(x) { return x['monto_venta_bebidas_hora'] }),
            type: 'bar',
            name: 'Venta Bebidas por hora',
            marker: { color: 'rgb(69, 123, 157 )' }
        };

        var Venta_Platillos_Por_Hora = {
            x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
            y: diccionario_datos.venta_por_hora.map(function(x) { return x['monto_venta_platillos_hora'] }),
            type: 'bar',
            name: 'Venta Platillos por hora',
            marker: { color: 'rgb(168, 218, 220)' }
        };

        var Venta_Vinos_Por_Hora = {
            x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
            y: diccionario_datos.venta_por_hora.map(function(x) { return x['monto_venta_vinos_hora'] }),
            type: 'bar',
            name: 'Venta Vinos por hora',
            marker: { color: 'rgb(230, 57, 70)' }
        };

        var layout_venta = {
            font: { size: 10 },
            xaxis: { tick0: 0, dtick: 1, title: { text: 'Hora' } },
            yaxis: { autorange: true, type: 'linear', title: { text: 'Monto de venta' } },
            barmode: 'group',
            autosize: true
        };

        var config = { responsive: true };

        var data_venta = [Venta_Total_Por_Hora, Venta_Bebidas_Por_Hora, Venta_Platillos_Por_Hora, Venta_Vinos_Por_Hora];

        Plotly.newPlot('grafica_monto_venta_hora', data_venta, layout_venta, config);

        // Grafica Volumen de venta por hora

        var Volumen_Total_Por_Hora = {
            x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
            y: diccionario_datos.venta_por_hora.map(function(x) { return x['volumen_venta'] }),
            type: 'scatter',
            line: { shape: 'spline' },
            name: 'Venta Total por hora',
            marker: { color: 'rgb(29, 53, 87)' }
        };

        var Volumen_Bebidas_Por_Hora = {
            x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
            y: diccionario_datos.venta_por_hora.map(function(x) { return x['volumen_venta_bebidas_hora'] }),
            type: 'bar',
            name: 'Venta Bebidas por hora',
            marker: { color: 'rgb(69, 123, 157 )' }
        };

        var Volumen_Platillos_Por_Hora = {
            x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
            y: diccionario_datos.venta_por_hora.map(function(x) { return x['volumen_venta_platillos_hora'] }),
            type: 'bar',
            name: 'Venta Platillos por hora',
            marker: { color: 'rgb(168, 218, 220)' }
        };

        var Volumen_Vinos_Por_Hora = {
            x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
            y: diccionario_datos.venta_por_hora.map(function(x) { return x['volumen_venta_vinos_hora'] }),
            type: 'bar',
            name: 'Venta Vinos por hora',
            marker: { color: 'rgb(230, 57, 70)' }
        };

        var layout_volumen = {
            font: { size: 10 },
            xaxis: { tick0: 0, dtick: 1, title: { text: 'Hora' } },
            yaxis: { autorange: true, type: 'linear', title: { text: 'Volumen de venta' } },
            barmode: 'group',
            autosize: true
        };

        config = { responsive: true };

        var data_volumen = [Volumen_Total_Por_Hora, Volumen_Bebidas_Por_Hora, Volumen_Platillos_Por_Hora, Volumen_Vinos_Por_Hora];

        Plotly.newPlot('grafica_volumen_venta_hora', data_volumen, layout_volumen, config);



        d3.select("#costo_dia_click").on("click", function() {
            d3.select("#costo").style("display", "block")
            d3.select("#monto_venta").style("display", "none")
            d3.select("#volumen_venta").style("display", "none")
            d3.select("#utilidad").style("display", "none")
            d3.select("#mesero").style("display", "none")
            d3.select("#costo_dia_click").style("opacity", "1")
            d3.select("#venta_dia_click").style("opacity", "0.3")
            d3.select("#utilidad_dia_click").style("opacity", "0.3")
            d3.select("#mesero_click").style("opacity", "0.3")
            d3.select("#cheque_click").style("opacity", "0.3")


            // Grafica Costo por hora

            var Costo_Total_Por_Hora = {
                x: diccionario_datos.costo_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.costo_por_hora.map(function(x) { return x['costo'] }),
                type: 'scatter',
                line: { shape: 'spline' },
                name: 'Costo Total por hora',
                marker: { color: 'rgb(29, 53, 87)' }
            };

            var Costo_Bebidas_Por_Hora = {
                x: diccionario_datos.costo_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.costo_por_hora.map(function(x) { return x['costo_bebidas_hora'] }),
                type: 'bar',
                name: 'Costo Bebidas por hora',
                marker: { color: 'rgb(69, 123, 157 )' }
            };

            var Costo_Platillos_Por_Hora = {
                x: diccionario_datos.costo_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.costo_por_hora.map(function(x) { return x['costo_platillos_hora'] }),
                type: 'bar',
                name: 'Costo Platillos por hora',
                marker: { color: 'rgb(168, 218, 220)' }
            };

            var Costo_Vinos_Por_Hora = {
                x: diccionario_datos.costo_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.costo_por_hora.map(function(x) { return x['costo_vinos_hora'] }),
                type: 'bar',
                name: 'Costo Vinos por hora',
                marker: { color: 'rgb(230, 57, 70)' }
            };

            var layout_costo = {
                font: { size: 10 },
                xaxis: { tick0: 0, dtick: 1, title: { text: 'Hora' } },
                yaxis: { autorange: true, type: 'linear', title: { text: 'Costo' } },
                barmode: 'group',
                autosize: true
            };

            config = { responsive: true };

            var data_costo = [Costo_Total_Por_Hora, Costo_Bebidas_Por_Hora, Costo_Platillos_Por_Hora, Costo_Vinos_Por_Hora];

            Plotly.newPlot('grafica_costo_hora', data_costo, layout_costo, config);

            Plotly.purge('grafica_monto_venta_hora');
            Plotly.purge('grafica_volumen_venta_hora');
            Plotly.purge('grafica_utilidad_hora');
            Plotly.purge('grafica_mesero');
            Plotly.purge('grafica_monto_mesero');

        });

        d3.select("#venta_dia_click").on("click", function() {
            d3.select("#monto_venta").style("display", "block")
            d3.select("#volumen_venta").style("display", "block")
            d3.select("#costo").style("display", "none")
            d3.select("#utilidad").style("display", "none")
            d3.select("#mesero").style("display", "none")
            d3.select("#costo_dia_click").style("opacity", "0.3")
            d3.select("#utilidad_dia_click").style("opacity", "0.3")
            d3.select("#venta_dia_click").style("opacity", "1")
            d3.select("#mesero_click").style("opacity", "0.3")
            d3.select("#cheque_click").style("opacity", "0.3")

            // Grafica Monto de venta por hora

            var Venta_Total_Por_Hora = {
                x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.venta_por_hora.map(function(x) { return x['dinero'] }),
                type: 'scatter',
                line: { shape: 'spline' },
                name: 'Venta Total por hora',
                marker: { color: 'rgb(29, 53, 87)' }
            };

            var Venta_Bebidas_Por_Hora = {
                x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.venta_por_hora.map(function(x) { return x['monto_venta_bebidas_hora'] }),
                type: 'bar',
                name: 'Venta Bebidas por hora',
                marker: { color: 'rgb(69, 123, 157 )' }
            };

            var Venta_Platillos_Por_Hora = {
                x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.venta_por_hora.map(function(x) { return x['monto_venta_platillos_hora'] }),
                type: 'bar',
                name: 'Venta Platillos por hora',
                marker: { color: 'rgb(168, 218, 220)' }
            };

            var Venta_Vinos_Por_Hora = {
                x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.venta_por_hora.map(function(x) { return x['monto_venta_vinos_hora'] }),
                type: 'bar',
                name: 'Venta Vinos por hora',
                marker: { color: 'rgb(230, 57, 70)' }
            };

            var layout_venta = {
                font: { size: 10 },
                xaxis: { tick0: 0, dtick: 1, title: { text: 'Hora' } },
                yaxis: { autorange: true, type: 'linear', title: { text: 'Monto de venta' } },
                barmode: 'group',
                autosize: true
            };

            var config = { responsive: true };

            var data_venta = [Venta_Total_Por_Hora, Venta_Bebidas_Por_Hora, Venta_Platillos_Por_Hora, Venta_Vinos_Por_Hora];

            Plotly.newPlot('grafica_monto_venta_hora', data_venta, layout_venta, config);

            // Grafica Volumen de venta por hora

            var Volumen_Total_Por_Hora = {
                x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.venta_por_hora.map(function(x) { return x['volumen_venta'] }),
                type: 'scatter',
                line: { shape: 'spline' },
                name: 'Venta Total por hora',
                marker: { color: 'rgb(29, 53, 87)' }
            };

            var Volumen_Bebidas_Por_Hora = {
                x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.venta_por_hora.map(function(x) { return x['volumen_venta_bebidas_hora'] }),
                type: 'bar',
                name: 'Venta Bebidas por hora',
                marker: { color: 'rgb(69, 123, 157 )' }
            };

            var Volumen_Platillos_Por_Hora = {
                x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.venta_por_hora.map(function(x) { return x['volumen_venta_platillos_hora'] }),
                type: 'bar',
                name: 'Venta Platillos por hora',
                marker: { color: 'rgb(168, 218, 220)' }
            };

            var Volumen_Vinos_Por_Hora = {
                x: diccionario_datos.venta_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.venta_por_hora.map(function(x) { return x['volumen_venta_vinos_hora'] }),
                type: 'bar',
                name: 'Venta Vinos por hora',
                marker: { color: 'rgb(230, 57, 70)' }
            };

            var layout_volumen = {
                font: { size: 10 },
                xaxis: { tick0: 0, dtick: 1, title: { text: 'Hora' } },
                yaxis: { autorange: true, type: 'linear', title: { text: 'Volumen de venta' } },
                barmode: 'group',
                autosize: true
            };

            config = { responsive: true };

            var data_volumen = [Volumen_Total_Por_Hora, Volumen_Bebidas_Por_Hora, Volumen_Platillos_Por_Hora, Volumen_Vinos_Por_Hora];

            Plotly.newPlot('grafica_volumen_venta_hora', data_volumen, layout_volumen, config);

            Plotly.purge('grafica_costo_hora');
            Plotly.purge('grafica_utilidad_hora');
            Plotly.purge('grafica_mesero');
            Plotly.purge('grafica_monto_mesero');

        });

        d3.select("#utilidad_dia_click").on("click", function() {
            d3.select("#utilidad").style("display", "block")
            d3.select("#monto_venta").style("display", "none")
            d3.select("#volumen_venta").style("display", "none")
            d3.select("#costo").style("display", "none")
            d3.select("#mesero").style("display", "none")
            d3.select("#costo_dia_click").style("opacity", "0.3")
            d3.select("#utilidad_dia_click").style("opacity", "1")
            d3.select("#venta_dia_click").style("opacity", "0.3")
            d3.select("#mesero_click").style("opacity", "0.3")
            d3.select("#cheque_click").style("opacity", "0.3")


            // Grafica Utilidad por hora

            var Utilidad_Total_Por_Hora = {
                x: diccionario_datos.utilidad_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.utilidad_por_hora.map(function(x) { return x['utilidad'] }),
                type: 'scatter',
                line: { shape: 'spline' },
                name: 'Utilidad Total por hora',
                marker: { color: 'rgb(29, 53, 87)' }
            };

            var Utilidad_Bebidas_Por_Hora = {
                x: diccionario_datos.utilidad_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.utilidad_por_hora.map(function(x) { return x['utilidad_bebidas_hora'] }),
                type: 'bar',
                name: 'Utilidad Bebidas por hora',
                marker: { color: 'rgb(69, 123, 157 )' }
            };

            var Utilidad_Platillos_Por_Hora = {
                x: diccionario_datos.utilidad_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.utilidad_por_hora.map(function(x) { return x['utilidad_platillos_hora'] }),
                type: 'bar',
                name: 'Utilidad Platillos por hora',
                marker: { color: 'rgb(168, 218, 220)' }
            };

            var Utilidad_Vinos_Por_Hora = {
                x: diccionario_datos.utilidad_por_hora.map(function(x) { return x['hora'] }),
                y: diccionario_datos.utilidad_por_hora.map(function(x) { return x['utilidad_vinos_hora'] }),
                type: 'bar',
                name: 'Utilidad Vinos por hora',
                marker: { color: 'rgb(230, 57, 70)' }
            };

            var layout_utilidad = {
                font: { size: 10 },
                xaxis: { tick0: 0, dtick: 1, title: { text: 'Hora' } },
                yaxis: { autorange: true, type: 'linear', title: { text: 'Utilidad' } },
                barmode: 'group',
                autosize: true,
            };

            config = { responsive: true };

            var data_utilidad = [Utilidad_Total_Por_Hora, Utilidad_Bebidas_Por_Hora, Utilidad_Platillos_Por_Hora, Utilidad_Vinos_Por_Hora];

            Plotly.newPlot('grafica_utilidad_hora', data_utilidad, layout_utilidad, config);

            Plotly.purge('grafica_costo_hora');
            Plotly.purge('grafica_mesero');
            Plotly.purge('grafica_monto_mesero');
            Plotly.purge('grafica_monto_venta_hora');
            Plotly.purge('grafica_volumen_venta_hora');

        });

        d3.select("#mesero_click").on("click", function() {
            d3.select("#mesero").style("display", "block")
            d3.select("#monto_venta").style("display", "none")
            d3.select("#volumen_venta").style("display", "none")
            d3.select("#costo").style("display", "none")
            d3.select("#utilidad").style("display", "none")
            d3.select("#mesero_click").style("opacity", "1")
            d3.select("#utilidad_dia_click").style("opacity", "0.3")
            d3.select("#venta_dia_click").style("opacity", "0.3")
            d3.select("#costo_dia_click").style("opacity", "0.3")
            d3.select("#cheque_click").style("opacity", "0.3")


            // Graficas Mesero

            var Venta_Total_Mesero = {
                x: diccionario_datos.mesero[0].map(function(x) { return x['venta'] }),
                y: diccionario_datos.mesero[0].map(function(x) { return x['nombre'] }),
                type: 'bar',
                orientation: 'h',
                name: 'Venta total por mesero',
                marker: { color: 'rgb(29, 53, 87)' }
            };

            var Utilidad_Mesero = {
                x: diccionario_datos.mesero[0].map(function(x) { return x['utilidad'] }),
                y: diccionario_datos.mesero[0].map(function(x) { return x['nombre'] }),
                type: 'bar',
                orientation: 'h',
                name: 'Utilidad total por mesero',
                marker: { color: 'rgb(69, 123, 157 )' }
            };

            var Volumen_Platillos_Mesero = {
                x: diccionario_datos.mesero[0].map(function(x) { return x['nombre'] }),
                y: diccionario_datos.mesero[0].map(function(x) { return x['volumen_platillos'] }),
                type: 'bar',
                name: 'Volumen Platillos por mesero',
                marker: { color: 'rgb(168, 218, 220)' }
            };

            var Volumen_Bebidas_Mesero = {
                x: diccionario_datos.mesero[0].map(function(x) { return x['nombre'] }),
                y: diccionario_datos.mesero[0].map(function(x) { return x['volumen_bebidas'] }),
                type: 'bar',
                name: 'Volumen Bebidas por mesero',
                marker: { color: 'rgb(69, 123, 157 )' }
            };

            var Volumen_Vinos_Mesero = {
                x: diccionario_datos.mesero[0].map(function(x) { return x['nombre'] }),
                y: diccionario_datos.mesero[0].map(function(x) { return x['volumen_vinos'] }),
                type: 'bar',
                name: 'Volumen Vinos por mesero',
                marker: { color: 'rgb(230, 57, 70)' }
            };

            var Monto_Platillos_Mesero = {
                x: diccionario_datos.mesero[0].map(function(x) { return x['nombre'] }),
                y: diccionario_datos.mesero[0].map(function(x) { return x['monto_platillos'] }),
                type: 'bar',
                name: 'Monto Platillos por mesero',
                marker: { color: 'rgb(168, 218, 220)' }
            };

            var Monto_Bebidas_Mesero = {
                x: diccionario_datos.mesero[0].map(function(x) { return x['nombre'] }),
                y: diccionario_datos.mesero[0].map(function(x) { return x['monto_bebidas'] }),
                type: 'bar',
                name: 'Monto Bebidas por mesero',
                marker: { color: 'rgb(69, 123, 157 )' }
            };

            var Monto_Vinos_Mesero = {
                x: diccionario_datos.mesero[0].map(function(x) { return x['nombre'] }),
                y: diccionario_datos.mesero[0].map(function(x) { return x['monto_vinos'] }),
                type: 'bar',
                name: 'Monto Vinos por mesero',
                marker: { color: 'rgb(230, 57, 70)' }
            };


            var layout_mesero = {
                font: { size: 10 },
                xaxis: { autorange: true, title: { text: 'Venta' } },
                yaxis: { autorange: true, title: { text: 'Nombre' } },
                margin: {
                    l: 150
                },
                barmode: 'group',
                autosize: true
            };

            var layout_volumen_mesero = {
                font: { size: 10 },
                xaxis: { autorange: true, title: { text: 'Nombre' } },
                yaxis: { autorange: true, title: { text: 'Volumen' } },
                autosize: true,
                barmode: 'group'

            };

            var layout_monto_mesero = {
                font: { size: 10 },
                xaxis: { autorange: true, title: { text: 'Nombre' } },
                yaxis: { autorange: true, title: { text: 'Monto' } },
                autosize: true,
                barmode: 'group'

            }

            config = { responsive: true };

            var data_mesero = [Venta_Total_Mesero, Utilidad_Mesero];
            var data_volumen_mesero = [Volumen_Platillos_Mesero, Volumen_Bebidas_Mesero, Volumen_Vinos_Mesero];
            var data_monto_mesero = [Monto_Platillos_Mesero, Monto_Bebidas_Mesero, Monto_Vinos_Mesero];

            Plotly.newPlot('grafica_mesero', data_mesero, layout_mesero, config);
            Plotly.newPlot('grafica_volumen_mesero', data_volumen_mesero, layout_volumen_mesero, config = { responsive: true });
            Plotly.newPlot('grafica_monto_mesero', data_monto_mesero, layout_monto_mesero, config = { responsive: true });

            Plotly.purge('grafica_costo_hora');
            Plotly.purge('grafica_monto_venta_hora');
            Plotly.purge('grafica_volumen_venta_hora');
            Plotly.purge('grafica_utilidad_hora');
        });



    });
};

//Escuchador fecha calendario
$('#reportrange').on('apply.daterangepicker', function(ev, picker) {
    var fecha_menor = picker.startDate.format('YYYY-MM-DD');
    var fecha_mayor = picker.endDate.format('YYYY-MM-DD')
    console.log(fecha_menor)
    console.log(fecha_mayor)
        // d3.select(".texto-loader").text("Cargando Datos")
        // d3.select("#loader-container").style("display", "block")
    enviar_fecha(fecha_menor, fecha_mayor)
});

// var diccionario = d3.select("#dictionary_index").property("content")
// var diccionario_datos = JSON.parse(diccionario)
// console.log(diccionario_datos)


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
            {
                backgroundColor: 'rgba(255,65,105,0.1)',
                borderColor: 'rgb(255,65,105)',
                data: [1, 7, 1, 3, 1, 4, 8]
            },
            {
                backgroundColor: 'rgb(0,123,255,0.1)',
                borderColor: 'rgb(0,123,255)',
                data: [3, 2, 3, 2, 4, 5, 4]
            }
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