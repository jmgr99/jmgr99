$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				r1 : $('#r1').val(),
			//	r2 : $('#r2').val(),
			//	r3 : $('#r3').val(),
			//	r4 : $('#r4').val(),
			//	r5 : $('#r5').val(),
			//	r6 : $('#r6').val(),
			//	r7 : $('#r7').val(),
			//	r8 : $('#r8').val(),
			//	r9 : $('#r9').val(),
			//	r10 : $('#r10').val(),
			//	r11 : $('#r11').val(),
			//	r12 : $('#r12').val(),
			//	r13 : $('#r13').val(),
				a1 : $('#a1').html(),
				//a2 : $('#a2').html(),
				//a3 : $('#a3').html(),
				//a4 : $('#a4').html(),
				//a5 : $('#a5').html(),
				//a6 : $('#a6').html(),
				//a7 : $('#a7').html(),
				//a8 : $('#a8').html(),
				//a9 : $('#a9').html(),
				//a10 : $('#a10').html(),
				//a11 : $('#a11').html(),
				//a12 : $('#a12').html(),
				//a13 : $('#a13').html(),

			},
			type : 'POST',
			url : '/process'
		})}
		.done(function(data) {


			if ((data.r1) == 'sahih') {
				$('#successAlert1').text(data.r1).show();
				$('#errorAlert1').hide();
			}
			if ((data.r1) == 'hata') {
				$('#successAlert1').hide();
				$('#errorAlert1').text(data.r1).show();

			}		});

		//}}if ((data.r2) == 'sahih') {
		//}}	$('#successAlert2').text(data.r2).show();
		//}}	$('#errorAlert2').hide();
		//}}}
		//}}if ((data.r2) == 'hata') {
		//}}	$('#successAlert2').hide();
		//}}	$('#errorAlert2').text(data.r2).show();

		//}}}
		//}}if ((data.r3) == 'sahih') {
		//}}	$('#successAlert3').text(data.r3).show();
		//}}	$('#errorAlert3').hide();
		//}}}
		//}}if ((data.r3) == 'hata') {
		//}}	$('#successAlert3').hide();
		//}}	$('#errorAlert3').text(data.r3).show();

		//}}}
		//}}if ((data.r4) == 'sahih') {
		//}}  $('#successAlert4').text(data.r4).show();
		//}}  $('#errorAlert4').hide();
		//}}}
		//}}if ((data.r4) == 'hata') {
		//}}  $('#successAlert4').hide();
		//}}  $('#errorAlert4').text(data.r4).show();

		//}}}
		//}}if ((data.r5) == 'sahih') {
		//}}  $('#successAlert5').text(data.r5).show();
		//}}  $('#errorAlert5').hide();
		//}}}
		//}}if ((data.r5) == 'hata') {
		//}}  $('#successAlert5').hide();
		//}}  $('#errorAlert5').text(data.r5).show();

		//}}}
		//}}if ((data.r6) == 'sahih') {
		//}}  $('#successAlert6').text(data.r6).show();
		//}}  $('#errorAlert6').hide();
		//}}}
		//}}if ((data.r6) == 'hata') {
		//}}  $('#successAlert6').hide();
		//}}  $('#errorAlert6').text(data.r6).show();

		//}}}
		//}}if ((data.r7) == 'sahih') {
		//}}  $('#successAlert7').text(data.r7).show();
		//}}  $('#errorAlert7').hide();
		//}}}
		//}}if ((data.r7) == 'hata') {
		//}}  $('#successAlert7').hide();
		//}}  $('#errorAlert7').text(data.r7).show();

		//}}}
		//}}if ((data.r8) == 'sahih') {
		//}}  $('#successAlert8').text(data.r8).show();
		//}}  $('#errorAlert8').hide();
		//}}}
		//}}if ((data.r8) == 'hata') {
		//}}  $('#successAlert8').hide();
		//}}  $('#errorAlert8').text(data.r8).show();

		//}}}
		//}}if ((data.r9) == 'sahih') {
		//}}  $('#successAlert9').text(data.r9).show();
		//}}  $('#errorAlert9').hide();
		//}}}
		//}}if ((data.r9) == 'hata') {
		//}}  $('#successAlert9').hide();
		//}}  $('#errorAlert9').text(data.r9).show();

		//}}}
		//}}if ((data.r10) == 'sahih') {
		//}}  $('#successAlert10').text(data.r10).show();
		//}}  $('#errorAlert10').hide();
		//}}}
		//}}if ((data.r10) == 'hata') {
		//}}  $('#successAlert10').hide();
		//}}  $('#errorAlert10').text(data.r10).show();
		//}}}

		//}}if ((data.r11) == 'sahih') {
		//}}	$('#successAlert11').text(data.r11).show();
		//}}	$('#errorAlert11').hide();
		//}}	}
		//}}if ((data.r11) == 'hata') {
		//}}	 $('#successAlert11').hide();
		//}}	 $('#errorAlert11').text(data.r11).show();
		//}} }

		//}}if ((data.r12) == 'sahih') {
		//}}   $('#successAlert12').text(data.r12).show();
		//}}   $('#errorAlert12').hide();
		//}}   }
		//}}if ((data.r12) == 'hata') {
		//}}   $('#successAlert12').hide();
		//}}   $('#errorAlert12').text(data.r12).show();
		//}} }

		//}}if ((data.r13) == 'sahih') {
		//}}	  $('#successAlert13').text(data.r13).show();
		//}}	  $('#errorAlert13').hide();
		//}}	 }
		//}}if ((data.r13) == 'hata') {
		//}}	  $('#successAlert13').hide();
		//}}	  $('#errorAlert13').text(data.r13).show();
		//}}	}

	//	});
		event.preventDefault();


