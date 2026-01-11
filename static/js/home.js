/* ================= HOME JS ================= */
if (window.__HOME_JS_LOADED__) {
    console.warn("home.js already loaded — skipping re-execution");
} else {
    window.__HOME_JS_LOADED__ = true;

    console.log("home.js loaded");

    document.addEventListener("DOMContentLoaded", () => {

        /* =============================================================== */
        /* ================= TRAVEL MEMORIES AUTO SCROLL ================= */
        /* =============================================================== */
        function infiniteScroll(trackSelector, speed, direction) {
            const track = document.querySelector(trackSelector);
            if (!track) return;

            const cards = Array.from(track.children);
            const totalWidth = cards.reduce(
                (sum, card) => sum + card.offsetWidth + 20,
                0
            );

            cards.forEach(card => {
                track.appendChild(card.cloneNode(true));
            });

            let position = direction === "left" ? 0 : -totalWidth;

            function animate() {
                if (direction === "left") {
                    position -= speed;
                    if (position <= -totalWidth) position = 0;
                } else {
                    position += speed;
                    if (position >= 0) position = -totalWidth;
                }

                track.style.transform = `translateX(${position}px)`;
                requestAnimationFrame(animate);
            }

            animate();
        }

        infiniteScroll(".slider-left .travel-track", 0.4, "left");
        infiniteScroll(".slider-right .travel-track", 0.4, "right");

        /* ============================================================== */
        /* ======================== STATS COUNT-UP ====================== */
        /* ============================================================== */
        const counters = document.querySelectorAll(".stat-number");

        if (counters.length > 0) {
            let hasAnimated = false;

            const animateCounters = () => {
                counters.forEach(counter => {
                    const target = +counter.dataset.target;
                    const increment = target / 120;

                    const update = () => {
                        const current = +counter.innerText;
                        if (current < target) {
                            counter.innerText = Math.ceil(current + increment);
                            requestAnimationFrame(update);
                        } else {
                            counter.innerText = target.toLocaleString();
                        }
                    };
                    update();
                });
            };

            const observer = new IntersectionObserver(entries => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !hasAnimated) {
                        hasAnimated = true;
                        animateCounters();
                    }
                });
            }, { threshold: 0.4 });

            const statsSection = document.getElementById("stats");
            if (statsSection) observer.observe(statsSection);
        }
    });
}
