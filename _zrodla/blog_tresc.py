# -*- coding: utf-8 -*-
"""Tresc bloga i FAQ (wczytywana przez build.py).

Znaczniki w tresci:
  {R}            - sciezka do katalogu glownego strony (np. ../../)
  {TEL} {TEL_H}  - telefon i link tel:
  [[FOTO nazwa|alt|podpis]] - zdjecie z img/ przez funkcje img() (srcset)
Fakty przepisowe i oplaty WORD: zrodla w _zrodla/blog_zrodla.md (stan na 29.10.2026).
Klucze wpisu: 'okr' - krotka nazwa w okruszkach; 'zmiana' (opcjonalnie) - data ostatniej zmiany (sitemap, dateModified).
"""

DATA = '2026-10-29'
DATA_TXT = '29 października 2026'

WPISY = [
# ------------------------------------------------------------------ a) kat. B koszt i czas
{
 'slug': 'prawo-jazdy-kategorii-b-witnica-cena-czas',
 'okr': 'Koszt prawa jazdy kat. B',
 'h1': 'Prawo jazdy kat. B w Witnicy - ile kosztuje i ile trwa',
 'tytul': 'Ile kosztuje prawo jazdy kat. B w Witnicy i ile trwa kurs',
 'opis': 'Ile kosztuje prawo jazdy kat. B w Witnicy i ile trwa: kurs od 4 490 zł, egzaminy w WORD Gorzów (59 i 239 zł), PKK, badanie lekarskie i kolejność kroków.',
 'lead': 'Kurs w OSK Champion, oba egzaminy w WORD Gorzów zdane za pierwszym razem i wydanie dokumentu to razem 4 888 zł z teorią online albo 5 498 zł z teorią stacjonarną. Do tego badanie lekarskie i zdjęcie. Czas zależy głównie od tego, jak często jeździsz.',
 'foto': 'kat-b', 'foto_alt': 'Toyota Yaris OSK Champion na placu manewrowym',
 'kafel': 'Cena kursu, opłaty w WORD Gorzów i w urzędzie, a do tego kolejność kroków od badania lekarskiego do odbioru dokumentu.',
 'kurs': 'Kategoria B',
 'tresc': '''
<p>Płacisz w czterech miejscach: u nas za kurs, w WORD za egzaminy, w urzędzie za wydanie dokumentu i u lekarza za badanie.</p>

<h2>Cena kursu kat. B w OSK Champion</h2>
<p>Kurs prowadzimy na Toyocie Yaris. Obejmuje 30 godzin teorii i 30 godzin jazd. Cena zależy od tego, jak chcesz zrobić teorię:</p>
<dl class="dane">
  <div><dt>Kurs z teorią stacjonarną</dt><dd>5 100 zł</dd></div>
  <div><dt>Kurs z teorią online albo bez teorii</dt><dd>4 490 zł</dd></div>
  <div><dt>Kurs ekspresowy</dt><dd>dopłata 1 000 zł</dd></div>
  <div><dt>Godzina dodatkowa</dt><dd>150 zł (kursanci OSK Champion), 160 zł (kursanci z innych ośrodków)</dd></div>
</dl>
<p>W cenie kursu są podręczniki do nauki testów i pół godziny jazdy na placu egzaminacyjnym WORD. Honorujemy Kartę Dużej Rodziny. Za kurs możesz zapłacić w biurze albo przelewem. Aktualne ceny wszystkich kursów są w <a href="{R}cennik/">cenniku</a>.</p>
<p>Wersja „bez teorii” jest dla osób, które mają już zdany egzamin teoretyczny w WORD. Wtedy robisz 4 godziny pierwszej pomocy i 30 godzin jazd.</p>

<h2>Opłaty poza szkołą</h2>
<p>Egzaminy państwowe zdajesz w Wojewódzkim Ośrodku Ruchu Drogowego w Gorzowie Wielkopolskim. Stawki ustala sejmik województwa lubuskiego. Od 28 lutego 2026 r. w WORD Gorzów płacisz:</p>
<ul class="lista">
  <li>59 zł za egzamin teoretyczny kat. B,</li>
  <li>239 zł za egzamin praktyczny kat. B.</li>
</ul>
<p>Każde podejście do egzaminu opłacasz osobno. Po zdanym egzaminie praktycznym płacisz w urzędzie 100 zł za wydanie prawa jazdy. Badanie lekarskie u lekarza uprawnionego do badania kierowców też jest płatne, a cenę poda gabinet, w którym się zapiszesz. Potrzebne będzie jeszcze aktualne zdjęcie do wniosku.</p>

<aside class="skrot">
  <p class="skrot-h">W skrócie</p>
  <p>Kurs z teorią online (4 490 zł), oba egzaminy zdane za pierwszym razem (59 + 239 zł) i wydanie dokumentu (100 zł) to razem 4 888 zł. Z teorią stacjonarną wychodzi 5 498 zł. Do tego doliczasz badanie lekarskie i zdjęcie.</p>
</aside>

<h2>Kolejność kroków</h2>
<ol class="kroki-n">
  <li>Badanie lekarskie i numer PKK z wydziału komunikacji. Jak go zdobyć, opisujemy we wpisie <a href="{R}blog/pierwsza-jazda-jak-przygotowac-sie-do-kursu/">jak przygotować się do kursu prawa jazdy</a>.</li>
  <li>Zapis w biurze przy ul. Gorzowskiej 6 w Witnicy, telefonicznie albo przez <a href="{R}kontakt/#zapis">formularz</a>.</li>
  <li>Teoria: w sali wykładowej w Witnicy albo online.</li>
  <li>30 godzin jazd na Toyocie Yaris. Manewry ćwiczysz na naszym placu w Gorzowie Wielkopolskim.</li>
  <li>Egzamin wewnętrzny w szkole, a potem egzamin teoretyczny i praktyczny w WORD w Gorzowie.</li>
  <li>Opłata za wydanie prawa jazdy i odbiór dokumentu w urzędzie.</li>
</ol>

[[FOTO yaris-wnetrze|Kokpit Toyoty Yaris, na której prowadzimy kurs kat. B|Za tą kierownicą spędzisz wszystkie 30 godzin jazd.]]

<h2>Ile to trwa</h2>
<p>Najwięcej zależy od tego, jak często jeździsz. 30 godzin jazd można rozłożyć na kilka tygodni albo na dłużej, jeśli godzisz kurs ze szkołą lub pracą. Jeśli zależy ci na czasie, zapytaj w biurze o kurs ekspresowy.</p>
<p>Na formalności poza szkołą też trzeba zostawić trochę czasu:</p>
<ul class="lista">
  <li>numer PKK urząd nadaje od ręki, jeśli wniosek jest kompletny, albo do 2 dni roboczych, gdy musi sprawdzić dane,</li>
  <li>egzamin teoretyczny w WORD Gorzów jest dostępny na bieżąco, często nawet w dniu zapisu,</li>
  <li>na egzamin praktyczny czekało się w październiku 2026 r. około 3 tygodni (dane WORD z 22.10.2026),</li>
  <li>po zdanym egzaminie urząd przygotowuje prawo jazdy do 9 dni roboczych od otrzymania potwierdzenia opłaty.</li>
</ul>
<p>Terminy w WORD zmieniają się z miesiąca na miesiąc, więc przed zapisem na egzamin sprawdź je na bieżąco.</p>

<h2>Kurs dla 17-latków</h2>
<p>Od 3 marca 2026 r. prawo jazdy kat. B można dostać po ukończeniu 17 lat. Do 18. urodzin prowadzisz tylko w Polsce, a przez pierwsze 6 miesięcy jeździsz z osobą towarzyszącą. Siedzi ona obok, z przodu, ma co najmniej 25 lat i prawo jazdy kat. B nieprzerwanie od 5 lat, w ostatnich 5 latach nie miała zakazu prowadzenia pojazdów i musi być trzeźwa. Do 18 lat nie możesz też wykonywać przewozu osób taksówką ani przewozu rzeczy. Kurs możesz zacząć najwcześniej 3 miesiące przed 17. urodzinami, a jako osoba niepełnoletnia potrzebujesz pisemnej zgody rodzica lub opiekuna.</p>
''',
 'faq': [
  ('Ile w sumie kosztuje prawo jazdy kat. B?', 'Z kursem z teorią online, egzaminami zdanymi za pierwszym razem i opłatą za dokument 4 888 zł, z teorią stacjonarną 5 498 zł. Do tego badanie lekarskie i zdjęcie.'),
  ('Czy podręczniki są w cenie kursu kat. B?', 'Tak. Podręczniki do nauki testów są w cenie kursu, podobnie jak pół godziny jazdy na placu egzaminacyjnym WORD.'),
  ('Dla kogo jest kurs kat. B bez teorii?', 'Dla osób, które mają już zdany egzamin teoretyczny w WORD. Robisz wtedy 4 godziny pierwszej pomocy i 30 godzin jazd, za 4 490 zł.'),
 ],
 'zobacz': ['egzamin-praktyczny-word-gorzow', 'pierwsza-jazda-jak-przygotowac-sie-do-kursu'],
},

# ------------------------------------------------------------------ b) egzamin WORD Gorzow
{
 'slug': 'egzamin-praktyczny-word-gorzow',
 'okr': 'Egzamin w WORD Gorzów',
 'h1': 'Egzamin praktyczny w WORD Gorzów Wielkopolski - plac i miasto',
 'tytul': 'Egzamin praktyczny w WORD Gorzów - plac i miasto | Champion',
 'opis': 'Jak wygląda egzamin praktyczny kat. B w WORD Gorzów Wielkopolski: zapisy, opłata 239 zł, zadania na placu, jazda po mieście i jak się do niego przygotować.',
 'lead': 'Egzamin praktyczny kat. B w WORD Gorzów to zadania na placu i co najmniej 40 minut jazdy po Gorzowie. Zapiszesz się w pokoju 107 B albo przez INFO-KIEROWCA, a za podejście zapłacisz 239 zł.',
 'foto': 'plac-yaris', 'foto_alt': 'Toyota Yaris i ciężarówka na placu manewrowym OSK Champion w Gorzowie',
 'kafel': 'Zapisy w WORD przy ul. Podmiejskiej, zadania na placu, jazda po Gorzowie i to, co najczęściej przerywa egzamin.',
 'kurs': 'Kategoria B',
 'tresc': '''
<p>Egzamin państwowy zdajesz w Wojewódzkim Ośrodku Ruchu Drogowego w Gorzowie Wielkopolskim, przy ul. Podmiejskiej 18. Zadania na egzaminie określa rozporządzenie Ministra Infrastruktury, więc wiadomo z góry, czego egzaminator może od ciebie wymagać.</p>

<h2>Zapis na egzamin</h2>
<p>Do zapisu potrzebujesz numeru PESEL i numeru PKK. Termin ustalisz w Biurze Obsługi Interesanta WORD (pokój 107 B, I piętro, w dni robocze 7:30-15:15) albo przez internet w serwisie INFO-KIEROWCA. Telefonicznie nie da się zapisać. Z terminu możesz zrezygnować najpóźniej 2 dni robocze przed egzaminem.</p>
<p>Egzamin praktyczny kat. B kosztuje 239 zł (stawka od 28 lutego 2026 r.). W październiku 2026 r. WORD podawał, że na egzamin praktyczny czeka się około 3 tygodni.</p>

<h2>Początek egzaminu</h2>
<p>Weź dowód osobisty albo paszport, bez niego egzamin się nie zacznie. Przebieg egzaminu kat. B jest nagrywany kamerą w samochodzie, razem z dźwiękiem. Na twój wniosek na egzaminie może być obecny instruktor.</p>

<h2>Zadania na placu manewrowym</h2>
<ol class="kroki-n">
  <li>Przygotowanie do jazdy. System losuje dwie rzeczy: jeden z płynów albo sygnał dźwiękowy i jedno ze świateł. Przy płynach wystarczy pokazać, gdzie i czym sprawdza się poziom, światło albo sygnał trzeba włączyć i sprawdzić. Masz na to do 5 minut. Potem ustawiasz fotel, lusterka i zagłówek, zapinasz pas i sprawdzasz, czy drzwi są zamknięte.</li>
  <li>Ruszanie i jazda pasem ruchu do przodu i do tyłu, czyli popularny „łuk”. Cofając, obserwujesz tor jazdy przez tylną szybę i w lusterkach. Zatrzymujesz się w wyznaczonym polu na końcu i na początku pasa.</li>
  <li>Ruszanie do przodu na wzniesieniu. Po zatrzymaniu zaciągasz hamulec postojowy i ruszasz, zwalniając go. Samochód nie może się cofnąć więcej niż 20 cm, a silnik nie może zgasnąć.</li>
</ol>
<p>Do jazdy w mieście nie przejdziesz, jeśli przejedziesz kołem przez linię wyznaczającą zewnętrzną krawędź stanowiska, najedziesz na pachołek albo go potrącisz, dwa razy źle wykonasz to samo zadanie albo zachowasz się tak, że grozi to kolizją lub uszkodzeniem auta. Samo najechanie na linię to błąd w wykonaniu zadania, które możesz jeszcze raz powtórzyć.</p>

[[FOTO plac-szeroki|Plac manewrowy OSK Champion przy ul. Kostrzyńskiej 12 w Gorzowie Wielkopolskim|Nasz plac przy ul. Kostrzyńskiej 12 w Gorzowie - tu ćwiczysz łuk i ruszanie na wzniesieniu.]]

<h2>Jazda w ruchu drogowym</h2>
<p>Część w mieście trwa co najmniej 40 minut. Egzaminator może ją skończyć po 25 minutach, jeśli wszystkie wymagane zadania są już wykonane, a wynik jest pozytywny. Zadania to między innymi:</p>
<ul class="lista">
  <li>przejazd przez skrzyżowania równorzędne, ze znakami, z sygnalizacją i ronda,</li>
  <li>przejścia dla pieszych, zmiana pasa, skręty w prawo i w lewo, zawracanie na skrzyżowaniu,</li>
  <li>jedno parkowanie wskazane przez egzaminatora: prostopadłe albo skośne (wjazd przodem) lub równoległe (wjazd tyłem),</li>
  <li>zawracanie na biegu wstecznym z wykorzystaniem np. wjazdu albo zatoki,</li>
  <li>hamowanie do zatrzymania we wskazanym miejscu.</li>
</ul>
<p>Egzaminator ocenia też jazdę ekonomiczną. Na wyższy bieg zmieniasz przy 1800-2600 obrotach na minutę, a pierwsze cztery biegi powinny być włączone, zanim samochód osiągnie 50 km/h. Hamuj też silnikiem, a nie tylko pedałem hamulca. W Gorzowie jeżdżą tramwaje, a przepisy przewidują na egzaminie przejazd przez torowisko tramwajowe i obok przystanku tramwajowego, dlatego warto przećwiczyć takie miejsca.</p>

<h2>Po egzaminie</h2>
<p>Na koniec egzaminator omawia z tobą przebieg egzaminu i podaje wynik. Po zdanym egzaminie WORD sam przekazuje wynik do urzędu, który wydaje prawo jazdy, a ty wnosisz opłatę za wydanie dokumentu (100 zł). Jeśli się nie udało, zapisujesz się na kolejny termin i ponownie płacisz za egzamin. Przed poprawką warto dokupić godzinę jazdy i przećwiczyć dokładnie to, co poszło źle.</p>

<h2>Jak się przygotować</h2>
<p>Najwięcej daje powtarzanie zadań z placu do momentu, w którym robisz je bez zastanawiania się. Nasz plac manewrowy jest w Gorzowie Wielkopolskim, przy ul. Kostrzyńskiej 12, i korzystają z niego tylko kursanci OSK Champion. Ćwiczysz więc w tym samym mieście, w którym zdajesz egzamin. W cenie kursu kat. B jest też pół godziny jazdy na placu egzaminacyjnym WORD.</p>
<aside class="skrot">
  <p class="skrot-h">Przed egzaminem</p>
  <ul>
    <li>Sprawdź godzinę egzaminu i przyjdź wcześniej, żeby nie stresować się dojazdem.</li>
    <li>Weź dowód osobisty albo paszport.</li>
    <li>Powtórz z instruktorem, gdzie sprawdza się płyny i jak włącza się poszczególne światła.</li>
    <li>Jeśli czujesz, że czegoś brakuje, dokup godzinę jazdy przed egzaminem.</li>
  </ul>
</aside>
<p>Opis kursu i ceny znajdziesz na stronie <a href="{R}oferta/#kat-b">kurs prawa jazdy kat. B w OSK Champion</a>. O kosztach całego prawa jazdy piszemy we wpisie <a href="{R}blog/prawo-jazdy-kategorii-b-witnica-cena-czas/">Prawo jazdy kat. B w Witnicy - ile kosztuje i ile trwa</a>.</p>
''',
 'faq': [
  ('Gdzie jest WORD w Gorzowie Wielkopolskim?', 'Przy ul. Podmiejskiej 18, 66-400 Gorzów Wlkp. Biuro Obsługi Interesanta jest w pokoju 107 B na I piętrze.'),
  ('Ile trwa egzamin praktyczny kat. B?', 'Jazda w ruchu drogowym trwa co najmniej 40 minut, ale egzaminator może ją zakończyć po 25 minutach, jeśli wszystkie zadania zostały wykonane i wynik jest pozytywny. Do tego dochodzi część na placu.'),
  ('Co się stanie, jeśli pomylę się na placu?', 'Źle wykonane zadanie możesz powtórzyć raz. Egzamin kończy się na placu, jeśli drugi raz wykonasz je źle, przejedziesz kołem przez linię wyznaczającą zewnętrzną krawędź stanowiska, najedziesz na pachołek albo go potrącisz.'),
  ('Czy mogę zapisać się na egzamin przez telefon?', 'Nie. WORD Gorzów przyjmuje zapisy osobiście, przez pełnomocnika albo przez serwis INFO-KIEROWCA.'),
 ],
 'zobacz': ['prawo-jazdy-kategorii-b-witnica-cena-czas', 'pierwsza-jazda-jak-przygotowac-sie-do-kursu'],
},

# ------------------------------------------------------------------ c) C i C+E
{
 'slug': 'prawo-jazdy-c-ce-kwalifikacja-wstepna',
 'okr': 'Kat. C i C+E',
 'h1': 'Prawo jazdy kat. C i C+E - wymagania, kwalifikacja wstępna i przebieg kursu',
 'tytul': 'Prawo jazdy C i C+E, kwalifikacja wstępna | OSK Champion',
 'opis': 'Prawo jazdy kat. C i C+E w Witnicy: od ilu lat, badania, kwalifikacja wstępna i kod 95, kurs na MAN TGL i MAN TGX z naczepą, egzaminy w WORD Gorzów.',
 'lead': 'Na kat. C potrzebujesz prawa jazdy kat. B, badań lekarskich i psychologicznych oraz 21 lat, a z pełną kwalifikacją wstępną wystarczy 18. Kurs robisz u nas na MAN TGL, a kat. C+E na MAN TGX z naczepą.',
 'foto': 'kat-ce', 'foto_alt': 'MAN TGX z naczepą do nauki jazdy kat. C+E',
 'kafel': 'Wiek, badania, kolejność kategorii, kwalifikacja wstępna i kod 95, a także kurs na MAN TGL i MAN TGX z naczepą.',
 'kurs': 'Kategoria C',
 'tresc': '''
<p>Prawo jazdy kat. C pozwala prowadzić samochód o dopuszczalnej masie całkowitej powyżej 3,5 t, z wyjątkiem autobusu. Kat. C+E to ten sam samochód z przyczepą albo naczepą. Żeby jeździć ciężarówką zawodowo, oprócz prawa jazdy potrzebujesz kwalifikacji wstępnej i kodu 95.</p>

<h2>Kolejność kategorii</h2>
<p>Każda kategoria wymaga poprzedniej. Do kursu C potrzebujesz prawa jazdy kat. B, a do C+E kat. C. Nie da się zrobić C+E z pominięciem C.</p>

<h2>Od ilu lat</h2>
<p>Bez kwalifikacji prawo jazdy C dostaniesz w wieku 21 lat. Z pełną kwalifikacją wstępną już w wieku 18 lat, z przyspieszoną nadal od 21. Kurs możesz zacząć 3 miesiące przed wymaganym wiekiem.</p>
<p>Jeśli masz mniej niż 21 lat i chcesz jeździć zawodowo, nie musisz czekać z kursem kat. C na koniec kwalifikacji. Szkolenie na prawo jazdy możesz zacząć także w trakcie kwalifikacji wstępnej, najwcześniej 3 miesiące przed 18. urodzinami. Plan kursu i kwalifikacji najlepiej ustalić od razu przy zapisie.</p>

<h2>Badania i PKK</h2>
<p>Do profilu kandydata na kierowcę (PKK) na kat. C i C+E potrzebujesz dwóch orzeczeń: lekarskiego i psychologicznego. Prawo jazdy tych kategorii wydaje się na 5 lat. Po 5 latach wymieniasz dokument na nowy, z aktualnymi badaniami. Z dokumentami pomagamy w biurze w Witnicy.</p>

<h2>Kurs kat. C na MAN TGL</h2>
<p>Szkolimy na ciężarówce MAN TGL 12.240. Kurs to 20 godzin teorii i 30 godzin jazd, cena 5 800 zł, godzina dodatkowa 250 zł. Kto ma już zdany egzamin teoretyczny na kat. C w WORD, robi u nas same jazdy, czyli 30 godzin.</p>
<p>W WORD Gorzów za egzamin teoretyczny kat. C zapłacisz 59 zł, a za praktyczny 298 zł (stawki od 28 lutego 2026 r.). Na placu wykonujesz między innymi jazdę pasem ruchu do przodu i cofanie po prostej i łuku (do 5 minut) oraz jeden wylosowany zestaw z manewrami parkowania i ruszaniem na wzniesieniu. Jazda w ruchu drogowym trwa co najmniej 45 minut.</p>

[[FOTO kat-c|Ciężarówka MAN TGL 12.240 OSK Champion na placu manewrowym|MAN TGL 12.240 - na nim robisz kurs kat. C.]]

<h2>Kurs kat. C+E na MAN TGX z naczepą</h2>
<p>Kurs C+E prowadzimy na ciągniku MAN TGX 18.500 z naczepą Wielton. To 25 godzin jazd bez części teoretycznej, cena 6 500 zł, godzina dodatkowa 280 zł. Na kat. C+E nie zdajesz egzaminu teoretycznego, tylko praktyczny (298 zł w WORD Gorzów).</p>
<p>Egzamin zaczyna się od sprawdzenia zestawu i sprzęgania. Na sprzęganie masz do 15 minut, a na rozprzęganie po powrocie na plac do 10 minut. Do tego dochodzi cofanie po łuku, manewry z wylosowanego zestawu i co najmniej 45 minut jazdy w ruchu.</p>

<h2>Kwalifikacja wstępna i kod 95</h2>
<p>Bez kwalifikacji wstępnej nie podejmiesz pracy jako kierowca ciężarówki, nawet z prawem jazdy C albo C+E w portfelu. U nas zrobisz ją w jednej z dwóch wersji:</p>
<dl class="dane">
  <div><dt>Kwalifikacja wstępna (280 godzin)</dt><dd>5 900 zł</dd></div>
  <div><dt>Kwalifikacja wstępna przyspieszona (140 godzin)</dt><dd>3 500 zł</dd></div>
</dl>
<p>Pełna kwalifikacja trwa dwa razy dłużej, ale pozwala zrobić prawo jazdy C i C+E od 18 lat. Szkolenie kończy test kwalifikacyjny w WORD. W Gorzowie testy odbywają się w środy i piątki, na wolny termin czeka się zwykle 2-3 dni robocze, a opłata wynosi 50 zł. Po zdanym teście dostajesz świadectwo kwalifikacji zawodowej, a potem na twój wniosek starostwo wpisuje kod 95 do prawa jazdy (wymiana dokumentu, opłata), na 5 lat.</p>
<aside class="skrot">
  <p class="skrot-h">W skrócie</p>
  <ul>
    <li>C wymaga B, a C+E wymaga C.</li>
    <li>Wiek: 21 lat albo 18 lat z pełną kwalifikacją wstępną.</li>
    <li>Badania: lekarskie i psychologiczne.</li>
    <li>Praca jako kierowca: kwalifikacja wstępna i kod 95, potem szkolenie okresowe co 5 lat.</li>
  </ul>
</aside>

<h2>Szkolenie okresowe</h2>
<p>Kierowca zawodowy co 5 lat przechodzi szkolenie okresowe. U nas trwa ono 35 godzin (5 dni) i kosztuje 1 000 zł. Potrzebny jest numer profilu kierowcy zawodowego (PKZ). Po szkoleniu, na twój wniosek, starostwo wpisuje kod 95 na kolejne 5 lat (wymiana dokumentu, opłata).</p>
<p>Szczegóły i ceny znajdziesz na stronie <a href="{R}oferta/#kat-c">kurs prawa jazdy kat. C i C+E</a> i w <a href="{R}cennik/">cenniku</a>. Jeśli najpierw potrzebujesz prawa jazdy na przyczepę do auta osobowego, przeczytaj wpis o <a href="{R}blog/prawo-jazdy-be-przyczepa-b96/">kat. B+E i kodzie 96</a>.</p>
''',
 'faq': [
  ('Czy mogę od razu zrobić prawo jazdy C+E?', 'Nie. Do kat. C+E trzeba mieć kat. C, a do kat. C kat. B.'),
  ('Na jak długo wydaje się prawo jazdy kat. C?', 'Na 5 lat, nie dłużej niż wynika z orzeczenia lekarskiego i psychologicznego. Potem wymieniasz dokument na nowy, z aktualnymi badaniami.'),
  ('Czym różni się kwalifikacja wstępna od przyspieszonej?', 'Obie dają uprawnienie do zawodowego przewozu rzeczy. Pełna trwa 280 godzin i pozwala dodatkowo zrobić prawo jazdy kat. C i C+E od 18 lat, przyspieszona trwa 140 godzin. U nas pełna kosztuje 5 900 zł, przyspieszona 3 500 zł.'),
 ],
 'zobacz': ['prawo-jazdy-be-przyczepa-b96', 'egzamin-praktyczny-word-gorzow'],
},

# ------------------------------------------------------------------ d) B+E i B96
{
 'slug': 'prawo-jazdy-be-przyczepa-b96',
 'okr': 'B+E i kod 96',
 'h1': 'Kat. B+E czy kod 96 - jaką przyczepę pociągniesz na prawie jazdy kat. B',
 'tytul': 'Prawo jazdy B+E czy kod 96? Przyczepa na kat. B | Champion',
 'opis': 'Kiedy wystarczy kat. B, kiedy kod 96, a kiedy potrzebne prawo jazdy B+E: limity DMC przyczepy i zestawu, egzamin w WORD Gorzów, kurs B+E na Fiacie Scudo.',
 'lead': 'Na kat. B pociągniesz przyczepę do 750 kg albo cięższą, jeśli cały zestaw ma DMC do 3 500 kg. Zestaw do 4 250 kg wymaga kodu 96 (popularnie B96), a cięższy prawa jazdy kat. B+E.',
 'foto': 'kat-be', 'foto_alt': 'Fiat Scudo z przyczepą do nauki jazdy kat. B+E',
 'kafel': 'Jak policzyć DMC zestawu, kiedy wystarczy kat. B, a kiedy kod 96 albo B+E. Kurs B+E na Fiacie Scudo z przyczepą.',
 'kurs': 'Kategoria B+E',
 'tresc': '''
<p>Wszystko sprowadza się do dopuszczalnej masy całkowitej, w skrócie DMC. To nie jest to, ile przyczepa waży w danej chwili, tylko największa masa, z jaką może jechać. Znajdziesz ją w dowodzie rejestracyjnym samochodu i przyczepy. Liczysz zawsze na DMC, nawet gdy przyczepa jest pusta.</p>

<h2>Na co pozwala kat. B</h2>
<p>Na prawie jazdy kat. B prowadzisz samochód o DMC do 3 500 kg. Możesz do niego podpiąć:</p>
<ul class="lista">
  <li>przyczepę lekką, czyli o DMC do 750 kg, bez dodatkowych warunków,</li>
  <li>cięższą przyczepę, jeśli DMC samochodu i przyczepy razem nie przekracza 3 500 kg.</li>
</ul>
<p>Przykład: samochód o DMC 2 000 kg i przyczepa o DMC 1 300 kg dają razem 3 300 kg, więc wystarczy kat. B. Ten sam samochód z przyczepą o DMC 1 800 kg to już 3 800 kg i kat. B nie wystarczy.</p>
<p>Niezależnie od prawa jazdy sprawdź w dowodzie rejestracyjnym, jaką masę przyczepy wolno ciągnąć twojemu samochodowi.</p>

<h3>Jak to wygląda w praktyce</h3>
<p>Mała przyczepka ogrodowa albo bagażowa zwykle mieści się w 750 kg i nie wymaga niczego poza kat. B. Inaczej jest z lawetą. Laweta pod auto osobowe ma ładowność ponad tonę, więc jej DMC jest dużo wyższe niż 750 kg. Podobnie z większą przyczepą kempingową czy przyczepą dla koni. W takich przypadkach dodaj DMC samochodu i DMC przyczepy z dowodów rejestracyjnych i dopiero wtedy sprawdź, do której grupy poniżej trafiasz.</p>

<h2>Kod 96 - zestaw do 4 250 kg</h2>
<p>Jeśli zestaw ma DMC powyżej 3 500 kg, ale nie więcej niż 4 250 kg, wystarczy kat. B z wpisanym kodem 96. Żeby go dostać, zdajesz w WORD część praktyczną egzaminu, bez teorii. Zadania są takie jak na egzaminie B+E. W WORD Gorzów egzamin na kod 96 kosztuje 239 zł.</p>

<h2>Kat. B+E - przyczepa do 3 500 kg</h2>
<p>Kat. B+E pozwala ciągnąć samochodem z kat. B przyczepę o DMC do 3 500 kg. To rozwiązanie dla osób, które jeżdżą z cięższą lawetą, dużą przyczepą kempingową albo przyczepą dla koni, i dla tych, których zestaw przekracza 4 250 kg. Prawo jazdy B+E można zrobić od 18 lat i trzeba mieć już kat. B.</p>

<h2>Kurs B+E w OSK Champion</h2>
<p>Kurs prowadzimy na Fiacie Scudo z przyczepą. To 15 godzin jazd, bez części teoretycznej. Kosztuje 2 900 zł, godzina dodatkowa 200 zł. Manewry ćwiczysz na placu przy ul. Kostrzyńskiej 12 w Gorzowie Wielkopolskim.</p>

<h2>Egzamin B+E w WORD Gorzów</h2>
<p>Na kat. B+E zdajesz tylko egzamin praktyczny. W WORD Gorzów kosztuje 298 zł (stawka od 28 lutego 2026 r.). Egzamin wygląda tak:</p>
<ol class="kroki-n">
  <li>Sprawdzenie zestawu i sprzęganie przyczepy z samochodem. Na sprzęganie masz do 15 minut. Po cofnięciu zaczep może być do 0,5 m od kuli haka, nie musi trafić idealnie.</li>
  <li>Jazda pasem ruchu do przodu i cofanie po prostej i łuku, w czasie do 5 minut.</li>
  <li>Wylosowany zestaw zadań. Pierwszy wariant: parkowanie skośne (wjazd przodem) i prostopadłe (wjazd tyłem). Drugi wariant: parkowanie prostopadłe (wjazd przodem) i ruszanie na wzniesieniu.</li>
  <li>Co najmniej 25 minut jazdy w ruchu drogowym.</li>
  <li>Rozprzęganie po powrocie na plac, do 10 minut.</li>
</ol>

<aside class="skrot">
  <p class="skrot-h">W skrócie</p>
  <ul>
    <li>Przyczepa do 750 kg albo zestaw do 3 500 kg: wystarczy kat. B.</li>
    <li>Zestaw powyżej 3 500 kg, ale nie więcej niż 4 250 kg: kat. B z kodem 96 (albo B+E).</li>
    <li>Zestaw powyżej 4 250 kg (przyczepa do 3 500 kg): kat. B+E.</li>
  </ul>
</aside>
<p>Jeśli nie masz pewności, którą drogę wybrać, zadzwoń do biura z danymi z dowodów rejestracyjnych. Pełny opis i cena są na stronie <a href="{R}oferta/#kat-be">kurs prawa jazdy B+E</a>, a wszystkie ceny w <a href="{R}cennik/">cenniku</a>. Jeśli myślisz o cięższych pojazdach, zajrzyj do wpisu o <a href="{R}blog/prawo-jazdy-c-ce-kwalifikacja-wstepna/">kat. C i C+E</a>.</p>
''',
 'faq': [
  ('Czy na kat. B pociągnę przyczepę o DMC 750 kg?', 'Tak. Przyczepa o DMC do 750 kg to przyczepa lekka i możesz ją ciągnąć każdym samochodem, który prowadzisz na kat. B, o ile pozwala na to jego dowód rejestracyjny.'),
  ('Jak sprawdzić, czy wystarczy mi kod 96?', 'Dodaj DMC samochodu i DMC przyczepy z dowodów rejestracyjnych. Jeśli wynik jest powyżej 3 500 kg, ale nie więcej niż 4 250 kg, wystarczy kat. B z kodem 96.'),
  ('Czy na kod 96 trzeba zdawać teorię?', 'Nie. W WORD zdajesz tylko część praktyczną egzaminu, z zadaniami takimi jak na kat. B+E.'),
  ('Czy do kat. B+E trzeba zdawać teorię?', 'Nie. Kurs B+E to same jazdy (u nas 15 godzin), a w WORD zdajesz tylko egzamin praktyczny.'),
 ],
 'zobacz': ['prawo-jazdy-c-ce-kwalifikacja-wstepna', 'egzamin-praktyczny-word-gorzow'],
},

# ------------------------------------------------------------------ e) pierwsza jazda
{
 'slug': 'pierwsza-jazda-jak-przygotowac-sie-do-kursu',
 'okr': 'Pierwsza jazda',
 'h1': 'Pierwsza jazda - jak przygotować się do kursu prawa jazdy',
 'tytul': 'Jak przygotować się do kursu prawa jazdy - PKK i 1. jazda',
 'opis': 'Jak przygotować się do kursu prawa jazdy: badanie lekarskie, numer PKK, dokumenty, co zabrać na pierwszą jazdę i jak wyglądają pierwsze godziny.',
 'lead': 'Przed kursem potrzebujesz numeru PKK: najpierw badanie u lekarza, potem wniosek w wydziale komunikacji. Na pierwszą jazdę weź dokument tożsamości i wygodne buty, a resztę pokaże instruktor.',
 'foto': 'sala', 'foto_alt': 'Sala wykładowa OSK Champion w Witnicy',
 'kafel': 'Badanie lekarskie, numer PKK, dokumenty i to, czego spodziewać się na pierwszej godzinie za kierownicą.',
 'kurs': 'Kategoria B',
 'tresc': '''
<p>Zanim usiądziesz za kierownicą, musisz mieć numer profilu kandydata na kierowcę, czyli PKK. Bez niego nie zaczniemy szkolenia, a WORD nie zapisze cię na egzamin. Całość da się załatwić w kilka dni.</p>

<h2>Krok 1: badanie lekarskie</h2>
<p>Zacznij od lekarza uprawnionego do badania kierowców. Lekarz sprawdza między innymi wzrok i ogólny stan zdrowia, a potem wydaje orzeczenie lekarskie. Jeśli nosisz okulary, lekarz może wpisać, że musisz w nich prowadzić. Na kat. C i C+E potrzebne jest dodatkowo badanie psychologiczne.</p>

<h2>Krok 2: numer PKK</h2>
<p>Wniosek składasz w wydziale komunikacji starostwa powiatowego właściwego dla miejsca zamieszkania, a jeśli mieszkasz w mieście na prawach powiatu, w urzędzie miasta. Przygotuj:</p>
<ul class="lista">
  <li>wypełniony wniosek o wydanie prawa jazdy,</li>
  <li>orzeczenie lekarskie (i psychologiczne, jeśli jest wymagane),</li>
  <li>aktualne zdjęcie,</li>
  <li>dowód osobisty albo paszport,</li>
  <li>dokument potwierdzający adres zameldowania, jeśli nowy dowód osobisty go nie ma,</li>
  <li>pisemną zgodę rodzica lub opiekuna, jeśli nie masz jeszcze 18 lat (rodzic podpisuje ją przy urzędniku),</li>
  <li>kopię prawa jazdy, jeśli masz już inną kategorię.</li>
</ul>
<p>Gdy wniosek jest kompletny, numer PKK dostajesz od ręki, a jeśli urząd musi sprawdzić dane, do 2 dni roboczych. Opłatę za wydanie prawa jazdy (100 zł) wnosisz dopiero po zdanym egzaminie praktycznym.</p>
<p>Pomagamy przygotować dokumenty do PKK. Jeśli coś jest niejasne, zadzwoń do biura pod numer <a href="{TEL_H}">{TEL}</a>.</p>

<h2>Krok 3: zapis i teoria</h2>
<p>Z numerem PKK zapisujesz się w biurze przy ul. Gorzowskiej 6 w Witnicy (pn-pt 10:00-17:00), telefonicznie albo przez formularz. Na kursie kat. B wybierasz teorię stacjonarną w sali wykładowej w Witnicy albo teorię online. Podręczniki do nauki testów są w cenie kursu. Częścią szkolenia jest też nauka pierwszej pomocy.</p>
<p>Testy na egzaminie państwowym są z bazy pytań. Na egzaminie teoretycznym kat. B dostajesz 32 pytania i masz na nie 25 minut. Zdajesz, jeśli zdobędziesz co najmniej 68 z 74 punktów. Rozwiązuj pytania regularnie, po kilkanaście minut dziennie, zamiast uczyć się wszystkiego na ostatnią chwilę.</p>

<h2>Krok 4: pierwsza jazda</h2>
<p>Terminy jazd ustalasz w biurze. Jeśli z góry wiesz, kiedy masz szkołę, pracę albo dojazdy, powiedz o tym przy zapisie. Łatwiej wtedy ułożyć stały rytm jazd.</p>
<aside class="skrot">
  <p class="skrot-h">Co zabrać na pierwszą jazdę</p>
  <ul>
    <li>Dokument tożsamości.</li>
    <li>Okulary albo soczewki, jeśli lekarz wpisał je do orzeczenia.</li>
    <li>Wygodne buty z cienką, płaską podeszwą. Klapki, wysokie obcasy i ciężkie buty zimowe utrudniają wyczucie pedałów.</li>
    <li>Wodę, zwłaszcza latem.</li>
    <li>Wyśpij się i zjedz coś przed jazdą. Zmęczenie i głód utrudniają skupienie bardziej, niż się wydaje.</li>
  </ul>
</aside>

<h3>Jak wygląda pierwsza godzina</h3>
<p>Najpierw instruktor pokaże ci samochód i to, jak usiąść. Ustawiasz fotel tak, żeby wcisnąć sprzęgło do końca z lekko ugiętą nogą, potem zagłówek, lusterka i pas. To samo robisz na początku egzaminu, więc od razu nabierz tego nawyku.</p>

[[FOTO yaris-wnetrze|Kokpit Toyoty Yaris używanej na kursie kat. B|Pierwszą jazdę zaczynasz od ustawienia fotela, lusterek i zagłówka.]]

<p>Dalej uczysz się ruszać, zmieniać biegi i płynnie hamować. Nikt nie oczekuje, że za pierwszym razem wszystko wyjdzie. Gaśnięcie silnika na starcie jest normalne. Na kolejnych jazdach dochodzą manewry, które ćwiczysz na naszym placu w Gorzowie Wielkopolskim, i jazda w ruchu drogowym.</p>
<p>Najszybciej uczą się ci, którzy jeżdżą co kilka dni, a nie raz na dwa tygodnie. I pytaj od razu, w aucie, po to jest instruktor.</p>
<p>Ile kosztuje cały proces i ile trwa, opisaliśmy we wpisie <a href="{R}blog/prawo-jazdy-kategorii-b-witnica-cena-czas/">Prawo jazdy kat. B w Witnicy - ile kosztuje i ile trwa</a>. O egzaminie w Gorzowie przeczytasz we wpisie <a href="{R}blog/egzamin-praktyczny-word-gorzow/">Egzamin praktyczny w WORD Gorzów</a>.</p>
''',
 'faq': [
  ('Czy przed zapisem na kurs muszę mieć numer PKK?', 'Do zapisu nie, ale bez numeru PKK nie zaczniemy zajęć. Zadzwoń, podpowiemy, co przygotować.'),
  ('Kiedy płacę za wydanie prawa jazdy?', 'Po zdanym egzaminie praktycznym. WORD przekazuje wynik do urzędu, ty wnosisz opłatę 100 zł, a urząd przygotowuje dokument do 9 dni roboczych od otrzymania potwierdzenia opłaty.'),
  ('Czy mogę zrobić teorię online?', 'Tak. Na kursie kat. B wybierasz teorię stacjonarną w Witnicy albo online. Kurs z teorią online kosztuje 4 490 zł, a ze stacjonarną 5 100 zł.'),
 ],
 'zobacz': ['prawo-jazdy-kategorii-b-witnica-cena-czas', 'egzamin-praktyczny-word-gorzow'],
},
]


