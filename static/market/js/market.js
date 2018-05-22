$(document).ready(function (){

    var alltypebtn = document.getElementById("alltypebtn");
    var showsortbtn = document.getElementById("showsortbtn");

    var typediv = document.getElementById("typediv");
    var sortdiv = document.getElementById("sortdiv");

    typediv.style.display = "none";
    sortdiv.style.display = "none";

    alltypebtn.addEventListener("click", function () {
        typediv.style.display = "block";
        sortdiv.style.display = "none";
    }, false);

    showsortbtn.addEventListener("click", function () {
        typediv.style.display = "none";
        sortdiv.style.display = "block";
    }, false);

    typediv.addEventListener("click", function () {
        this.style.display = "none";
    }, false);
    sortdiv.addEventListener("click", function () {
        this.style.display = "none";
    }, false);


    var sortas = document.getElementsByClassName("sorta");
    for (var i = 0; i < sortas.length; i++) {
        var str = window.location.href;
        var str1 = str.split(":")[2];
        var arr2 = str1.split("/");
        hrefstr = "/" + arr2[1] + "/" + arr2[2] + "/" + arr2[3] + "/" + i + "/";
        sortas[i].href = hrefstr;
    }


    // 加入购物车
    var addShoppings = document.getElementsByClassName("addShopping");
    var subShoppings = document.getElementsByClassName("subShopping");

    for (var i = 0; i < subShoppings.length; i++) {

        addShoppings[i].addEventListener("click", function () {
            sid = this.getAttribute("ga");
            $.ajax({
                url: "/changcart/0/",
                type: "post",
                typedata:"json",
                data:{"productid": sid},
                success: function (data) {
                    if (data.status == "success") {
                        document.getElementById(sid).innerHTML = data.data;
                    } else {
                        if (data.data == '0') {
                            //说明没登录
                            window.location.href = "http://127.0.0.1:8000/login/";
                        }
                    }
                }
            })
        }, false);


        subShoppings[i].addEventListener("click", function () {
            sid = this.getAttribute("ga");
            $.post("/changcart/1/", {"productid": this.getAttribute("ga")}, function (data) {
                if (data.status == "success") {
                    document.getElementById(sid).innerHTML = data.data;
                } else {
                    if (data.data == '0') {
                        window.location.href = "http://127.0.0.1:8000/login/"
                    }
                }
            })
        }, false);

    }

});

