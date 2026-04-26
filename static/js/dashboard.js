// Animate numbers (count-up effect)
document.querySelectorAll('.card-box p').forEach(el => {
    let value = parseInt(el.innerText);
    let count = 0;

    let interval = setInterval(() => {
        count += Math.ceil(value / 30);
        if (count >= value) {
            el.innerText = value;
            clearInterval(interval);
        } else {
            el.innerText = count;
        }
    }, 30);
});


// Chart
const ctx = document.getElementById('chart');

if (ctx) {
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Phishing', 'Safe'],
            datasets: [{
                data: [
                    window.phishing_count || 0,
                    window.safe_count || 0
                ],
                borderWidth: 1
            }]
        },
        options: {
            plugins: {
                legend: {
                    labels: {
                        color: "white"
                    }
                }
            }
        }
    });
}