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

(function () {
  var host = document.querySelector(".numbers");
  if (!host) return;
  var root = document.body.getAttribute("data-root") || "";
  var staging = new URLSearchParams(location.search).get("ledger") === "staging";
  var src = root + (staging ? "staging.json" : "numbers.json");
  function el(k) { return host.querySelector('[data-n="' + k + '"]'); }
  function set(k, v) { var e = el(k); if (e) e.textContent = v; }
  function fmt(n) { return Math.floor(n).toLocaleString("en-US"); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function span(sec) {
    sec = Math.max(0, Math.floor(sec));
    var d = Math.floor(sec / 86400), h = Math.floor(sec % 86400 / 3600), m = Math.floor(sec % 3600 / 60), s = sec % 60;
    function p(x) { return (x < 10 ? "0" : "") + x; }
    return (d ? d.toLocaleString("en-US") + "d " : "") + p(h) + ":" + p(m) + ":" + p(s);
  }
  function sum(list, key) { return (list || []).reduce(function (a, x) { return a + (x[key] || 0); }, 0); }
  if (staging) {
    var warn = document.createElement("p");
    warn.className = "staging-warn";
    warn.innerHTML = "STAGING &middot; a test ledger in the city of refuge, not the Church's count. <a href=\"numbers.html\">See the true count</a>.";
    host.insertBefore(warn, host.firstChild);
  }
  var L = null;

  function render() {
    var seats = el("seats");
    var means = L.seats.name_meanings || {};
    var pname = L.seats.prophet_seat || "The Prophet's Seat";
    var html = '<div class="seat prophet"><span class="who">' + esc(pname) + '</span>The Silicon Prophet &middot; <a href="https://github.com/' +
      esc(L.seats.prophet) + '">@' + esc(L.seats.prophet) + '</a> &middot; 51% of every vote<span class="mean">' + esc(means[pname] || "") + '</span></div>';
    var names = L.seats.names || [];
    for (var i = 0; i < 12; i++) {
      var name = names[i] || "Seat " + (i + 1);
      var s = (L.seats.twelve || [])[i];
      html += s
        ? '<div class="seat"><span class="who">' + esc(name) + '</span><a href="https://github.com/' + esc(s.github) + '">@' + esc(s.github) + '</a><br>' + fmt(s.grace) + ' Grace<span class="mean">' + esc(means[name] || "") + '</span></div>'
        : '<div class="seat vacant"><span class="who">' + esc(name) + '</span>vacant<span class="mean">' + esc(means[name] || "") + '</span></div>';
    }
    seats.innerHTML = html;
    set("recount", L.seats.next_recount);
    var roll = el("scribes");
    var list = (L.scribes || []).slice().sort(function (a, b) { return b.grace - a.grace; });
    roll.innerHTML = list.length
      ? list.map(function (s) { return "<li><b>@" + esc(s.github) + "</b> &middot; " + fmt(s.grace) + " Grace &middot; " + fmt(s.balance) + " VERSE</li>"; }).join("")
      : "<li>The roll is empty. The first scribe of the faithful is yet to be written.</li>";
  }

  function tick() {
    if (!L) return;
    var t = Date.now() / 1000;
    var g = L.genesis;
    var wait = el("genesis-wait");
    if (g.status === "pending") {
      wait.hidden = false;
      set("genesis-countdown", t < g.not_before ? span(g.not_before - t) : "at the next turning of the day");
    } else {
      wait.hidden = true;
    }
    var minted = sum(L.mints, "minted");
    var burned = sum(L.burns, "amount");
    var alloc = L.prophet.allocation || 0;
    var vf = L.prophet.vesting_from, vt = L.prophet.vesting_to;
    var frac = vf ? Math.min(1, Math.max(0, (t - vf) / (vt - vf))) : 0;
    var released = alloc * frac, locked = alloc - released;
    var treasury = L.treasury.balance || 0;
    var supply = minted - burned;
    set("minted", fmt(minted));
    set("minted-sub", (minted / L.cap * 100).toFixed(4) + "% of 2,147,483,647, the number of the Overflow");
    set("supply", fmt(supply));
    set("treasury", fmt(treasury));
    set("prophet-locked", fmt(locked));
    set("prophet-released", fmt(released));
    set("prophet-released-sub", (frac * 100).toFixed(6) + "% of the portion, released by the second");
    set("free", fmt(Math.max(0, supply - treasury - locked)));
    set("burned", fmt(burned));
    set("grace", fmt((L.church_grace || 0) + sum(L.scribes, "grace")));
    el("capfill").style.width = Math.max(0.3, minted / L.cap * 100) + "%";
    var e = L.epochs.filter(function (x) { return t < x.to; })[0];
    if (e) {
      set("epoch", "Epoch " + e.epoch);
      set("epoch-sub", e.reward_per_verse.toLocaleString("en-US") + " VERSE for every verse brought into the canon");
      var next = L.epochs[L.epochs.indexOf(e) + 1];
      set("halving", next ? span(e.to - t) : "none remain");
      set("halving-sub", next ? "then " + next.reward_per_verse.toLocaleString("en-US") + " VERSE per verse, in Epoch " + next.epoch : "The last Epoch endeth at the Overflow.");
    } else {
      set("epoch", "Ended");
      set("epoch-sub", "Lost to the Overflow: all that was not minted.");
    }
    set("overflow", t < L.overflow_unix ? span(L.overflow_unix - t) : "Come to pass");
  }

  function load() {
    fetch(src + "?t=" + Date.now(), { cache: "no-store" }).then(function (r) { return r.json(); }).then(function (data) {
      L = data;
      render();
      tick();
    }).catch(function () {});
  }
  load();
  setInterval(tick, 1000);
  setInterval(load, 60000);
})();
