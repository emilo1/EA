function init() {

    d3.json("../data/esgsby1.json").then(data => {
        var ESportsGenreData = data
        console.log(ESportsGenreData)

        //*****All*****

        function filterESportsGenresAll(ESports) {
            return ESports.genre;
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresAll = ESportsGenreData.filter(filterESportsGenresAll);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresAll);

        // Use the map method with the arrow function to return all
        var Alltournpool = filterESportsGenresAll.map(ESports => ESports.total_earnings);
        var Alldate = filterESportsGenresAll.map(ESports => ESports.releasedate);

        //  Check your filtered types
        console.log(Alltournpool);
        console.log(Alldate);


        // *****Battle Royale*****

        function filterESportsGenresBR(ESports) {
            return ESports.genre == "Battle Royale";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresBR = ESportsGenreData.filter(filterESportsGenresBR);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresBR);

        // Use the map method with the arrow function to return all
        var BRtournpool = filterESportsGenresBR.map(ESports => ESports.total_earnings);
        var BRdate = filterESportsGenresBR.map(ESports => ESports.releasedate);


        //  Check your filtered types
        console.log(BRtournpool);
        console.log(BRdate);


        // *****Game Card*****

        function filterESportsGenresGC(ESports) {
            return ESports.genre == "Collectible Card Game";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresGC = ESportsGenreData.filter(filterESportsGenresGC);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresGC);

        // Use the map method with the arrow function to return all
        var GCtournpool = filterESportsGenresGC.map(ESports => ESports.total_earnings);
        var GCdate = filterESportsGenresGC.map(ESports => ESports.releasedate);


        //  Check your filtered types
        console.log(GCtournpool);
        console.log(GCdate);


        // *****Fighting Game*****

        function filterESportsGenresFG(ESports) {
            return ESports.genre == "Fighting Game";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresFG = ESportsGenreData.filter(filterESportsGenresFG);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresFG);

        // Use the map method with the arrow function to return all
        var FGtournpool = filterESportsGenresFG.map(ESports => ESports.total_earnings);
        var FGdate = filterESportsGenresFG.map(ESports => ESports.releasedate);


        //  Check your filtered pokemon types
        console.log(FGtournpool);
        console.log(FGdate);


        // *****First-Person Shooter*****

        function filterESportsGenresFP(ESports) {
            return ESports.genre == "First-Person Shooter";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresFP = ESportsGenreData.filter(filterESportsGenresFP);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresFP);

        // Use the map method with the arrow function to return all
        var FPtournpool = filterESportsGenresFP.map(ESports => ESports.total_earnings);
        var FPdate = filterESportsGenresFP.map(ESports => ESports.releasedate);


        //  Check your filtered pokemon types
        console.log(FPtournpool);
        console.log(FPdate);


        // *****Battle Arena*****

        function filterESportsGenresBA(ESports) {
            return ESports.genre == "Multiplayer Online Battle Arena";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresBA = ESportsGenreData.filter(filterESportsGenresBA);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresBA);

        // Use the map method with the arrow function to return all
        var BAtournpool = filterESportsGenresBA.map(ESports => ESports.total_earnings);
        var BAdate = filterESportsGenresBA.map(ESports => ESports.releasedate);


        //  Check your filtered pokemon types
        console.log(BAtournpool);
        console.log(BAdate);


        // *****Puzzle Game*****

        function filterESportsGenresPG(ESports) {
            return ESports.genre == "Puzzle Game";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresPG = ESportsGenreData.filter(filterESportsGenresPG);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresPG);

        // Use the map method with the arrow function to return all
        var PGtournpool = filterESportsGenresPG.map(ESports => ESports.total_earnings);
        var PGdate = filterESportsGenresPG.map(ESports => ESports.releasedate);


        //  Check your filtered pokemon types
        console.log(PGtournpool);
        console.log(PGdate);


        // *****Racing*****

        function filterESportsGenresR(ESports) {
            return ESports.genre == "Racing";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresR = ESportsGenreData.filter(filterESportsGenresR);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresR);

        // Use the map method with the arrow function to return all
        var Rtournpool = filterESportsGenresR.map(ESports => ESports.total_earnings);
        var Rdate = filterESportsGenresR.map(ESports => ESports.releasedate);


        //  Check your filtered pokemon types
        console.log(Rtournpool);
        console.log(Rdate);


        // *****Role-Playing*****

        function filterESportsGenresRP(ESports) {
            return ESports.genre == "Role-Playing Game";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresRP = ESportsGenreData.filter(filterESportsGenresRP);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresRP);

        // Use the map method with the arrow function to return all
        var RPtournpool = filterESportsGenresRP.map(ESports => ESports.total_earnings);
        var RPdate = filterESportsGenresRP.map(ESports => ESports.releasedate);


        //  Check your filtered pokemon types
        console.log(RPtournpool);
        console.log(RPdate);


        // *****Sports*****

        function filterESportsGenresS(ESports) {
            return ESports.genre == "Sports";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresS = ESportsGenreData.filter(filterESportsGenresS);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresS);

        // Use the map method with the arrow function to return all
        var Stournpool = filterESportsGenresS.map(ESports => ESports.total_earnings);
        var Sdate = filterESportsGenresS.map(ESports => ESports.releasedate);


        //  Check your filtered pokemon types
        console.log(Stournpool);
        console.log(Sdate);


        // *****Strategy*****

        function filterESportsGenresSG(ESports) {
            return ESports.genre == "Strategy";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresSG = ESportsGenreData.filter(filterESportsGenresSG);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresSG);

        // Use the map method with the arrow function to return all
        var SGtournpool = filterESportsGenresSG.map(ESports => ESports.total_earnings);
        var SGdate = filterESportsGenresSG.map(ESports => ESports.releasedate);


        //  Check your filtered pokemon types
        console.log(SGtournpool);
        console.log(SGdate);


        // *****Third Person*****

        function filterESportsGenresTP(ESports) {
            return ESports.genre == "Third-Person Shooter";
        }

        // Use filter() to pass the function as its argument
        var filterESportsGenresTP = ESportsGenreData.filter(filterESportsGenresTP);

        //  Check to make sure your are filtering
        console.log(filterESportsGenresTP);

        // Use the map method with the arrow function to return all
        var TPtournpool = filterESportsGenresTP.map(ESports => ESports.total_earnings);
        var TPdate = filterESportsGenresTP.map(ESports => ESports.releasedate);


        //  Check your filtered pokemon types
        console.log(TPtournpool);
        console.log(TPdate);


        // fetch('/api/genre/Racing')
        //     .then(response => response.json())
        //     .then(data => {
        //         console.log(data)


        // Create your trace.
        var trace = {
            x: Alldate,
            // marker: {
            //     color: ['#A6B91A', '#705746', '#6F35FC', '#F7D02C',
            //         '#D685AD', '#C22E28', '#EE8130', '#A98FF3', '#735797',
            //         '#7AC74C', '#E2BF65', '#96D9D6', '#A8A77A', '#A33EA1',
            //         '#F95587', '#B6A136', '#B7B7CE', '#6390F0']
            // },
            y: Alltournpool,
            
            type: "bar"

        };


        // Create the data array for plot
        var data = [trace];

        // Define plot layout
        var layout = {
            barmode: 'stack',
            title: "Total Prize Money Awarded by Year",
            xaxis: { title: "Year" },
            yaxis: { title: "Total Tournament Prize Money" }

        };

        // Plot the chart
        Plotly.newPlot("barchart", data, layout);

        //****************/

        // Initializes the page with a default plot
        function init() {
            data = [{
                x: xvaluesAll,
                y: yvaluesAll,
                // marker: {
                //     color: ['#A6B91A', '#705746', '#6F35FC', '#F7D02C',
                //         '#D685AD', '#C22E28', '#EE8130', '#A98FF3', '#735797',
                //         '#7AC74C', '#E2BF65', '#96D9D6', '#A8A77A', '#A33EA1',
                //         '#F95587', '#B6A136', '#B7B7CE', '#6390F0']
                // },
                type: "bar"
            }];

            var layout = {
                barmode: 'stack',
                title: "Total Prize Money Awarded by Year",
                xaxis: { title: "Year" },
                yaxis: { title: "Total Tournament Prize Money" }

            };



            Plotly.newPlot("barchart", data, layout);
        }

        // Call updatePlotly() when a change takes place to the DOM
        d3.selectAll("body").on("change", updatePlotly);

        // This function is called when a dropdown menu item is selected
        function updatePlotly() {
            // Use D3 to select the dropdown menu
            var dropdownMenu = d3.select("#selDataset");
            // Assign the value of the dropdown menu option to a variable
            var dataset = dropdownMenu.property("value");

            // Initialize x and y arrays
            var x = [];
            var y = [];

            switch (dataset) {
                case "ESportsBattle":
                    x = BRdate;
                    y = BRtournpool;
                    break;

                case "ESportsCard":
                    x = GCdate;
                    y = GCtournpool;
                    break;

                case "ESportsFighting":
                    x = FGdate;
                    y = FGtournpool;
                    break;

                case "ESportsFirst":
                    x = FPdate;
                    y = FPtournpool;
                    break;

                case "ESportsArena":
                    x = BAdate;
                    y = BAtournpool;
                    break;

                case "ESportsPuzzle":
                    x = PGdate;
                    y = PGtournpool;
                    break;

                case "ESportsRacing":
                    x = Rdate;
                    y = Rtournpool;                    break;

                case "ESportsRole":
                    x = RPdate;
                    y = RPtournpool;                    break;

                case "ESportsSports":
                    x = Sdate;
                    y = Stournpool;                    break;

                case "ESportsStrategy":
                    x = SGdate;
                    y = SGtournpool;
                    break;

                case "ESportsThird":
                    x = TPdate;
                    y = TPtournpool;
                    break;

                case "ESportsAll":
                    x = Alldate;
                    y = Alltournpool;
                    break;
            }


            // Note the extra brackets around 'x' and 'y'
            Plotly.restyle("barchart", "x", [x]);
            Plotly.restyle("barchart", "y", [y]);

        }

    })
}

init()
