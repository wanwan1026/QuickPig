function getorder(){
    tableAPI = "http://127.0.0.1:3000/works"
    fetch(tableAPI)
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        if(res["logincode"] == "false"){
            location.href='http://127.0.0.1:3000'
        }
        if("logincode" in res){
            for( i = 0 ; i < res["data"].length ; i++){
                let mainbox = document.getElementById("main");
                let outbox = document.createElement("div");
                outbox.className = "work";
                let inbox1 = document.createElement("div");
                inbox1.className = "work_txt02";
                let inbox1_tx1 = document.createElement("div");
                let inbox1_tx1_1 = document.createTextNode(res["data"][i]["code"]);
                inbox1_tx1.appendChild(inbox1_tx1_1);
                let inbox1_tx2 = document.createElement("div");
                let inbox1_tx2_2 = document.createTextNode("單號 : " + res["data"][i]["number"]);
                inbox1_tx2.appendChild(inbox1_tx2_2);
                let inbox1_tx3 = document.createElement("div");

                let content = res["data"][i]["content"]
                pick = content.split(";")
                allpick = ""
                for(j = 0 ; j < pick.length ;j++){
                    let foodname = pick[j].split(",")[0]
                    let foodfeq = pick[j].split(",")[2]
                    allpick = allpick + "," + " " + foodname + "*" + foodfeq
                }
                allpick = allpick.substr(1) + "。"

                let inbox1_tx3_3 = document.createTextNode("內容 : " + allpick);
                inbox1_tx3.appendChild(inbox1_tx3_3);
                inbox1.appendChild(inbox1_tx1)
                inbox1.appendChild(inbox1_tx2)
                inbox1.appendChild(inbox1_tx3)
                outbox.appendChild(inbox1)
                let inbox2 = document.createElement("div");
                inbox2.className = "gb_box"

                if(i == 0){
                    let inbox2_bt = document.createElement("button");
                    inbox2_bt.className = "go_btn"
                    let inbox2_bttx = document.createTextNode("完成餐點");
                    inbox2_bt.id = res["data"][i]["number"]
                    inbox2_bt.setAttribute("onclick","postok(this);");
                    inbox2_bt.appendChild(inbox2_bttx)
                    inbox2.appendChild(inbox2_bt)
                }

                outbox.appendChild(inbox2)
                mainbox.appendChild(outbox)
        }
        }
    })
}

function postok(obj){
    finishdata = {"ok":obj.id}
    let postAPI = "http://127.0.0.1:3000/works"
    fetch(postAPI,{
        method:'POST',
        body:JSON.stringify(finishdata),
    })
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        
        console.log(res);
        location.reload();

    })
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