$(document).ready(function () {
    var addShoppings = document.getElementsByClassName("addShopping");
    var subShoppings = document.getElementsByClassName("subShopping");

    for (var i = 0; i < subShoppings.length; i++) {
        addShoppings[i].addEventListener("click", function () {
            sid = this.getAttribute("ga");
            $.post("/changcart/0/", {"productid": this.getAttribute("ga")}, function (data) {
                if (data.status == "success") {
                    document.getElementById(sid).innerHTML = data.data;
                }
            })
        }, false);

        subShoppings[i].addEventListener("click", function () {
            sid = this.getAttribute("ga");
            $.post("/changcart/1/", {"productid": this.getAttribute("ga")}, function (data) {
                if (data.status == "success") {
                    if (data.data == '0') {
                        window.location.reload()
                    }
                    document.getElementById(sid).innerHTML = data.data;
                }
            })
        }, false)
    }


    var ischoses = document.getElementsByClassName("ischose");
    for (var j = 0; j < ischoses.length; j++) {
        ischoses[j].addEventListener("click", function () {
            ssid = this.getAttribute("goodsid") + "a";
            $.post("/changcart/2/", {"productid": this.getAttribute("goodsid")}, function (data) {
                if (data.status == "success") {
                    document.getElementById(ssid).innerHTML = data.data;
                }
            })
        }, false)
    }


    var ok = document.getElementById("ok");
    ok.addEventListener("click", function () {
        var d = confirm("是否下单？");
        if (!d) {
            return
        }

        $.get("/saveorder/", function (data) {
            if (data.status == "error") {
                console.log("订单失败");
            } else {
                console.log("订单成功");
                window.location.reload()
            }
        })
    })

});