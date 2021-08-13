// // function init() {
// //     var data = [];
// //     d3.request("/home").get(response => {

// //         data = JSON.parse(response.response);
// //         console.log(data);
// //         })};
// function searchForItem() {
//     var searchTerm = d3.select("#search_term").property("value");
//     var baseURL = window.location.origin;
//     window.location.href = `${baseURL}/products/${searchTerm}`

//     window.location.replace(`${baseURL}/products/${searchTerm}`)
// }
// d3.selectAll("#filter-btn").on("click", searchForItem);

// var rawData=fetch('/nutritionfacts')
//   .then(response => response.json())
//   .then(data => plotData(data));

// function plotData(rawData){
//     // console.log(rawData)
//     // console.log(Object.entries(rawData))
//     var xvalues = []
//     var ylabels = []

//     Object.entries(rawData).slice(0,-1).forEach((fact)=> {
//         var facts=fact[1]
//         xvalues.push(facts["percent"])

//         ylabels.push(facts["label"])


//     })
//     console.log(ylabels)
//     console.log(xvalues)


//     var trace = {
//         // x: [0,1,2],
//         // y: [0,1,2],
//         // text: [0,1,2],
//         x: xvalues,
//         y: ylabels,
        

//         marker: {
//             color: 'blue'
//         },
//         type: "bar",
//         orientation: "h",
//     };
//     // create data variable
//     var data = [trace];
    
//     // create layout variable to set plots layout
//     var layout = {
//         title: "Nutrition Facts",
//         yaxis: {
//             tickmode: "linear",
//         },
//         // margin: {
//         //     l: 100,
//         //     r: 100,
//         //     t: 100,
//         //     b: 30
//         // }
//     };
    
//     // create the bar plot
//     Plotly.newPlot("barplotdiv", data, layout);
// }