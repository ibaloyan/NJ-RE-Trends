// console.log("made some more changes");

d3.json("/NJRE").then((json) => {
    // console.log("returning some data");
    // if (error) return console.warn(error);
    var data1 = json;
    console.log(data1)
    // get table references
    

    // console.log('Hello World');
    

    var tbody = d3.select("tbody");
    console.log(tbody);

    function buildTable(data) {
    // First, clear out any existing data
    console.log(data)
    var testUse =[data]
    tbody.html("");

    // Next, loop through each object in the data
    // and append a row and cells for each value in the row
    testUse.forEach((dataRow) => {
        // Append a row to the table body
        var row = tbody.append("tr");

        // Loop through each field in the dataRow and add
        // each value as a table cell (td)
        Object.values(dataRow).forEach((val) => {
        var cell = row.append("td");
        cell.html("<h1>" + val + "</h1>");
        });
    });
    };
    buildTable(data1);
});
// console.log("I am also working");

// function workingPrint() {
//     console.log("This function works")
// };
// workingPrint()