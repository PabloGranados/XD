function ParaCuandoDigaSi() {
	alert('Ahora somos nobios <3');
}

function MoverBoton() {
	width = window.innerWidth;
	height = window.innerHeight;

	newWidth = Math.random() * width;
	newHeight = Math.random() * height;

	document.getElementById('no').style.position = 'absolute';
	document.getElementById('no').style.left = newWidth + 'px';
	document.getElementById('no').style.top = newHeight + 'px';
}
