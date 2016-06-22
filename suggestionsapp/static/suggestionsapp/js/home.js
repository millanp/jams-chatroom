$(document).ready(function() {
	$( ".increment.up").unbind( "click" );
	$('.increment.up').click(function (event) {
        upvote($(this));
	});
	$('.increment.down').click(function(event) {
		downvote($(this));
	});
	function upvote ($upvoteButton) {
		var $parent = $upvoteButton.parent().parent();
		var $counter = $parent.find('.count');
		$counter.html(parseInt($counter.html())+1);
		var $upvoteForm = $parent.find('.upvote-form');
		$.ajax({
            type: 'POST',
            data: $upvoteForm.serialize(), 
            success: function(response) {
                $('#upvote-success-message').slideDown('fast').delay(500).slideUp('slow');
            },
            error: function() {
                 //$("#commentList").append($("#name").val() + "<br/>" + $("#body").val());
                alert("There was an error submitting comment");
            }
     	});
	}
	function downvote ($upvoteButton) {
		var $parent = $upvoteButton.parent().parent();
		var $counter = $parent.find('.count');
		$counter.html(parseInt($counter.html())-1);
		var $downvoteForm = $parent.find('.downvote-form');
		$.ajax({
            type: 'POST',
            data: $downvoteForm.serialize(), 
            success: function(response) {
                $('#downvote-success-message').slideDown('fast').delay(500).slideUp('slow');
            },
            error: function() {
                 //$("#commentList").append($("#name").val() + "<br/>" + $("#body").val());
                alert("There was an error submitting comment");
            }
     	});
	}
});