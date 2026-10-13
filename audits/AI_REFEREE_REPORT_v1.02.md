---
title: "INDEPENDENT SCIENTIFIC REFEREE REPORT — CC_CAUSAL_EXPANSION v1.02"
subtitle: "Valutazione critica indipendente del working paper cumulativo (372 pp.) e del recovery v1.02"
date: "12 ottobre 2026"
---

# INDEPENDENT SCIENTIFIC REFEREE REPORT — CC_CAUSAL_EXPANSION v1.02

**Revisore:** Claude (Anthropic; sessione configurata come `claude-opus-5-5`), revisione automatizzata senza supervisione umana durante i calcoli.
**Committente:** Pietro Risi.
**Data:** 12 ottobre 2026.
**Oggetto:** *CC_CAUSAL_EXPANSION — Causalità, luce ed espansione cosmologica*, Working Paper v1.02 (372 pagine), sorgente LaTeX e recovery `CC_CAUSAL_EXPANSION_v1.02_RECOVERY_LIGHT`.
**Allegati:** registro delle affermazioni (`..._CLAIMS_REGISTER.csv` / `.md`, 99 voci); archivio `..._REFEREE_INDEPENDENT_CHECKS.zip` con i programmi del revisore e i loro risultati.

Il rapporto non corregge il lavoro e non propone una nuova teoria: valuta che cosa è corretto, che cosa è errato, che cosa è già noto e che cosa non è dimostrato. Non ho modificato né il recovery né il paper; tutti i miei file stanno in una directory separata.

---

## 0. Ambito effettivo della revisione

La sezione va letta prima del verdetto. Le etichette sono:

- **VERIFICATO:** ricalcolato con codice mio o riderivato a mano.
- **SPOT CHECK:** ricalcolati soltanto alcuni numeri o enunciati campione.
- **LETTO:** letto criticamente, senza ricalcolo.
- **NON ESAMINATO**.

I numeri di pagina si riferiscono al PDF di 372 pagine.

| Parte del lavoro | Pagine | Livello di controllo |
|----------|--|----------|
| Integrità di ZIP, manifest, TeX e PDF | — | VERIFICATO |
| Gate R0–R7: cinematica dei due raggi, orizzonti, $\alpha$, $\beta$, tabelle ΛCDM | 21–28 | VERIFICATO (script C01) |
| R8–R12h: chiusure termodinamiche, HDE, $V_4$, kernel, Bianchi | 29–68 | VERIFICATO (C02, C03, a mano) |
| R12i–R12j: rumore tensoriale, Ward | 69–74 | LETTO |
| R12k–R12n: cumulanti, DOS esatta | 75–87 | VERIFICATO (C04 esatto; C05 Monte Carlo proprio) |
| R12o–R12x: metodi per il sign problem | 88–120 | LETTO; non ricalcolato, perché il codice non è nel recovery |
| R12y–R12ac: combinatoria esatta degli ordini 2D, concentrazione | 121–139 | VERIFICATO (C06; R12ac a livello di sketch) |
| R12ad–R12ah: proiezioni di Hoeffding, resampling | 140–164 | SPOT CHECK (solo $N=2$; identità di R12ah) |
| R12ai–R12ar | 165–191 | SPOT CHECK a mano |
| R12as–R12bb | 192–217 | LETTO integralmente; SPOT CHECK numerico (C07) |
| Roadmap, stato canonico, appendici A–J | 218–244 | LETTO; le identità di A–I sono coperte da C01–C02 |
| Bibliografia | 245–251 | 13 voci sospette o recenti controllate |
| Appendici v0.59–v0.71 (LQ…FI) | 252–291 | LETTO; SPOT CHECK esatti (C07); FI non ricalcolata |
| Appendici v0.72–v0.85 (RG, PT, LI-v0.74, PI, SP, RT, ES, GW, AP, FH, CB, SB) | 292–338 | Soltanto enunciati e verdetti: NON VERIFICATO. Eccezioni: BD e UC, verificate |
| Appendici v0.86–v0.88 (ON, RB, NK) | 339–344 | VERIFICATO (Q14) |
| Appendici v0.89–v1.02 (NC…LI): priorità del mandato | 345–372 | VERIFICATO integralmente (Q1a–Q13), con un motore QSG indipendente |
| Fonte primaria Srivastava–Surya, arXiv:2603.25503v1 | — | LETTA integralmente (HTML v1). Versione PRD pubblicata NON letta: il sito APS era protetto da una verifica anti-bot che non ho aggirato |
| Documenti di audit | — | LETTI: HANDOFF, SR strategic assessment, SR e SO referee brief, `DERIVATION_AND_LIMITS` di XL, L3, TD, P3, IR, SO, FP, BC, LI |
| Codice Python degli autori | — | Deliberatamente NON letto: tutte le verifiche sono state scritte da zero |

---

## A. Executive summary

**Che cosa è il lavoro.** Il manoscritto non è un articolo. È il registro cumulativo di circa novanta "gate", screening e appendici. Il progetto parte dall'intuizione "l'Universo si espande a $c+c$" e, attraverso chiusure termodinamiche, modelli causal-set, rumore stocastico, azioni BDG e crescita quantistica sequenziale (QSG), cerca una legge autonoma per $H(t)$. Gli autori stessi concludono che la legge non è stata ottenuta: R13 è "BLOCCATO" e nessuno dei requisiti M1–M6 è soddisfatto. Concordo con questa conclusione.

**Che cosa funziona.**

1. La matematica che ho ricalcolato è quasi sempre corretta, sia le identità sia i numeri stampati. Parlo di circa 80 affermazioni con stato PASS nel registro: cinematica FLRW, tabelle ΛCDM, chiusure entropiche, tabella DOS esatta di R12n, combinatoria esatta degli ordini 2D, screening R12at–R12bb, benchmark CSG complessi, l'intera catena QSG $2\times2$ (NC, PL, E2, XL, L3, TD, P3, IR) e i testimoni SO, FP, BC e LI.
2. L'onestà epistemica è sopra la media. I risultati negativi sono conservati, le ipotesi sono dichiarate e la promozione di risultati 2D o su sfondo fisso a gravità 4D è esplicitamente vietata e di fatto evitata.
3. Non ho trovato usi impliciti delle equazioni di Friedmann presentati come derivazioni indipendenti.

**Che cosa non funziona, o non è ciò che sembra.**

1. **Nessun risultato fisico nuovo.** La parte "c+c" (R0–R12h) consiste di identità cinematiche standard e di riformulazioni note: Cai–Kim, Padmanabhan, NADE, Tsallis/Rényi HDE. L'intuizione iniziale non contiene dinamica: un tasso di separazione $2c$ segue da qualunque $a(t)$ e non può determinarlo.
2. **MAJOR — la catena QSG XL→L3→TD→P3→IR (v0.92–v0.97) studia una famiglia già esclusa dalla fonte.** Il Teorema 3.7 di Srivastava–Surya (eq. 114/119) vale per gli operatori *gregarious* di causal set qualsiasi. Il progetto lo applica solo ai generatori di anticatena, cioè al caso particolare (120), e lo chiama "(119)".
   - Applicando la (114) della fonte a $(G(V),Q_1,Q_2)$, dove $V$ sono due minimi sotto un massimo, ottengo sull'intera curva XL il residuo $\beta(4a^2-1)/(10a^4)\,I\neq0$.
   - Applicandola a $(G(\text{catena}_2),Q_1,Q_3)$ ottengo il residuo $-4\beta u^2/(a^2-1)\,I$ sull'intera classe Hermitiana traceless non commutativa.
   - Ne segue che la conclusione di P3 è vera, anzi più forte di quanto dichiarato, ma segue da due relazioni a tre elementi. Il teorema "se e solo se" XL.3, letto con la (119) della fonte, è falso: la curva eccezionale non sopravvive.
