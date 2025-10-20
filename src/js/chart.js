Chart.register(ChartDataLabels);

const chart1 = new Chart(document.getElementById('chart1'), {
  type: 'pie',
  data: {
    labels: ['Superior', 'Básica', 'Média'],
    datasets: [{
      label: 'Chart 1',
      data: [32, 45, 23],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)'
      ],
      borderColor: [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)'
      ],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'bottom'
      }
    },
    responsive: false,
  }
});

const chart2 = new Chart(document.getElementById('chart2'), {
  type: 'bar',
  data: {
    labels: ['1', '2', '3', '4'],
    datasets: [{
      label: 'Tempo de Estudo (h)',
      data: [12.5, 13.5, 15, 15],
      backgroundColor: [
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(226, 255, 64, 0.2)'
      ],
      borderColor: [
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(226, 255, 64, 1)'
      ],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        display: false
      }
    },
    responsive: false,
    scales: {
      y: {
        min: 0,
        max: 16,
        beginAtZero: true,
        title: {
          display: true,
          text: 'Nota média'
        }
      },
    }
  }
});

const chart3 = new Chart(document.getElementById('chart3'), {
  type: 'bar',
  data: {
    labels: ['Sem Apoio', 'Com Apoio'],
    datasets: [{
      label: 'Apoio',
      data: [10, 12],
      backgroundColor: [
        'rgba(48, 70, 110, 0.2)',
        'rgba(138, 92, 231, 0.2)',
      ],
      borderColor: [
        'rgba(75, 192, 192, 1)',
        'rgba(100, 65, 182, 1)',
      ],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        display: false
      }
    },
    responsive: false,
    scales: {
      y: {
        beginAtZero: true,
        title: {
            display: true,
            text: 'Nota média'
        }
      },
    }
  }
});

const chart4 = new Chart(document.getElementById('chart4'), {
  type: 'bar',
  data: {
    labels: ['Sem internet', 'Com internet'],
    datasets: [{
        label: 'Nota média',
        data: [11, 12.2],
        backgroundColor: ['#9b4e9b60', '#5b87885e'],
        borderColor: ['#9b4e9b', '#5b8788'],
        borderWidth: 1
    }]
  },
  options: {
    responsive: false,
    plugins: {
      legend: {
        display: false
      }
    },
    scales: {
      y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Nota média'
          }
      },
    }
  }
});

const chart5 = new Chart(document.getElementById('chart5'), {
  type: 'line',
  data: {
    labels: ['15', '30', '45', '60'],
    datasets: [{
      label: 'Dataset 1',
      data: [14, 14, 13, 11.3],
      backgroundColor: 'rgba(255, 206, 86, 0.2)',
      borderColor: 'rgba(255, 206, 86, 1)',
      borderWidth: 1
    }]
  },
  options: {
    responsive: false,
    scales: {
      y: {
        min: 5,
        max: 15,
        beginAtZero: true,
        title: {
          display: true,
          text: 'Nota média'
        }
      },
      x: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Tempo em (min)'
        }
      }
    },
    plugins: {
      legend: {
        display: false
      }
    }
  }
});

const chart6 = new Chart(document.getElementById('chart6'), {
  type: 'bar',
  data: {
    labels: ['Sem atividade', 'Com atividade'],
    datasets: [{
        label: 'Nota média',
        data: [11, 12.2],
        backgroundColor: ['#fddc7060', '#3744b65e'],
        borderColor: ['#adac59ff', '#5b6588ff'],
        borderWidth: 1
    }]
  },
  options: {
    responsive: false,
    plugins: {
      legend: {
        display: false
      }
    },
    scales: {
      y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Nota média'
          }
      },
    }
  }
});

const chart7 = new Chart(document.getElementById('chart7'), {
  type: 'line',
  data: {
    labels: ['1', '2', '3', '4', '5'],
    datasets: [{
      label: 'Dataset 1',
      data: [45, 70, 50, 90, 66],
      backgroundColor: 'rgba(255, 206, 86, 0.2)',
      borderColor: 'rgba(255, 206, 86, 1)',
      borderWidth: 1
    },
    {
      label: 'Dataset 2',
      data: [30, 50, 80, 40, 76],
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1
    }]
  },
  options: {
    responsive: false,
    plugins: {
      legend: {
        display: false
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Nota média'
        }
      },
      x: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Nível de consumo'
        }
      }
    }
  }
});

const chart8 = new Chart(document.getElementById('chart8'), {
  type: 'bar',
  data: {
    labels: ['Sem vontade', 'Com vontade'],
    datasets: [{
        label: 'Nota média',
        data: [8.5, 12.2],
        backgroundColor: ['#9b4e9b60', '#5b87885e'],
        borderColor: ['#9b4e9b', '#5b8788'],
        borderWidth: 1
    }]
  },
  options: {
    responsive: false,
    plugins: {
      legend: {
        display: false
      }
    },
    scales: {
      y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Nota média'
          }
      },
    }
  }
});