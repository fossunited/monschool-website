/*

Livecode integration for courses.

To add a livecode example, use the following format.

```{.python .example}
print("hello, world!")
```

The `python` could be replaced with any of the supported languages.

The supported languages are:
- python
- rust
- html
- golang

*/

const LIVECODE_BASE_URL = "https://falcon.mon.school";

const CODEMIRROR_OPTIONS = {
  lineNumbers: true,
  keyMap: "sublime",
  matchBrackets: true,
  indentWithTabs: false,
  tabSize: 4,
  indentUnit: 4,
  extraKeys: {
    Tab: (cm) => {
      cm.somethingSelected()
      ? cm.execCommand('indentMore')
      : cm.execCommand('insertSoftTab');
    }
  }
}

var TEMPLATE = `
<div class="livecode-editor">
  <div class="controls">
    <button class="run">Run</button>
  </div>
  <div class="code-editor">
    <div class="code-wrapper">
      <textarea class="code"></textarea>
    </div>
    <div class="output-wrapper">
      <pre class="output"></pre>
    </div>
  </div>
</div>
`

function setupExample(element) {
  var editor = {
    element: $(element),
    editor: null,
    codemirror: null,

    options: {
      language: '',
      autopreview: false,
      mode: null,
      runtime: null,
      buttons: []
    },

    findLanguage() {
      var languageClass = this.element.find("code").attr("class");
      if (languageClass) {
        return languageClass.replace("language-", "");
      }
      else {
        return "";
      }
    },

    parseOptions() {
      var lang = this.findLanguage();
      this.options = {...this.options, ...livecode.getOptions(lang)};
      this.options.language = lang;
    },

    getMode() {
      return this.options.mode || this.options.language;
    },

    getRuntime() {
      return this.options.runtime || this.options.language;
    },


    injectTextArea() {
      var code = $(this.element).text();

      this.element
        .wrap('<div></div>')
        .hide()
        .parent()
        .append(TEMPLATE)
        .find("textarea.code")
        .val(code);
    },

    setupCodeMirror() {
      this.editor = this.element.parent().find(".livecode-editor");
      var textarea = $(this.editor).find("textarea.code")[0];

      var mode = this.getMode();
      var options = {...CODEMIRROR_OPTIONS, mode: mode};
      this.codemirror = CodeMirror.fromTextArea(textarea, options);
    },

    setup() {
      this.parseOptions();
      this.injectTextArea();
      this.setupCodeMirror();

      this.addRunButtons();
      this.setupRun();
    },

    setupRun() {
      var runtime = this.getRuntime();
      var url = `${LIVECODE_BASE_URL}/runtimes/${runtime}`;
      var codemirror = this.codemirror;

      var editor = this;

      $(this.editor).find(".run").on('click', function() {
        var code = codemirror.doc.getValue();
        var mode = $(this).data("mode") || "exec";

        editor.clearOutput();

        fetch(url, {
          method: "POST",
          body: code,
          headers: {'x-falcon-mode': mode}
        })
        .then(response => response.text())
        .then(output => {
          editor.showOutput(output);
        });
      });
    },
    showOutput(output) {
      $(this.editor).find(".output-wrapper").show();
      $(this.editor).find(".output").text(output);
    },

    clearOutput() {
      $(this.editor).find(".output-wrapper").hide();
      $(this.editor).find(".output").text("");
    },

    // extra run buttons specified in course.js
    addRunButtons() {
      var buttons = this.options.buttons;

      for (var i=0; i<buttons.length; i++) {
        var b = buttons[i];
        $("<button></button>")
          .addClass("run")
          .data(b.args)
          .html(b.label)
          .appendTo($(this.editor).find(".controls"));
      }
    }
  };

  editor.setup();
}

var livecode = {
  defaultOptions: {
    golang: {
      mode: "go"
    },
    html: {
      mode: "htmlmixed"
    }
  },

  options: {},

  // can set mode, runtime, autopreview etc. for a language.
  setOptions(language, options) {
    this.options[language] = options;
  },

  getOptions(language) {
    var defaults = this.defaultOptions[language] || {};
    var options = this.options[language] || {};
     return {...defaults, ...options}
  },

  addRunButton(options) {
    this.buttons.push(options);
  },

  setup() {
    $(function() {
      $("pre.example").each((i, e) => {
        setupExample(e);
      });
    });
  }
};


livecode.setup();