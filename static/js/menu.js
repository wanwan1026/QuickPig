function sidebtn(){
    document.getElementById("sidemenu").style.display="none";
    document.getElementById("sidebtn").style.display="none";
    document.getElementById("sidebtn2").style.display="block";
}
function sidebtn2(){
    document.getElementById("sidemenu").style.display="block";
    document.getElementById("sidebtn").style.display="block";
    document.getElementById("sidebtn2").style.display="none";
}

function mtb_change(obj){
    let getdata="";
    if(obj.value == "MM"){
        let btn1 = document.getElementById("mt_bt1");
        let btn2 = document.getElementById("mt_bt2");
        let btn3 = document.getElementById("mt_bt3");
        let btn4 = document.getElementById("mt_bt4");

        btn1.style = "background-color: #9F353A;color: #FFFFFB;border-bottom: 10px #FFFFFB double;"
        btn2.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
        btn3.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
        btn4.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
    
        getdata = "MM";
    
    }
    if(obj.value == "ST"){
        let btn1 = document.getElementById("mt_bt1");
        let btn2 = document.getElementById("mt_bt2");
        let btn3 = document.getElementById("mt_bt3");
        let btn4 = document.getElementById("mt_bt4");

        btn1.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
        btn2.style = "background-color: #9F353A;color: #FFFFFB;border-bottom: 10px #FFFFFB double;"
        btn3.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
        btn4.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
    
        getdata = "ST";
    
    }
    if(obj.value == "STM"){
        let btn1 = document.getElementById("mt_bt1");
        let btn2 = document.getElementById("mt_bt2");
        let btn3 = document.getElementById("mt_bt3");
        let btn4 = document.getElementById("mt_bt4");

        btn1.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
        btn2.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
        btn3.style = "background-color: #9F353A;color: #FFFFFB;border-bottom: 10px #FFFFFB double;"
        btn4.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
    
        getdata = "STM";

    }
    if(obj.value == "DK"){
        let btn1 = document.getElementById("mt_bt1");
        let btn2 = document.getElementById("mt_bt2");
        let btn3 = document.getElementById("mt_bt3");
        let btn4 = document.getElementById("mt_bt4");

        btn1.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
        btn2.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
        btn3.style = "background-color: #FFFFFB;color: #9F353A;border-bottom: 10px #FFFFFB solid;"
        btn4.style = "background-color: #9F353A;color: #FFFFFB;border-bottom: 10px #FFFFFB double;"

        getdata = "DK";
    }

    let menuUrl = `http://127.0.0.1:3000/menus?class=${getdata}`;
    fetch(menuUrl)
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        if(res["data"] == ""){
            console.log("指定類別並無餐點")
        }
        if(res["data"] != ""){
            document.getElementById("menu_box").innerHTML = ""; 
            for(i = 0 ; i < res["data"].length ; i++){
                let menu_box = document.getElementById("menu_box");
                let menu_inbox = document.createElement("div");
                let menu_img = document.createElement("img");
                let menu_txt1 = document.createElement("div");
                let menu_txt1_1 = document.createElement("a");
                let menu_txt2 = document.createElement("div");
                let tx1 = document.createTextNode("$ ");
                let tx2 = document.createTextNode(res["data"][i]["price"]);
                let tx3 = document.createTextNode(res["data"][i]["name"]);
                let req = document.createElement("div");
                let req_txt = document.createTextNode("1");

                menu_img.src = res["data"][i]["image"];
                menu_txt1.className = "menu_txt";
                menu_txt1_1.className = "menu_txt2";
                menu_txt2.className = "menu_txt";
                menu_inbox.className = "menu_inbox";
                menu_inbox.id = res["data"][i]["code"];
                menu_inbox.setAttribute("onclick","postMenu(this);");
                req.id = res["data"][i]["code"] + "-req";
                req.className = "menu_feq";
                req.appendChild(req_txt);
                
                menu_txt1_1.appendChild(tx2);
                menu_txt1.appendChild(tx1);
                menu_txt1.appendChild(menu_txt1_1);
                menu_txt2.appendChild(tx3)
                menu_inbox.appendChild(menu_img);
                menu_inbox.appendChild(menu_txt1);
                menu_inbox.appendChild(menu_txt2);
                menu_inbox.appendChild(req);
                menu_box.appendChild(menu_inbox);
                
                if(document.getElementById(res["data"][i]["code"] + "-order")){
                    document.getElementById(res["data"][i]["code"] + "-req").style.display="block";
                    reqfeq = document.getElementById(res["data"][i]["code"] + "-order").innerText;
                    reqfeq = parseInt(reqfeq);
                    document.getElementById(res["data"][i]["code"] + "-req").innerHTML = reqfeq;
                } 
            }
        }
    })
}

