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
        doc.text(nombre, 50, 75);

        doc.setFont("times", "bold");
        doc.text("Tipo de permiso: ", 20, 87);
        doc.setFont("times", "normal");
        doc.text(tipoPermiso, 70, 87);

        doc.setFont("times", "bold");
        doc.text("Departamento: ", 20, 99);
        doc.setFont("times", "normal");
        doc.text(departamento, 60, 99);

        doc.setFont("times", "bold");
        doc.text("Fecha Inicio: ", 20, 111);
        doc.setFont("times", "normal");
        doc.text(fechaInicio, 55, 111);

        doc.setFont("times", "bold");
        doc.text("Fecha Fin: ", 20, 123);
        doc.setFont("times", "normal");
        doc.text(fechaFin, 55, 123);

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
