
$(document).ready( function() {

    console.log($("#id_part"));

    // inline 그룹을 hide..
    switch ($("#id_part option:selected").text()) {
        case "먹다":
            $("#eatdrinkpart-group").show();
            $("#seepart-group").hide();
            $("#sleeppart-group").hide();
            $("#buypart-group").hide();
            break;
        case "마시다":
            $("#eatdrinkpart-group").show();
            $("#seepart-group").hide();
            $("#sleeppart-group").hide();
            $("#buypart-group").hide();
            break;
        case "보다":
            $("#eatdrinkpart-group").hide();
            $("#seepart-group").show();
            $("#sleeppart-group").hide();
            $("#buypart-group").hide();
            break;
        case "자다":
            $("#eatdrinkpart-group").hide();
            $("#seepart-group").hide();
            $("#sleeppart-group").show();
            $("#buypart-group").hide();
            break;
        case "사다":
            $("#eatdrinkpart-group").hide();
            $("#seepart-group").hide();
            $("#sleeppart-group").hide();
            $("#buypart-group").show();
            break;
        default:
            $("#eatdrinkpart-group").hide();
            $("#seepart-group").hide();
            $("#sleeppart-group").hide();
            $("#buypart-group").hide();
            break;
    }
    

    // 콤보박스의 변화가 생기면 선택된 텍스트를 판별하여 이벤트 발생..
    $( "#id_part" ).change(function() {
        switch ($("#id_part option:selected").text()) {
            case "먹다":
                $("#eatdrinkpart-group").show();
                $("#seepart-group").hide();
                $("#sleeppart-group").hide();
                $("#buypart-group").hide();
                break;
            case "마시다":
                $("#eatdrinkpart-group").show();
                $("#seepart-group").hide();
                $("#sleeppart-group").hide();
                $("#buypart-group").hide();
                break;
            case "보다":
                $("#eatdrinkpart-group").hide();
                $("#seepart-group").show();
                $("#sleeppart-group").hide();
                $("#buypart-group").hide();
                break;
            case "자다":
                $("#eatdrinkpart-group").hide();
                $("#seepart-group").hide();
                $("#sleeppart-group").show();
                $("#buypart-group").hide();
                break;
            case "사다":
                $("#eatdrinkpart-group").hide();
                $("#seepart-group").hide();
                $("#sleeppart-group").hide();
                $("#buypart-group").show();
                break;
            default:
                $("#eatdrinkpart-group").hide();
                $("#seepart-group").hide();
                $("#sleeppart-group").hide();
                $("#buypart-group").hide();
                break;
        }
        // if ($("#id_part option:selected").text() == "먹다/마시다"){
        //     $("#eatdrinkpart-group").show();
        // }else {
        //     $("#eatdrinkpart-group").hide();
        // }
        // alert($("#id_part option:selected").text());
        // console.log($("#id_part option:selected").val());
    });

    // $("input").click( function(event) {
    //     alert("You clicked the button using JQuery!");
    // });

//     $(document).ready(function(){
//         $.ajax({
//             type : "GET",
//             url : 'http://127.0.0.1:8000/en/cs-name-autocomplete/',
//             dataType : 'json',
//             error : function(){
//                 alert('통신실패!!');
//             },
//             success : function(data){
// //                 alert("통신데이터 값 : " + data) ;
// //                 $("#dataArea").html(data) ;
//                 console.log(data);
//                 console.log(data.results[0].text);
//             }
//         });
//      });

        
});
