$(document).ready(function () {
    // Inicializar DataTable
    var table = $('#dataTable').DataTable({
        "paging": true,
        "lengthMenu": [10, 15, 25, 50],
        "searching": true,
        "ordering": true,
        "info": true,
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

    // Función para filtrar por fecha
    $('#filtrarFechas').click(function () {
        var fechaInicio = $('#fechaInicio').val();
        var fechaFin = $('#fechaFin').val();

        // Convertir fechas a formato YYYY-MM-DD para comparación
        fechaInicio = fechaInicio ? new Date(fechaInicio).getTime() : null;
        fechaFin = fechaFin ? new Date(fechaFin).getTime() : null;

        // Filtro en DataTables
        $.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
            var fechaPermiso = new Date(data[3]).getTime(); // Columna 3: Fecha Inicio

            if ((fechaInicio === null || fechaPermiso >= fechaInicio) &&
                (fechaFin === null || fechaPermiso <= fechaFin)) {
                return true;
            }
            return false;
        });

        table.draw(); // Aplicar filtro
        $.fn.dataTable.ext.search.pop(); // Remover filtro después de aplicar
    });
});
