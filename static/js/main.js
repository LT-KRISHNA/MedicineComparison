// Main JavaScript for Medicine Price Comparison

document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Auto-focus search input on home page
    const searchInput = document.querySelector('input[name="q"]');
    if (searchInput && window.location.pathname === '/') {
        searchInput.focus();
    }
});
