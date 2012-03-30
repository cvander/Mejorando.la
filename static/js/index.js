jQuery(function ($) {
	// tomar la hora del atributo 
	var hora = $('#proximo').attr('data-time');

	if(hora) {
		// elementos que cambiaran
		var $dias = $('#nextday'),
			$horas = $('#nexthour'),
			$minutos = $('#nextmin');

		// cada minuto
		+function () {
			var time = Date.today().next().thursday().at(hora).getElapsed() * -1;

			if(Date.today().is().thursday() && Date.compare(new Date(), Date.today().at(hora)) == -1) {
				time = Date.today().at(hora).getElapsed() * -1;
			}

			var days = Math.floor(time/1000/60/60/24);
			time -= days*1000*60*60*24;

			var hours = Math.floor(time/1000/60/60);
			time -= hours*1000*60*60;

			var mins = Math.floor(time/1000/60);

			$dias.text(days);
			$horas.text(hours);
			$minutos.text(mins);

			setTimeout(arguments.callee, 6000);
		}();
	}
});