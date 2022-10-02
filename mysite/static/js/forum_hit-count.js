jQuery(document).ready(function ($) {
	// use the template tags in our JavaScript call
	$.postCSRF("{{ hitcount.ajax_url }}", { hitcountPK: "{{ hitcount.pk }}" })
		.done(function (data) {
			$('<i />').text(data.hit_counted).attr('id', 'hit-counted-value').appendTo('#hit-counted');
			$('#hit-response').text(data.hit_message);
		}).fail(function (data) {
			console.log('POST failed');
			console.log(data);
		});
});