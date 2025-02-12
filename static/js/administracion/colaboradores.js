// Función para obtener el token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener("DOMContentLoaded", function () {
    fetch('/registros/colaboradores/')  
        .then(response => response.json())
        .then(data => {
            console.log("Datos recibidos:", data); 
            llenarSelect('sucursal', data.sucursales, 'nombre_sucursal');
            llenarSelect('empresa', data.empresas, 'nombre_empresa');
            llenarSelect('unidadnegocio', data.unidades_negocio, 'nombre_unidad_de_negocio');
            llenarSelect('departamento', data.departamentos, 'nombre_departamento');
            llenarSelect('jefes', data.jefes, 'nombrejefe', true);
        })
        .catch(error => console.error("Error cargando listas:", error));
});

function llenarSelect(id, items, labelKey, addCodigo = false) {
    const select = document.getElementById(id);
    if (!select) return;  //  Evita errores si el `select` no está en la página
    select.innerHTML = '<option value="" selected disabled>Seleccione una opción</option>';

    items.forEach(item => {
        const option = document.createElement("option");
        option.value = item.id;
        option.textContent = addCodigo ? `${item.codigo} - ${item[labelKey]}` : item[labelKey];
        select.appendChild(option);
    });
}


function llenarSelect(id, items, labelKey, addCodigo = false) {
    const select = document.getElementById(id);
    if (!select) return;  // Evita errores si el `select` no está en la página
    select.innerHTML = '<option value="" selected disabled>Seleccione una opción</option>';

    items.forEach(item => {
        const option = document.createElement("option");
        option.value = item.id;
        option.textContent = addCodigo ? `${item.codigo} - ${item[labelKey]}` : item[labelKey];
        select.appendChild(option);
    });
}


function llenarFormularioEditar(boton) {
    var colaboradoresData = JSON.parse(document.getElementById('colaboradores-data').textContent);
    var idColaborador = boton.getAttribute('data-editar');
    var colaboradorSeleccionado = colaboradoresData.find(colaborador => colaborador.id == idColaborador);


    if (colaboradorSeleccionado) {
        document.getElementById('idcolaborador').value = colaboradorSeleccionado.id;
        document.getElementById('nombrejefeeditar').value = colaboradorSeleccionado.nombrecolaborador;
        document.getElementById('codigocolaboradoreditar').value = colaboradorSeleccionado.codigocolaborador;

        // Establece el valor de los select por su ID
        document.getElementById('sucursaleditar').value = colaboradorSeleccionado.sucursal_id;
        document.getElementById('empresaeditar').value = colaboradorSeleccionado.empresa_id;
        document.getElementById('unidadnegocioeditar').value = colaboradorSeleccionado.unidad_de_negocio_id;
        document.getElementById('departamentoeditar').value = colaboradorSeleccionado.departamento_id;
        document.getElementById('jefeseditar').value = colaboradorSeleccionado.jefe_id;

        document.getElementById('estadoeditar').value = colaboradorSeleccionado.estado;
    } else {
        console.error("Colaborador no encontrado para el ID:", idColaborador);
    }
}

document.getElementById('update-form-colaboradores').addEventListener('submit', function (event) {
    event.preventDefault();

    const idColaborador = document.getElementById('idcolaborador').value;
    const csrftoken = getCookie('csrftoken'); // Obtener el token CSRF si lo usas

    const data = {
        nombrecolaborador: document.getElementById('nombrejefeeditar').value,
        sucursal_id: document.getElementById('sucursaleditar').value,
        empresa_id: document.getElementById('empresaeditar').value,
        unidad_de_negocio_id: document.getElementById('unidadnegocioeditar').value,
        departamento_id: document.getElementById('departamentoeditar').value,
        jefe_id: document.getElementById('jefeseditar').value,
        estado: document.getElementById('estadoeditar').value,
        codigocolaborador: document.getElementById('codigocolaboradoreditar').value
    };

    fetch(`/Listas/Colaboradores/Update/${idColaborador}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                Swal.fire({
                    title: 'Éxito',
                    text: 'Colaborador actualizado correctamente',
                    icon: 'success',
                    confirmButtonText: 'Aceptar',
                    customClass: {
                        confirmButton: 'custom-alertas-button'
                    }
                }).then(() => {
                    window.location.reload(); 
                });
            } else {
                Swal.fire({
                    title: 'Error',
                    text: data.message,
                    icon: 'warning',
                    confirmButtonText: 'Aceptar',
                    customClass: {
                        confirmButton: 'custom-alertas-button'
                    }
                });
            }
        })
        .catch(error => {
            Swal.fire({
                title: 'Error',
                text: error.message,
                icon: 'error',
                confirmButtonText: 'Aceptar',
                customClass: {
                    confirmButton: 'custom-alertas-button'
                }
            });
        });
});