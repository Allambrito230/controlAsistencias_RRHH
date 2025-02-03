

document.querySelectorAll(".btn-imprimir").forEach(button => {
    button.addEventListener("click", async function () {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();

        // Nueva función que maneja correctamente la ñ y caracteres acentuados
        function toTitleCase(str) {
            return str.toLowerCase().replace(/(^|\s)\S/g, (l) => l.toUpperCase());
        }

        // Capturar datos de la fila seleccionada con formato corregido
        const nombre = toTitleCase(this.getAttribute("data-nombre"));
        const tipoPermiso = toTitleCase(this.getAttribute("data-tipo"));
        const departamento = toTitleCase(this.getAttribute("data-departamento"));
        const fechaInicio = this.getAttribute("data-inicio");
        const fechaFin = this.getAttribute("data-fin");
        const motivo = toTitleCase(this.getAttribute("data-motivo"));

        // Agregar logo
        const logo = new Image();
        logo.src = "/../static/img/logo_promaco.png";
        await new Promise((resolve) => {
            logo.onload = resolve;
        });

        // Configuración del PDF
        const startX = 10;
        const startY = 20;
        const tableWidth = 190;
        const rowHeight = 30;

        doc.setLineWidth(0.2);
        doc.rect(startX, startY, tableWidth, rowHeight);

        // Columnas
        const col1Width = 60;
        const col3Width = 60;
        const col2Width = tableWidth - col1Width - col3Width;

        doc.line(startX + col1Width, startY, startX + col1Width, startY + rowHeight);
        doc.line(startX + col1Width + col2Width, startY, startX + col1Width + col2Width, startY + rowHeight);

        const cellHeight = rowHeight / 4;
        for (let i = 1; i < 4; i++) {
            doc.line(startX + col1Width + col2Width, startY + i * cellHeight, startX + tableWidth, startY + i * cellHeight);
        }

        // Agregar logo
        doc.addImage(logo, "PNG", startX + 10, startY + 1, 40, 20);

        // Texto encabezado
        doc.setFontSize(10);
        doc.setFont("times", "bold");
        doc.text("Proveedora de Materiales de", startX + 10, startY + 22);
        doc.text("Construcción S de R.L.", startX + 12, startY + 26);

        doc.setFontSize(18);
        doc.setFont("times", "bold");
        doc.text("Solicitud de Permiso", startX + col1Width + col2Width / 2, startY + 15, { align: "center" });
        doc.text("Laboral", startX + col1Width + col2Width / 2, startY + 25, { align: "center" });

        // Texto en columna 3
        doc.setFontSize(8);
        doc.setFont("times", "bold");
        doc.text("CÓDIGO: RRHH-RE-26", startX + col1Width + col2Width + 2, startY + 5);
        doc.text("VERSIÓN: 00", startX + col1Width + col2Width + 2, startY + 13);
        doc.text("FECHA DE ACTUALIZACIÓN:", startX + col1Width + col2Width + 2, startY + 20);
        doc.text("08/08/2024", startX + col1Width + col2Width + 43, startY + 20);
        doc.text("ELABORADO POR:", startX + col1Width + col2Width + 2, startY + 26);
        doc.text("DEPTO. PROCESOS", startX + col1Width + col2Width + 30, startY + 26);

        // Datos del permiso
        doc.setFontSize(14);
        doc.setFont("times", "bold");

        doc.text("Nombre: ", 20, 75);
        doc.setFont("times", "normal");
        doc.text(nombre, 60, 75);

        doc.setFont("times", "bold");
        doc.text("Tipo de permiso: ", 20, 87);
        doc.setFont("times", "normal");
        doc.text(tipoPermiso, 60, 87);

        doc.setFont("times", "bold");
        doc.text("Departamento: ", 20, 99);
        doc.setFont("times", "normal");
        doc.text(departamento, 60, 99);

        doc.setFont("times", "bold");
        doc.text("Fecha Inicio: ", 20, 111);
        doc.setFont("times", "normal");
        doc.text(fechaInicio, 60, 111);

        doc.setFont("times", "bold");
        doc.text("Fecha Fin: ", 20, 123);
        doc.setFont("times", "normal");
        doc.text(fechaFin, 60, 123);

        doc.setFont("times", "bold");
        doc.text("Motivo del Permiso:", 20, 135);

        doc.setFont("times", "normal");
        const motivoAncho = 170;
        const motivoTextoDividido = doc.splitTextToSize(motivo, motivoAncho);
        doc.text(motivoTextoDividido, 20, 144);

        // Firmas
        doc.setFontSize(10);
        doc.setLineWidth(0.5);
        doc.line(20, 200, 80, 200);
        doc.text("Firma empleado", 35, 205);

        doc.line(120, 200, 180, 200);
        doc.text("Jefe de área", 140, 205);

        doc.line(70, 250, 130, 250);
        doc.text("Vo. Bo. de RRHH", 85, 255);

        // Descargar PDF
        doc.save(`Solicitud_${nombre}.pdf`);
    });
});

