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


			if ((data.object) == 'sahih') {
				$('#successAlert').text(data.object).show();
				$('#errorAlert').hide();
			}
			if ((data.object) == 'hata') {
				$('#successAlert').hide();
				$('#errorAlert').text(data.object).show();

			}
			if ((data.objectb) == 'sahih') {
				$('#successAlertb').text(data.objectb).show();
				$('#errorAlertb').hide();
			}
			if ((data.objectb) == 'hata') {
				$('#successAlertb').hide();
				$('#errorAlertb').text(data.objectb).show();
			}

		});

		event.preventDefault();

	});

});
