document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('productoForm');
    if (!form) return;

    const nombre = document.getElementById('id_nombre');
    const precio = document.getElementById('id_precio');
    const cantidad = document.getElementById('id_cantidad_disponible');
    const descripcion = document.getElementById('id_descripcion');

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

    const checkNombre = () => validateField(nombre, nombre.value.trim().length >= 3, 'El nombre es obligatorio y debe tener al menos 3 caracteres.');
    const checkPrecio = () => validateField(precio, parseFloat(precio.value) > 0, 'El precio debe ser un número mayor que 0.');
    const checkCantidad = () => validateField(cantidad, Number.isInteger(Number(cantidad.value)) && parseInt(cantidad.value, 10) >= 0, 'La cantidad debe ser un entero igual o mayor a 0.');
    const checkDescripcion = () => validateField(descripcion, descripcion.value.trim().length <= 500, 'La descripción no debe superar los 500 caracteres.');

    [nombre, precio, cantidad, descripcion].forEach(input => {
        input.addEventListener('input', () => {
            if (input === nombre) checkNombre();
            if (input === precio) checkPrecio();
            if (input === cantidad) checkCantidad();
            if (input === descripcion) checkDescripcion();
        });
    });

    form.addEventListener('submit', (e) => {
        const v1 = checkNombre();
        const v2 = checkPrecio();
        const v3 = checkCantidad();
        const v4 = checkDescripcion();

        if (!v1 || !v2 || !v3 || !v4) {
            e.preventDefault();
            e.stopPropagation();
        }
    });
});