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


	$(window).on('load', function(){
		$('#col2').html('<div class="chat"><iframe src="http://chat.mejorando.la" width="100%" height="75%" frameborder="0"></iframe></div>');
	});


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
	}

	resize();
	$(window).on('load debouncedresize', resize);
});