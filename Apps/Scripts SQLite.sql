-- SQLite
DELETE FROM roles;
DELETE FROM roles_asignados;
DELETE FROM registro_asistencias;
DELETE FROM colaboradores;

select * from colaboradores;
select * from permisos;
select * from tipos_de_permisos;
select * from departamento;

select * from empresas;
select * from jefes;
select * from sucursal;
select * from unidad_de_negocio;

INSERT INTO tipos_de_permisos (nombre_permiso) VALUES
('enfermedad'),
('vacaciones'),
('defuncion'),
('Lactancia'),
('tiempo libre no remunerado'),
('Otros');

INSERT INTO departamento(nombre_departamento, fechacreacion, fechaactualizacion, estado) VALUES
('ACERO222', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('ADMINISTRACIÓN', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('AUDITORÍA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('BODEGA CEDIS', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('BODEGA CEMENTO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('BODEGA CERÁMICA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('BODEGA HIERRO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('BODEGA MADERA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('BODEGA TIENDA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('CAJA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('COMPRAS', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('CONCRETO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('CONTABILIDAD', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('CRÉDITOS Y RECUPERACIONES', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('D.O.', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('FINANZAS', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('GERENCIA GENERAL', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('GESTIÓN DE CALIDAD', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('INGRESOS', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('INVENTARIO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('IT', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('LEGAL', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('LIMPIEZA Y ASEO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('LOGISTICA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('LOGÍSTICA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('MÉDICO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('MERCADEO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('MONITOREO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('OPERACIONES', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('PRODUCCIÓN', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('RRHH', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('SEGURIDAD', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('TALLER DE MANTENIMIENTO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('TESORERÍA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('VENTAS CAFETERÍA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('VENTAS CALL CENTER', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('VENTAS CONTRATISTA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('VENTAS MAYOREO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('VENTAS PROYECTOS', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('VENTAS SUPER TIENDA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO');

INSERT INTO empresas (nombre_empresa, fechacreacion, fechaactualizacion, estado)
VALUES ('PROMACO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('IMPORTADORA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('PROMACO PRODUCCIÓN', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('URBANIZADORA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('TRITURADOS', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO');

INSERT INTO jefes (codigo, identidadjefe, nombrejefe, estado, fechacreacion, fechaactualizacion)
VALUES 
('JF-1', '0601188925634', 'LUIS ALBERTO RODRIGUEZ', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('JF-2', '060119980042', 'NANCY PATRICIA MENDOZA HERNANDEZ', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('JF-3', '0601199900043', 'JOSE MANUEL ZAMBRANO GUZMAN', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('JF-4', '0601199700044', 'AMY ALEJANDRA RIVERA DIAZ', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('JF-5', '0601199010045', 'YURI LIZETH DOMINGUEZ TURCIOS', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO sucursal (nombre_sucursal, fechacreacion, fechaactualizacion, estado)
VALUES ('CHOLUTECA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO'),
('SAN LORENZO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO');

INSERT INTO unidad_de_negocio (nombre_unidad_de_negocio, fechacreacion, fechaactualizacion, estado)
VALUES ('nrCHRRHH', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'ACTIVO');

INSERT INTO colaboradores (codigocolaborador, nombrecolaborador, estado, fechacreacion, fechaactualizacion, departamento_id, empresa_id, jefe_id, sucursal_id, unidad_de_negocio_id)
VALUES ('KMSB', 'KATHERINE MELISSA SANCHEZ BRICEÑO', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 31, 1, 5, 1, 1),
('BJOR', 'BRAYAN JOSE ORTIZ RIVERA', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 3, 1, 1, 1, 1),
('KAMC', 'KAMILO ALEJANDRO MOLINA COREA', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1, 1, 1, 1, 1),
('VSRC', 'VILMA STEPHANIE ROMERO COLADO', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1, 1, 1, 1, 1),
('MYPC', 'MELODY YUNUEM PERALTA CARIAS', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 31, 1, 5, 1, 1),
('JJAO', 'JENNIFER JULIETH ARAUZ ORTIZ', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 3, 1, 3, 1, 1), -- AUDITORIA
('YLMH', 'YEFRI LENIN MEJIA HERNANDEZ', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 9, 1, 4, 1, 1), -- BODEGA TIENDA
('ADOG', 'ALEXIS DUVAN ORDOÑEZ GARCIA', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 21, 1, 6, 1, 1),
('KHMC', 'KELVIN HUMBERTO MARTINEZ CHAVARRIA', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 21, 1, 5, 1, 1),
('MJBC', 'MALCO JOSUE BAQUEDANO CRUZ', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 21, 1, 6, 1, 1),
('ACCA', 'ANA CRISTINA CONTRERAS AMADOR', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 2, 1, 2, 1, 1), --ADMINISTRACION
('ICSA', 'IVAN CELIN SORIANO', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 3, 3, 1, 1, 1), --ACERO
('CWCO', 'CINDY WALESKA CADENAS ORDOÑEZ', 'ACTIVO', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 3, 1, 3, 1, 1); --AUDITORIA

INSERT INTO permisos (colaborador, permiso_de, fecha_inicio, fecha_fin, motivo, comprobante, permiso_firmado, estado_inicial, estado_final, creado_por, fecha_creacion, modificado_por, fecha_modificacion, codigocolaborador_id, id_departamento_id, id_empresa_id, id_sucursal_id, id_tipo_permiso_id)
VALUES ('ALLAN ARNOLDO TORRES FLORES', 'Dias', '2025-01-25', '2025-01-30', 'Vacaciones pendiendtes', '', '', 'PENDIENTE', '', 'USER', CURRENT_TIMESTAMP, 'USER', CURRENT_TIMESTAMP, 2, 3, 1, 1, 2);


INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Administrador', 'Rol con acceso total al sistema', '08:00:00', '17:00:00', '09:00:00', '13:00:00', '10:00:00', '12:00:00', 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Gerente', 'Rol con acceso a la gestión de la empresa', '08:00:00', '17:00:00', '09:00:00', '13:00:00', '10:00:00', '12:00:00', 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Supervisor', 'Rol con acceso a la supervisión de empleados', '08:00:00', '17:00:00', '09:00:00', '13:00:00', '10:00:00', '12:00:00', 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Empleado', 'Rol con acceso limitado a sus propias tareas', '09:00:00', '18:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Contador', 'Rol con acceso a la contabilidad de la empresa', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Recursos Humanos', 'Rol con acceso a la gestión de personal', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('IT', 'Rol con acceso a la gestión de sistemas', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Marketing', 'Rol con acceso a la gestión de marketing', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Ventas', 'Rol con acceso a la gestión de ventas', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Logística', 'Rol con acceso a la gestión de logística', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Producción', 'Rol con acceso a la gestión de producción', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Calidad', 'Rol con acceso a la gestión de calidad', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Compras', 'Rol con acceso a la gestión de compras', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Mantenimiento', 'Rol con acceso a la gestión de mantenimiento', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Seguridad', 'Rol con acceso a la gestión de seguridad', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Auditoría', 'Rol con acceso a la gestión de auditorías', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Legal', 'Rol con acceso a la gestión legal', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Innovación', 'Rol con acceso a la gestión de innovación', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Proyectos', 'Rol con acceso a la gestión de proyectos', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
INSERT INTO roles (nombre, descripcion, hora_inicio_semana, hora_fin_semana, hora_inicio_sabado, hora_fin_sabado, hora_inicio_domingo, hora_fin_domingo, estado, creado_por, modificado_por, fecha_creacion, fecha_actualizacion) VALUES ('Desarrollo', 'Rol con acceso a la gestión de desarrollo', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 'ACTIVO', 'SISTEMA', NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);



-- Crear la tabla biometrico_asistencias
CREATE TABLE biometrico_asistencias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mes VARCHAR(20) NOT NULL,           -- Mes de la asistencia (Ejemplo: ENERO)
    sucursal VARCHAR(100) NOT NULL,     -- Sucursal donde trabaja el empleado
    empresa VARCHAR(100) NOT NULL,      -- Empresa donde labora el empleado
    ac_no INT NOT NULL,                 -- Código de empleado en el biométrico
    nombre VARCHAR(255) NOT NULL,       -- Nombre del empleado
    dni VARCHAR(20),                    -- Documento de identidad del empleado
    dia DATE NOT NULL,                   -- Fecha del registro
    horario_inicio TIME NOT NULL,       -- Hora establecida de entrada
    horario_salida TIME NOT NULL,       -- Hora establecida de salida
    marcacion_entrada TIME NOT NULL,    -- Hora registrada de entrada
    marcacion_salida TIME NOT NULL,     -- Hora registrada de salida
    falta BOOLEAN DEFAULT FALSE,        -- Indica si faltó (1 = Faltó, 0 = Asistió)
    tiempo_trabajado TIME,              -- Tiempo total trabajado
    simbolo VARCHAR(5),                 -- Indica si llegó temprano o tarde ("<", ">")
    departamento VARCHAR(100)           -- Departamento del empleado
);

-- Insertar registros de prueba
INSERT INTO biometrico_asistencias (mes, sucursal, empresa, ac_no, nombre, dni, dia, horario_inicio, horario_salida, marcacion_entrada, marcacion_salida, falta, tiempo_trabajado, simbolo, departamento)
VALUES
('ENERO', 'CHOLUTECA', 'PROMACO', 416114, 'Santos Alberto Palma', 'P-116', '2025-01-11', '08:00:00', '17:00:00', '06:49:00', '15:59:00', FALSE, '07:59:00', '<', 'TIENDA CD'),
('ENERO', 'CHOLUTECA', 'PROMACO', 416114, 'Santos Alberto Palma', 'P-116', '2025-01-12', '08:00:00', '17:00:00', '07:59:00', '15:55:00', FALSE, '07:55:00', '<', 'TIENDA CD'),
('ENERO', 'CHOLUTECA', 'PROMACO', 416114, 'Santos Alberto Palma', 'P-116', '2025-01-13', '08:00:00', '17:00:00', '07:00:00', '17:00:00', FALSE, '08:00:00', '<', 'TIENDA CD');



    INSERT INTO colaboradores 
    (codigocolaborador, nombrecolaborador, estado, fechacreacion, fechaactualizacion, 
    departamento_id, empresa_id, sucursal_id, unidad_de_negocio_id) 
    VALUES 
    ('P-1', 'ABNER ISAI MARTINEZ GUEVARA', 'Activo', 
    '2025-02-05 20:43:23', '2025-02-05 20:43:23', 33, 
    3, 1, 38);