function myFunction() {
	var aa1 = document.getElementById("aa1");
	if (aa1.style.display === "none") {
	  aa1.style.display = "block";
	} else {
	  aa1.style.display = "none";
	}
//	var aa2 = document.getElementById("aa2");
//	if (aa2.style.display === "none") {
//	  aa2.style.display = "block";
//	} else {
//	  aa2.style.display = "none";
//	}
//	var aa3 = document.getElementById("aa3");
//	if (aa3.style.display === "none") {
//		aa3.style.display = "block";
//	} else {
//		aa3.style.display = "none";
//	}
//	var aa4 = document.getElementById("aa4");
//	if (aa4.style.display === "none") {
//	  aa4.style.display = "block";
//	} else {
//	  aa4.style.display = "none";
//	}
//	var aa5 = document.getElementById("aa5");
//	if (aa5.style.display === "none") {
//	  aa5.style.display = "block";
//	} else {
//	  aa5.style.display = "none";
//	}
//	var aa6 = document.getElementById("aa6");
//	if (aa6.style.display === "none") {
//	  aa6.style.display = "block";
//	} else {
//	  aa6.style.display = "none";
//	}
//	var aa7 = document.getElementById("aa7");
//	if (aa7.style.display === "none") {
//	  aa7.style.display = "block";
//	} else {
//	  aa7.style.display = "none";
//	}
//
//	var aa8 = document.getElementById("aa8");
//	if (aa8.style.display === "none") {
//	  aa8.style.display = "block";
//	} else {
//	  aa8.style.display = "none";
//	}
//	var aa9 = document.getElementById("aa9");
//	if (aa9.style.display === "none") {
//	  aa9.style.display = "block";
//	} else {
//	  aa9.style.display = "none";
//	}
//	var aa10 = document.getElementById("aa10");
//	if (aa10.style.display === "none") {
//	  aa10.style.display = "block";
//	} else {
//	  aa10.style.display = "none";
//	}
//	var aa11 = document.getElementById("aa11");
//	if (aa11.style.display === "none") {
//	  aa11.style.display = "block";
//	} else {
//	  aa11.style.display = "none";
//	}
//
//	var aa12 = document.getElementById("aa12");
//	if (aa12.style.display === "none") {
//	  aa12.style.display = "block";
//	} else {
//	  aa12.style.display = "none";
//	}
//
//	var aa13 = document.getElementById("aa13");
//	if (aa13.style.display === "none") {
//	  aa13.style.display = "block";
//	} else {
//	  aa13.style.display = "none";
//	}
	}
