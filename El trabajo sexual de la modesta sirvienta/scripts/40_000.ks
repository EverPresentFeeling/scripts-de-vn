;※時間帯：夜〜日中
;※------------------------------------------------------------

;※背景：和室　夜

Todavía no puedo controlar mis sentimientos por Kochi.
[tp]

Pero eso causaría problemas a Kochi, y también estaría[r]traicionando a Yuuki.
[tp]

Aun así, supongo que debería decirle a Yuuki exactamente lo que[r]siento.
[tp]

Estoy seguro de que Yuuki se enfadará conmigo... o incluso[r]podría romper a llorar...
[tp]

...
[tp]

Qué persona muy débil soy. Realmente soy un perdedor inútil.
[tp]

Kochi.
[tp]

El mero hecho de pensar en ella hace que se me apriete el[r]pecho, y dudo incluso de intentar hablar con ella. Pero, ella es[r]lo único en lo que puedo pensar.
[tp]

;※効果：暗転

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]

;アイキャッチ

[haikei file="ec04a" st="bg" fade="cross" time="1500"]

[se file="ec02"]

[haikei file="ec04b" st="bg" fade="20" time="1500"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]



;※日中
;※背景：空

;背景　空　昼
[hide_char]
[haikei file="cmnbg9900" st="bg" fade="cross" time="1500"]

[haikei file="cmnbg9900b" st="nv" fade="cross" time="500"]

[bgm file="bgm15"]

El tiempo pasa así sin que yo haga nada.
[tp]

No he podido concentrarme en mis estudios porque no dejo de[r]pensar en ella. Es lo peor que podría pasar, pero no puedo[r]hacer nada al respecto...
[tp]

;背景　空　昼
[hide_char]
[haikei file="cmnbg9900" st="bg" fade="cross" time="1000"]

;※効果：暗転

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_textwindow]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1000"]

;※背景：屋敷玄関　昼

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="1500"]

[name text="Asato"]
Ah...
[tp]

;※声だけ
[name text="Sayuri"]
[voice id="syr" file="vf40_000syr0000"]
...
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Y cada vez que veo a Kochi en la mansión, mi intensa mirada la[r]sigue.
[tp]

Parece que Kochi es consciente de mí. Y, cada vez que nos[r]miramos, desvía apresuradamente la mirada.
[tp]

Eso solo me hace querer mirarla más.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="bg" fade="cross" time="1000"]

;※効果：暗転

[hide_char]
[hide_textwindow]
[haikei file="black" st="bg" fade="22" time="1200"]

;※背景：屋敷中庭　昼

;※立ち絵〜悠姫（私服）：イン

;背景　屋敷中庭　朝
[hide_char]
[haikei file="cmnbg1320" st="ev" fade="22" time="1200"]

;琴羽/私服/P1/Ｍ/ジト目
[char_c file="ta206"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf40_000kth0000"]
Fujimiya, ¿cómo van tus estudios para los exámenes? Últimamente[r]pareces muy desanimado, ¿no?
[tp]

[name text="Asato"]
Ah, ah, lo siento... Quizás estoy un poco cansado...
[tp]

;琴羽/私服/P2/Ｍ/ジト目
[char_c file="ta216"]
[char_action time="200"]

[name text="Kotoha"]
[voice id="kth" file="vf40_000kth0001"]
...
[tp]

[name text="Asato"]
Bueno, um, volveré a mi habitación...
[tp]

;琴羽/私服/P1/Ｍ/真剣
[char_c file="ta201"]
[char_action time="200"]

[name text="Kotoha"]
[voice id="kth" file="vf40_000kth0002"]
Fujimiya...
[tp]

;背景　屋敷中庭　朝
[hide_char]
[haikei file="cmnbg1320b" st="nv" fade="cross" time="500"]

Por otro lado, también me duele mirar la cara de Yuuki. Ya no[r]puedo tener una conversación adecuada con ella.
[tp]

Por eso la distancia entre Yuuki y yo parece crecer cada día.
[tp]

La impaciencia de sentir que no puedo seguir así no hace más[r]que crecer en mí... ¿Pero qué puedo hacer?
[tp]

;背景　屋敷中庭　朝
[hide_char]
[haikei file="cmnbg1320" st="bg" fade="cross" time="1000"]

;※効果：場面転換＋時間経過（昼　→数日後

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]
[return]

;※40_010へ