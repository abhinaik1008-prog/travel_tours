/* ================= EXECUTION GUARD ================= */
if (window.__COMMON_JS_LOADED__) {
    console.warn("common.js already loaded — skipping re-execution");
} else {
    window.__COMMON_JS_LOADED__ = true;

    console.log("common.js loaded");

    /* ================= GLOBAL ================= */
    window.BASE_URL = window.BASE_URL || "http://127.0.0.1:8000";

    /* ============================================================== */
    /* ============== NAVBAR HIDE ONCE → RETURN → LOCK ============== */
    /* ============================================================== */
    (() => {
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
}
