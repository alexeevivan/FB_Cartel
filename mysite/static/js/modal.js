var modals = document.getElementsByClassName("modal");
var modal__openbtn = document.getElementsByClassName("modal__open-btn");
var currentModal = null;

// Function to open modal by id
function openModal(id) {
	for (i = 0; i < modals.length; i++) {
		if (modals[i].getAttribute('id') == id) {
			currentModal = modals[i];
			currentModal.style.display = "flex" || currentModal.style.position === "fixed";
			break;
		}
	}
}

// When the user clicks the button, open modal with the same id
modal__openbtn.onclick = function () {
	let currentID = modal__openbtn.getAttribute('id');
	openModal(currentID);
}

// When the user clicks anywhere outside of the modal or the X, close
window.onclick = function (event) {
	if (event.target == currentModal || event.target.getAttribute('class') == 'modal__close') {
		currentModal.style.display = "none";
	}
}