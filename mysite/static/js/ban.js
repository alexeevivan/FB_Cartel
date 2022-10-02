Splitting();

// Replay animation by hiding & showing the element again
let el = document.body;
el.addEventListener("click", function (e) {
	el.hidden = true;
	requestAnimationFrame(() => {
		el.hidden = false;
	});
});

/* Play / Pause on keypress */
var s = document.createElement("style");
s.innerHTML =
	" *, *:before, *:after { animation-play-state: paused !important; }";

document.addEventListener("keypress", function () {
	s.parentNode ? document.head.removeChild(s) : document.head.appendChild(s);
});