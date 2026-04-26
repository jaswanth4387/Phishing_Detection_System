// Password toggle feature
const passwordField = document.querySelector("input[type='password']");

if (passwordField) {
    const toggle = document.createElement("span");
    toggle.innerText = "👁";
    toggle.style.cursor = "pointer";
    toggle.style.position = "absolute";
    toggle.style.right = "15px";
    toggle.style.top = "50%";
    toggle.style.transform = "translateY(-50%)";
    toggle.style.color = "#58a6ff";

    passwordField.parentElement.style.position = "relative";
    passwordField.parentElement.appendChild(toggle);

    toggle.addEventListener("click", () => {
        if (passwordField.type === "password") {
            passwordField.type = "text";
        } else {
            passwordField.type = "password";
        }
    });
}


// Simple input animation (focus highlight)
document.querySelectorAll("input").forEach(input => {
    input.addEventListener("focus", () => {
        input.style.transform = "scale(1.02)";
    });

    input.addEventListener("blur", () => {
        input.style.transform = "scale(1)";
    });
});