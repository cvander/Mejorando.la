jQuery(function ($) {
	$('#id_descripcion').wymeditor({ 
	    updateSelector: "input:submit",
	    updateEvent: "click",
	    skin: 'compact',
	    lang: 'es'
	  });
});