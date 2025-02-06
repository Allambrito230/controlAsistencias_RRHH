document.addEventListener("DOMContentLoaded", function () {
    const departamentoSelect = document.getElementById("departamento");
    const nombreInput = document.getElementById("nombre");
    const buscarBtn = document.getElementById("buscar");
    const tablaColaboradores = document.getElementById("tabla-colaboradores");

    // Función para obtener el CSRF token desde las cookies
    function getCSRFToken() {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            let cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.startsWith("csrftoken=")) {
                    cookieValue = decodeURIComponent(cookie.substring("csrftoken=".length));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Cargar departamentos al inicio
    function cargarDepartamentos() {
        fetch(urlListaDepartamentos)
            .then(response => response.json())
            .then(data => {
                departamentoSelect.innerHTML = '<option value="">Seleccione un departamento</option>';
                data.forEach(dep => {
                    const option = document.createElement("option");
                    option.value = dep.id;
                    option.textContent = dep.nombre_departamento;
                    departamentoSelect.appendChild(option);
                });
            })
            .catch(error => console.error("Error cargando departamentos:", error));
    }

    //  Buscar colaboradores por departamento y nombre
    function buscarColaboradores() {
        const departamentoId = departamentoSelect.value;
        const nombre = nombreInput.value.trim();

        if (!departamentoId) {
            Swal.fire({
                icon: "warning",
                title: "¡Atención!",
                text: "Seleccione un departamento.",
                confirmButtonText: "Aceptar"
            });
            return;
        }
        console.log(urlGuardarComprobante);

        fetch(`${urlColaboradores}?departamento_id=${departamentoId}&nombre=${encodeURIComponent(nombre)}`)


            .then(response => response.json())
            .then(data => {
                tablaColaboradores.innerHTML = ""; //  Limpiar la tabla

                if (data.colaboradores.length === 0) {
                    tablaColaboradores.innerHTML = "<tr><td colspan='3' class='text-center'>No se encontraron resultados</td></tr>";
                    return;
                }

                data.colaboradores.forEach(colaborador => {
                    const fila = document.createElement("tr");
                    fila.innerHTML = `
                        <td>${colaborador.nombre}</td>
                        <td>
                            <input type="file" class="form-control comprobante" data-permiso-id="${colaborador.id}">
                        </td>
                        <td>
                            <button class="btn btn-primary guardar-btn" data-permiso-id="${colaborador.id}">Guardar</button>
                        </td>
                    `;
                    tablaColaboradores.appendChild(fila);
                });

                // Agregar eventos a los botones de guardar
                agregarEventosGuardar();
            })
            .catch(error => console.error("Error buscando colaboradores:", error));
    }

    //  Función para agregar eventos a los botones "Guardar"
    function agregarEventosGuardar() {
        document.querySelectorAll(".guardar-btn").forEach(button => {
            button.addEventListener("click", function () {
                const permisoId = this.getAttribute("data-permiso-id");

                //  Buscar el input de archivo en la misma fila del botón
                const fila = this.closest("tr");
                const inputFile = fila.querySelector(".comprobante");

                if (!inputFile || inputFile.files.length === 0) {
                    Swal.fire({
                        icon: "warning",
                        title: "¡Atención!",
                        text: "Debe seleccionar un archivo antes de guardar.",
                        confirmButtonText: "Aceptar"
                    });
                    return;
                }

                let formData = new FormData();
                formData.append("permiso_id", permisoId);
                formData.append("comprobante", inputFile.files[0]);

                fetch(urlGuardarComprobante, {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-CSRFToken": getCSRFToken()
                    }
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.message) {
                            Swal.fire({
                                icon: "success",
                                title: "¡Éxito!",
                                text: " Comprobante guardado con éxito.",
                                confirmButtonText: "Aceptar"
                            });
                            inputFile.value = ""; // Limpia el input de archivo
                        } else {
                            Swal.fire({
                                icon: "error",
                                title: "¡Error!",
                                text: "⚠ Error al guardar comprobante.",
                                confirmButtonText: "Aceptar"
                            });
                        }
                    })
                    .catch(error => console.error("Error al enviar comprobante:", error));
            });
        });
    }

    // Eventos
    departamentoSelect.addEventListener("change", buscarColaboradores);
    buscarBtn.addEventListener("click", buscarColaboradores);

    //  Cargar departamentos al inicio
    cargarDepartamentos();
});

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
