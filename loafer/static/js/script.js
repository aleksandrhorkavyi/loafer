const ENTER = 13;
const L_SHIFT = 16;
const L_ALT = 18;
const T = 84;
const O = 79;
const CTRL = 17;
const QUOTE = 222;

var map = {
    // QUOTE
    222: false,
    // L_ALT
    18: false,
    // T
    84: false,
    // O
    79: false,
    // ENTER
    13: false,
    // CTRL
    17: false,
};



function showInfo(e, key) {
    if(e.which == key) {
        $('.hotkeys-container').removeClass('closed').addClass('open')
    }
}

function closeInfo(e, key) {
    if(e.which == key) {
        $('.hotkeys-container').removeClass('open').addClass('closed')
    }
}

function flipListClasses(selector, rem, add) {
    $(selector).each(function() {
        $(this).removeClass(rem).addClass(add);
    });
}

function showItemList(e, itemClass) {
    if ($(itemClass).hasClass('closed')) {
        flipListClasses(itemClass, 'closed', 'open');
    } else {
        flipListClasses(itemClass, 'open', 'closed');
    }
}

function changeButtonStatus(selector, icon = 'fa-toggle-on') {
    let $btn = $(selector);
    let $icon = $btn.find('span');
    $btn.toggleClass('status-off');
    $icon.toggleClass(icon);
}

// Activate single hotkey
$(document).on('keydown',function(e) {
    showInfo(e, L_SHIFT);
});

// Off single hotkey
$(document).on('keyup',function(e) {
    closeInfo(e, L_SHIFT);
});

// For few keys
$(document).keydown(function(e) {
    if (e.keyCode in map) {
        map[e.keyCode] = true;
        if (map[L_ALT] && map[T]) {
            showItemList(e, '.translation-item');
            changeButtonStatus('#btn-translation');
        }
        if (map[L_ALT] && map[O]) {
            showItemList(e, '.orig-phrase-item');
            changeButtonStatus('#btn-orig_phrase');
        }
    }
}).keyup(function(e) {
    if (e.keyCode in map) {
        map[e.keyCode] = false;
    }
});


// Sort phrases
$(function() {
   $("#phrase-list").sortable({
        update: function( event, ui ) {
            let itemsOrder = {};
            let i = 1;
            $('#phrase-list > li').each(function(){
                itemsOrder[($(this).data('key'))] = i++;
            });
            updateItemsOrder(itemsOrder);
        }
   });
 });

function updateItemsOrder(itemsOrder) {

    let csrf_token = $('#phrase-form > div > input[type=hidden]').val();
    $.ajax({
        type: "POST",
        url: $('#phrase-list').data('url'),
        headers: {'X-CSRFToken': csrf_token},
        data: itemsOrder,
        success: function (response) {
            console.log(response);
        }
    });


}