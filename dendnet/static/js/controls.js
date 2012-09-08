
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

function note_own_tag(tag) {
  $.cookie("own_tag", tag, {
    expires: 35,
    path: '/',
  })
}

function get_own_tag() {
  var tag = $.cookie("own_tag");
  if (_.isNull(tag)) {
    return '';
  }
  return tag;
}

function get_contacts() {
  var contacts_cookie = $.cookie("contacts");
  if (_.isNull(contacts_cookie)) {
    return {};
  }
  var contacts = JSON.parse(contacts_cookie);
  return contacts;
}

function set_contacts(contacts) {
  var contacts_json = JSON.stringify(contacts);
  $.cookie("contacts", contacts_json, {
    expires: 35,
    path: '/',
  });
}

function set_contact(label, tag) {
  var c = get_contacts();
  c[label] = tag;
  set_contacts(c);
}

function del_contact(label) {
  var c = get_contacts();
  delete c[label];
  set_contacts(c);
}

function add_new_contact() {
  var new_contact_label = $("#id_new_contact_label");
  var label = new_contact_label.val();
  if (label == "") {
    return false; // prevent normal form submit.
  }
  var new_contact_tag = $("#id_new_contact_tag");
  var tag = new_contact_tag.val();
  if (tag == "") {
    del_contact(label);
  } else {
    set_contact(label, tag);
  }
  new_contact_label.val("");
  new_contact_tag.val("");
  display_contacts();
  return false; // prevent normal form submit.
}

function display_contact(target, label, tag) {
  var d = $('<div class="contact_display"><a href="#">@<span></span></a></div>');
  d.find("span").text(label);
  d.find("a").click(function() {
    var burl = bump_url + tag;
    var duu = $("div#updatable_url");
    duu.find("span").text('@' + label + ' please check out');
    var taggy = duu.find("a");
    taggy.text(burl);
    taggy.attr("href", burl);
    console.log(burl);
    return false; // prevent navigation
  });
  d.appendTo(target);
}

function display_contacts() {
  var contacts = get_contacts();
  var target = $("#contacts");
  target.empty();
  _.each(contacts, function(tag, label) {
    display_contact(target, label, tag);
  })
}

function nonanon(base_url) {
  var own_tag = get_own_tag();
  if (own_tag != '') {
    var bump_url = base_url + own_tag
    window.location.href = bump_url;
    return true; // Dunno if this is needed.
  }
  return false;
}

function make_register_callback(reg_url, url_selector, tag_callback) {
  return function() {
    var urly = $(url_selector).val();
    if (urly != "") {
      $.post(reg_url, {'urly': urly}, tag_callback);
    }
    return false;
  }
}

