$(document).ready(function()  {
  $("form").submit(function() {
        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: $(this).serialize(),
            success: function(t) {
                if(t.success) {
                  window.location.href = "/";
                } else {
                  Materialize.toast(t.message, 150 * t.message.length);
                }
            }
        });
        return false;
    })
});
