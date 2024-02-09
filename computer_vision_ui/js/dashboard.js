$(document).ready(function () {
  $("#postDataForm").submit(function (event) {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    var name = $("#name").val();
    var age = $("#age").val();
    var alias = $("#alias").val();
    var image = $("#image")[0].files[0];
    var description = $("#description").val();
    var gender = $("#gender").val();

    // Data to be sent to the backend
    var formData = new FormData();
    formData.append("name", name);
    formData.append("age", age);
    formData.append("alias", alias);
    formData.append("image", image);
    formData.append("description", description);
    formData.append("gender", gender);
    formData.forEach(function (value, key) {
      console.log(key, value);
    });
    // Send AJAX POST request to the backend
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8000/intel/", // Replace with your actual backend URL
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // Handle success response from the backend
        console.log("Data sent successfully:", response);
        // Optionally, you can redirect the user or show a success message
      },
      error: function (xhr, status, error) {
        // Handle error response from the backend
        console.error("Error sending data:", error);
        // Optionally, you can show an error message to the user
      },
    });
  });
});