3. **MAJOR — incoerenza nella scelta del partner di Bell (L3).** Con il partner minimale l'elemento $R_{13}$ differisce da quello della convenzione TD e non si annulla a $\beta=1$. La differenza è un'istanza della (114) che fallisce. Il progetto adotta una sola convenzione senza dimostrare che il risultato non dipende dalla scelta.
4. **Contenuto vs volume.** Due blocchi hanno contenuto scientifico molto inferiore allo spazio che occupano:
   - la metodologia numerica per il sign problem su un modello giocattolo 2D (R12m–R12x, circa 40 pagine);
   - circa 30 appendici di screening scalari CSG/BDG (v0.59–v0.85, circa 90 pagine), con risultati elementari (Burnside, non identificabilità di accoppiamenti superiori, somme dirette) o casi particolari di Surya–Zalel (2020).
5. **Domande Q-A e Q-D.** La distinzione vettori/operatori (SO, FP, BC, LI) è corretta e utile come chiarimento della fonte, ma è algebra lineare standard. LI, cioè "MSR+GC non implicano la Bell causality", è logicamente banale: la Bell causality è un assioma indipendente già nel caso classico di Rideout–Sorkin.

**Verdetto sintetico (dettagli in F).**

| Oggetto | Giudizio |
|---|---|
| Manoscritto cumulativo come articolo scientifico | **REJECT** |
| Eventuale nota ristretta sull'ostruzione QSG $2\times2$, riformulata con il Teorema 3.7 completo | **MAJOR REVISION** |
| Combinatoria esatta degli ordini 2D (R12y–R12ac) | **INSUFFICIENT EVIDENCE**: originalità non determinata, prove a livello di sketch |

Nelle parti verificate non ho trovato errori CRITICAL. La conclusione fondamentale degli autori, cioè che nessuna cosmologia autonoma è stata derivata, è corretta.

---

## B. Verifica delle affermazioni

Il registro completo (99 voci, con posizione, ipotesi, metodo e motivazione) è nel file allegato `CC_CAUSAL_EXPANSION_v1.02_CLAIMS_REGISTER.csv`/`.md`. Qui riporto le affermazioni principali.

### B.1 Tabella delle affermazioni principali

