
function engage_action () {
    $.get(engage_url, function(data) {
        if (data) {
            window.location.href = iframe_url;
        }
    });
}

function forward_action () {
    $('#forward_dialog').reveal();
}

function reject_action () {
    $('#reject_dialog').reveal();
}

function size_iframe () {
    var window_height = $(window).height();
    var controls_height = $(".container").height();
    var iframe_height = window_height - controls_height - 4;
    $("iframe").height(iframe_height);
}

function setup_button(selector, icon, action) {
    $(selector)
      .button({icons:{secondary:icon},})
      .click(action);
}

function close_forward_dialog() {
  $('#forward_dialog').trigger('reveal:close');
}

function close_reject_dialog() {
  $('#reject_dialog').trigger('reveal:close');
}

function close_explain_dialog() {
  $('#explain_dialog').trigger('reveal:close');
}


