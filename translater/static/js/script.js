$(document).ready(function() {

    var temp_image, first_save;

    var range_slider = $("#threshold").slider({});

    $('#image-submit').click(function (argument) {

        var formData = new FormData($('#image-upload')[0]);
        $.ajax({

            url : '/upload',
            dataType: 'json',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                console.log(response);
                if (response['error'] == 0) {
                    temp_image = response['url'];
                    $('#result').attr('src', temp_image);
                    formData.append('url', temp_image);
                };
            }

        });

    });

});