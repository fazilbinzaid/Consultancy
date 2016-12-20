function add_inline_form(prefix) {
    var count = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val(), 10);
    var last_form = $('.' + prefix + ':last');

    var new_form = last_form.clone(false).html(last_form.html().replace(
          new RegExp(prefix + '-\\\\d-', 'g'), prefix + '-' + count + '-'));
    new_form.find('input[type="text"], textarea').each(function () {
        $(this).val('');
    });
    new_form.hide().insertAfter(last_form).slideDown(300);

    // Update the total form count
    $('#id_' + prefix + '-TOTAL_FORMS').val(count + 1);

    // re-initialise triggers

    return false;
}

var regex = /(?:inline\-form) ([\\w\-]*) (?:add|existing)/;
$('.add-inline').each(function () {
    var match = regex.exec($(this).closest('.body').find('.inline-form').attr('class'));
    if (match && match.length > 1) {
        $(this).click(function () {
            return add_inline_form(match[1]);
        });
    }
});



$(document).ready(function() {
    console.log('hellooo');
    $('#add-skill-button').click(function(ev) {
        console.log('world')
        ev.preventDefault();
        var count = $('#skills-form-container').children().length;
        var tmplMarkup = $('#skill-template').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $('div#skills-form-container').append(compiledTmpl);

        // update form count
        $('#id_skills-TOTAL_FORMS').attr('value', count+1);

        // some animate to scroll to view our new form
        $('html, body').animate({
                scrollTop: $("#add-skill-button").position().top-200
            }, 800);
    });
});
