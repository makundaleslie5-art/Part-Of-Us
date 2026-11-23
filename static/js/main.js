// PART OF US - Main JavaScript

document.addEventListener("DOMContentLoaded", function () {

    console.log("Part Of Us website loaded successfully!");

    const menuToggle = document.getElementById("menuToggle");
    const menuClose = document.getElementById("menuClose");
    const sideMenu = document.getElementById("sideMenu");
    const menuBackdrop = document.getElementById("menuBackdrop");

    if (!menuToggle || !menuClose || !sideMenu || !menuBackdrop) {
        return;
    }

    function openMenu() {
        document.body.classList.add("menu-open");
        menuToggle.setAttribute("aria-expanded", "true");
        menuToggle.setAttribute("aria-label", "Close navigation menu");
        sideMenu.setAttribute("aria-hidden", "false");
        menuClose.focus();
    }

    function closeMenu() {
        document.body.classList.remove("menu-open");
        menuToggle.setAttribute("aria-expanded", "false");
        menuToggle.setAttribute("aria-label", "Open navigation menu");
        sideMenu.setAttribute("aria-hidden", "true");
        menuToggle.focus();
    }

    menuToggle.addEventListener("click", function () {
        if (document.body.classList.contains("menu-open")) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    menuClose.addEventListener("click", closeMenu);
    menuBackdrop.addEventListener("click", closeMenu);

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && document.body.classList.contains("menu-open")) {
            closeMenu();
        }
    });

    sideMenu.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", function () {
            document.body.classList.remove("menu-open");
        });
    });

});
