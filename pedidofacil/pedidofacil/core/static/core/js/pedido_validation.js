document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('pedidoForm');
    if (!form) return;

    const numPedido = document.getElementById('id_numero_pedido');
    const cliente = document.getElementById('id_cliente');
    const descripcion = document.getElementById('id_descripcion');
    const valorTotal = document.getElementById('id_valor_total');
    const estado = document.getElementById('id_estado');

    const validateField = (input, condition, message) => {
        let errorDiv = input.nextElementSibling;
        if (!errorDiv || !errorDiv.classList.contains('js-error-feedback')) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'js-error-feedback text-danger small mt-1';
            input.parentNode.appendChild(errorDiv);
        }

        if (!condition) {
            input.classList.add('is-invalid');
            input.classList.remove('is-valid');
            errorDiv.textContent = message;
            return false;
        } else {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
            errorDiv.textContent = '';
            return true;
        }
    };

    const checkNumPedido = () => validateField(numPedido, numPedido.value.trim().length > 0, 'El número de pedido es obligatorio.');
    const checkCliente = () => validateField(cliente, cliente.value.trim().length > 0, 'El nombre del cliente es obligatorio.');
    const checkDescripcion = () => validateField(descripcion, descripcion.value.trim().length > 0, 'La descripción es obligatoria.');
    const checkValor = () => validateField(valorTotal, parseFloat(valorTotal.value) > 0, 'El valor total debe ser mayor a 0.');
    const checkEstado = () => validateField(estado, ['pendiente', 'confirmado', 'cancelado'].includes(estado.value), 'Seleccione un estado válido.');

    [numPedido, cliente, descripcion, valorTotal, estado].forEach(input => {
        input.addEventListener('change', () => {
            if (input === numPedido) checkNumPedido();
            if (input === cliente) checkCliente();
            if (input === descripcion) checkDescripcion();
            if (input === valorTotal) checkValor();
            if (input === estado) checkEstado();
        });
    });

    form.addEventListener('submit', (e) => {
        const v1 = checkNumPedido();
        const v2 = checkCliente();
        const v3 = checkDescripcion();
        const v4 = checkValor();
        const v5 = checkEstado();

        if (!v1 || !v2 || !v3 || !v4 || !v5) {
            e.preventDefault();
            e.stopPropagation();
        }
    });
});