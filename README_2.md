```SQL
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50) NOT NULL
);

CREATE TABLE producto (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipoProducto VARCHAR(50) NOT NULL
);

CREATE TABLE sucursal (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50) NOT NULL
);

CREATE TABLE inscripcion (
    idProducto INT,
    idCliente INT,
    PRIMARY KEY (idProducto, idCliente),
    FOREIGN KEY (idProducto) REFERENCES producto(id),
    FOREIGN KEY (idCliente) REFERENCES cliente(id)
);

CREATE TABLE disponibilidad (
    idSucursal INT,
    idProducto INT,
    PRIMARY KEY (idSucursal, idProducto),
    FOREIGN KEY (idSucursal) REFERENCES sucursal(id),
    FOREIGN KEY (idProducto) REFERENCES producto(id),
    cantidad INT NOT NULL
);

CREATE TABLE visitan (
    idSucursal INT,
    idCliente INT,
    fechaVisita DATE NOT NULL,
    PRIMARY KEY (idSucursal, idCliente),
    FOREIGN KEY (idSucursal) REFERENCES sucursal(id),
    FOREIGN KEY (idCliente) REFERENCES cliente(id)
);

INSERT INTO cliente (nombre, apellidos, ciudad) VALUES
('Juan', 'Pérez', 'Ciudad A'),
('Ana', 'López', 'Ciudad B'),
('Luis', 'García', 'Ciudad A');

INSERT INTO producto (nombre, tipoProducto) VALUES
('Producto 1', 'Tipo A'),
('Producto 2', 'Tipo B'),
('Producto 3', 'Tipo C');

INSERT INTO sucursal (nombre, ciudad) VALUES
('Sucursal 1', 'Ciudad A'),
('Sucursal 2', 'Ciudad B');

INSERT INTO inscripcion (idProducto, idCliente) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO disponibilidad (idSucursal, idProducto, cantidad) VALUES
(1, 1, 100),
(1, 2, 50),
(2, 3, 75);

INSERT INTO visitan (idSucursal, idCliente, fechaVisita) VALUES
(1, 1, '2023-10-01'),
(1, 2, '2023-10-01'),
(2, 2, '2023-10-02'),
(1, 3, '2023-10-03');
```

Solución 

```sql
SELECT DISTINCT c.nombre, c.apellidos
FROM cliente c
JOIN inscripcion i ON c.id = i.idCliente
JOIN disponibilidad d ON i.idProducto = d.idProducto
JOIN visitan v ON c.id = v.idCliente AND d.idSucursal = v.idSucursal
WHERE d.idProducto = i.idProducto;
```


https://sqlplayground.app/sandbox/6707af20c216ed00cb80899c