// Cambio de estado del permiso
document.addEventListener("DOMContentLoaded", function () {
    // Habilitar la subida del archivo después de imprimir
    document.querySelectorAll(".btn-imprimir").forEach(button => {
        button.addEventListener("click", function () {
            let permisoRow = this.closest("tr");
            let inputFile = permisoRow.querySelector(".permiso-firmado");

            inputFile.disabled = false;
            Swal.fire("¡Impresión completada!", "Ahora puedes subir el documento firmado.", "info");
        });
    });

    // Habilitar botón "Aceptar" solo cuando se suba un archivo
    document.querySelectorAll(".permiso-firmado").forEach(input => {
        input.addEventListener("change", function () {
            let permisoRow = this.closest("tr");
            let btnAceptar = permisoRow.querySelector(".btn-aceptar");

            if (this.files.length > 0) {
                btnAceptar.disabled = false;
            }
        });
    });

    // Evento para aprobar permisos
    document.querySelectorAll(".btn-aceptar").forEach(button => {
        button.addEventListener("click", function () {
            let permisoRow = this.closest("tr");
            let permisoId = permisoRow.dataset.permisoId;
            let inputFile = permisoRow.querySelector(".permiso-firmado");
            let formData = new FormData();

            formData.append("permiso_id", permisoId);
            formData.append("estado", "PRE-APROBADO");
            formData.append("permiso_firmado", inputFile.files[0]);

            Swal.fire({
                title: "¿Está seguro de aprobar este permiso?",
                text: "No podrá revertir esta acción.",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Sí, aprobar",
                cancelButtonText: "No, cancelar",
            }).then((result) => {
                if (result.isConfirmed) {
                    fetch("/permisos/actualizar-permiso/", {
                        method: "POST",
                        body: formData,
                        headers: {
                            "X-CSRFToken": getCookie("csrftoken"),
                        },
                    })
                        .then(response => response.json())
                        .then(data => {
                            if (data.status === "success") {
                                Swal.fire("¡Aprobado!", "El permiso ha sido aprobado correctamente.", "success");
                                permisoRow.remove();  // Eliminar la fila de la tabla
                            } else {
                                Swal.fire("Error", data.message, "error");
                            }
                        })
                        .catch(error => console.error("Error al actualizar permiso:", error));
                }
            });
        });
    });

    // Evento para rechazar permisos
    document.querySelectorAll(".btn-rechazar").forEach(button => {
        button.addEventListener("click", function () {
            let permisoRow = this.closest("tr");
            let permisoId = permisoRow.dataset.permisoId;
            let formData = new FormData();

            formData.append("permiso_id", permisoId);
            formData.append("estado", "Rechazado");

            Swal.fire({
                title: "¿Está seguro de rechazar este permiso?",
                text: "No podrá revertir esta acción.",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Sí, rechazar",
                cancelButtonText: "No, cancelar",
            }).then((result) => {
                if (result.isConfirmed) {
                    fetch("/permisos/actualizar-permiso/", {
                        method: "POST",
                        body: formData,
                        headers: {
                            "X-CSRFToken": getCookie("csrftoken"),
                        },
                    })
                        .then(response => response.json())
                        .then(data => {
                            if (data.status === "success") {
                                Swal.fire("¡Rechazado!", "El permiso ha sido rechazado correctamente.", "success");
                                permisoRow.remove();  // Eliminar la fila de la tabla
                            } else {
                                Swal.fire("Error", data.message, "error");
                            }
                        })
                        .catch(error => console.error("Error al actualizar permiso:", error));
                }
            });
        });
    });

    // Función para obtener el CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            let cookies = document.cookie.split(";");
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});


document.addEventListener("DOMContentLoaded", function () {
    // Inicializar popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Cerrar otros popovers al abrir uno nuevo
    popoverTriggerList.forEach(function (popoverTriggerEl) {
        popoverTriggerEl.addEventListener('click', function () {
            popoverList.forEach(function (popover) {
                if (popover._element !== popoverTriggerEl) {
                    popover.hide();
                }
            });
        });
    });

    // Cerrar popovers al hacer clic fuera
    document.addEventListener('click', function (event) {
        if (!event.target.matches('[data-bs-toggle="popover"]')) {
            popoverList.forEach(function (popover) {
                popover.hide();
            });
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("a.ver-archivo").forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // Evita la navegación
            let urlArchivo = this.getAttribute("href");

            // Asignar la imagen al modal
            let imagenModal = document.getElementById("imagenModal");
            imagenModal.src = urlArchivo;

            // Mostrar el modal
            let modal = new bootstrap.Modal(document.getElementById("modalImagen"));
            modal.show();
        });
    });
});


