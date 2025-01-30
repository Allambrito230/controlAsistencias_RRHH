document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const departamentoSelect = document.getElementById("departamento");
    const empresa = document.getElementById("empresa");
    const sucursal = document.getElementById("sucursal");
    const colaboradorInput = document.getElementById("colaborador");
    const sugerenciasList = document.getElementById("sugerencias");
    const desdeInput = document.getElementById("desde");
    const hastaInput = document.getElementById("hasta");
    const motivoInput = document.getElementById("motivo");
    const comprobanteInput = document.querySelector('input[type="file"]');

    // Validar campos vacíos antes de enviar
    function validarCampos() {
        let valido = true;
        const errores = [];

        if (!departamentoSelect.value) {
            errores.push("Debe seleccionar un departamento.");
            valido = false;
        }

        if (!colaboradorInput.value.trim()) {
            errores.push("Debe ingresar un colaborador válido.");
            valido = false;
        }

        if (!desdeInput.value || !hastaInput.value) {
            errores.push("Debe completar las fechas de inicio y fin.");
            valido = false;
        } else if (new Date(desdeInput.value) > new Date(hastaInput.value)) {
            errores.push("La fecha 'Desde' no puede ser mayor que la fecha 'Hasta'.");
            valido = false;
        }

        if (!motivoInput.value.trim()) {
            errores.push("Debe ingresar un motivo para el permiso.");
            valido = false;
        }

        if (!valido) {
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

        // Validar campos antes de enviar
        if (!validarCampos()) return;

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

    // Cambiar formato de fecha/hora según el tipo de permiso
    const permisoDeSelect = document.getElementById("permiso_de");
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

    // Manejar sugerencias de colaboradores
    colaboradorInput.addEventListener("input", function () {
        const query = colaboradorInput.value.toLowerCase();
        const departamentoId = departamentoSelect.value;

        if (departamentoId && query.length > 0) {
            fetch(`/permisos/colaboradores/${departamentoId}/`)
                .then((response) => response.json())
                .then((data) => {
                    const resultados = data.filter((colaborador) =>
                        colaborador.nombrecolaborador.toLowerCase().includes(query)
                    );

                    // Mostrar sugerencias
                    sugerenciasList.innerHTML = "";
                    resultados.forEach((colaborador) => {
                        const li = document.createElement("li");
                        li.textContent = `${colaborador.nombrecolaborador}`;
                        li.dataset.id = colaborador.id;
                        sugerenciasList.appendChild(li);
                    });
                    sugerenciasList.style.display = "block";
                })
                .catch((error) => {
                    console.error("Error al buscar colaboradores:", error);
                });
        } else {
            sugerenciasList.style.display = "none";
        }
    });

    sugerenciasList.addEventListener("click", function (event) {
        if (event.target.tagName === "LI") {
            colaboradorInput.value = event.target.textContent;
            sugerenciasList.style.display = "none";
        }
    });

    // Cargar departamentos, empresas y sucursales dinámicamente
    /*function cargarDatos(endpoint, selectElement) {
        fetch(endpoint)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`Error al cargar datos desde ${endpoint}`);
                }
                return response.json();
            })
            .then((data) => {
                data.forEach((item) => {
                    const option = document.createElement("option");
                    option.value = item.id;
                    option.textContent = item.nombre;
                    selectElement.appendChild(option);
                });
            })
            .catch((error) => {
                console.error(`Error al cargar datos desde ${endpoint}:`, error);
            });
    }*/

    // Cargar departamentos dinámicamente
    function cargarDepartamentos() {
        fetch("/permisos/Listas/departamentosJson/")
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Error al cargar departamentos");
                }
                return response.json();
            })
            .then((data) => {
                data.forEach((depto) => {
                    const option = document.createElement("option");
                    option.value = depto.id;
                    option.textContent = depto.nombre_departamento;
                    departamentoSelect.appendChild(option);
                });
            })
            .catch((error) => {
                console.error("Error al cargar departamentos:", error);
                alert("No se pudieron cargar los departamentos.");
            });
    }

    function cargarEmpresas() {
        fetch("/permisos/Listas/empresasJson/")
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Error al cargar empresas");
                }
                return response.json();
            })
            .then((data) => {
                data.forEach((emp) => {
                    const option = document.createElement("option");
                    option.value = emp.id;
                    option.textContent = emp.nombre_empresa;
                    empresa.appendChild(option);
                });
            })
            .catch((error) => {
                console.error("Error al cargar empresas:", error);
                alert("No se pudieron cargar las empresas.");
            });
    }

    function cargarSucursales() {
        fetch("/permisos/Listas/sucursalesJson/")
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Error al cargar sucursales");
                }
                return response.json();
            })
            .then((data) => {
                data.forEach((emp) => {
                    const option = document.createElement("option");
                    option.value = emp.id;
                    option.textContent = emp.nombre_sucursal;
                    sucursal.appendChild(option);
                });
            })
            .catch((error) => {
                console.error("Error al cargar sucursales:", error);
                alert("No se pudieron cargar las sucursales.");
            });
    }

    cargarDepartamentos();
    cargarEmpresas();   
    cargarSucursales();

    // Asignar evento de envío al formulario
    form.addEventListener("submit", enviarFormulario);
});
