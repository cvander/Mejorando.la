jQuery(function ($) {
		// elementos que cambiaran
		var $dias = $('#nextday'),
			$horas = $('#nexthour'),
			$minutos = $('#nextmin'),
			nextEpisode = parseInt($('#proximo').attr('timestamp'));
			hora = $('#hora');

		// cada minuto
		+function updateCounter(){
		var elapsed = nextEpisode - new Date(); // puede ser Date.now() pero iexplorer8 no lo reconoce;
                d = new Date(nextEpisode);
		hora.text(d.toString("htt"));
		if(elapsed < 0) return; // detenemos el contador;
		var days = Math.floor(elapsed/1000/60/60/24),
		hours = Math.floor(elapsed/1000/60/60) % 24,
		minutes = Math.floor(elapsed/1000/60) % 60;
		$dias.text(days), $horas.text(hours), $minutos.text(minutes);
		setTimeout(arguments.callee, 6000); // callee esta obsoleto y deberia llamarse por el nombre;
											// en este caso updateCounter, pero iexplorer8 no reconoce;
											// este tipo de declaracion de funcion;
		}()
});
