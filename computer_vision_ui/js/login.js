$(document).ready(function () {
  $("#login-form").submit(function (event) {
    event.preventDefault(); // Prevent default form submission

    // Call the function to submit the login form
    submitLoginForm();
  });
});

function submitLoginForm() {
  // Capture user input
  $("#spinner").removeClass("visually-hidden");
  const username = $("#username").val();
  const password = $("#password").val();

  // Create an object with login data
  const loginData = {
    username: username,
    password: password,
  };

  // Make a POST request to the Django backend
  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:8000/intel/login/", // Replace with your actual backend URL
    contentType: "application/json",
    data: JSON.stringify(loginData),
    success: function (response) {
      $("#success").removeClass("visually-hidden");
      localStorage.setItem("isLoggedIn", true);
      console.log("Login successful:", response);
      // Redirect the user or perform other actions based on the response
      setTimeout(function () {
        window.location.href = "../pages/dashboard.html";
      }, 2000);
    },
    error: function (xhr, status, error) {
      $("#fail").removeClass("visually-hidden");
      console.error("Error:", error);
    },
    complete: function () {
      $("#spinner").addClass("visually-hidden");
      setTimeout(function () {
        $("#success").addClass("visually-hidden");
        $("#fail").addClass("visually-hidden");
      }, 1500);
    },
  });
}
