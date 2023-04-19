// var copyButton = document.querySelector("#copy-button");

// copyButton.addEventListener("click", function() {
//     var text = copyButton.getAttribute("data-clipboard-text");
//     navigator.clipboard.writeText(text).then(function() {
//         console.log("Copied text to clipboard:", text);
//     }, function(error) {
//         console.error("Failed to copy text to clipboard:", error);
//     });
// });


// 
// Second method to write clipboard api 
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        console.log("Copied text to clipboard:", text);
    }, function(error) {
        console.error("Failed to copy text to clipboard:", error);
    });
}

var inputField = document.querySelector("#input-field");
var copyButton = document.querySelector("#copy-button");

copyButton.addEventListener("click", function() {
    var text = inputField.value;
    copyToClipboard(text);
});