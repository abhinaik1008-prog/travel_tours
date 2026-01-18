/* ================= DESTINATIONS JS ================= */
if (window.__DESTINATIONS_JS_LOADED__) {
    console.warn("destinations.js already loaded — skipping re-execution");
} else {
    window.__DESTINATIONS_JS_LOADED__ = true;
    console.log("destinations.js loaded");
    document.addEventListener("DOMContentLoaded", () => {
        /* ================= FILTER BUTTON ACTIVE ================= */
        const filterButtons = document.querySelectorAll(".filter-btn");
        filterButtons.forEach(btn => {
            btn.addEventListener("click", () => {
                filterButtons.forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
            });
        });
    });
}