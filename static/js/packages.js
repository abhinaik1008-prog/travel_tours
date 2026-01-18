/* ================= PACKAGES JS ================= */
if (window.__PACKAGES_JS_LOADED__) {
    console.warn("packages.js already loaded — skipping re-execution");
} else {
    window.__PACKAGES_JS_LOADED__ = true;
    console.log("packages.js loaded");
    document.addEventListener("DOMContentLoaded", () => {
        /* ================= PACKAGE MORE / LESS ================= */
        const packageToggles = document.querySelectorAll(".package-toggle");
        packageToggles.forEach(toggle => {
            toggle.addEventListener("click", function () {
                const card = this.closest(".package-card");
                if (!card) return;
                document.querySelectorAll(".package-card").forEach(otherCard => {
                    if (otherCard !== card) {
                        otherCard.classList.remove("expanded");
                        otherCard.querySelector(".short-desc")?.classList.remove("d-none");
                        otherCard.querySelector(".full-desc")?.classList.add("d-none");
                        otherCard.querySelector(".package-extra-details")?.classList.add("d-none");
                        const btn = otherCard.querySelector(".package-toggle");
                        if (btn) {
                            btn.innerHTML = `More <i class="bi bi-chevron-down ms-1"></i>`;
                        }
                    }
                });
                const isExpanded = card.classList.toggle("expanded");
                const shortDesc = card.querySelector(".short-desc");
                const fullDesc = card.querySelector(".full-desc");
                const extraDetails = card.querySelector(".package-extra-details");
                if (isExpanded) {
                    shortDesc?.classList.add("d-none");
                    fullDesc?.classList.remove("d-none");
                    extraDetails?.classList.remove("d-none");
                    this.innerHTML = `Less <i class="bi bi-chevron-up ms-1"></i>`;
                } else {
                    shortDesc?.classList.remove("d-none");
                    fullDesc?.classList.add("d-none");
                    extraDetails?.classList.add("d-none");
                    this.innerHTML = `More <i class="bi bi-chevron-down ms-1"></i>`;
                }
            });
        });
    });
}