// document.addEventListener("DOMContentLoaded", () => {
//   const toggle = document.getElementById("toggle-menu");
//   const navLinks = document.getElementById("navLinks");

//   if (toggle && navLinks) {
//     toggle.addEventListener("click", () => {
//       navLinks.classList.toggle("active");
//     });
//   }
// });
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("toggle-menu");
  const navLinks = document.getElementById("navLinks");

  if (toggle && navLinks) {
    // 🔹 Page load hote hi check kare ki pehle se open hai ya nahi
    if (localStorage.getItem("menuOpen") === "true") {
      navLinks.classList.add("active");
    }

    // 🔹 Toggle click hone pe state change kar
    toggle.addEventListener("click", () => {
      navLinks.classList.toggle("active");

      if (navLinks.classList.contains("active")) {
        localStorage.setItem("menuOpen", "true");
      } else {
        localStorage.setItem("menuOpen", "false");
      }
    });
  }
});
