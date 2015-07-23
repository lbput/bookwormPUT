function cookiepolicyclose(){
   document.getElementById('cookieHead').style.display="none";
   document.cookie = "cookiepolicy=true; path=/; max-age=2592000;";
}

var cookiepolicytext='<div id="cookieHead"><div class="cookie_header"><img src="http://www.empik.com/b/default/img/cookies_close.png"   alt="" onclick="cookiepolicyclose()" />Aby zapewnić najwyższą jakość usług wykorzystujemy informacje przechowywane w przeglądarce internetowej. Sprawdź cel, warunki przechowywania lub dostępu do nich w <a href="/privacy-policy/">Polityce Prywatności</a>.</div></div>';

if (document.cookie.indexOf('cookiepolicy=true') === -1){
   document.write(cookiepolicytext);
}