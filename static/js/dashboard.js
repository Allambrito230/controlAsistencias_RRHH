document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.querySelector('.toggle-sidebar-btn');
    const body = document.body;
  
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        body.classList.toggle('toggle-sidebar');
      });
    }
  });
  