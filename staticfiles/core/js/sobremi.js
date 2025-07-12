function showToast(message, type = 'error') {
  const container = document.getElementById('toast-container');
  const toast = document.createElement('div');
  toast.classList.add('toast', type === 'success' ? 'toast-success' : 'toast-error');
  toast.textContent = message;

  container.appendChild(toast);

  setTimeout(() => {
    toast.classList.add('show');
  }, 100);

  setTimeout(() => {
    toast.classList.remove('show');
    toast.classList.add('hide');
    setTimeout(() => container.removeChild(toast), 500);
  }, 4000);
}

document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('.formulario-contacto');
  const background = document.querySelector('.background');
  const mensajeExito = background?.dataset.mensajeExito;

  // Mostrar toast si hay mensaje de éxito
  if (mensajeExito) {
    showToast(mensajeExito, 'success');
  }

  if (!form) return;

  form.addEventListener('submit', function (event) {
    event.preventDefault();

    const nombre = this.querySelector('input[name="nombre"]');
    const email = this.querySelector('input[name="email"]');
    const mensaje = this.querySelector('textarea[name="mensaje"]');

    if (!nombre.value.trim()) {
      showToast('El campo "Nombre" es obligatorio.');
      nombre.focus();
      return;
    }

    if (!email.value.trim()) {
      showToast('El campo "Correo electrónico" es obligatorio.');
      email.focus();
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value.trim())) {
      showToast('Por favor ingresa un correo electrónico válido.');
      email.focus();
      return;
    }

    if (!mensaje.value.trim()) {
      showToast('El campo "Mensaje" es obligatorio.');
      mensaje.focus();
      return;
    }

    this.submit();
  });
});
