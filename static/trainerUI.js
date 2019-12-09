// Created on Nov 27 2019 by Weiting Ji

$(function() {
    $(".corrector").on({
        click: function() {           
            var fallingInput = $(".falling_input").val();
            var landingInput = $(".landing_input").val();
            var fileName = $(".file_input").val().replace("C:\\fakepath\\", "");
			fileName = 'Data Folder/' + fileName

            $.ajax({             // This ajax request send the falling and landing correction to python
                type: "POST",
                url: "/retrain_AI",       
                data: {"falling": fallingInput, "landing": landingInput, "path": fileName},
                dataType: "json",
                success: function (response) {
                    if (response.retrain == 'success') {
						alert("Retrain success!");
						$(".falling_input").val("");
						$(".landing_input").val("");
					}
					else {
						alert("Retrain failure. Invalid labels")
					}
                },
                error: function (error) {
                    alert("error");
                }
            });
        }
    });


    $(".performance").on({
        click: function() {
            var fileName = $(".file_input").val().replace("C:\\fakepath\\", "");
			fileName = 'Data Folder/' + fileName
            $.ajax({                                // This ajax request send the name of original data file to python
                type: "POST",
                url: "/test_performance",   
                dataType: "json",
                data: {"path": fileName},
                success: function (response) {
                    // GET the output of AI and	 post them on the table
                    
                    $("#falling_score").empty().text(response.fallOutput);
                    $("#landing_score").empty().text(response.landOutput);
					
                    if (response.fallOutput.includes("left")) {
                        $("#falling_comments").empty().text("Your body was tilting too far left while falling. Make sure to be as straight as possible when falling.");
                        $("#landing_comments").empty().text("Work on improving your fall technique. A poor fall will inevitably lead to a poor landing.");
						$("#falling_AI_explanation").empty().text("Your output Z-axis gyroscope data dropped strongly in the negative direction.");
						$("#landing_AI_explanation").empty()
                    } 
                    else if (response.fallOutput.includes("right")) {
                        $("#falling_comments").empty().text("Your body was tilting too far right while falling. Make sure to be as straight as possible when falling.");
                        $("#landing_comments").empty().text("Work on improving your fall technique. A poor fall will inevitably lead to a poor landing.");
						$("#falling_AI_explanation").empty().text("Your output Z-axis gyroscope data peaked strongly in the positive direction.");
						$("#landing_AI_explanation").empty()
                    }
                    else if (response.fallOutput.includes("center")) {
                        if (response.landOutput.includes("bad")) {
                            $("#falling_comments").empty().text("Your fall was executed correctly, since you kept your body centered. Make sure to maintain this technique while working on improving your landing.");
                            $("#landing_comments").empty().text("Landing was too abrupt. Make sure to roll back after landing to extend the time of impact");
							$("#falling_AI_explanation").empty().text("Your output Z-axis gyroscope data was within an acceptable range.");
							$("#landing_AI_explanation").empty().text("Your output X-axis gyroscope data did not peak as it should have during a roll backwards. Also, your Y-axis accelerometer data peaked high before dropping low, indicating an abrupt landing");
                        }
                        else if (response.landOutput.includes("good")) {
                            $("#falling_comments").empty().text("Great job! Maintain a centered body position in all future falls to avoid injury.");
                            $("#landing_comments").empty().text("Good work! Make sure you maintain this smooth roll after landing, to reduce the impact on your knees and ankles.");
							$("#falling_AI_explanation").empty().text("Your output Z-axis gyroscope data was within an acceptable range.");
							$("#landing_AI_explanation").empty().text("Your output X-axis gyroscope peaked strongly, which is a good sign. Also, your Y-axis accelerometer data peaked high before dropping low, indicating a smooth landing");
                        }
                    }

                    $("#accel_y").attr("src", "static/accel_y.png?m=" + Math.random()); 
                    $("#gyro_x").attr("src", "static/gyro_x.png?m=" + Math.random()).hide();
                    $("#gyro_z").attr("src", "static/gyro_z.png?m=" + Math.random()).hide(); 
                },
                error: function (error) {
                    alert("error");
                }
            });

        }
    });

    $("#accel_y").on({
        click: function() {           
           $(this).hide();
           $("#gyro_x").show();
        }
    });

    $("#gyro_x").on({
        click: function() {           
           $(this).hide();
           $("#gyro_z").show();
        }
    });

    $("#gyro_z").on({
        click: function() {           
           $(this).hide();
           $("#accel_y").show();
        }
    });
 
})