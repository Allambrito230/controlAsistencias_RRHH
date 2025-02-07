// // Función para obtener el token CSRF desde las cookies
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== "") {
//         let cookies = document.cookie.split(";");
//         for (let i = 0; i < cookies.length; i++) {
//             let cookie = cookies[i].trim();
//             if (cookie.startsWith(name + "=")) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

// // PROCESAMIENTO DEL PERMISO   
// document.addEventListener("DOMContentLoaded", function () {
//     // DESHABILITAR BOTONES SI EL PERMISO ESTÁ "RECHAZADO"
//     document.querySelectorAll("tr").forEach(permisoRow => {
//         let estadoPermiso = permisoRow.getAttribute("data-estado"); // Obtiene el estado del permiso
//         let btnAceptar = permisoRow.querySelector(".btn-aceptar");
//         let btnRechazar = permisoRow.querySelector(".btn-rechazar");

//         if (estadoPermiso && estadoPermiso.trim() === "RECHAZADO") {
//             if (btnAceptar) btnAceptar.disabled = true;
//             if (btnRechazar) btnRechazar.disabled = true;
//         }
//     });

//     // APROBAR PERMISOS
//     document.querySelectorAll(".btn-aceptar").forEach(button => {
//         button.addEventListener("click", function () {
//             let permisoRow = this.closest("tr");
//             let permisoId = permisoRow.getAttribute("data-permiso-id");
//             let formData = new FormData();

//             if (!permisoId) {
//                 Swal.fire("Error", "No se encontró el ID del permiso.", "error");
//                 return;
//             }
//             formData.append("permiso_id", permisoId);
//             formData.append("estado", "Aprobado");

//             fetch("/permisos/aprobar-permiso-rrhh/", {
//                 method: "POST",
//                 body: formData,
//                 headers: { "X-CSRFToken": getCookie("csrftoken") },
//             })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.status === "success") {
//                     Swal.fire("¡Aprobado!", "El permiso ha sido aprobado correctamente.", "success");
//                     permisoRow.remove();
//                 } else {
//                     Swal.fire("Error", data.message, "error");
//                 }
//             })
//             .catch(error => console.error("Error:", error));
//         });
//     });
// });



// // Mostrar comprobantes en un modal
// document.addEventListener("DOMContentLoaded", function () {
//     document.querySelectorAll("a.ver-archivo").forEach(link => {
//         link.addEventListener("click", function (event) {
//             event.preventDefault();
//             let urlArchivo = this.getAttribute("href");

//             let imagenModal = document.getElementById("imagenModal");
//             imagenModal.src = urlArchivo;

//             let modal = new bootstrap.Modal(document.getElementById("modalImagen"));
//             modal.show();
//         });
//     });
// });

/* Inicializar popovers */
document.addEventListener("DOMContentLoaded", function () {
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



// document.addEventListener("DOMContentLoaded", function () {
//     document.querySelectorAll(".ver-archivo").forEach(link => {
//         link.addEventListener("click", function (event) {
//             event.preventDefault();
//             let urlArchivo = this.getAttribute("href");

//             // Abrir el archivo en una nueva ventana y darle foco
//             let nuevaVentana = window.open(urlArchivo, "_blank", "width=800,height=600");

//             if (nuevaVentana) {
//                 nuevaVentana.focus(); // Traer la ventana al frente

//                 nuevaVentana.onload = function () {
//                     setTimeout(() => {
//                         nuevaVentana.print();
//                     }, 1000); // Esperar 1 segundo para asegurar carga completa

//                     // Cerrar la ventana después de imprimir (esperar un poco más)
//                     setTimeout(() => {
//                         nuevaVentana.close();
//                     }, 5000); // Cierra la ventana 5 segundos después de imprimir
//                 };
//             } else {
//                 alert("Permite las ventanas emergentes para imprimir el archivo.");
//             }
//         });
//     });
// });





document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".ver-archivo").forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            let fileUrl = this.getAttribute("href");

            // Obtener la extensión del archivo
            let fileExtension = fileUrl.split(".").pop().toLowerCase();

            if (["jpg", "jpeg", "png", "gif", "bmp"].includes(fileExtension)) {
                convertImageToPDF(fileUrl);
            } else if (fileExtension === "pdf") {
                printPDFInNewWindow(fileUrl);
            } else {
                alert("Formato de archivo no compatible. Solo se permiten imágenes y PDFs.");
            }
        });
    });
});