function postMenu(obj){
    let menu_txt = document.getElementById(obj.id).innerText;
    menu_txt = menu_txt.split("\n");
    let menu_name = menu_txt[1];
    let menu_price = menu_txt[0];

    order_id = obj.id + "-order"
    if(document.getElementById(order_id)){
        orderfeq = document.getElementById(obj.id + "-order").innerText;
        orderfeq = parseInt(orderfeq);
        orderfeq = orderfeq + 1 ;

        document.getElementById(obj.id + "-order").innerHTML = orderfeq;

        reqfeq = document.getElementById(obj.id + "-req").innerText;
        reqfeq = parseInt(reqfeq);
        reqfeq = reqfeq + 1 ;
        document.getElementById(obj.id + "-req").innerHTML = reqfeq;

        let order_all = document.getElementById("order_all").innerText;
        order_all = parseInt(order_all);
        let one_menu_price = menu_price.split(" ");
        one_menu_price = parseInt(one_menu_price[1]);
        order_all = order_all + one_menu_price;
        document.getElementById("order_all").innerHTML = order_all;

    }else{
        let order_out = document.getElementById("order_out");
        let order_box = document.createElement("div");
        let order_box1 = document.createElement("div");
        let order_number = document.createElement("div");
        let order_text1 = document.createElement("div");
        let order_text2 = document.createElement("div");
        let order_text1_a = document.createElement("a");
        let order_text_btn1 = document.createElement("button");
        let order_text_div = document.createElement("div");
        let order_text_btn2 = document.createElement("button");
        let tx1 = document.createTextNode(menu_name);
        let tx2 = document.createTextNode(menu_price);
        let tx3 = document.createTextNode("-");
        let tx4 = document.createTextNode("+");
        let tx5 = document.createTextNode("1");

        order_box.className = "order_box";
        order_number.className = "order_number";
        order_text1.className = "order_text1";
        order_text2.className = "order_text2";
        order_text_div.className = "order_text22";
        order_text_div.id = order_id;
        order_text_btn1.id = obj.id + "-down";
        order_text_btn2.id = obj.id + "-up";
        order_text_btn1.setAttribute("onclick","order_down(this);");
        order_text_btn2.setAttribute("onclick","order_up(this);");
        order_box.id = obj.id + "-box";
        order_text1.id = obj.id + "-price";
        
        order_box1.appendChild(tx1);
        order_text1_a.appendChild(tx2);
        order_text1.appendChild(order_text1_a);
        order_text_btn1.appendChild(tx3);
        order_text_btn2.appendChild(tx4);
        order_text_div.appendChild(tx5);
        order_text2.appendChild(order_text_btn1);
        order_text2.appendChild(order_text_div);
        order_text2.appendChild(order_text_btn2);
        order_number.appendChild(order_text1);
        order_number.appendChild(order_text2);
        order_box.appendChild(order_box1);
        order_box.appendChild(order_number);
        order_out.appendChild(order_box);

        document.getElementById(obj.id + "-req").style.display="block";

        let order_all = document.getElementById("order_all").innerText;
        order_all = parseInt(order_all);
        let one_menu_price = menu_price.split(" ");
        one_menu_price = parseInt(one_menu_price[1]);
        order_all = order_all + one_menu_price;
        document.getElementById("order_all").innerHTML = order_all;
    }

}

