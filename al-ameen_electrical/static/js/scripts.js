// Smooth Scrolling for Navigation Links
document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll(".navbar .nav-link");

    navLinks.forEach(link => {
        link.addEventListener("click", function (event) {
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                event.preventDefault();
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Adjust for the sticky navbar
                    behavior: "smooth"
                });
            }
        });
    });
});

// Placeholder for Live Chat or Future Features
console.log("Scripts loaded successfully.");