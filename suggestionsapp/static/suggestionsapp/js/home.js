$(document).ready(function() {
	var count = 0;
	$('.increment.up').click(function (event) {
		count++;
		$('.count').html(count);
	});
});