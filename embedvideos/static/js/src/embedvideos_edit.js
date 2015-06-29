function EmbedVideosEditXBlock(runtime, element) {
    /* Tabs functionality */
    $(function() {
        $("#tabs").tabs();
    });

    /* Selecting functionality on providers images */
    $('.providers-list li img').on('click', function() {
        $('.providers-list li img').removeClass('selected');
        $(this).addClass('selected');
    });

    $(element).find('.save-button').bind('click', function() {
        var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
        
        /* List of attributes that are inputs */
        var attrList = [
            'youtube_id',
            'youtube_width',
            'youtube_height',
            'vimeo_id',
            'vimeo_width',
            'vimeo_height',
            'vimeo_color'
        ]

        /* List of attributes that are selections */
        var attrListSelect = [
            'youtube_autohide',
            'youtube_color',
            'youtube_controls',
            'youtube_fs',
            'youtube_hl',
            'youtube_iv_load_policy',
            'youtube_loop',
            'youtube_modestbranding',
            'youtube_rel',
            'youtube_showinfo',
            'youtube_theme',
            'vimeo_autoplay',
            'vimeo_badge',
            'vimeo_byline',
            'vimeo_loop',
            'vimeo_portrait',
            'vimeo_title'
        ]

        var data = {}

        /* Save values from inputs to the data dict */
        attrList.forEach(function(item) {
            var value = $(element).find('input[name=' + item + ']').val();
            /* If the user leaves blank would cause errors in Django,
               this way they are left to the default values 
            */
            if (value != "None") {
                data[item] = value;
            }
        });

        /* Save values from selections to the data dict */
        attrListSelect.forEach(function(item) {
            var el = document.getElementById(item);
            var value = el.options[el.selectedIndex].value;
            data[item] = value;
        });

        runtime.notify('save', {
            state: 'start'
        });
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            runtime.notify('save', {
                state: 'end'
            });
        });
    });

    $(element).find('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
    });
}
