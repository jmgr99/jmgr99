$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				object : $('#nameInput').val(),
				objectb : $('#b').val(),
				dict: $('#dict').val(),


			},
			type : 'POST',
			url : '/process'
		})

		.done(function(data) {


			if ((data.object) == 'hata') {
				$('#errorAlert').text(data.object).show();
				$('#successAlert').hide();
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
