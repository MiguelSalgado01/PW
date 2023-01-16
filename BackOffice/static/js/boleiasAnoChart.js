


const data = {
    labels: generateLabels(),
    datasets: [
      {
        label: 'Dataset',
        data: generateData(),
        borderColor: Utils.CHART_COLORS.red,
        backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red),
        fill: false
      }
    ]
  };

  const config = {
    type: 'line',
    data: data,
    options: {
      plugins: {
        filler: {
          propagate: false,
        },
        title: {
          display: true,
          text: (ctx) => 'Fill: ' + ctx.chart.data.datasets[0].fill
        }
      },
      interaction: {
        intersect: false,
      }
    },
  };

  const inputs = {
    min: -100,
    max: 100,
    count: 8,
    decimals: 2,
    continuity: 1
  };
  
  const generateLabels = () => {
    return Utils.months({count: inputs.count});
  };
  
  const generateData = () => (Utils.numbers(inputs));