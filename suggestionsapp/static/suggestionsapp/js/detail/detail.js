$(document).ready(function() {
    // These unbinds are here to avoid a stupid bug in django-pipeline
    // that produces two copies of every js file
    $('#add-comment-button').unbind('click')
    $('#add-comment-button').click(function(event) {
        $(this).hide();
        $('#add-comment-panel').show();
    });

    $('#add-comment-form').unbind('submit');
    $('#add-comment-form').submit(function(event) {
        event.preventDefault();
        $(this).parent().hide();
        $('#add-comment-button').show();
        say($('#add-comment-form').serialize());
    });

    var model = {
        init: function () {
            this.data = ctx.CHATROOM_MESSAGES;
            if (Modernizr.localstorage) {
                localStorage.setItem('messages', JSON.stringify(this.data));
                delete this.data
            }
        },
        get: function () {
            console.log(localStorage.getItem('messages'));
            return this.data ? this.data : 
                JSON.parse(localStorage.getItem('messages'));
        },
        add: function(message) {
            function addLs(message) {
                var ls = JSON.parse(localStorage.getItem('messages'));
                ls.unshift(message);
                localStorage.setItem('messages', JSON.stringify(ls));
            }
            this.data ? 
                this.data.unshift(message) : // Notice the colon here
                addLs(message);
        },
    };
    var view = {
        init: function () {
            view.render(); 
        },
        render: function () {
            var messages = controller.get();
            $('#comment-list').html(''); // Erase the contents of the comment list
            var $msgTemplate = $('#comment-panel-template');
            messages.forEach(function(message) {
                var $toAppend = $msgTemplate.clone();
                var $toAppendContents = $($toAppend.html());
                $toAppendContents.find('.comment-text').text(message);
                // Then, append it!
                $('#comment-list').append($toAppendContents);
            });
        },
    };
    var controller = {
        init: function() {
            model.init();
            view.init();

        },
        get: function() {
            return model.get();
        },
        add: function (message) {
            model.add(message);
            view.render();
        }
    };
    controller.init();

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chat_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat/" + ctx.CHATROOM_LABEL);

    chat_socket.onmessage = function (message) {
        // This message will be the new comment, in JSON format
        // For now, it will just be the text
        controller.add(message['data']);
    }

    function say(message) {
        chat_socket.send(message);
    }
});
