function openNav() {
	document.getElementById("myNav").style.height = "100%";
	document.getElementById("myNav").style.display = "block";
	document.getElementById("myNav").style.zIndex = "10";
	document.body.style.overflow = "hidden";
	openBtn.addEventListener("click", showBlock);
}

function closeNav() {
	document.getElementById("myNav").style.height = "0%";
	document.getElementById("myNav").style.display = "none";
	document.getElementById("myNav").style.zIndex = "1";
	document.body.style.overflow = "inherit";
}