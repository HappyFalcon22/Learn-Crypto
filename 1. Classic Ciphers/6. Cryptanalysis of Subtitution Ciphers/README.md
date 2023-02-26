# Cryptanalysis of Subtitution Ciphers

## Ciphertext-only Attack

When you only have one ciphertext, it is possible to do a ***frequency analysis*** on the ciphertext.

***Frequency analysis*** is a study of counting how often a letter appears in a text. Frequency analysis can include 1-word analysis, 2-word analysis or 3-word, ... This is pretty useful in breaking classical cipher such as ***shift cipher, subtitution cipher***, with the efficiency is better when dealing with ***subtitution cipher***.

For the English language, studies have shown the frequency of letters appears in a regular text : ![Frequency analysis](Images/Freq.png)

As a result of the analysis, we have a very common and famous phrase : [etaoin shrdlu](https://en.wikipedia.org/wiki/Etaoin_shrdlu) , which reflect the descending frequency of each letter in the phrase.

So : how can we use this attack in breaking the subtitution cipher ? When can we use this attack ?

### How to attack ?

The core of frequency analysis attack is to make ***initial guesses***. It can be like this : if a letter in the ciphertext has the highest chance of presented in the ciphertext, it could be the case that the original letter was $e$, second for $t$, third for $a$ and so on. When we guess like that, some words may be guessed by us using our vocabulary or dictionary, which reveals more and more letter until all letters are revealed (recovering the key)

### When to attack ?

The core of the attack is to make ***initial guesses***, so the more chance we can make ***initial guesses***, the easier it gets to break the cipher. Which means we can use the attack when ***the ciphertext is relatively long, long enough to guess about 5 letters (in my experience)***. In the below example, we will witness the power of initial guess that helps us make other guesses which leads to solving the whole ciphertext.

If the ciphertext is not long enough, we will have less chance to make solid guesses, which prevents us from breaking the cipher

### Tools

There are some tools that can help us in analyzing the cipher text and break the cipher :

+ [Frequency Analysis Tool](https://math.dartmouth.edu/~awilson/tools/frequency_analysis.html) : This tool helps us do a frequency analysis and allows us to guess the letter in an interactive manner
+ [Frequency Analysis](https://www.101computing.net/frequency-analysis/) : Similar to the first tool
+ [quipqiup](https://quipqiup.com/) : Kind of a shortcut to break the cipher , just press Solve and some possible answers will be calculated. It is faster but less fun.

### Example

Nothing is clearer than a real example. Let's break this cipher giving this ciphertext : 

```
qv kjaigp 14 hgvp wunr fjkpnk pn hgucgu, pygug qh j afqgvp igo geayjvbg. gqpygu uhj, cjuqndh pokgh nw syig (sqwwqg-ygffrjvv igo geayjvbg), nu khi (kug-hyjugs igo) jfbnuqpyrh ajv tg dhgs wnu igo geayjvbg. qw uhj qh dhgs, pygv pyg afqgvp bgvgujpgh j ujvsnr cjfdg ajffgs pyg kugrjhpgu hgaugp, gvauokph qp dhqvb pyg kdtfqa igo wunr pyg agupqwqajpg hgvp to pyg hgucgu, jvs hgvsh pyqh pn pyg hgucgu. tnpy fjkpnk jvs hgucgu vnx yjcg pyg rgjvh pn ajfadfjpg pyg rjhpgu hgaugp jvs pygugwnug pyg hyjugs hghhqnv igo, to anrtqvqvb pyg kugrjhpgu hgaugp xqpy ujvsnr cjfdgh. qw sqwwqg-ygffrjv qh dhgs jh pyg igo geayjvbg jfbnuqpyr, pyg afqgvp jvs hgucgu hgvs gjay npygu pygqu sqwwqg-ygffrjvv kdtfqa cjfdgh, jffnxqvb pyg hjrg kugrjhpgu hgaugp pn tg ajfadfjpgs to tnpy hqsgh. pfh 1.3 anrkfgpgfo ugrncgs pyg afqgvp igo geayjvbg hpgk. qp qh vn fnvbgu vggsgs pyjvih pn pyg rnug fqrqpgs hgp nw hdkknupgs jfbnuqpyrh. nvfo gkygrgujf sqwwqg ygffrjv igo geayjvbgh jug hdkknupgs (kfdh pyg rday fghh anrrnvfo dhgs khi). pyg afqgvp vnx bdghhgh xyqay aqkygu hdqpg pyg hgucgu xqff jaagkp, jvs hgvsh pyg sqwwqg-ygffrjv kjujrgpguh qv pyg afqgvp ygffn. dfpqrjpgfo pyqh hjcgh j wdff vgpxnui undvspuqk xygv ghpjtfqhyqvb j anvvgapqnv, rjiqvb pfh 1.3 vnpqagjtfo wjhpgu xygv tunxhqvb pyg qvpguvgp.
```

Run this in the tool, we have a handy result : ![Analysis result](Images/Analysis.png)

So the letter `g` occurs `13%` of the ciphertext (the highest, and a bit too much too). So it could be the letter `e` that is encrypted

The letter `p` occurs `7%` of the ciphertext, it could be `t`, but the letter `h` and `j` occurs nearly `6%`, so we are not sure whether they are `a` and `o`, or `o` and `a`. So we stop our initial guesses here, and try subtituting `e` and `t` to the ciphertext :

```
QV KJAIet 14 HeVt WUNR FJKtNK tN HeUCeU, tYeUe QH J AFQeVt IeO eEAYJVBe. eQtYeU UHJ, CJUQNDH tOKeH NW SYIe (SQWWQe-YeFFRJVV IeO eEAYJVBe), NU KHI (KUe-HYJUeS IeO) JFBNUQtYRH AJV Te DHeS WNU IeO eEAYJVBe. QW UHJ QH DHeS, tYeV tYe AFQeVt BeVeUJteH J UJVSNR CJFDe AJFFeS tYe KUeRJHteU HeAUet, eVAUOKtH Qt DHQVB tYe KDTFQA IeO WUNR tYe AeUtQWQAJte HeVt TO tYe HeUCeU, JVS HeVSH tYQH tN tYe HeUCeU. TNtY FJKtNK JVS HeUCeU VNX YJCe tYe ReJVH tN AJFADFJte tYe RJHteU HeAUet JVS tYeUeWNUe tYe HYJUeS HeHHQNV IeO, TO ANRTQVQVB tYe KUeRJHteU HeAUet XQtY UJVSNR CJFDeH. QW SQWWQe-YeFFRJV QH DHeS JH tYe IeO eEAYJVBe JFBNUQtYR, tYe AFQeVt JVS HeUCeU HeVS eJAY NtYeU tYeQU SQWWQe-YeFFRJVV KDTFQA CJFDeH, JFFNXQVB tYe HJRe KUeRJHteU HeAUet tN Te AJFADFJteS TO TNtY HQSeH. tFH 1.3 ANRKFeteFO UeRNCeS tYe AFQeVt IeO eEAYJVBe HteK. Qt QH VN FNVBeU VeeSeS tYJVIH tN tYe RNUe FQRQteS Het NW HDKKNUteS JFBNUQtYRH. NVFO eKYeReUJF SQWWQe YeFFRJV IeO eEAYJVBeH JUe HDKKNUteS (KFDH tYe RDAY FeHH ANRRNVFO DHeS KHI). tYe AFQeVt VNX BDeHHeH XYQAY AQKYeU HDQte tYe HeUCeU XQFF JAAeKt, JVS HeVSH tYe SQWWQe-YeFFRJV KJUJReteUH QV tYe AFQeVt YeFFN. DFtQRJteFO tYQH HJCeH J WDFF VetXNUI UNDVStUQK XYeV eHtJTFQHYQVB J ANVVeAtQNV, RJIQVB tFH 1.3 VNtQAeJTFO WJHteU XYeV TUNXHQVB tYe QVteUVet.
```

Note that i am using the tool, so the uppercase letters are the encrypted and the lower are my guess.

Now we are able to safely guess a little more. There is `J` sitting on its own, which obviously be `a` encrypted to this.

The word `tYe` appears pretty much in the ciphertext, it could be the word `the`.

After these two guesses, the ciphertext should look like this :

```
QV KaAIet 14 HeVt WUNR FaKtNK tN HeUCeU, theUe QH a AFQeVt IeO eEAhaVBe. eQtheU UHa, CaUQNDH tOKeH NW ShIe (SQWWQe-heFFRaVV IeO eEAhaVBe), NU KHI (KUe-HhaUeS IeO) aFBNUQthRH AaV Te DHeS WNU IeO eEAhaVBe. QW UHa QH DHeS, theV the AFQeVt BeVeUateH a UaVSNR CaFDe AaFFeS the KUeRaHteU HeAUet, eVAUOKtH Qt DHQVB the KDTFQA IeO WUNR the AeUtQWQAate HeVt TO the HeUCeU, aVS HeVSH thQH tN the HeUCeU. TNth FaKtNK aVS HeUCeU VNX haCe the ReaVH tN AaFADFate the RaHteU HeAUet aVS theUeWNUe the HhaUeS HeHHQNV IeO, TO ANRTQVQVB the KUeRaHteU HeAUet XQth UaVSNR CaFDeH. QW SQWWQe-heFFRaV QH DHeS aH the IeO eEAhaVBe aFBNUQthR, the AFQeVt aVS HeUCeU HeVS eaAh NtheU theQU SQWWQe-heFFRaVV KDTFQA CaFDeH, aFFNXQVB the HaRe KUeRaHteU HeAUet tN Te AaFADFateS TO TNth HQSeH. tFH 1.3 ANRKFeteFO UeRNCeS the AFQeVt IeO eEAhaVBe HteK. Qt QH VN FNVBeU VeeSeS thaVIH tN the RNUe FQRQteS Het NW HDKKNUteS aFBNUQthRH. NVFO eKheReUaF SQWWQe heFFRaV IeO eEAhaVBeH aUe HDKKNUteS (KFDH the RDAh FeHH ANRRNVFO DHeS KHI). the AFQeVt VNX BDeHHeH XhQAh AQKheU HDQte the HeUCeU XQFF aAAeKt, aVS HeVSH the SQWWQe-heFFRaV KaUaReteUH QV the AFQeVt heFFN. DFtQRateFO thQH HaCeH a WDFF VetXNUI UNDVStUQK XheV eHtaTFQHhQVB a ANVVeAtQNV, RaIQVB tFH 1.3 VNtQAeaTFO WaHteU XheV TUNXHQVB the QVteUVet.
```

There is the word `tN`, which highly likely that the original word is `to`

There is the word `Te`, which highly likely that the original word is `be`

After these two guesses, the ciphertext should look like this :

```
QV KaAIet 14 HeVt WUoR FaKtoK to HeUCeU, theUe QH a AFQeVt IeO eEAhaVBe. eQtheU UHa, CaUQoDH tOKeH oW ShIe (SQWWQe-heFFRaVV IeO eEAhaVBe), oU KHI (KUe-HhaUeS IeO) aFBoUQthRH AaV be DHeS WoU IeO eEAhaVBe. QW UHa QH DHeS, theV the AFQeVt BeVeUateH a UaVSoR CaFDe AaFFeS the KUeRaHteU HeAUet, eVAUOKtH Qt DHQVB the KDbFQA IeO WUoR the AeUtQWQAate HeVt bO the HeUCeU, aVS HeVSH thQH to the HeUCeU. both FaKtoK aVS HeUCeU VoX haCe the ReaVH to AaFADFate the RaHteU HeAUet aVS theUeWoUe the HhaUeS HeHHQoV IeO, bO AoRbQVQVB the KUeRaHteU HeAUet XQth UaVSoR CaFDeH. QW SQWWQe-heFFRaV QH DHeS aH the IeO eEAhaVBe aFBoUQthR, the AFQeVt aVS HeUCeU HeVS eaAh otheU theQU SQWWQe-heFFRaVV KDbFQA CaFDeH, aFFoXQVB the HaRe KUeRaHteU HeAUet to be AaFADFateS bO both HQSeH. tFH 1.3 AoRKFeteFO UeRoCeS the AFQeVt IeO eEAhaVBe HteK. Qt QH Vo FoVBeU VeeSeS thaVIH to the RoUe FQRQteS Het oW HDKKoUteS aFBoUQthRH. oVFO eKheReUaF SQWWQe heFFRaV IeO eEAhaVBeH aUe HDKKoUteS (KFDH the RDAh FeHH AoRRoVFO DHeS KHI). the AFQeVt VoX BDeHHeH XhQAh AQKheU HDQte the HeUCeU XQFF aAAeKt, aVS HeVSH the SQWWQe-heFFRaV KaUaReteUH QV the AFQeVt heFFo. DFtQRateFO thQH HaCeH a WDFF VetXoUI UoDVStUQK XheV eHtabFQHhQVB a AoVVeAtQoV, RaIQVB tFH 1.3 VotQAeabFO WaHteU XheV bUoXHQVB the QVteUVet.
```

There is the word `bO`, because we guessed `be` before, this could be the word `by`

The word `theUe` could be `there`

The word `theV` could be `then` or `they`, for safety measures, we will standby this guess

After the two guesses, the ciphertext should look like this :

```
QV KaAIet 14 HeVt WroR FaKtoK to HerCer, there QH a AFQeVt Iey eEAhaVBe. eQther rHa, CarQoDH tyKeH oW ShIe (SQWWQe-heFFRaVV Iey eEAhaVBe), or KHI (Kre-HhareS Iey) aFBorQthRH AaV be DHeS Wor Iey eEAhaVBe. QW rHa QH DHeS, theV the AFQeVt BeVerateH a raVSoR CaFDe AaFFeS the KreRaHter HeAret, eVAryKtH Qt DHQVB the KDbFQA Iey WroR the AertQWQAate HeVt by the HerCer, aVS HeVSH thQH to the HerCer. both FaKtoK aVS HerCer VoX haCe the ReaVH to AaFADFate the RaHter HeAret aVS thereWore the HhareS HeHHQoV Iey, by AoRbQVQVB the KreRaHter HeAret XQth raVSoR CaFDeH. QW SQWWQe-heFFRaV QH DHeS aH the Iey eEAhaVBe aFBorQthR, the AFQeVt aVS HerCer HeVS eaAh other theQr SQWWQe-heFFRaVV KDbFQA CaFDeH, aFFoXQVB the HaRe KreRaHter HeAret to be AaFADFateS by both HQSeH. tFH 1.3 AoRKFeteFy reRoCeS the AFQeVt Iey eEAhaVBe HteK. Qt QH Vo FoVBer VeeSeS thaVIH to the Rore FQRQteS Het oW HDKKorteS aFBorQthRH. oVFy eKheReraF SQWWQe heFFRaV Iey eEAhaVBeH are HDKKorteS (KFDH the RDAh FeHH AoRRoVFy DHeS KHI). the AFQeVt VoX BDeHHeH XhQAh AQKher HDQte the HerCer XQFF aAAeKt, aVS HeVSH the SQWWQe-heFFRaV KaraReterH QV the AFQeVt heFFo. DFtQRateFy thQH HaCeH a WDFF VetXorI roDVStrQK XheV eHtabFQHhQVB a AoVVeAtQoV, RaIQVB tFH 1.3 VotQAeabFy WaHter XheV broXHQVB the QVterVet.
```

Pay attention to the words `there QH a`, this could be `there is a`

Which transform the ciphertext to this :

```
iV KaAIet 14 seVt WroR FaKtoK to serCer, there is a AFieVt Iey eEAhaVBe. either rsa, CarioDs tyKes oW ShIe (SiWWie-heFFRaVV Iey eEAhaVBe), or KsI (Kre-shareS Iey) aFBorithRs AaV be DseS Wor Iey eEAhaVBe. iW rsa is DseS, theV the AFieVt BeVerates a raVSoR CaFDe AaFFeS the KreRaster seAret, eVAryKts it DsiVB the KDbFiA Iey WroR the AertiWiAate seVt by the serCer, aVS seVSs this to the serCer. both FaKtoK aVS serCer VoX haCe the ReaVs to AaFADFate the Raster seAret aVS thereWore the shareS sessioV Iey, by AoRbiViVB the KreRaster seAret Xith raVSoR CaFDes. iW SiWWie-heFFRaV is DseS as the Iey eEAhaVBe aFBorithR, the AFieVt aVS serCer seVS eaAh other their SiWWie-heFFRaVV KDbFiA CaFDes, aFFoXiVB the saRe KreRaster seAret to be AaFADFateS by both siSes. tFs 1.3 AoRKFeteFy reRoCeS the AFieVt Iey eEAhaVBe steK. it is Vo FoVBer VeeSeS thaVIs to the Rore FiRiteS set oW sDKKorteS aFBorithRs. oVFy eKheReraF SiWWie heFFRaV Iey eEAhaVBes are sDKKorteS (KFDs the RDAh Fess AoRRoVFy DseS KsI). the AFieVt VoX BDesses XhiAh AiKher sDite the serCer XiFF aAAeKt, aVS seVSs the SiWWie-heFFRaV KaraReters iV the AFieVt heFFo. DFtiRateFy this saCes a WDFF VetXorI roDVStriK XheV estabFishiVB a AoVVeAtioV, RaIiVB tFs 1.3 VotiAeabFy Waster XheV broXsiVB the iVterVet.
```

The word `serCer`, could be `server`

The word `seAret`, must be `secret`

After these two guesses, the ciphertext should look like this :

```
iV KacIet 14 seVt WroR FaKtoK to server, there is a cFieVt Iey eEchaVBe. either rsa, varioDs tyKes oW ShIe (SiWWie-heFFRaVV Iey eEchaVBe), or KsI (Kre-shareS Iey) aFBorithRs caV be DseS Wor Iey eEchaVBe. iW rsa is DseS, theV the cFieVt BeVerates a raVSoR vaFDe caFFeS the KreRaster secret, eVcryKts it DsiVB the KDbFic Iey WroR the certiWicate seVt by the server, aVS seVSs this to the server. both FaKtoK aVS server VoX have the ReaVs to caFcDFate the Raster secret aVS thereWore the shareS sessioV Iey, by coRbiViVB the KreRaster secret Xith raVSoR vaFDes. iW SiWWie-heFFRaV is DseS as the Iey eEchaVBe aFBorithR, the cFieVt aVS server seVS each other their SiWWie-heFFRaVV KDbFic vaFDes, aFFoXiVB the saRe KreRaster secret to be caFcDFateS by both siSes. tFs 1.3 coRKFeteFy reRoveS the cFieVt Iey eEchaVBe steK. it is Vo FoVBer VeeSeS thaVIs to the Rore FiRiteS set oW sDKKorteS aFBorithRs. oVFy eKheReraF SiWWie heFFRaV Iey eEchaVBes are sDKKorteS (KFDs the RDch Fess coRRoVFy DseS KsI). the cFieVt VoX BDesses Xhich ciKher sDite the server XiFF acceKt, aVS seVSs the SiWWie-heFFRaV KaraReters iV the cFieVt heFFo. DFtiRateFy this saves a WDFF VetXorI roDVStriK XheV estabFishiVB a coVVectioV, RaIiVB tFs 1.3 VoticeabFy Waster XheV broXsiVB the iVterVet.
```

If you are confident, you can guess the word `VoticeabFy` to be `noticeably`, it really depends on your vocabulary.

```
in KacIet 14 sent WroR laKtoK to server, there is a client Iey eEchanBe. either rsa, varioDs tyKes oW ShIe (SiWWie-hellRann Iey eEchanBe), or KsI (Kre-shareS Iey) alBorithRs can be DseS Wor Iey eEchanBe. iW rsa is DseS, then the client Benerates a ranSoR valDe calleS the KreRaster secret, encryKts it DsinB the KDblic Iey WroR the certiWicate sent by the server, anS senSs this to the server. both laKtoK anS server noX have the Reans to calcDlate the Raster secret anS thereWore the shareS session Iey, by coRbininB the KreRaster secret Xith ranSoR valDes. iW SiWWie-hellRan is DseS as the Iey eEchanBe alBorithR, the client anS server senS each other their SiWWie-hellRann KDblic valDes, alloXinB the saRe KreRaster secret to be calcDlateS by both siSes. tls 1.3 coRKletely reRoveS the client Iey eEchanBe steK. it is no lonBer neeSeS thanIs to the Rore liRiteS set oW sDKKorteS alBorithRs. only eKheReral SiWWie hellRan Iey eEchanBes are sDKKorteS (KlDs the RDch less coRRonly DseS KsI). the client noX BDesses Xhich ciKher sDite the server Xill acceKt, anS senSs the SiWWie-hellRan KaraReters in the client hello. DltiRately this saves a WDll netXorI roDnStriK Xhen establishinB a connection, RaIinB tls 1.3 noticeably Waster Xhen broXsinB the internet.
```

Now the text looks clearer and clearer, which make it easy to have other guesses.

`Iey` : `key`

`anS` : `and`

`no lonBer` : `no longer` (which implies that guessed words can help guessing other words)

```
in Kacket 14 sent WroR laKtoK to server, there is a client key eEchange. either rsa, varioDs tyKes oW dhke (diWWie-hellRann key eEchange), or Ksk (Kre-shared key) algorithRs can be Dsed Wor key eEchange. iW rsa is Dsed, then the client generates a randoR valDe called the KreRaster secret, encryKts it Dsing the KDblic key WroR the certiWicate sent by the server, and sends this to the server. both laKtoK and server noX have the Reans to calcDlate the Raster secret and thereWore the shared session key, by coRbining the KreRaster secret Xith randoR valDes. iW diWWie-hellRan is Dsed as the key eEchange algorithR, the client and server send each other their diWWie-hellRann KDblic valDes, alloXing the saRe KreRaster secret to be calcDlated by both sides. tls 1.3 coRKletely reRoved the client key eEchange steK. it is no longer needed thanks to the Rore liRited set oW sDKKorted algorithRs. only eKheReral diWWie hellRan key eEchanges are sDKKorted (KlDs the RDch less coRRonly Dsed Ksk). the client noX gDesses Xhich ciKher sDite the server Xill acceKt, and sends the diWWie-hellRan KaraReters in the client hello. DltiRately this saves a WDll netXork roDndtriK Xhen establishing a connection, Raking tls 1.3 noticeably Waster Xhen broXsing the internet.
```

`alloXing` : `allowing`

`algorithmR`: `algorithm`

If you know a thing or two about cryptography, you can guess that `diWWie-hellRann` be `diffie-hellmann` (typo error lmao)

`eEchanges` : `exchanges`

```
in Kacket 14 sent from laKtoK to server, there is a client key exchange. either rsa, varioDs tyKes of dhke (diffie-hellmann key exchange), or Ksk (Kre-shared key) algorithms can be Dsed for key exchange. if rsa is Dsed, then the client generates a random valDe called the Kremaster secret, encryKts it Dsing the KDblic key from the certificate sent by the server, and sends this to the server. both laKtoK and server noX have the means to calcDlate the master secret and therefore the shared session key, by combining the Kremaster secret Xith random valDes. if diffie-hellman is Dsed as the key exchange algorithm, the client and server send each other their diffie-hellmann KDblic valDes, alloXing the same Kremaster secret to be calcDlated by both sides. tls 1.3 comKletely removed the client key exchange steK. it is no longer needed thanks to the more limited set of sDKKorted algorithms. only eKhemeral diffie hellman key exchanges are sDKKorted (KlDs the mDch less commonly Dsed Ksk). the client noX gDesses Xhich ciKher sDite the server Xill acceKt, and sends the diffie-hellman Karameters in the client hello. Dltimately this saves a fDll netXork roDndtriK Xhen establishing a connection, making tls 1.3 noticeably faster Xhen broXsing the internet.
```

Keep going :

`comKletely` : `completely`

`Dsing` : `using`

`laKtoK` : `laptop`

`broXsing` : `browsing`

```
in packet 14 sent from laptop to server, there is a client key exchange. either rsa, various types of dhke (diffie-hellmann key exchange), or psk (pre-shared key) algorithms can be used for key exchange. if rsa is used, then the client generates a random value called the premaster secret, encrypts it using the public key from the certificate sent by the server, and sends this to the server. both laptop and server now have the means to calculate the master secret and therefore the shared session key, by combining the premaster secret with random values. if diffie-hellman is used as the key exchange algorithm, the client and server send each other their diffie-hellmann public values, allowing the same premaster secret to be calculated by both sides. tls 1.3 completely removed the client key exchange step. it is no longer needed thanks to the more limited set of supported algorithms. only ephemeral diffie hellman key exchanges are supported (plus the much less commonly used psk). the client now guesses which cipher suite the server will accept, and sends the diffie-hellman parameters in the client hello. ultimately this saves a full network roundtrip when establishing a connection, making tls 1.3 noticeably faster when browsing the internet.
```

We are left with 3 letters : `l`, `m` and `z`. Because the ciphertext does not appears these word, we have no idea the original letters of these, but that is not important because `100%` of the ciphertext is solved.

### Extra : From Greek to Alphabet

This is needed when I did a CTF challenge, instead of the English alphabet, it gives me a Greek alphabet :( . If you need it somehow, that's great.

## Known Plaintext Attack

If you have the ciphertext and its corresponding plaintext, you can immediately restore a good portion of the key.

For example, here are the plaintext and the ciphertext :

+ Plaintext :    `watermelonsaredelicious`
+ Ciphertext : `dzgvinvolmhzivwvorxrlfh`

You can immediately a portion of the key : `z?xwv???r??onml??ihgf?d???`
By having more pairs of the ciphertext and plaintexts, you will eventually recover all the key.

## Chosen plaintext attack

This is easy to attack, you just need to give the API the plaintext that has all the letters in the alphabet and get the corresponding ciphertext. Then it is similar to the Known-plaintext attack, only this case you can recover the full key.
Some plaintext (human-readable) that has all 26 English letters : `the quick brown fox jumps over thirteen lazy dogs`
Or if you are not fancy in these, just `abcdefghijklmnopqrstuvwxyz`

## Chosen ciphertext attack

Well this is quite similar to the Chosen-plaintext attack, so i wont talk much about this case.

