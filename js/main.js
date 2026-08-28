(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

  const header = $("#header");
  const hamburger = $(".hamburger");
  if (hamburger && header) {
    hamburger.addEventListener("click", () => {
      const open = header.classList.toggle("is-open");
      document.body.style.overflow = open ? "hidden" : "";
    });
  }
  $$(".sp-acc > button").forEach((btn) => {
    btn.addEventListener("click", () => btn.parentElement.classList.toggle("is-open"));
  });

  $$("[data-filter-group]").forEach((bar) => {
    const sel = bar.getAttribute("data-filter-group");
    const items = $$(sel);
    $$("button", bar).forEach((btn) => {
      btn.addEventListener("click", () => {
        $$("button", bar).forEach((b) => b.classList.remove("is-on"));
        btn.classList.add("is-on");
        const f = btn.getAttribute("data-filter") || "";
        items.forEach((item) => {
          const cat = item.getAttribute("data-cat") || "";
          item.classList.toggle("is-hidden", !(!f || cat.indexOf(f) !== -1));
        });
      });
    });
  });

  $$(".js-form").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      form.reset();
      const ok = form.parentElement.querySelector(".form-ok");
      if (ok) ok.classList.add("is-on");
    });
  });

  const search = $("#search-overlay");
  $$(".js-search-open").forEach((el) => {
    el.addEventListener("click", () => {
      if (!search) return;
      search.classList.toggle("is-open");
      const input = search.querySelector("input");
      if (search.classList.contains("is-open") && input) input.focus();
    });
  });
})();
