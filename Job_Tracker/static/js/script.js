// Custom JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.onclick = function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        }
    });

    // Toggle sidebar on mobile
    const toggleSidebar = () => {
        const sidebar = document.getElementById('sidebar');
        const toggleBtn = document.getElementById('toggle-sidebar');

        if (sidebar.classList.contains('show')) {
            sidebar.classList.remove('show');
            toggleBtn.innerHTML = '<i class="bi bi-list"></i>';
        } else {
            sidebar.classList.add('show');
            toggleBtn.innerHTML = '<i class="bi bi-x"></i>';
        }
    };

    // Add event listener to toggle button
    document.getElementById('toggle-sidebar').addEventListener('click', toggleSidebar);

    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl)
    })
});
