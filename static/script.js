//  const toggle = document.getElementById("toggle-menu");
//         const navLinks = document.getElementById("navLinks");

//         toggle.addEventListener("click", () => {
//             navLinks.classList.toggle("active");
//         });

document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("toggle-menu");
  const navLinks = document.getElementById("navLinks");

  if (toggle && navLinks) {
    toggle.addEventListener("click", () => {
      navLinks.classList.toggle("active");
    });
  }
});