# ------------------------------------------------------------------ FAQ zbiorcze
FAQ = [
 ('Zapisy i dokumenty', [
  ('Jak zapisać się na kurs?', 'W biurze przy ul. Gorzowskiej 6 w Witnicy (pn-pt 10:00-17:00), telefonicznie pod numerem <a href="{TEL_H}">{TEL}</a> albo przez formularz na stronie. Biuro poda najbliższy termin rozpoczęcia kursu.'),
  ('Co muszę załatwić przed kursem?', 'Potrzebny jest numer profilu kandydata na kierowcę (PKK). Zakłada go wydział komunikacji starostwa albo urzędu miasta na podstawie wniosku, zdjęcia i orzeczenia lekarskiego. Pomagamy przygotować dokumenty. Szczegóły w <a href="{R}blog/pierwsza-jazda-jak-przygotowac-sie-do-kursu/">poradniku przed pierwszą jazdą</a>.'),
  ('Czy przyjmujecie osoby niepełnoletnie?', 'Tak. Na kurs kat. B zapraszamy także 17-latków. Osoba niepełnoletnia potrzebuje pisemnej zgody rodzica lub opiekuna.'),
  ('Od ilu lat mogę zrobić prawo jazdy kat. B?', 'Od 17 lat, z ograniczeniami do 18. urodzin. Kurs możesz zacząć 3 miesiące przed 17. urodzinami, za pisemną zgodą rodzica lub opiekuna.'),
  ('Gdzie odbywają się zajęcia?', 'Teoria w sali wykładowej przy ul. Gorzowskiej 6 w Witnicy (albo online na kursie kat. B). Manewry ćwiczysz na placu przy ul. Kostrzyńskiej 12 w Gorzowie Wielkopolskim, z którego korzystają tylko nasi kursanci.'),
 ]),
 ('Ceny i płatności', [
  ('Ile kosztuje kurs kat. B?', '4 490 zł z teorią online albo bez teorii, 5 100 zł z teorią stacjonarną. Kurs ekspresowy to dopłata 1 000 zł. Wszystkie ceny są w <a href="{R}cennik/">cenniku</a>.'),
  ('Ile kosztuje dodatkowa godzina jazdy?', 'Kat. B: 150 zł dla kursantów OSK Champion i 160 zł dla kursantów z innych ośrodków. Kat. B+E 200 zł, kat. C 250 zł, kat. C+E 280 zł.'),
  ('Jak mogę zapłacić za kurs?', 'W biurze albo przelewem na konto podane w cenniku. W tytule wpisz imię i nazwisko kursanta oraz kategorię. Honorujemy Kartę Dużej Rodziny.'),
  ('Co jest w cenie kursu kat. B?', '30 godzin teorii i 30 godzin jazd na Toyocie Yaris, podręczniki do nauki testów i pół godziny jazdy na placu egzaminacyjnym WORD.'),
 ]),
 ('Egzamin w WORD Gorzów', [
  ('Gdzie zdaje się egzamin państwowy?', 'W Wojewódzkim Ośrodku Ruchu Drogowego w Gorzowie Wielkopolskim, ul. Podmiejska 18. Jak wygląda egzamin, opisujemy we wpisie <a href="{R}blog/egzamin-praktyczny-word-gorzow/">Egzamin praktyczny w WORD Gorzów</a>.'),
  ('Ile kosztują egzaminy w WORD Gorzów?', 'Od 28 lutego 2026 r.: egzamin teoretyczny 59 zł (B, C), egzamin praktyczny 239 zł (B i kod 96) albo 298 zł (B+E, C, C+E). Na kat. B+E, C+E i kod 96 nie ma egzaminu teoretycznego. Każde podejście opłaca się osobno.'),
  ('Jak zapisać się na egzamin?', 'Z numerem PKK i numerem PESEL w Biurze Obsługi Interesanta WORD (pokój 107 B) albo przez serwis INFO-KIEROWCA. WORD nie przyjmuje zapisów telefonicznych.'),
 ]),
 ('Kursy na przyczepę i ciężarówkę', [
  ('Czy do kat. B+E jest teoria?', 'Nie. Kurs B+E to 15 godzin jazd na Fiacie Scudo z przyczepą. Kiedy B+E jest w ogóle potrzebne, a kiedy wystarczy kod 96, wyjaśniamy we wpisie <a href="{R}blog/prawo-jazdy-be-przyczepa-b96/">B+E czy kod 96</a>.'),
  ('Od ilu lat można zrobić prawo jazdy kat. C?', 'Od 21 lat, a z pełną kwalifikacją wstępną od 18 lat. Kurs możesz zacząć 3 miesiące przed osiągnięciem wymaganego wieku. Więcej we wpisie <a href="{R}blog/prawo-jazdy-c-ce-kwalifikacja-wstepna/">Prawo jazdy kat. C i C+E</a>.'),
  ('Na czym jeździ się na kursach C i C+E?', 'Kat. C na MAN TGL 12.240, kat. C+E na ciągniku MAN TGX 18.500 z naczepą Wielton.'),
  ('Co to jest szkolenie okresowe i kod 95?', 'Kierowca zawodowy co 5 lat przechodzi szkolenie okresowe. Po nim, na wniosek kierowcy, starostwo wpisuje kod 95 do prawa jazdy (wymiana dokumentu, opłata). U nas szkolenie trwa 35 godzin (5 dni) i kosztuje 1 000 zł. Potrzebny jest numer PKZ.'),
 ]),
]
