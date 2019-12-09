$(function() {
    $(".corrector").on({
        click: function() {           
            var fallingInput = $(".falling_input").val();
            var landingInput = $(".landing_input").val();
            $.ajax({             // This ajax request send the falling and landing correction to python
                type: "POST",
                url: "url",        //TBD
                data: JSON.stringify({falling: fallingInput, landing: landingInput}),
                dataType: "json",
                success: function (response) {
                    console.log(success);
                    $(".falling_input").val("");
                    $(".landing_input").val("");
                },
                error: function (error) {
                    console.log(error);
                }
            });
        }
    });

    $(".submit").on({
        click: function() {
            var fileName = $(".file_input").val().replace("C:\\fakepath\\", "");

            $.ajax({                // This ajax request send the name of original data file to python
                type: "POST",
                url: "url",   // 
                data: JSON.stringify({path: fileName}),
                dataType: "json",
                success: function (response) {
                    console.log(success);
                },
                error: function (error) {
                    console.log(error);
                }
            });
        }
    });

    $(".performance").on({
        click: function() {
            $.ajax({
                type: "GET",
                url: "url",   // TBD
                dataType: "json",
                success: function (data) {
                    // TODO: GET the output of AI and post them on the table
                    console.log(JSON.parse(data));
                },
                error: function (error) {
                    console.log(error);
                }
            });

            $("#waveform").attr("src", "accel_y.png");   
            // "accel_y.png" can be any value. Might need to use ajax to retrieve the file name from python
        }
    });

    
})