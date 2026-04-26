// 🔍 Search functionality
document.getElementById("searchInput").addEventListener("keyup", function () {

    let filter = this.value.toLowerCase();
    let rows = document.querySelectorAll("#predictionTable tr");

    rows.forEach(row => {
        let text = row.innerText.toLowerCase();

        if (text.includes(filter)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });

});