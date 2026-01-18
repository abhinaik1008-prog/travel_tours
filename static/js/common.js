// ======================
// GLOBAL BASE URL
// ======================
window.BASE_URL = window.BASE_URL || "http://127.0.0.1:8000";
// ======================
// NAVBAR HIDE ONCE → THEN LOCK
// ======================
(function () {
    const navbar = document.querySelector(".custom-navbar");
    if (!navbar) return;
    let hasTriggered = false;
    window.addEventListener("scroll", () => {
        if (hasTriggered) return;
        if (window.scrollY > 80) {
            hasTriggered = true;
            navbar.classList.add("nav-hidden");
            setTimeout(() => {
                navbar.classList.remove("nav-hidden");
                navbar.classList.add("nav-locked");
            }, 1000);
        }
    }, { passive: true });
})();
// Auto close navbar when Book Now modal opens (mobile)
document.addEventListener("shown.bs.modal", function () {
    const nav = document.querySelector(".navbar-collapse");
    if (nav && nav.classList.contains("show")) {
        nav.classList.remove("show");
    }
});
document.addEventListener("DOMContentLoaded", function () {
    const navbarCollapse = document.querySelector(".navbar-collapse");
    // Automatically remove .show when page loads
    if (navbarCollapse && navbarCollapse.classList.contains("show")) {
        navbarCollapse.classList.remove("show");
    }
    // Also close when clicking any nav link
    document.querySelectorAll(".navbar-collapse .nav-link").forEach(function (link) {
        link.addEventListener("click", function () {
            const bsCollapse = new bootstrap.Collapse(navbarCollapse, { toggle: false });
            bsCollapse.hide();
        });
    });
});