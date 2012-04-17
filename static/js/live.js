jQuery(function ($) {
	function enviando()
	{
		$("#formulario .tit").text("Inscribiendote...").fadeOut().fadeIn();
	}

	function recepcion(datos)
	{
		datos = $.trim(datos);
		if(datos=="OK")
		{
			$("#formulario .tit").text("¡Ya estás inscrito!").fadeOut().fadeIn();
		}
		else
		{
			$("#formulario .tit").text("Seguro ya estabas inscrito").fadeOut().fadeIn();
			$("#formulario  #confirmacion").text("Verifica que todos los datos estén bien escritos").slideDown();
			$("#formulario  #nombre").focus();
		}
	}

	var opciones = {
		beforeSubmit: enviando,
		success: recepcion,
		clearForm: true
	};
	
	$('#formulario').ajaxForm(opciones); 

	/*+function () {
		var alto = window.innerHeight;
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
	}()*/


	function getViewportSize()
	{
		var e = window, a = 'inner';
		if ( !( 'innerWidth' in window ) )
		{
			a = 'client';
			e = document.documentElement || document.body;
		}
		return { width : e[ a + 'Width' ] , height : e[ a + 'Height' ] }
	}

	function resize()
	{
		var viewport = getViewportSize();
		var $iframe = $('#col2 iframe');

		// resize chat
		if (viewport.width <= 768)
		{
			var height = viewport.height - $('#video').height();
			$iframe.css('height', height);
			$iframe.data('resized', true);
		}
		else {
			if ($iframe.data('resized'))
				$iframe.css('height', '');
		}

		// resize video
		// var $video = $('#video');
		// var height = $video.height();
		// var width = $video.width();
		// $video.find('object,embed').attr('height', height).attr('width', width);
	}

	resize();
	$(window).on('load debouncedresize', resize);
});