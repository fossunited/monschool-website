
livecode.setOptions("python", {
    "runtime": "mypy",
    "buttons": [{
        "id": "validate",
        "label": "Validate",
        "args": {
            "mode": "mypy"
        }
    }],
    events: {
        created: function(editor) {
            if ($(editor.element).hasClass("mypy-strict")) {
                editor.options.env['MYPY_STRICT'] = "true";
                editor.setLabel("mypy --strict")
            }
            else {
                editor.setLabel("mypy")
            }

            if (editor.options.stdin) {
                editor.options.env['FALCON_STDIN'] = editor.options.stdin;
            }
        }
    }
});

