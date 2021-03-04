/*
/*
 |--------------------------------------------------------------------------
 | Shards Dashboards: Blog Overview Template
 |--------------------------------------------------------------------------
 */
var usuarios = d3.select("#tabla_usuarios").property("content")
var tabla_usuarios = JSON.parse(usuarios)

console.log(tabla_usuarios[0])

crear_tabla("#tabla_usuarios tbody", tabla_usuarios)


var crear_usuario = (nombre, apellido, username, password) => {
    d3.json("/api/v1/indicadores/usuarios/crear_usuario", {
        method: "POST",
        body: JSON.stringify({ "nombre": nombre, "apellido": apellido, "username": username, "password": password }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }

    })

    crear_tabla("#tabla_usuarios tbody", tabla_usuarios)

};

//Escuchador crear usuario
d3.select("#crear_usuario").on("click", function() {
    location.reload();
    confirm("¿Estas seguro que quieres crear el usuario?")
    var nombre = d3.select("#nombre_crear").property("value")
    var apellido = d3.select("#apellido_crear").property("value")
    var username = d3.select("#usuario_crear").property("value")
    var password = d3.select("#password_crear").property("value")
    crear_usuario(nombre, apellido, username, password)
    location.reload();
});


var eliminar_usuario = (nombre, apellido) => {
    d3.json("/api/v1/indicadores/usuarios/eliminar_usuario", {
        method: "POST",
        body: JSON.stringify({ "nombre": nombre, "apellido": apellido }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }

    })

    crear_tabla("#tabla_usuarios tbody", tabla_usuarios)

};

//Escuchador eliminar usuario
d3.select("#eliminar_usuario").on("click", function() {
    location.reload();
    confirm("¿Estas seguro que quieres eliminar el usuario?")
    var nombre = d3.select("#nombre_eliminar").property("value")
    var apellido = d3.select("#apellido_eliminar").property("value")
    eliminar_usuario(nombre, apellido)
    location.reload();

});

function crear_tabla(div, datos) {
    var tr = d3.select(div)
        .selectAll("tr").data(datos).enter().append("tr").classed("nuevos", true);

    var td = tr.selectAll("td")
        .data(function(d, i) { return Object.values(d); })
        .enter().append("td")
        .text(function(d) { return d; });

};