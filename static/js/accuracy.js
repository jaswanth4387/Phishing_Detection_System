let el = document.getElementById("accuracyValue");

let target = parseFloat(el.innerText);
let count = 0;

let interval = setInterval(() => {
    count += target / 30;
    if (count >= target) {
        el.innerText = target + "%";
        clearInterval(interval);
    } else {
        el.innerText = count.toFixed(1) + "%";
    }
}, 30);