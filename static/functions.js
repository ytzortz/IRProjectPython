function search() {
    alert("Searching...");
}

function runSearch(){
    const query = document.getElementById('searchInput').value;
    //ajax here to call flask
    fetch('/search', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query: query }),
})
.then(response => response.json())
.then(data => {
    alert
    console.log("RETURN FROM runSearch(): " + data.message);  // Print the response from the server
})
.catch(error => {
    console.error('Error:', error);
});
}

