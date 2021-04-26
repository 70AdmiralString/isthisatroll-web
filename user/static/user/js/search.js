// Extra JavaScript code for the search template (search.html)
// Depends on: jQuery 3.6.0, jQuery validation plugin 1.19.3

$(document).ready(
  function() {

    // Form validation: overall form validation settings
    $("form.needs-validation").validate({
      debug: true,
      errorClass: "is-invalid",
      errorElement: "div",
      errorPlacement: function(error, element) {
        error.appendTo("#errorBox")
      }
    });

    // Form validation: rules for each input element
    $("input.needs-validation").each(
      function() {
        $(this).rules("add", {
          pattern: $(this).attr('data-validation-regex'),
          messages: {
            pattern: $(this).attr('data-validation-message')
          }
        });
      }
    );

  }
)
