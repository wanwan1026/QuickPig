function getusetable(){
    tableAPI = "http://127.0.0.1:3000/counts"
    fetch(tableAPI)
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        if("logincode" in res){
            if(res["logincode"] == "false"){
                location.href='http://127.0.0.1:3000'
            }
            if("logincode" in res){
                for(let i = res["tablepick"].length - 1 ; i >= 0 ; i--){
                    if(res["tablepick"][i]["finish"] == "true"){
                        let ordertable = res["tablepick"][i]["code"] + "-table"
                        let table = document.getElementById(ordertable);
                        let neworder = document.createElement("div");
                        let ordertxt = document.createTextNode("單號" + res["tablepick"][i]["number"]);
                        neworder.appendChild(ordertxt)
                        neworder.className = "tableorder"
                        neworder.style = "color: #FFFFFB;background: #005CAF;";
                        table.appendChild(neworder)
                    }
                    if(res["tablepick"][i]["finish"] == "false"){
                        let ordertable = res["tablepick"][i]["code"] + "-table"
                        let table = document.getElementById(ordertable);
                        let neworder = document.createElement("div");
                        let ordertxt = document.createTextNode("單號" + res["tablepick"][i]["number"]);
                        neworder.appendChild(ordertxt)
                        neworder.className = "tableorder"
                        neworder.style = "color: #FFFFFB;background: #91989F;";
                        table.appendChild(neworder)
                    }
                    if(res["tablepick"][i]["finish"] == "close"){
                        let ordertable = res["tablepick"][i]["code"] + "-table"
                        let table = document.getElementById(ordertable);
                        let neworder = document.createElement("div");
                        let ordertxt = document.createTextNode("單號" + res["tablepick"][i]["number"]);
                        neworder.appendChild(ordertxt)
                        neworder.className = "tableorder"
                        neworder.style = "color: #FFFFFB;background: #1C1C1C;";
                        table.appendChild(neworder)
                    }
                }
                for(let i = res["tablestatus"].length - 1 ; i >= 0 ; i--){
                    let order = res["tablestatus"][i]["code"] + "-order";
                    let orderuse = document.getElementById(order);
                    if(res["tablestatus"][i]["status"] == "true"){
                        orderuse.style = "background: #B9EFC9;"
                    }
                    if(res["tablestatus"][i]["status"] == "false"){
                        orderuse.style = "background: #FFFFFB;"
                    }
                    if(res["tablestatus"][i]["status"] == "close"){
                        orderuse.style = "background: #FEDFE1;"
                    }
                }            
            }            
        }
    })
}

function pay(obj){
    location.href=`http://127.0.0.1:3000/pay?tablecode=${obj.value}`
}

function loginout(){
    loginoutAPI = "http://127.0.0.1:3000/user"
    fetch(loginoutAPI,{
        method:'DELETE'
    })
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        if("success" in res){
            location.href='http://127.0.0.1:3000'
        }else{
            location.href='http://127.0.0.1:3000'
        }
    })
}