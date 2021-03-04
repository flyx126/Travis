CREATE TABLE tbl_maestra(
    id SERIAL,
    clave VARCHAR(20),
    precio FLOAT,
    cantidad FLOAT,
    fecha DATE,
    mesero VARCHAR(10),
    hora TIME,
    mesa INT,
    notven INT,
    pers FLOAT,
    grupplat VARCHAR(10),
    partida FLOAT,
    descuento FLOAT,
    descr VARCHAR(80),
    costo FLOAT,
    unidad VARCHAR(10),
    dia_vendido INT,
    mes_vendido INT,
    anio_vendido INT,
    utilidad FLOAT,
    hora_vendido INT,
    nombre_mesero VARCHAR(80)
);

COPY tbl_maestra(clave,precio,cantidad,fecha,mesero,hora,mesa,notven,pers,grupplat,partida,descuento,descr,costo,unidad,dia_vendido,mes_vendido,anio_vendido,utilidad,hora_vendido,nombre_mesero) FROM '/src/csv/tabla_maestra_2015.csv' DELIMITER ',' CSV HEADER;

COPY tbl_maestra(clave,precio,cantidad,fecha,mesero,hora,mesa,notven,pers,grupplat,partida,descuento,descr,costo,unidad,dia_vendido,mes_vendido,anio_vendido,utilidad,hora_vendido,nombre_mesero) FROM '/src/csv/tabla_maestra_2016.csv' DELIMITER ',' CSV HEADER;

COPY tbl_maestra(clave,precio,cantidad,fecha,mesero,hora,mesa,notven,pers,grupplat,partida,descuento,descr,costo,unidad,dia_vendido,mes_vendido,anio_vendido,utilidad,hora_vendido,nombre_mesero) FROM '/src/csv/tabla_maestra_2017.csv' DELIMITER ',' CSV HEADER;

COPY tbl_maestra(clave,precio,cantidad,fecha,mesero,hora,mesa,notven,pers,grupplat,partida,descuento,descr,costo,unidad,dia_vendido,mes_vendido,anio_vendido,utilidad,hora_vendido,nombre_mesero) FROM '/src/csv/tabla_maestra_2018.csv' DELIMITER ',' CSV HEADER;

COPY tbl_maestra(clave,precio,cantidad,fecha,mesero,hora,mesa,notven,pers,grupplat,partida,descuento,descr,costo,unidad,dia_vendido,mes_vendido,anio_vendido,utilidad,hora_vendido,nombre_mesero) FROM '/src/csv/tabla_maestra_2019.csv' DELIMITER ',' CSV HEADER;

COPY tbl_maestra(clave,precio,cantidad,fecha,mesero,hora,mesa,notven,pers,grupplat,partida,descuento,descr,costo,unidad,dia_vendido,mes_vendido,anio_vendido,utilidad,hora_vendido,nombre_mesero) FROM '/src/csv/tabla_maestra_2020.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE costo_inventario(
    auxcosp FLOAT,
    descr VARCHAR (80),
    unidad VARCHAR(80),
    grupplat VARCHAR(20)
);

COPY costo_inventario (auxcosp,descr,unidad,grupplat) FROM '/src/csv/costo_inventario.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE users(
    id SERIAL,
    nombre VARCHAR (20),
    apellido VARCHAR (20),
    username VARCHAR(20),
    password VARCHAR(20)
);

INSERT INTO users(nombre,apellido,username,password) VALUES ('Mauricio','Montenegro','Mauricio','12345');