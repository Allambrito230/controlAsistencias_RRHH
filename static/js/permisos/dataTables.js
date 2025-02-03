document.addEventListener("DOMContentLoaded", function () {
    $('#dataTable').DataTable({
        "paging": true,         // Habilita paginación
        "lengthMenu": [5, 10, 25, 50], // Opciones de cantidad de registros por página
        "searching": true,      // Activa el cuadro de búsqueda
        "ordering": true,       // Permite ordenar columnas
        "info": true,           // Muestra información de la tabla
        "language": {
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "zeroRecords": "No se encontraron resultados",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
            "infoEmpty": "No hay registros disponibles",
            "infoFiltered": "(filtrado de _MAX_ registros totales)",
            "search": "Buscar:",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            }
        }
    });
});