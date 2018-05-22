$(document).ready(function () {
    var loginBtn = document.getElementById("loginBtn");

    var ui = document.getElementById("ui");
    var pi = document.getElementById("pi");

    var errorp = document.getElementById("errorp");
    errorp.style.display = "none";

    loginBtn.addEventListener("click", function () {
        $.post("/checkuserlogin/", {"ua": ui.value, "up": pi.value}, function (data) {
            if (data.status == "error") {
                errorp.style.display = "block";
            } else {
                window.location.href = "http://127.0.0.1:8000/mine/";
            }
        })
    }, false)


});