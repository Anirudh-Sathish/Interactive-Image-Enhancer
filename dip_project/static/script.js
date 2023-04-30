"use strict";
console.log("Hey");
const fileInput = document.getElementById("inputImg");
const previewImage = document.getElementById("preview-image");

fileInput.addEventListener("change", (e) => {
  const file = e.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
      previewImage.setAttribute("src", reader.result);
    });
    reader.readAsDataURL(file);
  } else {
    previewImage.setAttribute("src", "#");
  }
});

// var inputs = document.querySelectorAll(".custom-file-input");
// Array.prototype.forEach.call(inputs, function (input) {
//   var label = input.nextElementSibling;
//   var labelVal = label.innerHTML;

//   input.addEventListener("change", function (e) {
//     var fileName = "";
//     if (this.files && this.files.length > 1)
//       fileName = (this.getAttribute("data-multiple-caption") || "").replace(
//         "{count}",
//         this.files.length
//       );
//     else fileName = e.target.value.split("'").pop();

//     if (fileName) label.querySelector("span").innerHTML = fileName;
//     else label.innerHTML = labelVal;
//   });
// });
