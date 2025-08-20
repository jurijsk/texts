


function onClick(event: PointerEvent) {
	const element = (event.target as HTMLElement);
	//element.style.border = "1px solid red";
	console.log('click y', event.clientY);
	console.log('elem bounding rect', element.getBoundingClientRect().top);
	console.log('current selection:', window.getSelection());
}


document.addEventListener("click", onClick);
