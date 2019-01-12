

$(document).ready(function () {
    // var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var config = {
        type: 'line',
        data: {
            labels: ["30", "29", "28", "27", "26", "25", "24", "23", "22", "21", "20", "19", "18", "17", "16", "15", "14", "13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"],
            datasets: [{
                label: "Daily Increase in CSR Score",
                fill: false,
                backgroundColor: window.chartColors.blue,
                borderColor: window.chartColors.blue,
                data: [
                    13.8,
                    3,
                    4,
                    5,
                    3,
                    2,
                    1,
                    3,
                    6,
                    7,
                    4,
                    7,
                    3,
                    9,
                    13.8,
                    3,
                    4,
                    5,
                    3,
                    2,
                    1,
                    3,
                    6,
                    7,
                    4,
                    7,
                    3,
                    9,
                    4,
                    10
                ],
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'CSR Score Summary of last 30 days'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Past Days'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Increase in CSR Score'
                    }
                }]
            }
        }
    };
    var ctx = document.getElementById("chartjs_line").getContext("2d");
    window.myLine = new Chart(ctx, config);
});




$(document).ready(function () {
    // var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var config = {
        type: 'line',
        data: {
            labels: ["14", "13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"],
            datasets: [{
                label: "Creds",
                fill: false,
                backgroundColor: window.chartColors.blue,
                borderColor: window.chartColors.blue,
                data: [
                    13.8,
                    3,
                    4,
                    5,
                    3,
                    2,
                    1,
                    3,
                    6,
                    7,
                    4,
                    7,
                    3,
                    9
                ],
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Cred Summary of last 14 days'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Past Days'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Creds Won'
                    }
                }]
            }
        }
    };
    var ctx = document.getElementById("chart_bet").getContext("2d");
    window.myLine = new Chart(ctx, config);
});


$(document).ready(function () {

    var color = Chart.helpers.color;
    var barChartData = {
        labels: ["7", "6", "5", "4", "3", "2", "1"],
        datasets: [{
            label: 'Placed Bets',
            backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
            borderColor: window.chartColors.red,
            borderWidth: 1,
            data: [
                186,
                165,
                300,
                180,
                350,
                200,
                180

            ]
        }, {
            label: 'Actual QCAL values',
            backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
            borderColor: window.chartColors.blue,
            borderWidth: 1,
            data: [
                170,
                189,
                205,
                300,
                180,
                250,
                184,
            ]
        }]

    };

    var ctx = document.getElementById("chartjs_bar_cct").getContext("2d");
    window.myBar = new Chart(ctx, {
        type: 'bar',
        data: barChartData,
        options: {
            responsive: true,
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'QCAL Betting History of 7 days'
            }
        }
    });

});

$(document).ready(function () {

    var color = Chart.helpers.color;
    var barChartData = {
        labels: ["7", "6", "5", "4", "3", "2", "1"],
        datasets: [{
            label: 'Placed Bets',
            backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
            borderColor: window.chartColors.red,
            borderWidth: 1,
            data: [
                300,
                180,
                250,
                184,
                170,
                189,
                205
            ]
        }, {
            label: 'Actual CCT values',
            backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
            borderColor: window.chartColors.blue,
            borderWidth: 1,
            data: [
                350,
                200,
                180,
                186,
                165,
                300,
                180
            ]
        }]

    };

    var ctx = document.getElementById("chartjs_bar_qcal").getContext("2d");
    window.myBar = new Chart(ctx, {
        type: 'bar',
        data: barChartData,
        options: {
            responsive: true,
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'CCT Betting History of 7 days'
            }
        }
    });

});

$(document).ready(function () {
    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100);
    };

    var config = {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                ],
                backgroundColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                    window.chartColors.yellow,
                    window.chartColors.green,
                    window.chartColors.blue,
                ],
                label: 'Dataset 1'
            }],
            labels: [
                "Excellent",
                "Good",
                "Average",
                "Satisfactory",
                "Poor"
            ]
        },
        options: {
            responsive: true,
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                // text: 'Doughnut Chart'
            },
            animation: {
                animateScale: true,
                animateRotate: true
            }
        }
    };

    var ctx = document.getElementById("chartjs_doughnut").getContext("2d");
    window.myDoughnut = new Chart(ctx, config);

});


