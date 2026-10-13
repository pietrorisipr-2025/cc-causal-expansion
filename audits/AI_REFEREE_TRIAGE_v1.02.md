# CC_CAUSAL_EXPANSION — Verifica critica del rapporto Claude, 13 ottobre 2026

**Stato:** `MAJOR_1_CONFIRMED; MAJOR_2_NECESSARY_CONSISTENCY_FAILURE_CONFIRMED; CANONICAL_v1.02_UNCHANGED`.

**Tipo di verifica:** secondo audit AI, autonomo rispetto ai programmi del progetto e di Claude per i certificati riportati sotto. Non è peer review umana, non è una valutazione di originalità esaustiva, non è un controllo integrale delle 372 pagine del paper.

## Materiale esaminato

- `CC_CAUSAL_EXPANSION_v1.02_RECOVERY_LIGHT.zip` (canonico v1.02; SHA-256 `b44dc6af6ff7c546cdf41ba7391b1c6b115abd6022189a9d7690617e68de4d9d`), 545 file, CRC PASS, manifest 544/544 PASS in questa sessione.
- `CC_CAUSAL_EXPANSION_v1.02_REFEREE_INDEPENDENT_CHECKS.zip` (SHA-256 `2a15823fc3fbcfa856b77cfc45156321a1ab66aa6c3866b2dcfcdaf9f41d6308`), CRC PASS e manifest 52/52 PASS in questa sessione.
- Rapporto Claude e registro delle 99 affermazioni ricevuti come file utente.
- Srivastava e Surya, *Implementing Bell causality in Quantum Sequential Growth*, https://arxiv.org/html/2603.25503v1 (versione arXiv v1, non la versione PRD).
- Materiali storici v0.92 XL e v0.93 L3 estratti dal recovery v1.02, consultati come interpretazione del dominio originariamente dichiarato.

## Risultato 1 — MAJOR-1: confermato

Nella fonte il Teorema 3.7 (equazioni 114/119) impone, per **operatori gregarious generici**, non soltanto per i generatori delle anticatene,

\[
G_n G_k^{-1}G_m=G_m G_k^{-1}G_n, \qquad m\ne n, \quad k<\min(m,n).
\]

L'equazione (120) è il **caso speciale** per `Q_n`. Il manoscritto XL ha usato il caso particolare indicando spesso (119), creando un ambito eccessivo per il proprio `iff`.

Sul locus XL hermitiano traceless noncommutativo invertibile, parametrizzato con

\[
a=\frac{t^2+1}{4t},\quad b=-\frac{t}{t^2+1},\quad u=\frac{t^2-1}{2(t^2+1)},\quad Q_3=\beta Q_2,
\]

con `t` reale diverso da `0,±1`, e con gli inversi richiesti, le formule originali danno

\[
T_2=I-2(I-Q_1)Q_2Q_1^{-1}-Q_2, \qquad
G(V)=T_2Q_3T_2^{-1},\quad G(K_2)=(I-Q_1)Q_2(I-Q_1)^{-1}.
\]

Due istanze ammissibili di (114) hanno residui proporzionali all'identità:

\[
\begin{aligned}
G(V)Q_1^{-1}Q_2-Q_2Q_1^{-1}G(V)&=\frac{\beta(4a^2-1)}{10a^4}I,\\
G(K_2)Q_1^{-1}Q_3-Q_3Q_1^{-1}G(K_2)&=-\frac{4\beta u^2}{a^2-1}I.
\end{aligned}
\]

Le formule sono state ricalcolate **da zero** nel codice consegnato, senza importare moduli di Claude o delle versioni storiche. A `t=3, beta=1` risultano esattamente `1152/3125 I` e `576/275 I`. Al contrario, le condizioni locali Eq.(120) e Eq.(145) continuano ad annullarsi: il problema consiste precisamente nella **promozione illegittima del controllo ristretto a controllo della CPOBC completa**.

**Decisione di scopo:** il certificato XL locale resta matematicamente corretto come classificazione per (120), (130), (145) e le invertibilità dichiarate; non rappresenta soluzioni neppure provvisorie per l'intero insieme di condizioni necessarie (119) del modello forte. Il suo titolo e i registri di autorità devono essere corretti. Il no-go P3 rimane compatibile, ma non rappresenta la prova più corta.

## Risultato 2 — MAJOR-2: conferma della violazione necessaria

Assumendo in aggiunta L3 `Q_3=Q_2, Q_4=delta Q_2`, per il poset di quattro eventi costituito da `a3` e un massimo comune si ricostruisce il timid dell'anticatena:

\[
T_3=I-3(I-Q_1)Q_2Q_1^{-1}-3T_2-Q_2.
\]

Quindi `G(a3+top)=T_3 Q_4 T_3^{-1}` e la (114) impone un residuo nullo. Il risultato effettivo è

\[
G(a_3+top)Q_1^{-1}Q_3-Q_3Q_1^{-1}G(a_3+top)
=\frac{16\delta t^2(t^2-1)^2}{3(t^2+1)^4}I\ne0
\]

nel dominio ammissibile con `delta != 0`. L'identità esatta è stata ricavata senza il motore QSG del revisore. Il fallimento conferma la sostanza dell'obiezione di consistenza. **Non** costituisce una nostra ricostruzione esaustiva di tutte le coppie `R13` nei due procedimenti di partner: la localizzazione al confronto di partner specifici deriva anche dalla documentazione del revisore.

## Disposizione delle altre osservazioni

- `REJECT` per il working paper da 372 pagine **come articolo di rivista**: valutazione editoriale ragionevole, non conclusione di invalidità scientifica del quaderno di ricerca.
- Nessuna legge autonoma `H(z)` o microdinamica gravitazionale 4D è stata derivata: conclusione già registrata come blocco nel progetto.
- Le formule su ordini 2D e la concentrazione `R12y–R12ac` restano **non valutate qui** rispetto all'originalità bibliografica e alla completezza della dimostrazione.
- `Q2=lambda Q1`, con `Q3` successivamente non commutante, non è escluso dal no-go per `[Q1,Q2] != 0`; non chiamare l'ostruzione P3 "no-go di tutta l'algebra non commutativa 2x2".
- PDF standalone e PDF nel recovery hanno hash diversi; questo è un tema di provenienza/packaging, non una discrepanza fisica.
- Il recovery `light` è autosufficiente per la ricerca corrente, **non** per ogni replay storico: i file storici elencati nell'inventario devono essere resi disponibili per verifiche integrali.

## Prossima azione raccomandata (non ancora eseguita)

1. Mantenere immutabile il recovery canonico v1.02 come evidenza storica.
2. Aprire un gate **CORRIGENDUM_REFEREE_AUDIT** con protocollo congelato per aggiornare classificazione XL e riferimenti Eq.(119)/(120), riportare tutti i residui con i relativi domini, indicare L3/P3/IR come verifiche matematiche storiche ma non criteri minimi.
3. Non sovrascrivere silenziosamente le appendici storiche: includere un erratum ben visibile nel successivo PDF cumulativo e aggiornare roadmap, abstract, status e handoff.
4. Verificare ulteriormente la fonte PRD e sottoporre il certificato a un revisore umano esperto prima di rivendicare novità e pubblicabilità.
5. Mantenere `R12bc NOT_OPEN`, `R12as physical NOT_AUTHORIZED`, `R13 BLOCKED`.

**Integrità epistemica:** non è stato inventato un selettore fisico, introdotta una nuova matrice candidato o rieseguita una ricerca opportunistica di parametri; l'esito negativo deve essere conservato.
