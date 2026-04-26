const ctx = document.getElementById('chart');

new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Phishing', 'Safe'],
        datasets: [{
            data: [window.phishing, window.safe],
        }]
    },
    options: {
        plugins: {
            legend: {
                labels: { color: "white" }
            }
        }
    }
});