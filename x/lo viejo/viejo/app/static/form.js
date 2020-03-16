$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#b').val(),
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if ((data.name) == 'x' {
				$('#errorAlert').text('Hata').show();
				$('#successAlert').hide();
			}
			if ((data.name) !='x' {
				$('#successAlert').text('Hata').show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});
