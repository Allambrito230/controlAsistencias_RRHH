// Función para obtener el token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function llenarFormularioEditar(boton) {
    try {
        var jefesData = JSON.parse(document.getElementById('jefes-data').textContent);
        var idJefe = boton.getAttribute('data-editar');

        var jefeSeleccionado = jefesData.find(jefe => jefe.id == idJefe);

        if (jefeSeleccionado) {
            document.getElementById('idjefe').value = jefeSeleccionado.id;
            document.getElementById('codigoeditar').value = jefeSeleccionado.codigo;
            document.getElementById('nombrejefeeditar').value = jefeSeleccionado.nombrejefe;
            document.getElementById('estadoeditar').value = jefeSeleccionado.estado;
            document.getElementById('identidadjefeditar').value = jefeSeleccionado.identidadjefe || "";
            document.getElementById('correoeditar').value = jefeSeleccionado.correo || "";
        } else {
            console.error("Jefe no encontrado para el ID:", idJefe);
        }
    } catch (error) {
        console.error("Error al llenar el formulario de edición:", error);
    }
}

// Función para registrar un nuevo jefe
document.getElementById('register-form-jefes').addEventListener('submit', function (event) {
    event.preventDefault();

    const csrftoken = getCookie('csrftoken');
    const data = {
        identidadjefe: document.getElementById('identidadjefe').value,
        nombrejefe: document.getElementById('nombrejefe').value,
        correo: document.getElementById('correo').value,
        estado: document.getElementById('estado').value
    };

    fetch('/registros/jefes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                Swal.fire('Éxito', 'Jefe registrado correctamente', 'success').then(() => location.reload());
            } else {
                Swal.fire('Error', data.message, 'error');
            }
        })
        .catch(error => Swal.fire('Error', error.message, 'error'));
});

// Función para actualizar un jefe existente
document.getElementById('update-form-jefes').addEventListener('submit', function (event) {
    event.preventDefault();

    const idjefe = document.getElementById('idjefe').value;
    const csrftoken = getCookie('csrftoken');

    const data = {
        identidadjefe: document.getElementById('identidadjefeditar').value,
        nombrejefe: document.getElementById('nombrejefeeditar').value,
        correo: document.getElementById('correoeditar').value,
        estado: document.getElementById('estadoeditar').value
    };

    fetch(`/registros/jefes/${idjefe}/`, {
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
                Swal.fire('Éxito', 'Jefe actualizado correctamente', 'success').then(() => location.reload());
            } else {
                Swal.fire('Error', data.message, 'error');
            }
        })
        .catch(error => Swal.fire('Error', error.message, 'error'));
});

// Función para validar números en DNI
function validateNumber(input) {
    input.value = input.value.replace(/[^0-9]/g, '');
}
