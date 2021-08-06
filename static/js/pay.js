let pay_table = ""
let pay_number = []

function getpay(){
    let tablecode = location.search.split("=")[1]
    pay_table = tablecode
    let tablecode_box = document.getElementById("table_box");
    let oldtxt = document.getElementById("table_tx1");
    let newtxt = document.createElement("a");
    let tablecode_txt = document.createTextNode(tablecode);
    newtxt.appendChild(tablecode_txt)
    newtxt.className = "table_tx1"
    newtxt.id = "table_tx1"
    tablecode_box.replaceChild(newtxt,oldtxt)

    payAPI=`http://127.0.0.1:3000/pays?tablecode=${tablecode}`
    fetch(payAPI)
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        if("error" in res){
            location.href='http://127.0.0.1:3000'
        }
        let allprice = 0
        for(i = 0 ; i < res["pick"].length ; i++){
            let contentnumber = res["pick"][i]["number"]
            pay_number.push(contentnumber);
            let contentprice = res["pick"][i]["allprice"]
            contentprice = parseInt(contentprice)
            allprice = allprice + contentprice
            contentone= res["pick"][i]["content"].replace(/,/g,"*")
            contentone = contentone.split(";")
            
            let contentall = ""
            for(j=0;j<contentone.length;j++){
                contentall = contentall + " , " + contentone[j]
            }
            contentall = contentall.substr(3)

            let pick_outbox = document.getElementById("in_tableimf")
            let pick_box = document.createElement("div")
            let picktable_box =document.createElement("div")
            let picktable_box_txt =document.createElement("a")
            let picktable_box_txt1 = document.createTextNode("單號 " + res["pick"][i]["number"])
            let pickimf_box =document.createElement("div")
            let pickimf =document.createElement("div")
            let imf_txt = document.createTextNode(contentall)
            pick_box.className = "pick"
            picktable_box.className = "pick_table"
            pickimf.className = "pick_imf"
            picktable_box_txt.appendChild(picktable_box_txt1)
            picktable_box.appendChild(picktable_box_txt)
            pickimf.appendChild(imf_txt)
            pickimf_box.appendChild(pickimf)
            pick_box.appendChild(picktable_box)
            pick_box.appendChild(pickimf_box)
            pick_outbox.appendChild(pick_box)
        }
        allprice = allprice.toString();

        let allprice_box = document.getElementById("allprice_box");
        let oldallprice = document.getElementById("allprice");
        let newallprice = document.createElement("a");
        let allprice_txt = document.createTextNode(allprice);
        newallprice.appendChild(allprice_txt)
        newallprice.id = "allprice"
        allprice_box.replaceChild(newallprice,oldallprice)
    })
}

function pay(){
    paydata = {}
    for(i = 0 ; i < pay_number.length ; i++){
        paydata[`${i}`] = pay_number[i]
    }
    paydata["table"] = pay_table

    let postAPI = "http://127.0.0.1:3000/pays"
    fetch(postAPI,{
        method:'POST',
        body:JSON.stringify(paydata),
    })
    .then(function(data) {
        return data.json();
    }).then(function(res) {
        if("ok" in res){
            console.log(res)
            location.href='http://127.0.0.1:3000/count'
        }
    })
}