
    function runSearch(){
        const query = document.getElementById('searchInput').value;

        let genres = checkboxChecking();
        let titleFlag = dropdownValue();

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

            console.log(results[0].common_genres_count);

           // console.log("results: "+results)

            printTitles(results);


            //resultsOn();
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



    function resultsOn(){
        document.getElementById("results").style.display = "block";
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



