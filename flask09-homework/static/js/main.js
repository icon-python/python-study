$(function () {
    $('#dl').click(function () {
        var user = $('#username').val();
        var pwd = $('#password').val();
        // $.ajax({
        //     // type:"post"
        //     method: "POST",
        //     url: '/login',
        //     data: {"user": user, "pwd": pwd},
        //     dataType: "json",
        //     success:function (data) {
        //         if(data.code === '1'){
        //             alert(data.msg);
        //         }
        //         else {
        //             $('#dl').next().append('<h1>'+data.msg+'</h1>');
        //             alert(data.msg);
        //         }
        //     }.error(alert('请求失败'))
        // })
        $.ajax({
            method: "POST",
            url: '/login',
            data: {"user": user, "pwd": pwd},
            dataType: "json",
        }).done(function (data) {
            if(data.code === '1'){
                    alert(data.msg);
                }else {
                    $('#dl').next().append('<h1>'+data.msg+'</h1>');
                    alert(data.msg);
                }
        }).fail(function () {
            alert('请求失败')
        });
    });
    var pro = $("#pro");
    $.ajax({
        url: '/pro_list',
        method: 'get',
        dataType: 'json'
    }).done(function (data) {
        var res = data.data;
        // console.log(res)
        for (i in res) {
            var option = '<option value=' + res[i].id + '>' + res[i].title + '</option>';
            pro.append(option);
        }
    });
    pro.change(function () {
        var pro_id = pro.val();
        console.log(pro_id);
        $.ajax({
            method: 'POST',
            url: '/interface',
            data: {'pro_id': pro_id},
            dataType: 'json'
        }).done(function (data) {
            var inter = $('#interface');
            if (data.code === '1') {
                var res2 = data.data;
                inter.empty();
                for (var i=0;i<res2.length;i++) {
                    var op2 = '<option value="">' + res2[i].name + '</option>';
                    inter.append(op2);
                }
            }
        })
    })
});