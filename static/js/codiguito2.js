

$(document).ready(function() {

	var alto = window.innerHeight;
	/*$('.cuerpo').css('min-height',alto)*/
	$('#col2 .chat iframe').css('height',alto-alto*0.25)
	var alto1 = screen.height;
	var x = true
	document.onkeydown = function(){ 
	if(window.event.keyCode == 122 ){
		if (x == true)
		{
			$('#col2 .chat iframe').css('height',alto1-alto1*0.25)
			x = false;
		}
		else{
			$('#col2 .chat iframe').css('height',alto-alto*0.25)
			x = true;
		}
	}
}
});

