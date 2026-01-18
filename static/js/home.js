(function () {
    function initHome() {
        // ============================================
        // TRAVEL MEMORIES AUTO SCROLL
        // ============================================
        function infiniteScroll(trackSelector, speed, direction) {
            const track = document.querySelector(trackSelector);
            if (!track || track.dataset.init === "true") return;
            track.dataset.init = "true";
            const images = track.querySelectorAll("img");
            const start = () => {
                const cards = Array.from(track.children);
                if (!cards.length) return;
                const gap = 20; // because you used .me-3
                const totalWidth = cards.reduce(
                    (sum, card) => sum + card.offsetWidth + gap,
                    0
                );
                // Clone once
                cards.forEach(card => {
                    track.appendChild(card.cloneNode(true));
                });
                let position = direction === "left" ? 0 : -totalWidth;
                function animate() {
                    position += direction === "left" ? -speed : speed;
                    if (direction === "left" && position <= -totalWidth) {
                        position = 0;
                    }
                    if (direction === "right" && position >= 0) {
                        position = -totalWidth;
                    }
                    track.style.transform = `translateX(${position}px)`;
                    requestAnimationFrame(animate);
                }
                animate();
            };
            // Wait until images load
            let loaded = 0;
            images.forEach(img => {
                if (img.complete) {
                    loaded++;
                } else {
                    img.onload = () => {
                        loaded++;
                        if (loaded === images.length) start();
                    };
                }
            });
            if (loaded === images.length) start();
        }
        // Initialize with YOUR correct selectors
        infiniteScroll(".slider-left .track-left", 0.4, "left");   // RIGHT → LEFT
        infiniteScroll(".slider-right .track-right", 0.4, "right"); // LEFT → RIGHT
        // ============================================
        // STATS COUNT-UP
        // ============================================
        const counters = document.querySelectorAll(".stat-number");
        const statsSection = document.getElementById("stats");
        if (!counters.length || !statsSection) return;
        let animated = false;
        const animateCounters = () => {
            if (animated) return;
            animated = true;
            counters.forEach(counter => {
                const target = +counter.dataset.target;
                let current = 0;
                const step = Math.max(1, Math.floor(target / 120));
                function update() {
                    current += step;
                    if (current < target) {
                        counter.innerText = current;
                        requestAnimationFrame(update);
                    } else {
                        counter.innerText = target.toLocaleString();
                    }
                }
                update();
            });
        };
        const observer = new IntersectionObserver(entries => {
            if (entries[0].isIntersecting) animateCounters();
        }, { threshold: 0.4 });
        observer.observe(statsSection);
    }
    // ✅ Normal load
    document.addEventListener("DOMContentLoaded", initHome);
    // ✅ BACK / FORWARD NAVIGATION (THIS WAS MISSING)
    window.addEventListener("pageshow", function (event) {
        if (event.persisted) {
            initHome();
        }
    });
})();