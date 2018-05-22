$(document).ready(function(){
    accunt = document.getElementById('accunt');
    pass = document.getElementById('pass');
    passwd = document.getElementById('passwd');

    accunterr = document.getElementById('accunterr');
    checkerr = document.getElementById('checkerr');
    passerr = document.getElementById('passerr');
    passwderr = document.getElementById('passwderr');

    accunt.addEventListener("focus",function(){
        accunterr.style.display = "none";
        checkerr.style.display = "none";
    },false);
    accunt.addEventListener("blur",function(){
        var inputStr = this.value;
        if (inputStr.length != 8) {
            accunterr.style.display = "block";
        }else{
            // 验证账号是否被注册
            $.ajax({
                url:"/checkuserid/",
                type:"post",
                typedata:"json",
                data:{"checkid":accunt.value},
                success:function(data){
                    if (data.status == "error"){
                        checkerr.style.display = "block";
                    }
                }
            })
        }
    },false);

    pass.addEventListener("focus",function(){
        passerr.style.display = "none";
    },false);
    pass.addEventListener("blur",function(){
        var inputStr = this.value;
        if (inputStr.length < 6 || inputStr.length > 16) {
            passerr.style.display = "block"
        }
    },false);


    passwd.addEventListener("focus",function(){
        passwderr.style.display = "none";
    },false);
    passwd.addEventListener("blur",function(){
        var inputStr = this.value;
        if (inputStr != pass.value) {
            passwderr.style.display = "block";
        }
    },false)

});