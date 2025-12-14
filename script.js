document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links (optional, if you add navigation)
    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    for (const link of smoothScrollLinks) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    }

    // Add any other JavaScript functionality here, e.g., animations, dynamic content loading.
    // For a static portfolio like this, JS might be minimal.
    console.log("Portfolio page loaded and ready!");
});