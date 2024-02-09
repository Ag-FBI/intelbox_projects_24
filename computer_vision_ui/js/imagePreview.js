// Optional: Display the image filename and update the image src
document
.getElementById("imageInput")
.addEventListener("change", function () {
  // Update the src attribute of the existing img element in the container
  var imageContainer = document.getElementById("imageContainer");
  var previewImage = document.getElementById("previewImage");
  var file = this.files[0];

  if (file) {
    var reader = new FileReader();
    reader.onload = function (e) {
      previewImage.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }
});