| ID | Affermazione | Pag. / eq. | Ipotesi | Stato | Metodo | Motivazione |
|----|------------|-----|-----|------|----|-------|
| PHY-1 | $\dot D = HD+(s_1-s_2)c$ | p. 23; App. A | FLRW piatta, raggi radiali | PASS | C01, SymPy | Standard |
| PHY-2 | $\dot R_p=HR_p+c$, $\dot R_e=HR_e-c$, $\dot R_H=c(1+q)$ | pp. 24–27 | FLRW | PASS | C01 | Standard |
| PHY-3 | $\alpha=n/(1-n)=2/(1+3w)$, $\alpha'=1-q\alpha$, $(\ln\beta)'=-q$ | pp. 25–28 | legge di potenza | PASS | C01 | Riformulazione |
| PHY-4 | Tabella ΛCDM $\Delta D_0$ = 0.483 / 2.662 / 7.562 / 18.243 / 32.342 Gly; $t_B(2c)=3.660$ Gyr | pp. 24–27 | $H_0=67.4$, $\Omega_m=0.315$ | PASS | C01, quadratura indipendente | Tutte le cifre |
| PHY-5 | Tassi di separazione $\ge2c$ non sono velocità locali | TeX 189–194, 460–553 | — | PASS | lettura | Distinzione esplicita e corretta |
| PHY-6 | Tracking $\alpha=1/q$ | pp. 40–46 | legge di potenza | PASS con riserva | a mano | Esatto solo per una legge di potenza che vale fino al Big Bang; altrimenti è un attrattore (MINOR-6) |
| PHY-7 | Clausius → Friedmann; $d\rho/dX=3S_A/(2\pi)$; chiusure Rényi/log/potenza | pp. 29–36 | Cai–Kim | PASS | C02 | Noto, attribuito |
| PHY-8 | $q_0=-0.5273$, $\alpha_0=3.180$, $\varepsilon_0=1.1497$, $z_{acc}=0.632$, radice $y=1.81696$ | pp. 33–39 | ΛCDM | PASS | C02 | — |
| PHY-13 | $V_4=\pi c^4t^4/[(1+p)(3+p)(1+3p)]$ | p. 57 | $a\propto t^p$ | PASS | C03 | — |
| PHY-16 | Nessun Friedmann nascosto | pp. 21–75 | — | PASS | lettura | Transizioni dichiarate "assumendo Friedmann" |
| BDY-3 | $\gamma_{spr}=1.857\;[1.840,1.875]$ | p. 82 | sprinkling 2D, $\varepsilon=0.21$ | PASS (compatibile) | C05 | Mia stima: 1.869 [1.838, 1.900] |
| BDY-4 | Tabella esatta R12n ($N=4..9$; 10/28/95/369/1750/9566 stati) | p. 85 | azione 2D smeared | PASS | C04 | Tutte le cifre; $f(n,\varepsilon)$ non definita al primo uso |
| BDY-2 | $\langle S\rangle_{cont}\sim N$ | p. 79 | — | NOT_VERIFIED | C05 | A $\beta=0$, $\langle S\rangle\approx4$ per ogni $N$ |
| BDY-6/7 | $F(z)$, $\sum f(2j)=2/(2-\varepsilon)^3$, $E[S_N]=4(1-q^N)$, $E[N_k]/N$, $E[C_N(k)]$ | pp. 121–136 | ordini 2D uniformi a $N$ fissato | PASS | C06, enumerazione esatta $N\le8$ | — |
| BDY-9 | Concentrazione tipo Efron–Stein | p. 137 | — | PASS (sketch) | a mano | Non in forma pubblicabile |
| BDY-11 | Identità di resampling | p. 162 | — | PASS | a mano | È l'operatore di rumore standard; manca l'attribuzione |
| LAT-4 | $N_{00,00}^{vac}=5.17152\times10^{-5}$, $N^{\ln3}_{00,00}=4.36419\times10^{-4}$, commutatore $1.2061\times10^{-3}$ | pp. 200–202 | 7 modi | PASS | C07, Wick e Fock indipendenti | — |
| LAT-5 | Tabelle $\mathcal C_K$ e varianze di R12aw; bound $K^{-6}$ | pp. 203–206 | — | PASS | C07 | — |
| LAT-7 | Teoremi Markov+Kraus; esempio a 5 rami, residuo ternario $117/70$ | p. 209 | — | PASS | C07 | Elementare, noto |
| LAT-8 | Testimone SJ $65/(2\sqrt{66})-1/2=3.5004734568$ | p. 211 | — | PASS | C07 | Caso particolare di Fewster–Verch |
| APP-CX/OG/CV | Tabelle $V_n$, testimoni di interferenza, $\mu(\mathcal O)$, eventi di stem | pp. 259–288 | modelli di Surya–Zalel | PASS | C07, interi di Gauss esatti | — |
| APP-ON/RB/NK | Testimoni non commutativi e loro ostruzioni | pp. 339–344 | — | PASS | Q14 | — |
| SRC-1 | Srivastava–Surya, PRD **114**, 086007 (2026), DOI 10.1103/thx5-dknv | bibliografia | — | PASS | Crossref | Pubblicato online il 7 ott. 2026 |
| SRC-3/4 | Fonte: MSR e GC operatoriali "dedotte" dai vettori | arXiv (32)–(34), (54), (74), (84), (109) | — | FAIL come inferenza | a mano | Vedi B.2, Q-A |
| SRC-5 | Fonte: (139) per $m,k<n$, ma usata con $k=n$ in (145) | arXiv (139), (145) | — | FAIL come enunciato | a mano | TD colma la lacuna correttamente |
| SRC-6 | Fonte: "ogni rappresentazione non banale ha dimensione maggiore" | abstract; (164) | — | FAIL (sovra-generalizzazione) | a mano | Test su 4 assegnazioni coordinate, già escluse da (145) |
| QSG-NC | NC.4: (130) ⇔ traccia nulla (normali, non commutanti); inverso senza normalità | p. 345 | $d=2$ | PASS | Q1a | — |
| QSG-PL | PL.3: $Q_n=\alpha_nQ_1+\beta_nQ_2$ | p. 347 | (120) con $k=1$, $m=2$ | PASS | Q1a | Etichetta "(119)" impropria |
| QSG-E2 | Esclusione della coppia storica ($\det P=34/75$, $\det T=7/25$, $\det M=-18660/34391$) | p. 349 | — | PASS | Q1a | — |
| **QSG-XL** | **XL.3: Q3 invertibile sse $b=-1/(4a)$, $u^2=(4a^2-1)/(16a^2)$, $Q_3=\beta Q_2$** | p. 351 | Hermitiani traceless non commutanti | **FAIL (MAJOR)** rispetto alla (114)/(119) della fonte; PASS solo nella lettura ristretta alla (120) | Q8, Q9, Q5, Q13 | Vedi C, MAJOR-1 |
| **QSG-L3** | L3.5 ($R_{13}$), $R_{23}=-2R_{13}$, $\det X_3$ | p. 353 | convenzione di partner TD | PASS nella convenzione; **incoerenza tra partner** (MAJOR-2) | Q2, Q10, Q4 | — |
| QSG-TD | (139) valida anche per la crescita timid ($1\le k<m\le n$) | p. 355 | GC e CPOBC operatoriali | PASS | a mano | — |
| QSG-P3 | P3.5: $D_{11}=-\tfrac{1024\,\delta\,t^3(t^2-1)^4(7t^4+46t^2+7)}{125(t^2+1)^9}$, $D_{22}=-D_{11}$ | p. 357 | poset N | PASS | Q3, motore da principi primi | — |
| QSG-P3c | Esclusa la classe Hermitiana $2\times2$ con $[Q_1,Q_2]\neq0$ (modello forte non singolare) | pp. 357–362 | vedi B.2, Q-C | PASS, più forte del dichiarato | Q3, Q5, Q13 | — |
| QSG-IR | IR.5/IR.6; assenza di radici reali; $a^2\in\{1,2,3\}$ | p. 361 | — | PASS | Q11 | — |
| QSG-SO/FP/BC | Testimoni e criteri | pp. 363–370 | — | PASS | Q11 | Algebra lineare standard |
| QSG-LI | MSR+GC non implicano CPOBC | p. 371 | — | PASS | Q11 + controesempio scalare proprio | Logicamente banale; noto |
| QSG-OPEN | Ramo $Q_2=\lambda Q_1$ con $Q_3$ non commutante | non trattato | Hermitiani $2\times2$ | OPEN QUESTION | Q6, Q7 | Vedi C |

### B.2 Risposte alle domande 4.A–4.E del mandato

#### Q-A — MSR e GC: assiomi o deduzioni?

**Nella fonte.** La MSR, eq. (32), è enunciata sui vettori, $\sum_j A_n^j|c_n\rangle=|c_n\rangle$. La (33) scrive "$\Rightarrow\sum_jA_n^j=I$". Come inferenza è invalida: da un solo vettore non nullo segue soltanto che $\sum_jA_n^j-I$ annulla quel vettore.

