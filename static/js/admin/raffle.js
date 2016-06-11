$(document).ready(function()  {
  $("form").submit(function() {
        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: $(this).serialize(),
            success: function(t) {
                $('#response').text(t.message);
            }
        });
        return false;
    })
});
