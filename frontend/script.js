var x = "Generating...";
var keyword;

function visible() {
    var y = document.getElementById("scroller");
    y.style.display = "block";
}

function clearFunction() {
    document.getElementById("myForm").reset();
    var y = document.getElementById("scroller");
    y.style.display = "none";
}


function myFunction() {
    var elements = document.getElementById("myForm").elements;
    var inputs = {};
    var columns = ['Open', 'High', 'Low', 'Close', 'Volume', '7day_open', '7day_close',
               '7day_high', '7day_low', '40day_open', '40day_close', '40day_high', '40day_low']
    
    if (elements[0].value == "") {
        alert("Enter one or More Manglish words !");
    } else if (elements[0].value.includes("(") ||
        elements[0].value.includes(")")) {
        alert("Enter only Manglish keywords !");
        clearFunction();
    } else {
        document.getElementById("demo").innerHTML = x;
        visible();
        for (let i = 0; i < 13; i++) { 
            inputs[columns[i]]=elements[i].value;
        }
        // keyword = elements[0].value;
        console.log(keyword)
        axios.post("https://dogecoin-prediction-bot.herokuapp.com/", json = inputs).then(response => {
            console.log(response);
            document.getElementById("demo").innerHTML = 'DOGE Closing price prediction is ' + response.data.close + ' USD';

        })
    }

}
