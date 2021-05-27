$(function() {
    $('[data-open-modal]').click(function() {
        var modal = $(this).attr('data-open-modal'),
            code = '<div class="modal" id="modal_'+modal+'"><h5>'+$('noscript[name="'+modal+'"]').data('title')+'</h5><div class="content">'+$('noscript[name="'+modal+'"]').html()+'</div><button data-close>Закрыть</button></div>';
        $('body').append(code);
        $('.modal [data-close]').click(function() {
            $(this).parents('.modal').remove();
        });
    });
});