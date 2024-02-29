$(document).ready(function () {
  // Logout button click event
  $("#logOut").click(function () {
    // Send AJAX POST request to logout endpoint
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8000/intel/logout/", // Update with your actual logout endpoint
      success: function (response) {
       
        localStorage.removeItem("isLoggedIn");
        console.log(response);
        // Example: Redirect to login page
        window.location.href = "/index.html";
      },
      error: function (xhr, status, error) {
        // If logout fails, log error message
        console.error("Error:", error);
      },
    });
  });
});
