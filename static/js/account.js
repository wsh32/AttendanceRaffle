$(document).ready(function()  {
  $("#logout").click(function() {
        $.ajax({
            type: "GET",
            url: "/api/logout",
            success: function(e) {
                if(e.success) {
                  window.location.href = "/";
                } else {
                  Materialize.toast(e.message, 150 * e.message.length);
                }
            }
        })
    })
});
