(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* rok w stopce */
  var rok = $('#rok'); if (rok) rok.textContent = new Date().getFullYear();

  /* menu mobilne */
  var ham = $('#ham'), panel = $('#panel');
  function zamknij() { panel.hidden = true; ham.setAttribute('aria-expanded', 'false'); ham.setAttribute('aria-label', 'Otwórz menu'); }
  ham.addEventListener('click', function () {
    var otw = panel.hidden;
    panel.hidden = !otw;
    ham.setAttribute('aria-expanded', String(otw));
    ham.setAttribute('aria-label', otw ? 'Zamknij menu' : 'Otwórz menu');
  });
  $$('a', panel).forEach(function (a) { a.addEventListener('click', zamknij); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) { zamknij(); ham.focus(); } });
  window.addEventListener('resize', function () { if (window.innerWidth > 1024 && !panel.hidden) zamknij(); });

  /* dolny pasek (telefon): dopiero po przewinieciu za pierwszy ekran / przyciski hero */
  var mob = $('#mob'), cel = $('#heroCta') || $('.ph');
  function pasek(w) {
    mob.classList.toggle('widac', w);
    mob.setAttribute('aria-hidden', String(!w));
    $$('a', mob).forEach(function (a) { a.tabIndex = w ? 0 : -1; });
  }
  if (cel && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (en) {
      en.forEach(function (x) { pasek(!x.isIntersecting && x.boundingClientRect.top < 0); });
    }).observe(cel);
  } else { pasek(true); }

  /* formularz zapisu (FormSubmit). Adres odbiorcy w atrybucie data-adres. */
  $$('form[data-adres]').forEach(function (f) {
    var wynik = $('.form-wynik', f);
    var kurs = f.elements['kurs'];
    // ?kurs=Kategoria+B z podstrony Kursy ustawia wybor
    var m = /[?&]kurs=([^&#]+)/.exec(location.search);
    if (m && kurs) {
      var v = decodeURIComponent(m[1].replace(/\+/g, ' '));
      var opcje = $$('option', kurs), traf = opcje.filter(function (o) { return o.value === v; })[0] ||
        opcje.filter(function (o) { return o.value.indexOf(v) === 0; })[0];
      if (traf) kurs.value = traf.value;
    }
    function pokaz(t, blad) { wynik.textContent = t; wynik.className = 'form-wynik ' + (blad ? 'blad' : 'ok'); wynik.setAttribute('role', blad ? 'alert' : 'status'); }
    function oznacz(el, zle, tekst) {
      var w = el.parentNode.querySelector('.pole-blad');
      el.setAttribute('aria-invalid', zle ? 'true' : 'false');
      if (zle) {
        if (!w) { w = document.createElement('span'); w.className = 'pole-blad'; el.insertAdjacentElement('afterend', w); }
        w.textContent = tekst;
      } else if (w) { w.remove(); }
    }
    $$('input, textarea', f).forEach(function (el) { el.addEventListener('input', function () { oznacz(el, false); }); });
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var imie = f.elements['imie'], tel = f.elements['telefon'], mail = f.elements['email'], tresc = f.elements['wiadomosc'];
      var t = tel.value.replace(/[\s()+-]/g, ''), ma = mail.value.trim();
      var vi = imie.value.trim().length >= 2, vt = /^\d{9,13}$/.test(t), vm = ma === '' || /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(ma);
      oznacz(imie, !vi, 'Wpisz imię i nazwisko.');
      oznacz(tel, !vt, 'Wpisz numer telefonu (9 cyfr).');
      oznacz(mail, !vm, 'Wpisz poprawny adres e-mail albo zostaw pole puste.');
      if (!(vi && vt && vm)) { pokaz('Popraw zaznaczone pola i wyślij ponownie.', true); var p = $('[aria-invalid="true"]', f); if (p) p.focus(); return; }
      if (f.elements['_honey'].value) return;
      var btn = $('button[type="submit"]', f);
      btn.disabled = true; btn.textContent = 'Wysyłanie...';
      var dane = {
        _subject: 'Zgłoszenie ze strony: ' + kurs.value,
        _template: 'table', _captcha: 'false',
        'Kurs': kurs.value,
        'Imię i nazwisko': imie.value.trim(),
        'Telefon': tel.value.trim(),
        email: ma || '-',
        'Pytanie': tresc.value.trim() || '-',
        'Strona': location.href.split('?')[0]
      };
      if (ma) dane._replyto = ma;
      fetch(f.getAttribute('data-adres'), { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(dane) })
        .then(function (r) { return r.json().catch(function () { return {}; }); })
        .then(function (j) {
          if (j && (j.success === true || j.success === 'true')) {
            pokaz('Dziękujemy, zgłoszenie zostało wysłane. Biuro oddzwoni najszybciej, jak to możliwe.', false);
            f.reset();
          } else {
            pokaz('Nie udało się wysłać zgłoszenia. Prosimy zadzwonić: 729 993 243 albo napisać na biuro.oskchampion@wp.pl.', true);
          }
        })
        .catch(function () { pokaz('Brak połączenia, zgłoszenie nie zostało wysłane. Prosimy zadzwonić: 729 993 243.', true); })
        .then(function () { btn.disabled = false; btn.textContent = 'Wyślij zgłoszenie'; });
    });
  });
})();
