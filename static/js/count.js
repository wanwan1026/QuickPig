function getusetable(){
    tableAPI = "http://127.0.0.1:3000/counts"
    fetch(tableAPI)
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        // console.log(res["tablepick"]);
        // console.log(res["tablepick"][0]["code"]);
        // console.log(res["tablepick"].length)
        for(let i = res["tablepick"].length - 1 ; i >= 0 ; i--){
            // console.log(res["tablepick"][i]["number"]);
            let ordertable = res["tablepick"][i]["code"] + "-table"
            let table = document.getElementById(ordertable);
            let neworder = document.createElement("div");
            let ordertxt = document.createTextNode("單號" + res["tablepick"][i]["number"]);
            neworder.appendChild(ordertxt)
            neworder.className = "tableorder"
            if(res["tablepick"][i]["finish"] == "true"){
                neworder.style = "color: #373C38;background: #D9CD90;";
            }
            table.appendChild(neworder)
            let order = res["tablepick"][i]["code"] + "-order";
            let orderuse = document.getElementById(order);
            orderuse.style = "background: #B9EFC9;"

        }
        // document.getElementById("table").innerHTML = res["table"];
    })
}