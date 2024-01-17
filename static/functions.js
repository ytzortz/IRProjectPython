
    function runSearch(){
        const query = document.getElementById('searchInput').value;

        let genres = checkboxChecking();
        let titleFlag = dropdownValue();

        clearTable();

        if(query === "")
            resultsNone();
        else{
            //ajax here to call flask
            fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
             query: query,
             genres: genres,
             titleFlag: titleFlag //if this is 1, we search in titles. if 2, we search in description
             }),
        })
        .then(response => response.json())
        .then(data => {
            console.log("RETURN FROM runSearch() --OK");

            let results =  JSON.parse(data.results);

            console.log("results: "+results[0].perc)
         //  console.log("Score 1: "+results.perc[0]);
         //  console.log("Score 2: "+results.perc[1]);

          //  printTitles(results);


            resultsOn(results);
        })
        .catch(error => {
            console.error('Error:', error);
        });

        }


    }

    function printTitles(results) {

        console.log(results.length);
        for (let i = 0; i < results.length; i++) {
            console.log("Title: ", results[i].title, "genres hits: ", results[i].common_genres_count);
        }

    }

    function checkboxChecking(){
          var checkboxes = document.getElementsByName('checkboxGroup');
          var checkedCheckboxes = [];

          for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
              checkedCheckboxes.push(checkboxes[i].value);
            }
          }

          return checkedCheckboxes;
    }


    function resultsOn(results){
        document.getElementById("results").style.display = "block";
        let table = document.getElementById("tableResults");

          // Loop through the data and populate the table
          for (let i = 0; i < results.length; i++) {
            var newRow = table.insertRow();
            var titleCell = newRow.insertCell(0);
            var genresCell = newRow.insertCell(1);
            var percCell = newRow.insertCell(2);
            var watchCell = newRow.insertCell(3);

            // Set the content for each cell using the data array
            titleCell.innerHTML = results[i].title;


           // console.log(extractNames(results[i].genres))



            genresCell.innerHTML = extractNames(results[i].genres);

            percCell.innerHTML = results[i].perc;

            var watchButton = document.createElement("button");
            watchButton.innerHTML = "Watch";
            watchButton.style.backgroundColor = "orange";

            // Assign an empty function to the button's onclick attribute
            watchButton.onclick = function() {};


            watchCell.appendChild(watchButton);


          }

    }


    function resultsNone(){
        document.getElementById("results").style.display = "none";
    }

    function dropdownValue(){
        if(document.getElementById("dropdown").value === "titles")
            return 1;
        else
            if(document.getElementById("dropdown").value === "both")
                return 2;


    return 0;
    }

    function destroyIndex(){
        fetch('/run-destroy-index-script', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            .then(() => {
                console.log("Destroying Indexes --OK")
            })
            .catch(error => {
                console.error(error);
                alert('Error occurred while running the script.');
            });
    }

    function initIndex() {
        fetch('/run-index-script', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(() => {
            console.log("Indexing --OK")
        })
        .catch(error => {
            console.error(error);
            alert('Error occurred while running the script.');
        });
    }

    function clearTable() {
      var table = document.getElementById("tableResults");

      // Remove all rows except the first one (header row)
      while (table.rows.length > 1) {
        table.deleteRow(1);
      }
    }

    function extractNames(inputString) {
    let resultList = [];

    // Find occurrences of 'name': and extract the values without single quotes
    const regex = /'name':\s*'([^']*)'/g;
    let match;

    while ((match = regex.exec(inputString)) !== null) {
        resultList.push(match[1]);
    }

    return resultList;
    }