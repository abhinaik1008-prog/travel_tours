/* ================= EXECUTION GUARD ================= */
if (window.__HOME_JS_LOADED__) {
    console.warn("home.js already loaded — skipping re-execution");
} else {
    window.__HOME_JS_LOADED__ = true;

    console.log("home.js loaded");

    /* ================= GLOBAL ================= */
    window.BASE_URL = window.BASE_URL || "http://127.0.0.1:8000";

    /* ================= NAVBAR HIDE ONCE → RETURN → LOCK ================= */
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

    document.addEventListener("DOMContentLoaded", () => {

        /* ================= PACKAGES ================= */
        const packagesContainer = document.getElementById("packages-container");
        const noPackages = document.getElementById("no-packages");

        if (packagesContainer) {
            fetch(`${window.BASE_URL}/api/packages/`)
                .then(res => res.json())
                .then(data => {

                    packagesContainer.innerHTML = "";

                    if (!Array.isArray(data) || data.length === 0) {
                        noPackages?.classList.remove("d-none");
                        return;
                    }

                    noPackages?.classList.add("d-none");

                    data.forEach(pkg => {
                        let image = "/static/images/placeholder.jpg";

                        if (pkg.images?.length && pkg.images[0].image_url) {
                            image = pkg.images[0].image_url;
                        }

                        packagesContainer.insertAdjacentHTML("beforeend", `
                            <div class="col-12 col-sm-6 col-lg-3">
                                <div class="custom-card h-100">
                                    <div class="card-img-wrapper">
                                        <img src="${image}" alt="${pkg.title}">
                                    </div>
                                    <div class="card-body text-center">
                                        <h6>${pkg.title}</h6>
                                        <p>${pkg.destination} • ${pkg.duration_days} days</p>
                                        <p class="fw-semibold text-warning">₹${pkg.price}</p>
                                        <button class="btn book-btn-disabled  w-100" disabled>
                                            Book Now
                                        </button>
                                    </div>
                                </div>
                            </div>
                        `);
                    });
                })
                .catch(err => console.error("Packages API error:", err));
        }
      
        /* ================= DESTINATIONS ================= */
        const destinationsContainer = document.getElementById("destinations-container");
        const noDestinations = document.getElementById("no-destinations");

        if (destinationsContainer) {
            fetch(`${window.BASE_URL}/api/destinations/`)
                .then(res => res.json())
                .then(destinations => {

                    destinationsContainer.innerHTML = "";

                    if (!Array.isArray(destinations) || destinations.length === 0) {
                        noDestinations?.classList.remove("d-none");
                        return;
                    }

                    noDestinations?.classList.add("d-none");

                    destinations.forEach(dest => {
                        let image = "/static/images/placeholder.jpg";

                        if (dest.image) {
                            image = dest.image.startsWith("http")
                                ? dest.image
                                : `${window.BASE_URL}${dest.image}`;
                        }

                        destinationsContainer.insertAdjacentHTML("beforeend", `
                            <div class="col-12 col-sm-6 col-lg-4">
                                <div class="destination-card">
                                    <img src="${image}" alt="${dest.name}">
                                    <div class="destination-overlay">
                                        <span class="destination-country">
                                            ${dest.country || "India"}
                                        </span>
                                        <h5 class="destination-name">${dest.name}</h5>
                                        <p class="destination-desc">
                                            ${
                                                dest.description
                                                    ? dest.description.slice(0, 90)
                                                    : "A popular travel destination loved by explorers."
                                            }
                                        </p>
                                    </div>
                                </div>
                            </div>
                        `);
                    });
                })
                .catch(err => console.error("Destinations API error:", err));
        }


/* ================= PACKAGE MORE / LESS TOGGLE ================= */
/* ================= PACKAGE MORE / LESS TOGGLE ================= */

const packageToggles = document.querySelectorAll(".package-toggle");

packageToggles.forEach(toggle => {
    toggle.addEventListener("click", function () {

        const card = this.closest(".package-card");
        if (!card) return;

        // Close all other cards
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


        /* ================= TRAVEL MEMORIES AUTO SCROLL ================= */
        /* ================= TRAVEL MOMENTS — TRUE INFINITE BOTH DIRECTIONS ================= */

        function infiniteScroll(trackSelector, speed, direction) {
            const track = document.querySelector(trackSelector);
            if (!track) return;

            const cards = Array.from(track.children);
            const totalWidth = cards.reduce(
                (sum, card) => sum + card.offsetWidth + 20,
                0
            );

            // Clone ONCE for seamless looping (NOT visually noticeable)
            cards.forEach(card => {
                track.appendChild(card.cloneNode(true));
            });

            let position =
                direction === "left" ? 0 : -totalWidth;

            function animate() {
                if (direction === "left") {
                    position -= speed;

                    if (position <= -totalWidth) {
                        position = 0;
                    }
                } else {
                    position += speed;

                    if (position >= 0) {
                        position = -totalWidth;
                    }
                }

                track.style.transform = `translateX(${position}px)`;
                requestAnimationFrame(animate);
            }

            animate();
        }

        /* INIT — OPPOSITE DIRECTIONS */
        infiniteScroll(".slider-left .travel-track", 0.4, "left");   // RIGHT → LEFT
        infiniteScroll(".slider-right .travel-track", 0.4, "right"); // LEFT → RIGHT

        /* ================= STATS COUNT-UP ================= */
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