function order_up(obj){
    obj = obj.id;
    obj = obj.split("up");
    obj = obj[0];

    orderfeq = document.getElementById(obj + "order").innerText;
    orderfeq = parseInt(orderfeq);
    orderfeq = orderfeq + 1 ;
    document.getElementById(obj + "order").innerHTML = orderfeq;

    let order_all = document.getElementById("order_all").innerText;
    order_all = parseInt(order_all);
    menu_price = document.getElementById(obj + "price").innerText;
    let one_menu_price = menu_price.split(" ");
    one_menu_price = parseInt(one_menu_price[1]);
    order_all = order_all + one_menu_price;
    document.getElementById("order_all").innerHTML = order_all;

    if(document.getElementById(obj + "req")){
        reqfeq = document.getElementById(obj + "req").innerText;
        reqfeq = parseInt(reqfeq);
        reqfeq = reqfeq + 1 ;
        document.getElementById(obj + "req").innerHTML = reqfeq;
    }
    
}

function order_down(obj){
    obj = obj.id;
    obj = obj.split("down");
    obj = obj[0];

    orderfeq = document.getElementById(obj + "order").innerText;
    orderfeq = parseInt(orderfeq);
    orderfeq = orderfeq - 1 ;

    let order_all = document.getElementById("order_all").innerText;
    order_all = parseInt(order_all);
    menu_price = document.getElementById(obj + "price").innerText;
    let one_menu_price = menu_price.split(" ");
    one_menu_price = parseInt(one_menu_price[1]);
    order_all = order_all - one_menu_price;
    document.getElementById("order_all").innerHTML = order_all;

    if(orderfeq == 0){
        let box = document.getElementById(obj + "box");
        box.parentNode.removeChild(box);
        if(document.getElementById(obj + "req")){
            document.getElementById(obj + "req").style.display="none";
        }
    }else{
        document.getElementById(obj + "order").innerHTML = orderfeq;

        if(document.getElementById(obj + "req")){
            reqfeq = document.getElementById(obj + "req").innerText;
            reqfeq = parseInt(reqfeq);
            reqfeq = reqfeq - 1 ;
            document.getElementById(obj + "req").innerHTML = reqfeq;            
        }

    }
}

function post(){
    orderout = document.getElementById("order_out").innerText;
    orderout = orderout.split("+\n");
    let allpostdata = {};
    let alllist = [];
    for( let i = 0 ; i < orderout.length ; i++ ){
        let post_box = orderout[i].split("\n");
        let post_name = post_box[0].replace('"'," ");
        post_name = post_name.toString();
        let post_price = post_box[1].replace("$ ","");
        post_price = post_price.replace('"',"");
        post_price = post_price.toString();
        let post_feq = post_box[2].replace("-","");
        post_feq = post_feq.replace('+',"");
        post_feq = post_feq.replace('"',"");
        post_feq = post_feq.toString();

        postdata = {"name":post_name,"price":post_price,"feq":post_feq};
        alllist.push(postdata);
    }
    allpostdata["order"] = alllist;

    let table = document.getElementById("table").innerText;
    allpostdata["table"] = table;

    let allprice = document.getElementById("order_all").innerText;
    allpostdata["subtotal"] = allprice;

    // console.log(allpostdata);

    let postAPI = "http://127.0.0.1:3000/menus"
    fetch(postAPI,{
        method:'POST',
        body:JSON.stringify(allpostdata),
    })
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        
        // console.log(res);
        location.reload();

    })
}

function gettable(){
    tableAPI = "http://127.0.0.1:3000/table"
    fetch(tableAPI)
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        if("ok" in res){
            // console.log(res["ok"][0]["code"]);
            console.log(res["ok"][0]["time"]);
            let tableImf = document.getElementById("table");
            let tablecode = document.createTextNode(res["ok"][0]["code"]);
            tableImf.removeChild(tableImf.firstChild)
            tableImf.appendChild(tablecode)
            
        }
        if("error" in res){
            console.log(res["message"]);
        }
    })
}
