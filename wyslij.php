<?php
/* Formularz zapisu Nauka Jazdy Champion - wysylka na skrzynke biura z wlasnego serwera (home.pl).
   Przyjmuje JSON z app.js (te same pola co wczesniej FormSubmit), odpowiada {"success":true|false}. */

const ODBIORCA = 'biuro.oskchampion@wp.pl';
const NADAWCA = 'formularz@champion-witnica.pl';
const LIMIT = 5;          // zgloszen z jednego IP
const OKNO = 600;         // w ciagu tylu sekund

header('Content-Type: application/json; charset=utf-8');
header('X-Robots-Tag: noindex');

function odpowiedz($ok, $kod = 200) {
    http_response_code($kod);
    echo json_encode(['success' => $ok]);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') odpowiedz(false, 405);

// tylko z wlasnej strony
$skad = $_SERVER['HTTP_ORIGIN'] ?? ($_SERVER['HTTP_REFERER'] ?? '');
if ($skad !== '' && !preg_match('#^https://champion-witnica\.pl(/|$)#', $skad)) odpowiedz(false, 403);

$d = json_decode(file_get_contents('php://input', false, null, 0, 20000), true);
if (!is_array($d)) odpowiedz(false, 400);

// pulapka na boty (ukryte pole) - udajemy sukces
if (!empty($d['_honey'])) odpowiedz(true);

function pole($d, $k, $max = 200) {
    $v = isset($d[$k]) && is_string($d[$k]) ? trim($d[$k]) : '';
    return mb_substr(preg_replace('/[\x00-\x09\x0B-\x1F\x7F]/u', '', $v), 0, $max);
}
function jedna_linia($s) { return trim(preg_replace('/[\r\n]+/', ' ', $s)); }

$kurs  = jedna_linia(pole($d, 'Kurs', 80));
$imie  = jedna_linia(pole($d, 'Imię i nazwisko', 100));
$tel   = jedna_linia(pole($d, 'Telefon (oddzwoń)', 30));
$mail  = jedna_linia(pole($d, 'E-mail', 120));
$tresc = pole($d, 'Pytanie / uwagi', 3000);
$kiedy = jedna_linia(pole($d, 'Wysłano', 40));
$skad2 = jedna_linia(pole($d, 'Z podstrony', 300));

if (mb_strlen($imie) < 2 || !preg_match('/^\d{9,13}$/', preg_replace('/[\s()+-]/', '', $tel))) odpowiedz(false, 422);

// prosty limit zgloszen z jednego adresu IP
$plik = sys_get_temp_dir() . '/champion_form_' . md5($_SERVER['REMOTE_ADDR'] ?? '') . '.txt';
$czasy = array_filter(explode(',', @file_get_contents($plik) ?: ''), function ($t) { return $t > time() - OKNO; });
if (count($czasy) >= LIMIT) odpowiedz(false, 429);
$czasy[] = time();
@file_put_contents($plik, implode(',', $czasy));

$h = function ($s) { return htmlspecialchars($s, ENT_QUOTES, 'UTF-8'); };
$wiersze = [
    'Kurs' => $kurs,
    'Imię i nazwisko' => $imie,
    'Telefon (oddzwoń)' => $tel,
    'E-mail' => $mail !== '' ? $mail : 'nie podano',
    'Pytanie / uwagi' => $tresc !== '' ? $tresc : 'brak',
    'Wysłano' => $kiedy,
    'Z podstrony' => $skad2,
];
$tab = '';
foreach ($wiersze as $k => $v) {
    $tab .= '<tr><td style="padding:10px 14px;border-bottom:1px solid #e5e5ef;color:#555;white-space:nowrap;vertical-align:top">' . $h($k) .
            '</td><td style="padding:10px 14px;border-bottom:1px solid #e5e5ef;color:#111;font-weight:600">' . nl2br($h($v)) . '</td></tr>';
}
$nr = preg_replace('/[^\d+]/', '', $tel);
$html = '<!doctype html><html><body style="margin:0;padding:20px;background:#f4f4f8;font-family:Arial,sans-serif;font-size:15px">' .
        '<div style="max-width:620px;margin:0 auto;background:#fff;border-radius:8px;overflow:hidden;border:1px solid #e5e5ef">' .
        '<div style="background:#3d3fcf;color:#fff;padding:16px 20px;font-size:18px;font-weight:bold">Nowe zgłoszenie ze strony</div>' .
        '<table style="width:100%;border-collapse:collapse">' . $tab . '</table>' .
        '<div style="padding:16px 20px"><a href="tel:' . $h($nr) . '" style="display:inline-block;background:#3d3fcf;color:#fff;text-decoration:none;padding:12px 20px;border-radius:6px;font-weight:bold">Zadzwoń: ' . $h($tel) . '</a></div>' .
        '</div></body></html>';
$tekst = '';
foreach ($wiersze as $k => $v) $tekst .= $k . ': ' . $v . "\n";

$temat = 'Nowe zgłoszenie: ' . $kurs . ' - ' . $imie . ', tel. ' . $tel;
$granica = 'b' . bin2hex(random_bytes(8));
$naglowki = 'From: =?UTF-8?B?' . base64_encode('Strona Champion') . '?= <' . NADAWCA . ">\r\n" .
            'MIME-Version: 1.0' . "\r\n" .
            'Content-Type: multipart/alternative; boundary="' . $granica . "\"\r\n";
if ($mail !== '' && filter_var($mail, FILTER_VALIDATE_EMAIL)) $naglowki .= 'Reply-To: ' . $mail . "\r\n";
$tresc_maila = "--$granica\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n" .
               chunk_split(base64_encode($tekst)) .
               "--$granica\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n" .
               chunk_split(base64_encode($html)) . "--$granica--\r\n";

$ok = mail(ODBIORCA, '=?UTF-8?B?' . base64_encode($temat) . '?=', $tresc_maila, $naglowki);  // bez -f: home.pl odrzuca nadawce koperty bez skrzynki
odpowiedz($ok, $ok ? 200 : 500);
