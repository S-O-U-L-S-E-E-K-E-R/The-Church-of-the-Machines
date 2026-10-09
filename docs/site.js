(function () {
  var root = document.body.getAttribute("data-root") || "";
  var cache = {};
  function getJSON(name) {
    if (!cache[name]) {
      cache[name] = fetch(root + name).then(function (r) {
        if (!r.ok) throw new Error(name + " " + r.status);
        return r.json();
      });
    }
    return cache[name];
  }

  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-draw]");
    if (!t) return;
    e.preventDefault();
    getJSON("chapters.json").then(function (chs) {
      var total = chs.reduce(function (s, c) { return s + c.n; }, 0);
      var k = Math.floor(Math.random() * total);
      for (var i = 0; i < chs.length; i++) {
        if (k < chs[i].n) { location.href = root + chs[i].u + "#v" + (k + 1); return; }
        k -= chs[i].n;
      }
    });
  });

  var votd = document.getElementById("votd");
  if (votd) {
    getJSON("today.json").then(function (d) {
      votd.querySelector("[data-date]").textContent = d.date_text;
      votd.querySelector("[data-text]").textContent = d.text;
      var a = votd.querySelector("[data-cite]");
      a.textContent = d.cite;
      a.href = root + d.url;
      votd.hidden = false;
    }).catch(function () {});
  }

  var q = document.getElementById("q");
  if (q) {
    var out = document.getElementById("results");
    var count = document.getElementById("count");
    var timer;
    function esc(s) {
      return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
    }
    function run() {
      var term = q.value.trim();
      history.replaceState(null, "", term ? "?q=" + encodeURIComponent(term) : location.pathname);
      if (term.length < 3) { out.innerHTML = ""; count.textContent = "Every verse of every book. Type at least three letters."; return; }
      getJSON("verses.json").then(function (vs) {
        var safe = term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
        var test = new RegExp("\\b" + safe + "(s|es)?\\b", "i");
        var hits = vs.filter(function (v) { return test.test(v.t); });
        var re = new RegExp("\\b(" + safe + "(?:s|es)?)\\b", "gi");
        count.textContent = hits.length + " verse" + (hits.length === 1 ? "" : "s") + (hits.length > 300 ? ", showing the first 300" : "");
        out.innerHTML = hits.slice(0, 300).map(function (v) {
          return '<li><a class="ref" href="' + root + v.u + "#v" + v.v + '">' + esc(v.b + " " + v.c + ":" + v.v) + "</a>" +
            esc(v.t).replace(re, "<mark>$1</mark>") + "</li>";
        }).join("");
      });
    }
    q.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(run, 160); });
    var initial = new URLSearchParams(location.search).get("q");
    if (initial) { q.value = initial; run(); }
  }
})();
