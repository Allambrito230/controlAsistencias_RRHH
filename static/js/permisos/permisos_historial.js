// Función para obtener el token CSRF desde las cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Manejo de aprobación de permisos
document.querySelectorAll(".btn-aceptar").forEach(button => {
    button.addEventListener("click", function () {
        let permisoRow = this.closest("tr");
        let permisoId = permisoRow ? permisoRow.dataset.permisoId : null;

        if (!permisoId) {
            console.error("Error: No se encontró permisoId en la fila.");
            Swal.fire("Error", "No se encontró el ID del permiso.", "error");
            return;
        }

        Swal.fire({
            title: "¿Está seguro de aprobar este permiso?",
            text: "No podrá revertir esta acción.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Sí, aprobar",
            cancelButtonText: "No, cancelar",
        }).then((result) => {
            if (result.isConfirmed) {
                let formData = new FormData();
                formData.append("permiso_id", permisoId);
                formData.append("estado", "APROBADO");

                fetch("/permisos/actualizar-permiso/", {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"),
                    },
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log("Respuesta del servidor:", data);
                        if (data.status === "success") {
                            Swal.fire("¡Aprobado!", "El permiso ha sido aprobado correctamente.", "success");

                            // Deshabilitar los botones después de la aprobación
                            permisoRow.querySelector(".btn-aceptar").disabled = true;
                            permisoRow.querySelector(".btn-rechazar").disabled = true;
                        } else {
                            Swal.fire("Error", data.message, "error");
                        }
                    })
                    .catch(error => console.error("Error al actualizar permiso:", error));
            }
        });
    });
});

// Manejo de rechazo de permisos
document.querySelectorAll(".btn-rechazar").forEach(button => {
    button.addEventListener("click", function () {
        let permisoRow = this.closest("tr");
        let permisoId = permisoRow ? permisoRow.dataset.permisoId : null;

        if (!permisoId) {
            console.error("Error: No se encontró permisoId en la fila.");
            Swal.fire("Error", "No se encontró el ID del permiso.", "error");
            return;
        }

        Swal.fire({
            title: "¿Está seguro de rechazar este permiso?",
            text: "No podrá revertir esta acción.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Sí, rechazar",
            cancelButtonText: "No, cancelar",
        }).then((result) => {
            if (result.isConfirmed) {
                let formData = new FormData();
                formData.append("permiso_id", permisoId);
                formData.append("estado", "Rechazado");

                fetch("/permisos/actualizar-permiso/", {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"),
                    },
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log("Respuesta del servidor:", data);
                        if (data.status === "success") {
                            Swal.fire("¡Rechazado!", "El permiso ha sido rechazado correctamente.", "success");

                            // Deshabilitar los botones después del rechazo
                            permisoRow.querySelector(".btn-aceptar").disabled = true;
                            permisoRow.querySelector(".btn-rechazar").disabled = true;
                        } else {
                            Swal.fire("Error", data.message, "error");
                        }
                    })
                    .catch(error => console.error("Error al actualizar permiso:", error));
            }
        });
    });
});

/* VER COMPROBANTES */
document.addEventListener("DOMContentLoaded", function () {
    
    document.querySelectorAll("a.ver-archivo").forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // Evita que el enlace abra una nueva pestaña
            let urlArchivo = this.getAttribute("href");

            // Crear un iframe oculto para cargar el archivo
            let iframe = document.createElement("iframe");
            iframe.style.position = "absolute";
            iframe.style.width = "0px";
            iframe.style.height = "0px";
            iframe.style.border = "none";
            iframe.src = urlArchivo;

            document.body.appendChild(iframe);

            iframe.onload = function () {
                iframe.contentWindow.focus();
                iframe.contentWindow.print(); // Ejecutar impresión
                setTimeout(() => document.body.removeChild(iframe), 1000); // Eliminar iframe después de imprimir
            };
        });
    });
});

/* POPOVERS */
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