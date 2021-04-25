// Extra JavaScript code for the search template (search.html)

// Form validation: overall validation
$("form.needs-validation").validate({
  debug: true,
  errorClass: "is-invalid",
  errorElement: "div",
  errorPlacement: function(error, element) {
    error.appendTo("#errorBox")
  }
});

// Form validation: rules for each input element
$("input.needs-validation").rules("add", {
  pattern: "^[A-Za-z0-9\-\_]{3,20}$",
  messages: {
    pattern: "Should match ^[A-Za-z0-9\-\_]{3,20}$"
  }
});