Lo stesso vale per la GC. È definita sui vettori ($A_\gamma|\Omega\rangle=A_{\gamma'}|\Omega\rangle$), ma nelle (54), (74), (84) e (109) è usata come identità tra operatori, dopo aver cancellato i prefissi.

**Nel modello forte le identità operatoriali sono dunque assiomi aggiuntivi.** Nella v1 di arXiv non ho trovato nessuna ipotesi esplicita di ciclicità o di vettore separante che le giustifichi. La versione PRD non è stata consultata.

**Quali ipotesi servirebbero.** Non basta che i vettori raggiunti generino lo spazio. Il testimone SO lo mostra: $A|\Omega\rangle$ e $B|\Omega\rangle$ generano $\mathbb C^2$, eppure $XA-YB=\begin{pmatrix}0&-1/8\\0&0\end{pmatrix}\neq0$, mentre $XA|\Omega\rangle=YB|\Omega\rangle$.

Il motivo è che a ogni diamante GC, con $|\Omega\rangle$ fissato, corrisponde *un solo* vincolo vettoriale. Le identità operatoriali seguono se valgono **per ogni stato iniziale di un insieme che genera $\mathcal H$**: indipendenza dallo stato, o equivalentemente uno stato iniziale fedele (criterio FP). In aggiunta, la cancellazione dei prefissi richiede che siano invertibili.

Il progetto (SO, FP) individua correttamente il punto. Ho verificato il testimone SO (autovalori di Gram $\{1/2,2\}$) e i valori FP ($\rho=\mathrm{diag}(1/5,4/5)$, $E=4/5$ e $1/80$).

#### Q-B — classificazioni $2\times2$ (v0.89–v0.94)

**Che cosa è corretto.**

- **NC.** Corretto, compreso l'inverso, che non richiede la normalità. Il controesempio non normale è corretto.
- **PL.** Corretto, ma non serve l'argomento di traccia. Il lemma di R12ax, dimostrato dagli stessi autori, garantisce che ogni famiglia $\mathrm{span}\{Q_1,Q_2\}$ soddisfi automaticamente le relazioni ternarie.
- **E2.** Corretto.
- **XL.** L'identità di traccia XL.4, la condizione XL.5 e le formule XL.7–XL.9 sono corrette. La parte "solo se" vale nella lettura ristretta: sulla superficie di traccia il gcd dei cofattori è $64a^5b^3(4ab+1)(6ab-1)$, e le altre possibilità sono escluse dalle ipotesi.
- **TD.** Corretto per $1\le k<m\le n$.

**Che cosa non è corretto: la restrizione degli indici della (119).** Il Teorema 3.7 della fonte recita testualmente:

> "Suppose that $\hat G_n,\hat G_k,\hat G_m$ are gregarious transition operators corresponding to gregarious transition from causal sets $c_n,c_k$ and $c_m$ respectively, where $m\neq n$ and $k<\min\{m,n\}$."

La (120) è il caso particolare $\hat Q_n\hat Q_k^{-1}\hat Q_m=\hat Q_m\hat Q_k^{-1}\hat Q_n$. Il progetto (TeX 11795–11802, 11922–11934) usa soltanto questo caso particolare e lo chiama "(119)".

Le esclusioni di parametri non nascondono soluzioni valide; semmai è vero il contrario. La curva XL, presentata come sopravvissuta alle condizioni necessarie, non lo è (vedi C, MAJOR-1).

#### Q-C — ostruzione P3

Ho ricostruito l'ostruzione da principi primi con un motore indipendente (`Q_engine.py`), costruito così:

- generatori liberi $Q_n$ per le anticatene;
- CPOBC con partner di Bell minimale: $\mathrm{Op}(c,S)=T(S)\,G(c)\,G(S)^{-1}$;
- operatori timid ottenuti dalla MSR operatoriale;
- operatori gregarious per atomizzazione, secondo la (111);
- ordine dei prodotti preservato e memoizzazione sulle classi di isomorfismo di (poset, downset).

**Autotest.** Con scalari commutanti la GC vale per $N=3,4,5$ (5, 16 e 63 classi; 7, 40 e 357 storie) e la MSR somma a 1. Il motore riproduce l'eq. (22) di Rideout–Sorkin. Nell'eq. (22) della fonte c'è un refuso: $Q_{\varpi-m}$ va letto $Q_{\varpi-k}$.

**Controlli puntuali.**

- *Poset.* È il poset N: $x<y$, $x<w$, $z<w$. I due cammini (prima $y$, prima $w$) coincidono con quelli di P3.3.
- *Risultato.* La differenza dei due cammini riproduce **esattamente** P3.5, $D_{22}=-D_{11}$ compreso.
- *Denominatori.* $(t^2+1)^9$ e $t^2\pm4t+1$ (cioè $a^2=1$) sono esclusi dalle ipotesi.
- *Fattori.* $7t^4+46t^2+7$ non ha radici reali, e nemmeno il $p(t)$ di IR.
- *Corrispondenza $a^2\in\{1,2,3\}$.* $a^2=1$ ⇔ $(t^2-4t+1)(t^2+4t+1)=0$; $a^2=2$ ⇔ $t^4-30t^2+1=0$; $a^2=3$ ⇔ $t^4-46t^2+1=0$. Tutte verificate.

**Classe esclusa (ottengo la stessa esclusione con un certificato più breve).** Si tratta della CPOBC non singolare nel modello forte (operatoriale), con:

- dimensione $d=2$;
- $Q_1,Q_2$ Hermitiani invertibili con $[Q_1,Q_2]\neq0$, e quindi traceless per NC;
- assenza di fasi nella GC e ordinamento CPOBC.

Già due istanze del Teorema 3.7 a livello di tre elementi, cioè $(G(V),Q_1,Q_2)$ e $(G(K_2),Q_1,Q_3)$, insieme alla (145), escludono ogni $Q_3$ invertibile.

**Classi non escluse dal progetto, né da me.**

- operatori normali non Hermitiani, per esempio $e^{i\varphi}H$;
- operatori non normali;
- dimensione $d\ge3$;
- dinamiche singolari;
- la formulazione debole, cioè vettoriale, tramite il funzionale di decoerenza;
- la GC con fasi;
- gli altri ordinamenti di Bell;
- **il ramo $[Q_1,Q_2]=0$, $Q_2=\lambda Q_1$ con $Q_3$ non commutante.** In questo ramo l'algebra generata *è* non commutativa e tutte le condizioni di livello 3 valgono identicamente: GC sulle 40 storie con $N=4$, atomizzazione e indipendenza dal partner (Q6). Al livello 4, per un'istanza razionale di $Q_3$, le 122 condizioni lineari di indipendenza dal partner forzano $Q_4=0$ (Q7, base di Gröbner). Il ramo è dunque probabilmente escluso al livello 4, ma non è dimostrato. Il termine "non commutativo" nei riassunti del progetto (MS, SR, HANDOFF) è quindi ambiguo (MINOR-3).

#### Q-D — SO, FP e il fallimento CPOBC (v0.98–v1.02)

Le tre parti sono matematicamente corrette:

- SO: tutte le matrici, $A+B=\mathrm{diag}(1,2)$, i 6 determinanti;
- FP: $\rho$, $E_\rho$;
- BC: $R_{cat}$, $R_{anti}$, norme $37/64$ e $493/64$, somma dei 7 amplitudi terminali uguale a $\Omega$.

Le implicazioni fisiche sono modeste. SO e FP sono esempi di un fatto elementare: un'identità tra operatori non è determinata dal suo valore su un insieme non separante. BC e LI mostrano che il testimone SO viola la CPOBC e che MSR+GC non implicano CPOBC. Che la Bell causality sia indipendente dalle altre condizioni è noto dal caso classico di Rideout–Sorkin (1999): basta il mio controesempio scalare con $d=1$ ($q_1=1/2$, $W=Y=X=1/4$, $U=1/2$, $U'=1/4$).

Il contributo reale di questo blocco è un chiarimento utile della fonte su Q-A, non un risultato nuovo.

#### Q-E — trasformazioni illegittime in teoremi universali

Il progetto in genere delimita bene i propri risultati: R12ay, ON, RB, NK, P3, BC e LI sono tutti dichiarati circoscritti. Le eccezioni che ho trovato sono tre:

1. l'enunciato XL.3 "se e solo se", dove la (119) è etichettata impropriamente (MAJOR-1);
2. l'aggettivo "non commutativo" nei riassunti, che fa sembrare escluso più di quanto lo sia (MINOR-3);
3. la sovra-generalizzazione nell'abstract della **fonte** sulle rappresentazioni di Pauli. Il progetto non la adotta: a p. 361 scrive correttamente che la fonte "documenta una propria ostruzione per alcune rappresentazioni di Pauli, non una classificazione universale".

### B.3 Fondamenti fisici (sezione 3 del mandato)

- **"c+c".** Per due fronti opposti emessi nello stesso evento si ha $\dot D=HD+2c$, e la separazione propria può crescere a $2c$ o più. Il paper distingue correttamente questi tassi, che dipendono dalla foliazione, dalle velocità locali, che valgono $c$ (TeX 189–194). È cinematica di qualunque FLRW: vale per ogni $a(t)$ e quindi **non può selezionare $a(t)$**. L'intuizione iniziale non contiene una legge fisica nuova, e il progetto lo riconosce.
- **Orizzonti, $H$, $q$.** Tutte le identità sono standard e verificate (C01).
- **Chiusure termodinamiche ed entropiche (R8–R12e).** Sono riformulazioni corrette e attribuite di Cai–Kim (2005), Cai–Cao–Hu (2008), Padmanabhan (2012), NADE e Tsallis/Rényi/Barrow HDE. Con l'entropia d'area restituiscono Friedmann. Con entropie non additive danno le equazioni di Friedmann modificate note in letteratura. Nessuna previsione verificabile nuova.
- **Causal set, rumore, BDG (R12f–R12bb).** I risultati sono identità esatte su modelli finiti, diagnostiche 2D o controlli su sfondo fisso. Il trasferimento alla gravità 4D è correttamente negato dagli autori.
- **Uso implicito di Friedmann.** Non trovato. Le transizioni condizionate sono dichiarate.

---

## C. Errori e criticità

### CRITICAL

Nessuno, nelle parti verificate (vedi sez. 0). Non escludo errori nelle parti marcate NOT_VERIFIED, in particolare v0.72–v0.85 e R12o–R12x.

### MAJOR

**MAJOR-1 — Teorema 3.7 della fonte applicato in forma ristretta; XL.3 è falso nella sua forma enunciata.**
*Posizione:* PL (p. 347, TeX 11795–11810), XL (p. 351, TeX 11922–11934); di conseguenza L3, TD, P3, MS e IR (pp. 353–362).

La fonte enuncia la (114)/(119) per operatori gregarious di causal set $c_n,c_k,c_m$ arbitrari, con $m\neq n$ e $k<\min\{m,n\}$. La dimostrazione usa la CPOBC (115)–(117) tra transizioni di genitori diversi che hanno lo stesso genitore ridotto. Il progetto impone soltanto il caso (120) sulle anticatene e lo chiama "(119)". Uso le formule della fonte riprodotte dal progetto: $T=A_2^{(2)}=I-2(I-Q_1)Q_2Q_1^{-1}-Q_2$ (141), $G(V)=T\,Q_3\,T^{-1}$ (159), $G(K_2)=(I-Q_1)Q_2(I-Q_1)^{-1}$ (142), con $Q_3=\alpha Q_1+\beta Q_2$.

1. **$(G(V),Q_1,Q_2)$, con $n=3$, $k=1$, $m=2$: ipotesi letterali soddisfatte.** Il residuo è diagonale, con elementi
   $$\frac{4u^2\,(3a^2\alpha-8ab\alpha+4ab\beta-10b^2\beta+6\beta u^2)}{a^2b^2+9a^2u^2-a^2+4ab-4b^2-4u^2}.$$
   Sulla curva XL, con $Q_3=\beta Q_2$, il residuo vale
   $$\frac{\beta(4a^2-1)}{10a^4}\,I\neq0\qquad(|a|>1/2,\ \beta\neq0).$$
2. **$(G(K_2),Q_1,Q_3)$, con $n=2$, $k=1$, $m=3$.** Il residuo vale $-4\beta u^2/(a^2-1)\,I$ sull'intera classe Hermitiana traceless non commutativa, quindi forza $\beta=0$.
   - Combinato con il punto 1 dà $\alpha\,a(3a-8b)=0$.
   - Combinato con la (145), cioè con XL.4–XL.9 (fuori dalla superficie di traccia non esiste alcun $Q_3$ invertibile; sulla superficie $E_A\neq0$ impone $\alpha=0$), esclude ogni $Q_3$ invertibile.
3. **Controllo in sole frazioni (Q13), nel punto $t=3$ usato dagli autori ($a=5/6$, $b=-3/10$, $u=2/5$).** La (145) nella forma XL.2 ha residuo $0$. I due residui del Teorema 3.7 valgono $\tfrac{1152}{3125}I$ e $\tfrac{576}{275}I$, in accordo con le formule simboliche.

*Conseguenza.* La conclusione di P3 è corretta, ma la catena v0.92–v0.97 (circa 12 pagine, più cinque gate di audit) studia un insieme che la (114) della fonte esclude già. L'"iff" di XL.3 è vero solo se si sostituisce "(119)" con "(120)".

*Riserva.* Il risultato presuppone che la CPOBC sia imposta tra *tutte* le coppie di transizioni Bell-correlate, come nella dimostrazione (115)–(117) della fonte, e non soltanto tra ciascuna coppia e il suo genitore ridotto. Se il progetto adotta deliberatamente la versione debole, deve dichiararlo, spiegare perché e notare che, in quella versione, il Teorema 3.7 della fonte non è più disponibile neppure per i generatori $Q_n$. In entrambi i casi l'attuale formulazione è incoerente.

**MAJOR-2 — dipendenza dalla scelta del partner di Bell (L3).**
*Posizione:* L3, p. 353; TD, p. 355.

Il gate L3 calcola gli operatori di livello 3 con il partner "adiacente per stadio" della convenzione TD. Con il partner minimale, che rimuove tutti gli spettatori come nella (107), ottengo:

- lo stesso $R_{23}$;
- un $R_{13}$ diverso, che non si annulla a $\beta=1$.

La differenza coincide con il residuo della (114) per $(G(c_2),Q_1,Q_3)$, dove $c_2$ è un'anticatena di tre elementi con un massimo sopra tutti. Sul locus vale
$$\frac{16\,\delta\,t^2(t^2-1)^2}{3(t^2+1)^4}\,I\neq0.$$

Se la CPOBC vale per tutte le coppie Bell-correlate, le due scelte devono coincidere. Che non coincidano è un'ulteriore ostruzione, non una libertà di convenzione. Il progetto non discute l'indipendenza dal partner.

**MAJOR-3 — rapporto contenuto/volume e struttura del manoscritto.**
Il documento è un registro di laboratorio (372 pagine, circa 90 gate). Molte decine di pagine ripetono le stesse clausole ("R12bc NON APERTO; R12as fisico NON AUTORIZZATO; R13 BLOCCATO"). I risultati originali potenziali sono pochi e sepolti. Così com'è, il manoscritto non è valutabile come articolo.

**MAJOR-4 — riproducibilità del recovery "light".**
Il recovery contiene il codice dei soli gate R12bb recenti. Per R12m–R12ah (DOS, sprinkling, sign problem, proiezioni di Hoeffding) e per i gate precedenti il codice manca, quindi molte affermazioni numeriche non sono ripetibili dal pacchetto consegnato. Io le ho ripetute in parte con codice mio (C04, C05, C06). La funzione $f(n,\varepsilon)$ usata in R12m/R12n non è definita nel testo prima di R12y (p. 121). L'ho ricostruita come azione 2D smeared standard e riproduce tutte le cifre di R12n, il che conferma l'ipotesi.

**MAJOR-5 — esplorazione oltre il contenuto scientifico.**
Tre blocchi, dettagliati in F.3, occupano molto più spazio di quanto contengano: R12m–R12x (metodi per il sign problem su un modello 2D), v0.59–v0.85 (screening scalari) e XL–IR (vedi MAJOR-1).

### MINOR

1. **Provenienza del PDF.** Il PDF inviato al revisore (sha256 `cf803491…`, 4.52 MB) non coincide né con il canonico del recovery (`e8b05f67…`) né con la ricompilazione dichiarata (`dea42cf3…`). Testo e pagine campione sono identici. È un terzo binario non registrato nell'audit.
2. **Etichette duplicate.** "R12bb-LI" indica due gate diversi: v0.74, saturazione degli intervalli (p. 300), e v1.02, indipendenza logica (p. 371). Anche i tag LI.1–LI.3 si sovrappongono.
3. **Ambiguità di "non commutativo".** Nei riassunti (MS, SR, HANDOFF) il dominio escluso è $[Q_1,Q_2]\neq0$, non "algebra non commutativa". Vedi il ramo aperto in Q-C.
4. **Tabella "Cosa è già noto" obsoleta.** A p. 148 (TeX 5181–5357) si ferma a R12aj "PROSSIMO" e non contiene i gate QSG.
5. **Attribuzioni mancanti.** L'identità di resampling di R12ah è l'identità standard dell'operatore di rumore (per esempio O'Donnell, *Analysis of Boolean Functions*, 2014). Il lemma di R12ax e i teoremi di R12ay sono elementari e andrebbero presentati come tali.
6. **Teorema di tracking.** $\alpha=1/q$ è esatto solo per una legge di potenza che vale fino al Big Bang; in generale è un attrattore.
7. **R12l.** Lo schema $\langle S\rangle_{cont}\sim N$ non è sostenuto nel regime $\beta=0$: misuro $\langle S\rangle\approx4$ per $24\le N\le96$ (C05).
8. **Bibliografia incompleta.** Fazlollahi (2022) è citato solo come arXiv, ma è pubblicato su EPJC (2023). Due voci (Zadeh 2018, Gizbert-Studnicki 2024) non sono state confermate da me.
9. **Ridondanze.** L'argomento di traccia di PL.2 è reso superfluo dal lemma di R12ax.
10. **Paternità.** Il frontespizio accredita "ChatGPT, OpenAI (supporto matematico e redazionale)". Le principali riviste non accettano sistemi di IA come autori; il contributo va dichiarato nei metodi o nei ringraziamenti.

