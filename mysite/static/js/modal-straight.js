// Get the modal
var modal1 = document.getElementById("myModal-straight");

// Get the button that opens the modal
var btn1 = document.getElementById("openModalBtn-straight");

// Get the <span> element that closes the modal
var span1 = document.getElementsByClassName("closeModal-straight")[0];

// When the user clicks on the button, open the modal 
btn1.onclick = function() {
modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span1.onclick = function() {
modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}