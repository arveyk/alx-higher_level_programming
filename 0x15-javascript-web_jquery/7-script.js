$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json",
	function (data, textStatus, jqXHR) {
	  $('#character').text(data);
	});
