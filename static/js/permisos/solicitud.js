document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const departamentoSelect = document.getElementById("departamento");
    const empresaSelect = document.getElementById("empresa");
    const sucursalSelect = document.getElementById("sucursal");
    const colaboradorInput = document.getElementById("colaborador");
    const sugerenciasList = document.getElementById("sugerencias");
    const desdeInput = document.getElementById("desde");
    const hastaInput = document.getElementById("hasta");
    const motivoInput = document.getElementById("motivo");
    const permisoDeSelect = document.getElementById("permiso_de");

    // Cambiar formato de fecha/hora según el tipo de permiso
    if (permisoDeSelect) {
        permisoDeSelect.addEventListener("change", function () {
            if (this.value === "Horas") {
                desdeInput.type = "datetime-local";
                hastaInput.type = "datetime-local";
            } else if (this.value === "Días") {
                desdeInput.type = "date";
                hastaInput.type = "date";
            }
        });
    }

    // Cargar datos dinámicos
    function cargarDatos(endpoint, selectElement, nombrePropiedad) {
        fetch(endpoint)
            .then(response => response.json())
            .then(data => {
                selectElement.innerHTML = '<option value="">Seleccione</option>';
                data.forEach(item => {
                    const option = document.createElement("option");
                    option.value = item.id;
                    option.textContent = item[nombrePropiedad];
                    selectElement.appendChild(option);
                });
            })
            .catch(error => console.error(`Error cargando ${endpoint}:`, error));
    }

    // Cargar listas dinámicas
    cargarDatos("/permisos/Listas/departamentosJson/", departamentoSelect, "nombre_departamento");
    cargarDatos("/permisos/Listas/empresasJson/", empresaSelect, "nombre_empresa");
    cargarDatos("/permisos/Listas/sucursalesJson/", sucursalSelect, "nombre_sucursal");

    // Manejo de sugerencias de colaboradores con carga automática de empresa y sucursal
    colaboradorInput.addEventListener("input", function () {
        const query = colaboradorInput.value.toLowerCase();
        const departamentoId = departamentoSelect.value;

        if (departamentoId && query.length > 0) {
            fetch(`/permisos/colaboradores/${departamentoId}/`)
                .then(response => response.json())
                .then(data => {
                    sugerenciasList.innerHTML = "";
                    if (data.length > 0) {
                        data.forEach(colaborador => {
                            const li = document.createElement("li");
                            li.textContent = colaborador.nombrecolaborador;
                            li.dataset.id = colaborador.id;
                            li.dataset.empresa = colaborador.empresa_id;
                            li.dataset.sucursal = colaborador.sucursal_id;
                            sugerenciasList.appendChild(li);
                        });
                        sugerenciasList.style.display = "block";
                    } else {
                        sugerenciasList.style.display = "none";
                    }
                })
                .catch(error => console.error("Error al buscar colaboradores:", error));
        } else {
            sugerenciasList.style.display = "none";
        }
    });

    // Selección de colaborador y carga automática de empresa y sucursal
    sugerenciasList.addEventListener("click", function (event) {
        if (event.target.tagName === "LI") {
            colaboradorInput.value = event.target.textContent;
            empresaSelect.value = event.target.dataset.empresa;
            sucursalSelect.value = event.target.dataset.sucursal;
            sugerenciasList.style.display = "none";
        }
    });

    // Validación del colaborador antes de enviar el formulario
    async function validarColaborador() {
        const empresaId = empresaSelect.value;
        const sucursalId = sucursalSelect.value;
        const nombreColaborador = colaboradorInput.value.trim();

        if (!empresaId || !sucursalId || !nombreColaborador) {
            console.error("Validación fallida: Faltan parámetros.");
            return false;
        }

        try {
            const response = await fetch(`/permisos/verificar-colaborador/?empresa=${empresaId}&sucursal=${sucursalId}&nombre=${encodeURIComponent(nombreColaborador)}`);

            if (!response.ok) {
                console.error("Error HTTP:", response.status);
                return false;
            }

            const data = await response.json();
            return data.existe;
        } catch (error) {
            console.error("Error verificando colaborador:", error);
            return false;
        }
    }

    // Validación de campos antes de enviar el formulario
    async function validarCampos() {
        let valido = true;
        const errores = [];

        if (!departamentoSelect.value) errores.push("Debe seleccionar un departamento.");
        if (!empresaSelect.value) errores.push("Debe seleccionar una empresa.");
        if (!sucursalSelect.value) errores.push("Debe seleccionar una sucursal.");
        if (!colaboradorInput.value.trim()) errores.push("Debe ingresar un colaborador válido.");
        if (!desdeInput.value || !hastaInput.value) errores.push("Debe completar las fechas de inicio y fin.");
        if (new Date(desdeInput.value) > new Date(hastaInput.value)) errores.push("La fecha 'Desde' no puede ser mayor que la fecha 'Hasta'.");
        if (!motivoInput.value.trim()) errores.push("Debe ingresar un motivo para el permiso.");

        if (!await validarColaborador()) {
            errores.push("El colaborador no pertenece a la empresa y sucursal seleccionadas.");
            valido = false;
        }

        if (errores.length > 0) {
            Swal.fire({
                title: "Error",
                text: errores.join("\n"),
                icon: "error",
                confirmButtonText: "Aceptar",
            });
        }

        return valido;
    }

    // Enviar formulario 
    async function enviarFormulario(event) {
        event.preventDefault();

        if (!await validarCampos()) return;

        const formData = new FormData(form);

        try {
            const response = await fetch(form.action, {
                method: "POST",
                body: formData,
            });

            const data = await response.json();

            if (response.ok && data.status === "Success") {
                Swal.fire({
                    title: "Éxito",
                    text: data.message,
                    icon: "success",
                    confirmButtonText: "Aceptar",
                }).then(() => {
                    form.reset();
                    location.reload();
                });
            } else {
                Swal.fire({
                    title: "Error",
                    text: data.message,
                    icon: "error",
                    confirmButtonText: "Aceptar",
                });
            }
        } catch (error) {
            console.error("Error enviando la solicitud:", error);
            Swal.fire({
                title: "Error",
                text: "Hubo un problema al procesar la solicitud. Intente nuevamente más tarde.",
                icon: "error",
                confirmButtonText: "Aceptar",
            });
        }
    }

    // Evento de envío del formulario
    form.addEventListener("submit", enviarFormulario);
});
