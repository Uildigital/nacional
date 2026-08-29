document.addEventListener('DOMContentLoaded', () => {
    // Cookie Popup Logic
    const cookiePopup = document.getElementById('cookiePopup');
    const backgroundOverlay = document.getElementById('backgroundOverlay');
    const acceptBtn = document.getElementById('acceptBtn');
    const closeBtn = document.getElementById('closeBtn');

    // Check if user already accepted cookies
    if (!localStorage.getItem('cookiesAccepted')) {
        setTimeout(() => {
            cookiePopup.style.display = 'block';
            backgroundOverlay.style.display = 'block';
        }, 1500); // Show popup after 1.5s
    }

    function closePopup() {
        cookiePopup.style.display = 'none';
        backgroundOverlay.style.display = 'none';
    }

    function acceptCookies() {
        localStorage.setItem('cookiesAccepted', 'true');
        closePopup();
    }

    acceptBtn.addEventListener('click', acceptCookies);
    closeBtn.addEventListener('click', closePopup);

    // Smooth Scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            
            if(targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
