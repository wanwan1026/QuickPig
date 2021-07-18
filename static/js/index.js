function g1_btn(){
    let countcode = document.getElementById("cbi_text1").value;
    let countpassword = document.getElementById("cbi_text2").value;
    count_data = {"code":countcode,"password":countpassword}

    countAPI="http://127.0.0.1:3000/user"
    fetch(countAPI,{
        method:'PATCH',
        body:JSON.stringify(count_data),
    })
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        // console.log(res);
        if ("error" in res){
            document.getElementById("count_error").innerHTML = "";
            let error = document.getElementById("count_error");
            let error_text = document.createTextNode(res["message"]);
            error.appendChild(error_text);
            error.style = "color: #FFFFFB;";
        }
        if ("ok" in res){
            window.location.href='http://127.0.0.1:3000/count';
        }
    })

    
}
function g2_btn(){
    let countcode = document.getElementById("cbi_text3").value;
    let countpassword = document.getElementById("cbi_text4").value;
    count_data = {"code":countcode,"password":countpassword}

    countAPI="http://127.0.0.1:3000/user"
    fetch(countAPI,{
        method:'PATCH',
        body:JSON.stringify(count_data),
    })
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        // console.log(res);
        if ("error" in res){
            document.getElementById("waiter_error").innerHTML = "";
            let error = document.getElementById("waiter_error");
            let error_text = document.createTextNode(res["message"]);
            error.appendChild(error_text);
            error.style = "color: #FFFFFB;";
        }
        if ("ok" in res){
            window.location.href='http://127.0.0.1:3000/work';
        }
    })
}
function g3_btn(){
    let tablewaiter = document.getElementById("cbi_text5").value;
    let tablecode = document.getElementById("cbi_text6").value;
    let tablepassword = document.getElementById("cbi_text7").value;
    table_data = {"waiter":tablewaiter,"code":tablecode,"password":tablepassword}
    tableAPI = "http://127.0.0.1:3000/table"
    fetch(tableAPI,{
        method:'PATCH',
        body:JSON.stringify(table_data),
    })
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        // console.log(res);
        if ("error" in res){
            document.getElementById("table_error").innerHTML = "";
            let error = document.getElementById("table_error");
            let error_text = document.createTextNode(res["message"]);
            error.appendChild(error_text);
            error.style = "color: #FFFFFB;";
        }
        if ("ok" in res){
            window.location.href='http://127.0.0.1:3000/menu';
        }
    })
}