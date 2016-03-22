window.onload = function () {
    var chart = new CanvasJS.Chart("basic_line_chart",
    {
      zoomEnabled: true,
      title:{
        text: "Simple Date-Time Chart"
    },
    axisX:{
        title: "timeline",
        gridThickness: 2
    },
    axisY: {
        title: "Downloads"
    },
    data: [
    {
        type: "area",
        dataPoints: [//array
        { x: new Date(2012, 01, 1), y: 26},
        { x: new Date(2012, 01, 3), y: 38},
        { x: new Date(2012, 01, 5), y: 43},
        { x: new Date(2012, 01, 7), y: 29},
        { x: new Date(2012, 01, 11), y: 41},
        { x: new Date(2012, 01, 13), y: 54},
        { x: new Date(2012, 01, 20), y: 66},
        { x: new Date(2012, 01, 21), y: 60},
        { x: new Date(2012, 01, 25), y: 53},
        { x: new Date(2012, 01, 27), y: 60}
        ]
    }
    ]
});

    chart.render();
}

function hidePanel(panel) {
    //var parentNode = panel.parentNode.parentNode.parentNode.parentNode.parentNode.getElementsByClassName("panel-body");
    var parentNode = panel.parentNode.parentNode.parentNode.parentNode.parentNode;
    $(parentNode).fadeOut('slow');
    console.log(parentNode);
}

function closePanel(panel) {
    //var parentNode = panel.parentNode.parentNode.parentNode.parentNode.parentNode.getElementsByClassName("panel-body");
    var parentNode = panel.parentNode.parentNode.parentNode.parentNode.parentNode;
    $(parentNode).fadeOut('slow');
    console.log(parentNode);
}