### OPEN QUESTIONS

1. Quale versione della CPOBC si adotta: tutte le coppie Bell-correlate, o solo coppia ↔ genitore ridotto? La risposta determina la validità del Teorema 3.7, e quindi sia MAJOR-1 sia MAJOR-2.
2. Il ramo Hermitiano $Q_2=\lambda Q_1$ con $Q_3$ non commutante è escluso al livello 4 per ogni $Q_3$? Un'istanza dice sì.
3. Esistono rappresentazioni non singolari con $d=2$ non Hermitiane (normali o non normali) compatibili con (114), (130), (139) e (145)? E con $d\ge3$?
4. Le ostruzioni di tipo P3 sopravvivono nella formulazione debole, cioè vettoriale o con funzionale di decoerenza, che è quella fisicamente rilevante?
5. Le formule a $N$ fissato di R12y–R12ab per gli ordini 2D casuali sono note? Vedi E.

---

## D. Verifiche indipendenti

Tutti i programmi sono miei, scritti senza consultare il codice degli autori, e sono nell'archivio allegato (`indep/`, con `README`). Ambiente: Python 3, SymPy, NumPy, SciPy; aritmetica esatta (`Fraction`, interi di Gauss, SymPy) dove possibile.

| Script | Oggetto | Metodo (diverso da quello degli autori, quando possibile) | Esito |
|--|------|-------|-----|
| C01 | Cinematica FLRW, tabelle ΛCDM, esempio di sorgente lontana | SymPy simbolico; quadratura su $t(a)$ con sostituzione $u=1/a$ per le code | Tutte le cifre stampate riprodotte |
| C02 | Mappa entropia → Friedmann, chiusure, $q_0$, $z_{acc}$ | Integrazione simbolica | PASS |
| C03 | Toy simmetrico, $V_4$, $\Omega_{rms}$, kernel di lente | SymPy + root finding | PASS |
| C04 | Tabella esatta R12n ($N=4..9$) | Enumerazione completa delle permutazioni, con $f(n,\varepsilon)$ standard | PASS, tutte le cifre |
| C05 | $\gamma_{spr}$ di R12m | Sprinkling proprio, 6000 campioni per $N$, bootstrap | 1.869 [1.838, 1.900] contro 1.857 [1.840, 1.875]: compatibile |
| C06 | Identità esatte di R12y–R12ab | Serie, enumerazione esatta $N=2..8$ | PASS |
| C07 | R12at–R12bb e appendici v0.59–v0.81 | Wick analitico ridotto a 2 modi collettivi + Fock indipendente; enumerazione dei poset naturalmente etichettati per downset ($1,2,7,40,357,4824$); interi di Gauss esatti; Burnside | PASS su tutti i numeri campione |
| T0 + `Q_engine` | Motore QSG forte da principi primi | Classi di poset, atomizzazione, partner minimale | Autotest PASS (GC, MSR, RS eq. 22) |
| Q1a | NC, PL, E2 | Simbolico | PASS |
| Q2, Q10 | L3 | Formule dirette | PASS, nella convenzione TD |
| Q3 | P3.5 | Motore, cammini nel poset N | PASS esatto |
| Q4 | Teorema 3.7 sul locus; partner | Motore | **Discrepanze**: MAJOR-1, MAJOR-2 |
| Q5 | Teorema 3.7 sull'intera classe | Formule della fonte (141), (142), (159) | **Residui non nulli**: MAJOR-1 |
| Q6, Q7 | Ramo $Q_2=\lambda Q_1$ | Motore; Gröbner | OPEN (livello 3 libero; un'istanza di livello 4 dà $Q_4=0$) |
| Q8, Q9 | XL: minori e "solo se" | Minori aggiugati; gcd sulla superficie di traccia | PASS (lettura ristretta) |
| Q11 | IR, SO, FP, BC, LI | Simbolico; controesempio scalare | PASS |
| Q12 | AC, SF | Simbolico; Bézout mod 13 | PASS |
| Q13 | Teorema 3.7 in sole frazioni nel punto $t=3$ | Matrici $2\times2$ su $\mathbb Q$ | Residui $1152/3125\,I$ e $576/275\,I$; (145) $=0$ |
| Q14 | ON, RB, NK | SymPy su $\mathbb Q(\sqrt{21})$ | PASS |

**Discrepanze trovate.**

1. MAJOR-1: Teorema 3.7 contro XL.
2. MAJOR-2: partner minimale contro partner TD.
3. Piccola differenza in $\gamma_{spr}$, entro gli intervalli di confidenza.

Non ho trovato numeri stampati errati nelle parti verificate.

**Controlli a mano.** Ho rifatto a mano la derivazione TD della (139) per $1\le k<m\le n$; i teoremi di R12ay; ON.1; l'identità R12ah; le proiezioni di Hoeffding con $N=2$; gli integrali di R12ac; BD.3 ($1-9+16-8=0$); UC.2 e UC.5; i bound OG.5, FN.7 e NS.8.

**Limiti.**

- Non ho rieseguito: le simulazioni numeriche di R12o–R12x; il censimento FI a $N=7$; i casi di LQ con $m=7,8$; le simulazioni di G4; le appendici v0.72–v0.85 (salvo BD e UC).
- La versione pubblicata (PRD) della fonte non è stata letta.

---

## E. Valutazione dell'originalità

Categorie: **ORIGINALE / NOTO / CASO PARTICOLARE / NON DETERMINATA**. La ricerca bibliografica è stata fatta con ricerca web e Crossref, non con banche dati specialistiche complete, quindi **non è esaustiva**. I riferimenti di confronto che non ho controllato io stesso (per esempio Cai–Kim, Cai–Cao–Hu, Padmanabhan, Hu–Verdaguer, Hollands–Wald, Fewster–Verch) sono ripresi dalla bibliografia del paper e sono lavori standard del settore.

| Blocco | Classificazione | Riferimenti di confronto |
|-------|-----|-------|
| Cinematica "c+c", orizzonti, $\alpha$, $\beta$ (R0–R7) | NOTO | Testi standard di cosmologia; il paper stesso |
| Chiusure termodinamiche ed entropiche (R8–R11) | NOTO | Cai & Kim, JHEP 02 (2005) 050; Cai, Cao & Hu, JHEP 08 (2008) 090; Padmanabhan (2012); Fazlollahi, EPJC (2023) |
| NADE/THDE con orizzonte di particella (R12–R12c) | CASO PARTICOLARE | Tsallis HDE, per es. Zadeh et al. (2018), non confermato; Das, PRD 113, 123531 (2026), DOI 10.1103/52nb-z52f |
| $V_4$ del cono passato; kernel di sovrapposizione (R12f–g) | NON DETERMINATA, probabilmente noto | — |
| Ostacolo Bianchi/unimodulare (R12h) | NOTO | Jirousek, arXiv:2301.01662; Buchmüller & Dragon, arXiv:2203.15714 |
| Formule esatte a $N$ fissato per l'azione BD 2D su ordini casuali (R12y–R12ab) | **NON DETERMINATA** | Glaser & Surya, PRD 88, 124026 (2013), arXiv:1309.3403 (abbondanze di intervalli, ensemble di Poisson); Benincasa, Dowker & Schmitzer, CQG 28 (2011) 105018; Glaser, O'Connor & Surya (2018); Surya (2012). Le formule a $N$ fissato potrebbero essere nuove, ma va verificato con specialisti |
| Concentrazione Efron–Stein e Hoeffding (R12ac–ah) | Tecnica NOTA; applicazione NON DETERMINATA | O'Donnell (2014) per l'identità di resampling |
| Percolazione transitiva e complessa (R12al–ap) | NOTO / CASO PARTICOLARE | Rideout & Sorkin, PRD 61, 024002 (1999); Dowker, Johnston & Surya, J. Phys. A 43, 505305 (2010), arXiv:1007.2725 |
| Free field: noise, Ward, Wick (R12au–aw) | NOTO | Hu & Verdaguer (2008); Hollands & Wald (2001) |
| Lemma ternario a due generatori (R12ax) | NON DETERMINATA (elementare) | — |
| Doppia normalizzazione Markov–Kraus (R12ay, ON) | NOTO (algebra lineare elementare) | — |
| Restrizione dello stato SJ (R12az) | CASO PARTICOLARE | Fewster & Verch (2012) |
| CDT a volume fissato (R12ba) | NOTO | Ambjørn–Loll; Glaser–Loll |
| Sottoclasse bipartita BDG (R12bb, LQ, CP, QP) | NOTO / elementare; QP NON DETERMINATA | Kleitman–Rothschild; Loomis & Carlip (2018); Carlip, GRG 56, 95 (2024) |
| CSG complesse estendibili (CX, OG, FN, NS, DS, CV) | CASO PARTICOLARE | Surya & Zalel, CQG 37, 195030 (2020), arXiv:2003.11311 |
| Diagnostica geometrica $r$, $H$, $N_k$ (G4) | NOTO | Myrheim–Meyer; Glaser & Surya (2013) |
| Degenerazione BDG (BD, ES) | NOTO / elementare | — |
| Classificazione QSG $2\times2$ (NC, PL, E2, XL, L3, TD, P3, IR) | **CASO PARTICOLARE** del quadro di Srivastava–Surya. Le classificazioni specifiche non sono nella fonte, ma sono in gran parte superate dal Teorema 3.7 (MAJOR-1). TD è un complemento legittimo alla fonte | Srivastava & Surya, PRD 114, 086007 (2026) |
| Vettori vs operatori (SO, FP) | NOTO in sostanza (stato fedele / vettore separante); utile come osservazione sulla fonte | — |
| Indipendenza della Bell causality (LI) | NOTO | Rideout & Sorkin (1999) |

**Conclusione.** Nessun risultato è classificabile con sicurezza come ORIGINALE e significativo. I candidati più plausibili a un contributo nuovo sono due:

1. le formule esatte a $N$ fissato di R12y–R12ab, con la concentrazione di R12ac;
2. una nota sull'ostruzione QSG $2\times2$, riformulata con il Teorema 3.7 completo, che includa la discussione vettori/operatori di SO e FP.

Entrambi richiedono una verifica bibliografica specialistica che non ho potuto completare.

**Bibliografia controllata.**

- Confermate via Crossref: Das 2026, Carlip 2024, Moradi–Yazdi–Zilhão 2025 (rivista, volume e anno), Srivastava–Surya 2026.
- Confermata via Imperial Spiral: Dowker 2021, Boundary.
- Esistenza su arXiv confermata: Asvar 2026, Glaser 2023/24, Das–Nasiri–Yazdi I/II, Jirousek, Buchmüller–Dragon, Machet–Wang, Surya–Zalel.
- Non confermate: Zadeh 2018, Gizbert-Studnicki 2024; per Machet–Wang il numero di articolo.

---

## F. Valutazione della pubblicabilità e della validità fisica

### F.1 Requisiti M1–M6

| Req. | Contenuto | Stato secondo il revisore | Motivazione |
|-|----|-----|------|
| M1 | Spazio delle storie, misura/stato quantistico | **MANCANTE** per un candidato del progetto; esistente solo per benchmark noti | Le misure complesse estendibili (CX, OG, NS) replicano la classe di Surya–Zalel; per la QSG operatoriale non commutativa non esiste costruzione |
| M2 | Selezione indipendente della dinamica | **MANCANTE** | Dimostrata anzi la non identificabilità a orizzonte finito (FN, NS), che è banale; nessun principio di selezione |
| M3 | Markov, covarianza e Bell causality globali | **MANCANTE** in regime non commutativo; presente solo per classi scalari, quindi commutative | P3 e MAJOR-1 escludono il caso Hermitiano $2\times2$ |
| M4 | Sorgente conservata, noise/risposta dalla microfisica | **PARZIALE** solo su sfondo fisso (R12au–aw, materia libera); gravitazionale **MANCANTE** | — |
| M5 | Limite Lorentziano $3+1$ dinamico | **MANCANTE** | — |
| M6 | $H(z)$ autonoma, verificabile, non adattata | **MANCANTE** | R13–R16 bloccati, correttamente |

Concordo con il registro MS degli autori (p. 359). Il mancato raggiungimento di M1–M6 non rende errate le singole dimostrazioni, che ho valutato separatamente in B.

### F.2 Giudizio

**Manoscritto cumulativo v1.02: REJECT.**

- Non contiene un risultato fisico nuovo: la parte cosmologica è una riformulazione di teoria nota, e gli autori stessi riconoscono che la dinamica non è stata derivata.
- I risultati matematici, in genere corretti, sono per lo più elementari o casi particolari di lavori pubblicati.
- Il principale filone tecnico non banale, XL–IR, è superato da un certificato a tre elementi ricavabile dalla stessa fonte (MAJOR-1).
- Il formato è quello di un quaderno di laboratorio di 372 pagine (MAJOR-3).

Il giudizio riguarda la pubblicabilità, non l'onestà o la cura del lavoro, che sono evidenti.

**Articolo ristretto A: nota sulla QSG $2\times2$ con CPOBC operatoriale — MAJOR REVISION, se riscritto.** Condizioni minime:

1. dichiarare la versione della CPOBC adottata;
2. usare il Teorema 3.7 completo e il certificato breve;
3. trattare il ramo $Q_2=\lambda Q_1$ e almeno le classi normali non Hermitiane;
4. includere la discussione vettori/operatori (SO, FP) come limite di validità.

Il formato adatto sarebbe un *comment* o una *short note* in relazione a Srivastava–Surya. Il contributo resterebbe modesto.

**Articolo ristretto B: valori attesi esatti dell'azione BD 2D su ordini casuali a $N$ fissato, con concentrazione — INSUFFICIENT EVIDENCE.** L'originalità non è determinata, la dimostrazione di R12ac è a livello di sketch e manca il confronto con la letteratura citata in E.

**Articolo ristretto C: l'ipotesi "c+c" come risultato fisico — REJECT.** Si tratta di cinematica standard.

### F.3 Roadmap: alternative trascurate e direzioni sovra-esplorate

**Sovra-esplorate.**

- R12m–R12x: una dozzina di gate e circa 40 pagine di metodologia per il sign problem su un modello 2D di piccole dimensioni. Il collegamento con la cosmologia 4D non è mai stabilito, e R12w ha richiesto una "interpretazione corretta" a posteriori.
- v0.59–v0.85: circa 27 appendici di screening scalari che si chiudono tutte con "R13 BLOCCATO". Molte confermano proprietà banali (non identificabilità di accoppiamenti superiori, somme dirette di rango 2, Burnside) o replicano Surya–Zalel.
- XL–IR: vedi MAJOR-1.
- SO–LI: domanda pertinente, risposte standard; LI è logicamente banale.

**Trascurate.**

1. La formulazione debole della QSG: Bell causality sulla misura quantistica e sul funzionale di decoerenza, invece che su identità operatoriali. È il livello fisicamente rilevante e quello su cui SO e FP mostrano che le identità operatoriali non sono obbligate.
2. Un trattamento algebrico sistematico, con decomposizione primaria o Gröbner, dell'insieme completo delle relazioni necessarie ai livelli 2–4 per $2\times2$ generali (anche non Hermitiane) e per $3\times3$, invece di un'esplorazione gate per gate di singole famiglie.
3. Le rappresentazioni di dimensione superiore suggerite dalla fonte.
4. Sul versante cosmologico, il confronto con la fenomenologia causal-set esistente e testabile. L'Everpresent Λ, con le sue verifiche osservative di Das, Nasiri e Yazdi (2023–24), è citato ma non sviluppato. Resta comunque il fatto che derivare $H(t)$ da una microdinamica causal-set è un problema aperto dell'intero campo.

---

## G. Raccomandazioni

L'ordine segue l'importanza scientifica e la dipendenza logica.

1. **Fissare gli assiomi (prerequisito di tutto il ramo QSG).** Dichiarare se MSR e GC sono assiomi operatoriali, cioè il modello forte, o identità vettoriali. Dichiarare se la CPOBC vale tra tutte le coppie Bell-correlate o solo verso il genitore ridotto, e se la GC ammette fasi. Da queste scelte dipendono la validità del Teorema 3.7 e i punti 2–4.
2. **Correggere XL.** Applicare il Teorema 3.7 nella generalità della fonte, sostituire la catena XL–L3–TD–P3–IR con il certificato a tre elementi (sez. C, MAJOR-1) e correggere l'etichetta "(119)" in "(120)". Ritirare o riformulare l'"iff" di XL.3.
3. **Trattare l'indipendenza dal partner di Bell** come condizione di consistenza necessaria (MAJOR-2), e in generale verificare la coerenza tra tutte le scelte di partner e di atomizzazione.
4. **Delimitare esattamente il dominio escluso.** Chiudere, o dichiarare aperto, il ramo $Q_2=\lambda Q_1$; trattare le classi normali non Hermitiane; sostituire "non commutativo" con "$[Q_1,Q_2]\neq0$".
5. **Valutare la formulazione debole.** Se le identità operatoriali non hanno una motivazione fisica indipendente, studiare la Bell causality sul funzionale di decoerenza. È l'unica direzione del ramo QSG con potenziale significato fisico.
6. **R12y–R12ac.** Prima di qualsiasi stesura, fare una ricerca bibliografica specialistica (vedi E) e scrivere dimostrazioni complete. Pubblicare eventualmente come nota combinatoria autonoma, senza pretese cosmologiche.
7. **Sospendere:**
   - le simulazioni per il sign problem (R12m–x);
   - nuovi screening scalari CSG/BDG;
   - nuovi "gate" il cui unico esito possibile è confermare "R13 BLOCCATO";
   - la linea "c+c" come ipotesi fisica, che può restare come introduzione didattica.
8. **Igiene del manoscritto e del recovery:**
   - separare il registro di audit dall'articolo;
   - rendere univoche le etichette dei gate;
   - aggiornare "Cosa è già noto";
   - definire $f(n,\varepsilon)$ al primo uso;
   - completare la bibliografia;
   - includere nel recovery il codice di ogni affermazione numerica;
   - registrare l'hash di ogni PDF distribuito;
   - dichiarare il contributo dei sistemi di IA secondo le politiche editoriali.

---

### Appendice al rapporto: integrità del materiale

| Oggetto | SHA-256 (prefisso) | Esito |
|---|---|---|
| `RECOVERY_LIGHT.zip` | `b44dc6af…` (= sidecar) | OK; CRC OK; 545 membri |
| Manifest `CHECKS/SHA256SUMS.txt` | — | 544/544 OK |
| `SOURCE/…v1.02.tex` = TeX caricato | `45a42743…` | identici |
| `PAPER/…v1.02.pdf` (canonico) | `e8b05f67…` | = `pdf_canonical_sha256` di POSTPACK_AUDIT |
| PDF caricato separatamente | `cf803491…` | ≠ canonico e ≠ ricompilazione `dea42cf3…`; testo identico (MINOR-1) |

*Fine del rapporto.*
