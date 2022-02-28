
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
            if (editor.options.stdin) {
                editor.options.headers['X-FALCON-ENV'] = `FALCON_STDIN=${editor.options.stdin}`;
            }
        }
    }
});

