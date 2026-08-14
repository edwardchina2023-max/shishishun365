(function () {
  "use strict";

  var body = document.body;
  var ageGate = document.getElementById("ageGate");
  var ageConfirm = document.getElementById("ageConfirm");
  var ageDecline = document.getElementById("ageDecline");
  var ageAccepted = false;

  try {
    ageAccepted = window.localStorage.getItem("shishishun_age_confirmed") === "yes";
  } catch (error) {
    ageAccepted = false;
  }

  function closeAgeGate() {
    if (!ageGate) return;
    ageGate.classList.add("is-hidden");
    body.classList.remove("gate-open");
  }

  if (ageAccepted) {
    closeAgeGate();
  } else {
    body.classList.add("gate-open");
  }

  if (ageConfirm) {
    ageConfirm.addEventListener("click", function () {
      try {
        window.localStorage.setItem("shishishun_age_confirmed", "yes");
      } catch (error) {
        // The visit can continue when storage is unavailable.
      }
      closeAgeGate();
    });
  }

  if (ageDecline) {
    ageDecline.addEventListener("click", function () {
      if (window.history.length > 1) {
        window.history.back();
      } else {
        window.location.replace("about:blank");
      }
    });
  }

  var siteHeader = document.getElementById("siteHeader");
  var menuToggle = document.getElementById("menuToggle");
  var siteNav = document.getElementById("siteNav");
  var lastScrollY = 0;

  function setMenu(open) {
    if (!menuToggle || !siteNav) return;
    menuToggle.setAttribute("aria-expanded", String(open));
    siteNav.classList.toggle("is-open", open);
    body.classList.toggle("menu-open", open);
  }

  if (menuToggle && siteNav) {
    menuToggle.addEventListener("click", function () {
      setMenu(menuToggle.getAttribute("aria-expanded") !== "true");
    });

    siteNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () { setMenu(false); });
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") setMenu(false);
    });
  }

  function updateHeader() {
    if (!siteHeader) return;
    var currentY = window.scrollY;
    siteHeader.classList.toggle("is-scrolled", currentY > 32);
    siteHeader.classList.toggle("is-hidden", currentY > 560 && currentY > lastScrollY + 5 && !body.classList.contains("menu-open"));
    if (currentY < lastScrollY - 5 || currentY < 180) {
      siteHeader.classList.remove("is-hidden");
    }
    lastScrollY = currentY;
  }

  window.addEventListener("scroll", updateHeader, { passive: true });
  updateHeader();

  var revealElements = document.querySelectorAll(".reveal");
  revealElements.forEach(function (element) {
    var delay = element.getAttribute("data-delay");
    if (delay) element.style.transitionDelay = delay + "ms";
  });

  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -48px" });
    revealElements.forEach(function (element) { revealObserver.observe(element); });
  } else {
    revealElements.forEach(function (element) { element.classList.add("in"); });
  }

  var products = {
    "365": {
      meaning: "顺一年",
      name: "事事顺365",
      copy: "一年三百六十五天，愿日子有序、心里有光。",
      spec: "浓香型白酒 · 42%vol · 500ml"
    },
    "516": {
      meaning: "我要顺",
      name: "事事顺516",
      copy: "把一份直白的好愿望，说给重要的人听。",
      spec: "浓香型白酒 · 45%vol · 500ml"
    },
    "china-red": {
      meaning: "中国红",
      name: "事事顺·中国红",
      copy: "一抹中国红，敬相逢，也敬圆满。",
      spec: "浓香型白酒 · 42%vol · 500ml"
    },
    "family": {
      meaning: "家和万事顺",
      name: "事事顺·家顺",
      copy: "家在，心就有归处；家顺，日子便有暖意。",
      spec: "浓香型白酒 · 42%vol · 450ml"
    }
  };

  var productButtons = document.querySelectorAll(".product-exhibit");
  var productMeaning = document.getElementById("productMeaning");
  var productName = document.getElementById("productName");
  var productCopy = document.getElementById("productCopy");
  var productSpec = document.getElementById("productSpec");

  productButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      var product = products[button.getAttribute("data-product")];
      if (!product) return;

      productButtons.forEach(function (item) {
        var active = item === button;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-pressed", String(active));
      });

      productMeaning.textContent = product.meaning;
      productName.textContent = product.name;
      productCopy.textContent = product.copy;
      productSpec.textContent = product.spec;
    });
  });

  var observedSections = Array.from(document.querySelectorAll("main section[id]"));
  var navLinks = Array.from(document.querySelectorAll(".site-nav a[href^='#']"));
  if ("IntersectionObserver" in window) {
    var sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navLinks.forEach(function (link) {
          link.classList.toggle("is-current", link.getAttribute("href") === "#" + entry.target.id);
        });
      });
    }, { rootMargin: "-38% 0px -54%", threshold: 0 });
    observedSections.forEach(function (section) { sectionObserver.observe(section); });
  }
})();
