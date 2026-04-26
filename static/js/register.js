function togglePassword(fieldId, icon) {
    let field = document.getElementById(fieldId);

    if (field.type === "password") {
        field.type = "text";
        icon.textContent = "🙈";
    } else {
        field.type = "password";
        icon.textContent = "👁️";
    }
}

function validateForm() {
    let password = document.getElementById("password").value;
    let confirm = document.getElementById("confirm_password").value;

    if (password !== confirm) {
        alert("Passwords do not match!");
        return false;
    }

    return true;
}