$.get("https://swapi-api.alx-tools.com/api/films/?format=json",
	function (data, textStatus, jqXHR) {
	  $('UL#list_movies').html(jqXHR);
	  alert(jqXHR);
	});

