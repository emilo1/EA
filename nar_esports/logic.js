var queryUrl = 'https://api.sportradar.us/csgo-t1/en/schedules/2016-06-05/schedule.json?api_key=h55zmfc8rnc4znu9z3wp7m6h'
   
d3.json(queryUrl).then(function(data) {
    console.log(data)
})