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



INSERT INTO "auth_user" 
    ("id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined") 
VALUES
	(1, 'pbkdf2_sha256$720000$qWJoP8APCJKonqXey6H0zB$ouMP4Sn9rWBvcKAHSal0KS0xsdHfbIo04bskIAal+Pk=', '2025-02-07 00:59:25.4067450 +00:00', 1, 'admin', '', '', '', 1, 1, '2025-02-07 00:43:14.4768860 +00:00'),
	(2, 'pbkdf2_sha256$720000$0B8YKwIKXGYHN5b09b581U$3QocYW9mXYiqAyTp9KKH4ng5IP4Bd5zdMxTBa48iHms=', NULL, 0, '0602198800163', 'OSCAR', 'HERNANDEZ', 'ohernandez@promacohn.com', 0, 1, '2025-02-07 00:44:45.0000000 +00:00'),
	(3, 'pbkdf2_sha256$720000$eVMn3pu8H0nSkP9ed2hoBW$pIvf9/mT1dxEHVEXk9T/Bd62PtSUrqTNRNiEfGQmhc8=', NULL, 0, '0601198900628', 'NANCY PATRICIA', 'MENDOZA HERNANDEZ', 'nmendoza@promacohn.com', 0, 1, '2025-02-07 00:46:07.0000000 +00:00'),
	(4, 'pbkdf2_sha256$720000$YGaesnfZscduGtaHP5pz16$tGgdS5YwKkHEb9WXqHmBKOdIxPID/6LSJnj30F8cWa0=', NULL, 0, '0801197400921', 'JOSE MANUEL', 'ZAMBRANO GUZMAN', 'jzambrano@promacohn.com', 0, 1, '2025-02-07 00:46:26.0000000 +00:00'),
	(5, 'pbkdf2_sha256$720000$Fm9fVi86tFiGBxj57RgmY2$eaBcUYGhl3SDEECCWWLH+e5Rshu2e74wf6vy3jcyJk4=', NULL, 0, '0601197802307', 'MARLENE ELENA', 'PACHECO MORALES', 'MPACHECO@PROMACOHN.COM', 0, 1, '2025-02-07 00:52:24.7869100 +00:00'),
	(6, 'pbkdf2_sha256$720000$5M09qRMZIRAZ7DUlPzQqTp$aPmRQYqlUsyWyR0BYU2f/8gVGkSEBo/+UrVi5er5se4=', '2025-02-07 00:56:55.8587970 +00:00', 0, '0601198902619', 'HECTOR MAURICIO', 'ESPINAL MORENO', 'HESPINAL@PROMACOHN.COM', 0, 1, '2025-02-07 00:55:12.8807880 +00:00'),
	(10, 'pbkdf2_sha256$720000$gfxnv70zV3TiR9FfEQt1Kd$Ac+i7IpVXJUPj88v6Y6optFWjgy2aoGag5pGL04RWPg=', NULL, 0, '1709199100101', 'JOSE RAUL', 'QUIROZ FLORES', 'RQUIROZ@PROMACOHN.COM', 0, 1, '2025-02-07 02:33:48.8709780 +00:00'),
	(11, 'pbkdf2_sha256$720000$dnJAoKvxi9MUMsqEDtcnm5$G6Fxdf+p4AP1Hc8bnJOlHjcvRNb0IkJvjlaHDWOXImU=', NULL, 0, '1701199800411', 'DARIELA ALEJANDRA', 'ANDINO AGUILERA', 'DANDINO@PROMACOHN.COM', 0, 1, '2025-02-07 02:34:48.1273990 +00:00'),
	(12, 'pbkdf2_sha256$720000$OQKvkwWKAb44n1ADoZaEyW$6P1MXHkPzfC+QSpVt2eXQC9iLYiuY42sFW6ekD7X1A8=', NULL, 0, '0601199500390', 'CLARA MARIA', 'VASQUEZ GARCIA', 'BODEGATIENDA.SUPERVISOR@PROMACO.HN', 0, 1, '2025-02-07 02:36:14.8362030 +00:00'),
	(13, 'pbkdf2_sha256$720000$jO9JrATYdJPqoiHw2KUEdq$NpSqdvoWFgKWRM392gRl2HoJnEwndzwR/6dfPZAw1h4=', NULL, 0, '0601197902994', 'ALEXIS GIOVANY', 'CARRASCO ESPINAL', 'ACARRASCO@PROMACOHN.COM', 0, 1, '2025-02-07 02:36:55.4907840 +00:00'),
	(14, 'pbkdf2_sha256$720000$KusRKgBZyQ3OGL3kJcclQw$MRu3kvyEVBP/UnI1LdL26HKlMtRv5FWlYaoMBQohCsQ=', NULL, 0, '0801198418516', 'VICTOR MIGUEL', 'IRIAS GARCIA', 'VIRIAS@PROMACOHN.COM', 0, 1, '2025-02-07 02:37:53.1808250 +00:00'),
	(16, 'pbkdf2_sha256$720000$JZcYtykxoIEXpVB9OqkBUs$vxhAqogW/4BwSats4TIaFKpUxjMs14Mxe0Zj0TbFARM=', NULL, 0, '0801197505772', 'WENDER EDGARDO ', 'CASTRO MALTEZ', 'WCASTRO@PROMACOHN.COM', 0, 1, '2025-02-07 02:42:19.3098110 +00:00'),
	(17, 'pbkdf2_sha256$720000$drY1wbLkRt2HYe302qzzn8$hilcJ52E4AvmIqBL9aPGwXOmpdYLwG+SRd0Vqsa0DpQ=', NULL, 0, '0714198600339', 'YASADIS OSMANI ', 'ALVAREZ DIAZ', 'YALVAREZ@PROMACOHN.COM', 0, 1, '2025-02-07 02:43:03.9808480 +00:00'),
	(18, 'pbkdf2_sha256$720000$s6L45EaCxyBENZyiSxNsnw$VjhUbJfYbI2EP198xnIZ5nrkoZAxOJk5UZGI/YZ6YIc=', NULL, 0, '10111200606417', 'ANDREA ALEJANDRA', 'MORA BENAVIDES', 'AMORA@PROMACOHN.COM', 0, 1, '2025-02-07 02:43:56.1251320 +00:00'),
	(19, 'pbkdf2_sha256$720000$DMbodHUYa9p5jH10hI4hrc$EAZeTt8vn+Ra1l9Z5Xl6IEb8SRePl0RFmUs9jWQ+BKE=', NULL, 0, '0601198000020', 'LUIS DANIEL ', 'FLORES GALO', 'LFLORES@PROMACOHN.COM', 0, 1, '2025-02-07 02:44:55.2409180 +00:00'),
	(20, 'pbkdf2_sha256$720000$COm2IZDE4pbyoTyfGUVB88$v5o6yRp6xMvXeE52VMTjX6IxckF8eYTURTzk38WId9U=', NULL, 0, '0801197912815', 'VICTOR JAVIER ', 'MATAMOROS MATAMOROS', 'VJAVIERM2@GMAIL.COM', 0, 1, '2025-02-07 02:55:13.7418280 +00:00'),
	(21, 'pbkdf2_sha256$720000$KbT74r5lc7SEytEv1GbOPt$x3Gv020naBTA6C6MWpfmC/LPkYrffHixf2TufjMRYMs=', NULL, 0, '0601198101282', 'LUIS ALBERTO', 'RODRIGUEZ ALCOCER', 'LRALCOCER@PROMACOHN.COM', 0, 1, '2025-02-07 02:56:11.4675430 +00:00'),
	(22, 'pbkdf2_sha256$720000$jr9wq76OYwj1jvpbu9FcNw$f8RBY5zjTPOrE33WJ0SjvL1tNqdOrumgOkqRsfzF8A4=', NULL, 0, '0615197500017', 'ELMER ANTONIO ', 'FIALLOS CACERES', 'EFIALLOS@PROMACOHN.COM', 0, 1, '2025-02-07 02:57:07.8524950 +00:00'),
	(23, 'pbkdf2_sha256$720000$80KDcQGl9iwQtkDIg6uBSZ$smPYvd4xqPt8xnUQlAOMVsyZ8VEDQRpbag8ShrTHMUc=', NULL, 0, '0801199322574', 'KELVIN HUMBERTO ', 'MARTINEZ CHAVARRIA', 'KMARTINEZ@PROMACOHN.COM', 0, 1, '2025-02-07 02:57:46.8680990 +00:00'),
	(24, 'pbkdf2_sha256$720000$UPcVahMbxs6E3OsnGd9eXg$G5900W73KVCWVjykgnPk6JhMGXw1IP+SOIM+yMSPLmA=', NULL, 0, '1501198600077', 'YURI LIZETH ', 'DOMINGUEZ TURCIOS', 'YDOMINGUEZ@PROMACOHN.COM', 0, 1, '2025-02-07 02:58:28.3472260 +00:00'),
	(25, 'pbkdf2_sha256$720000$geqkUpaWbQD6XgfhJdC8R8$ra5li8Al+O2S+Ys0gybKPkfdRCejzea2D9JIMzPIDEA=', NULL, 0, '0601199402728', 'ABNER JOSUE ', 'RODRIGUEZ AGUILERA', 'AAGUILERA@PROMACOHN.COM', 0, 1, '2025-02-07 02:59:17.3923060 +00:00'),
	(26, 'pbkdf2_sha256$720000$fvBiBOdPsXHUgu2KmqGdBM$6hHCR0YoM8P0y4DOfxEEc7rGp0JYUoo17WvswWNFTds=', NULL, 0, '0615198800283', 'MARCIO JOSE ', 'ARIAS BANEGAS', 'MARIAS@PROMACOHN.COM', 0, 1, '2025-02-07 03:00:41.2603140 +00:00'),
	(27, 'pbkdf2_sha256$720000$XHhHtKzfikiAyiTLd6dnTW$2TkTF7SGPR05jisg75GjrixFy6dQ3wNO1Lir7c9dXgM=', NULL, 0, '1707197200114', 'LUBBY DANELIA', 'DIAZ ORTIZ', 'CAFETERIA.VENTAS@PROMACO.HN', 0, 1, '2025-02-07 03:01:30.3623620 +00:00'),
	(28, 'pbkdf2_sha256$720000$NcJro44q1MpuzZAxTE83ia$dhPaqB8BHnUIB+V4haXviBo+dtyHMA/T08wraMEcyLE=', NULL, 0, '0501197708336', 'ARTURO JOSUEL', 'LANDAVERDE ROBLES', 'JLANDAVERDE@PROMACOHN.COM', 0, 1, '2025-02-07 03:02:21.0162650 +00:00'),
	(29, 'pbkdf2_sha256$720000$AfwLEwyxbmh7t0D1OTCIXv$65B71Hc+LojZCrD5g8gXoAZCxQIpgGgY0uD5fYXhNhE=', NULL, 0, '0601199804234', 'DANNIS ALESSANDRO ', 'FLORES LOPEZ', 'DFLORES@PROMACOHN.COM', 0, 1, '2025-02-07 03:03:06.4160270 +00:00'),
	(30, 'pbkdf2_sha256$720000$I3dHCZyexFNJi6gflp3lIl$nlh7iY9EqBJvErQQ/gXHu6+kACMDXlPd1zps7nRdBV0=', NULL, 0, '0601199500203', 'CHERLYS ANAI ', 'PINEDA BARAHONA', 'CPINEDA@PROMACOHN.COM', 0, 1, '2025-02-07 03:03:51.8673770 +00:00'),
	(31, 'pbkdf2_sha256$720000$sYWE42J9GiGR4H4VaBifWU$V/riROvZvg9HyEhmSEWNnGAUMvS1cYo4MSNkLmywmv4=', NULL, 0, '1143121308', 'KARLA PATRICIA', 'ARIAS RENDON', 'KARIAS@PROMACOHN.COM', 0, 1, '2025-02-07 03:05:10.7649780 +00:00'),
	(32, 'pbkdf2_sha256$720000$2dD2VjaC1eBZh5XgtZrJJ2$wzOImdwrf5zMqQ6ZICTkLqdJQxDVxZKCVLHLm5dY7YM=', NULL, 0, '0601197900802', 'WILMER ALEXIS', 'RUEDA HERNANDEZ', 'WRUEDA@PROMACOHN.COM', 0, 1, '2025-02-07 03:06:00.8997850 +00:00'),
	(33, 'pbkdf2_sha256$720000$cEeCzcMCt8p78N71J2ETA5$VTcYZIRaITD4JmrSiY403mYM9w6n/B9OcO4v8FiaGmQ=', NULL, 0, '0603198600429', 'ALEX DANILO', 'BUSTILLO CASTILLO', 'ABUSTILLO@PROMACOHN.COM', 0, 1, '2025-02-07 03:06:53.0832830 +00:00'),
	(34, 'pbkdf2_sha256$720000$ksSZjJf5o9YggC8CHZlmhq$rwjm4BPd+YFwde1axpVi0iy6iH23iOCB+DVjlOsLkJo=', NULL, 0, '0601198903028', 'KILVETH LEONEL ', 'MARADIAGA RIVAS', 'KMARADIAGA@PROMACOHN.COM', 0, 1, '2025-02-07 03:08:00.8532420 +00:00'),
	(35, 'pbkdf2_sha256$720000$Qx6Og2P0lLvz4OdrydBw5S$BPeGbyQGpR6Hx3qw3ZOCg4N0YEDCs7je0rv1lQTkmtI=', NULL, 0, '0601199002406', 'AMY ALEJANDRA', 'RIVERA DIAZ', 'ARIVERA@PROMACOHN.COM', 0, 1, '2025-02-07 03:09:24.8108270 +00:00'),
	(36, 'pbkdf2_sha256$720000$micQ7qpfiltUV6210VKvJy$8VKDE1GGTF+urI8L2NpCgdHh9M0lKVK5tg1j1AinR5g=', NULL, 0, '0601197800457', 'VIOLETA SUYAPA', 'GUILLEN ZELAYA', 'VGUILLEN@PROMACOHN.COM', 0, 1, '2025-02-07 03:11:42.2292160 +00:00'),
	(37, 'pbkdf2_sha256$720000$HpU12kY3pZpsJTXgV38LJJ$sNLdKrDeX1+o97N2w9uvx2mlHtp9Tt1FJazfAjVRymA=', NULL, 0, '1709197900429', 'DENNYS ROBERTO', 'FUNEZ OSEGUERA', 'RFUNEZ@PROMACOHN.COM', 0, 1, '2025-02-07 03:18:03.0327630 +00:00');