//Convertir Imagen a PDF & Imprimir
function convertImageToPDF(imageUrl) {
    const { jsPDF } = window.jspdf;
    let pdf = new jsPDF({
        orientation: "portrait",
        unit: "mm",
        format: "a4"
    });

    let img = new Image();
    img.crossOrigin = "Anonymous"; // Evita problemas de CORS
    img.src = imageUrl;

    img.onload = function () {
        let imgWidth = 180; //  ancho en mm (A4 ~ 210mm)
        let imgHeight = (img.height / img.width) * imgWidth; // Mantener proporción

        pdf.addImage(img, "JPEG", 15, 20, imgWidth, imgHeight);

        // Crear un Blob URL del PDF
        let pdfBlob = pdf.output("bloburl");

        // Abrir el PDF en una nueva ventana para imprimir
        printPDFInNewWindow(pdfBlob);
    };
}

// Abrir & Imprimir PDF en una nueva ventana
function printPDFInNewWindow(pdfUrl) {
    let printWindow = window.open("", "_blank", "width=800,height=600");

    if (!printWindow) {
        alert("Por favor, habilita las ventanas emergentes para esta página.");
        return;
    }

    // Escribir el contenido HTML para mostrar el PDF antes de imprimir
    printWindow.document.write(`
        <html>
        <head>
            <title>Impresión de Documento</title>
            <style>
                body { margin: 0; text-align: center; }
                embed { width: 100%; height: 100vh; }
            </style>
        </head>
        <body>
            <embed src="${pdfUrl}" type="application/pdf" />
            <script>
                // Espera hasta que el usuario haga clic en imprimir
                window.onload = function () {
                    setTimeout(() => {
                        window.print();
                    }, 1000); // Espera un poco para asegurarse de que el PDF cargó
                };
            </script>
        </body>
        </html>
    `);
    
    printWindow.document.close(); // Cerrar el documento para que cargue bien
}











document.getElementById("exportarExcel").addEventListener("click", function () {
    let url = this.getAttribute("data-url"); // Obtener la URL del botón
    window.location.href = url; // Redirigir a la URL
});



function aprobarPermisoRRHH(button) {
    actualizarEstadoRRHH(button, "APROBADO");
}

function rechazarPermisoRRHH(button) {
    actualizarEstadoRRHH(button, "RECHAZADO");
}

function actualizarEstadoRRHH(button, nuevoEstado) {
    const permisoId = button.getAttribute("data-permiso-id");

    Swal.fire({
        title: "¿Estás seguro?",
        text: `¿Quieres marcar este permiso como ${nuevoEstado}?`,
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sí, confirmar",
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            let formData = new FormData();
            formData.append("permiso_id", permisoId);
            formData.append("nuevo_estado", nuevoEstado);

            fetch("/permisos/actualizar_estado_rrhh/", {  // 🔹 URL correcta
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: formData
            })
                .then(response => response.json())
                .then(data => {
                    if (data.status === "Success") {
                        Swal.fire("Éxito", data.message, "success").then(() => {
                            location.reload(); // Recargar la página después de actualizar
                        });
                    } else {
                        Swal.fire("Error", data.message, "error");
                    }
                })
                .catch(error => {
                    Swal.fire("Error", "Hubo un problema con la solicitud.", "error");
                    console.error("Error:", error);
                });
        }
    });
}

// Función para obtener el token CSRF
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
