$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				object : $('#nameInput').val(),
				objectb : $('#b').val(),			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if ((data.object) == 'hata') {
				$('#errorAlertb').text(data.object).show();
				$('#successAlertb').hide();
			}
			if ((data.object) == 'sahih') {
				$('#successAlert').text(data.object).show();
				$('#errorAlert').hide();
			}
			if ((data.objectb) == 'hata') {
				$('#errorAlertb').text(data.objectb).show();
				$('#successAlertb').hide();
			}
			if ((data.objectb) == 'sahih') {
				$('#successAlertb').text(data.objectb).show();
				$('#errorAlertb').hide();
			}

		});

		event.preventDefault();

	});

});
