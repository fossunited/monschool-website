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

To enable instance preview for html examples, add .autopreview to the
header.

```{.html .example .autopreview}
<h1>Heading 1</h1>
<h2>Heading 2</h2>
```
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
    <div class="tabs">
      <button class="tab-link tab-output active" data-target=".tab-content-output">Output</button>
      <button class="tab-link tab-preview" data-target=".tab-content-preview">Preview</button>
    </div>

    <div class="output-wrapper tab-content tab-content-output">
      <pre class="output"></pre>
    </div>
    <div class="preview tab-content tab-content-preview">
      <iframe frameborder="0" ></iframe>
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
      outputPreview: false,
      mode: null,
      runtime: null,
      buttons: []
    },

    outputHooks: [],

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

      if (this.element.hasClass("autopreview")) {
        this.options.autopreview = true;
      }
      else if (this.element.hasClass("no-autopreview")) {
        this.options.autopreview = false;
      }
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
      this.setupPreview();
      this.setupTabs();
    },

    setupPreview() {
      if (this.options.autopreview) {
        this.setupAutoPreview();
      }
      else if (this.options.outputPreview) {
        this.setupOutputPreview();
      }
      else {
        this.removePreview();
      }
    },
    setupAutoPreview() {
      $(this.editor).find(".controls, .tab-output, .tab-content-output").remove();

      $(this.editor).find(".tab-preview").addClass("active");

      var codemirror = this.codemirror;
      var $iframe = $(this.editor).find(".preview iframe");

      function update() {
          var html = codemirror.doc.getValue();
          $iframe.attr("srcdoc", html);
      }
      codemirror.on("change", update);
      update();
    },

    setupOutputPreview() {
      var $iframe = $(this.editor).find(".preview iframe");

      function update(output) {
          $iframe.attr("srcdoc", output);
      }
      this.outputHooks.push(update);
    },

    removePreview() {
      $(this.editor).find(".tab-preview, .tab-content-preview").remove();
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

    setupTabs() {
      var editor = this.editor;
      function updateTabs() {
        var target = $(editor).find(".tab-link.active").data("target");

        $(editor).find(".tab-content").hide();
        $(editor).find(target).show();
      }

      $(function() {
        updateTabs();

        $(editor).find(".tab-link").click(function() {
          $(editor).find(".tab-link").removeClass("active");
          $(this).addClass("active");
          updateTabs();
        });
      });
    },

    showOutput(output) {
      $(this.editor).find(".output-wrapper").show();
      $(this.editor).find(".output").text(output);

      for (var i=0; i < this.outputHooks.length; i++) {
        this.outputHooks[i](output);
      }
    },

    clearOutput() {
      $(this.editor).find(".output-wrapper").hide();
      $(this.editor).find(".output").text("");

      for (var i=0; i < this.outputHooks.length; i++) {
        this.outputHooks[i]("");
      }
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
      mode: "htmlmixed",
      autopreview: true
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