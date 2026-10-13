# R12BB-ER — Errata verificata dopo revisione esterna AI (v1.03, 13 ottobre 2026)

**Decisione:** `CORRIGENDUM_REFEREE_AUDIT_CONFIRMED`; `XL_GLOBAL_SURVIVAL_WITHDRAWN`.
**Dominio:** CPOBC operatoriale forte non singolare; `Q1,Q2` hermitiani, traceless, invertibili, noncommutanti `2x2`, e ramo parametrico XL–L3. NON no-go universale per tutte le matrici `2x2`.

## Provenienza / priorità

1. Rapporto Claude (revisione AI automatizzata) ricevuto il 13/10/2026 e congelato in `REFEREE/CLAUDE_REFEREE_REPORT_V102.md`, con originali nell'archivio del referee incluso. NON peer review umana.
2. Arbitrazione successiva indipendente dal codice di Claude in `REFEREE/INTERNAL_TRIAGE_REPORT_V102.md` e nell'archivio piccolo `REFEREE/INTERNAL_TRIAGE_REPLAY_V102.zip`.
3. Nuovi codici v1.03: SymPy simbolico `AUDIT/R12BB_ER_PRIMARY.py` e secondo certificatore Python `Fraction` senza SymPy `AUDIT/R12BB_ER_INDEPENDENT.py`. Il secondo certifica esattamente un controllo razionale a `t=3`, NON tutta la formula globale.
4. Fonte scientifica primaria: R. Srivastava, S. Surya, *Implementing Bell causality in Quantum Sequential Growth*, `https://arxiv.org/html/2603.25503v1`, Teorema 3.7 e Eq. (114), (119), (120), (141), (142), (145), (159). **La versione finale PRD non è stata riesaminata in questo gate**.

## MAJOR-1: necessità generale ≠ caso sulle sole anticatene

Per operatori gregarious generici di causal set rispettivamente di taglie `n,k,m`, con `m != n` e `k < min(m,n)`:

`G_n G_k^{-1} G_m = G_m G_k^{-1} G_n` (Eq.114/119).

Per `Q_n` associati alle sole anticatene si ottiene un caso particolare, Eq.(120). XL ha testato soprattutto Eq.(120) e Eq.(145), spesso sotto l'etichetta impropria `(119)`. `XL.3` deve essere interpretato come classificazione *solo del sistema ristretto* Eq.(120),(130),(145) con gli inversi specificati; non è corretto leggerlo come equivalenza per tutto il sistema delle condizioni necessarie della CPOBC forte.

Parametrizzazione storica XL, senza nuovi parametri:

```
Q1 = diag(a,-a); Q2 = [[b,u],[u,-b]]; Q3=beta Q2
b=-1/(4a), u²=(4a²-1)/(16a²), |a|>1/2, a² != 1,2, beta !=0.
P=(I-Q1)Q2 Q1^-1
T2=I-2P-Q2
G(V)=T2 Q3 T2^-1
G(K2)=(I-Q1)Q2 (I-Q1)^-1
```

Due istanze ammissibili del Teorema 3.7 soddisfano il criterio sulle taglie ma hanno residui non nulli:

```
G(V) Q1^-1 Q2 - Q2 Q1^-1 G(V) = beta (4a²-1) / (10a^4) I !=0
G(K2) Q1^-1 Q3 - Q3 Q1^-1 G(K2) = -4 beta u² / (a²-1) I !=0
```

Non nulli ovunque nel dominio non singolare XL. Con `a=5/6,b=-3/10,u=2/5,beta=1` i residui sono `1152/3125 I` e `576/275 I`. I controlli Eq.(120) ed Eq.(145) risultano contemporaneamente zero. La contraddizione non è quindi una discrepanza numerica.

**Disposizione:** `XL.3` resta matematicamente utilizzabile SOLO nella formulazione esplicitamente ristretta. Il precedente linguaggio «sopravvive alle condizioni necessarie CPOBC» senza qualifiche è ritirato. PL non certifica la (119) generale.

## MAJOR-2: controllo necessario su atomizzazione/partner Bell

Assumendo ulteriormente L3: `Q3=Q2`, `Q4=delta Q2`, `delta !=0`, e `T3=I-3P-3T2-Q2`, `G(a3+top)=T3 Q4 T3^-1`, il residuo della relazione generale vale:

`G(a3+top)Q1^-1 Q3 - Q3 Q1^-1 G(a3+top) = 16 delta t²(t²-1)² / [3(t²+1)^4] I !=0`,

con `a=(t²+1)/(4t), b=-t/(t²+1), u=(t²-1)/(2(t²+1))`, `t != 0, ±1` e inversi richiesti. Il controllo è esatto. **Non** viene qui rivendicata una ricostruzione indipendente completa di tutti i partner `R13`, solo dell'ostruzione necessaria che sostiene la contestazione. Il revisore Claude ha riportato una differenza tra partner minimale e partner TD: il suo intero workflow di confronto non è stato replicato qui.

## Autorità degli enunciati storici dopo il corrigendum

| Oggetto | Interpretazione consentita |
|---|---|
| `R12BB-PL`, `R12BB-XL` | Teoremi condizionati all'insieme di equazioni specificamente testate. NON soluzioni nemmeno provvisorie per tutta la CPOBC forte |
| `R12BB-L3`, `R12BB-TD` | Equazioni e diagnostiche locali storiche, ma la loro candidatura globale viene superseduta dai residui (ER.5)–(ER.7) |
| `R12BB-P3`, `R12BB-IR` | Certificati condizionati coerenti con un blocco più precoce; non necessari per l'esclusione nel ramo XL; non sono no-go universali |
| `R12BB-SO`, `FP`, `BC`, `LI` | Differenza fra regole su stato e operatori: utile ma sostanzialmente algebra lineare standard. Testimone SO non soddisfa la CPOBC forte |
| Domini rimanenti | `Q2=lambda Q1` e `Q3` potenzialmente noncommutante non esclusi, normali nonhermitiani, non normali, dimensioni maggiori, GC con fasi, altre Bell orderings, formulazioni deboli, dinamiche singolari: NON DECISI |

## Raccomandazioni future e decisione fisica

- Aggiornare i report destinati a pubblicazione e tenere separate le appendici storiche dagli enunciati correnti.
- Chiedere controllo umano esperto indipendente della versione PRD e dell'assiomatica prima di rivendicare originalità.
- Chiarire nel paper futuro l'oggetto da pubblicare, anziché presentare tutto il cumulativo come articolo.
- Le formule combinatorie R12y–R12ac restano da verificare per prior art e completezza di prova; sign problem storico non rigiocato, nessun nuovo fit.
- Nessun selettore microfisico, misura QSG gravitazionale globale, Ward metrica conservata, limite 4d o H(z) autonomo derivati.
- R12bc `NOT_OPEN`, R12as fisico `NOT_AUTHORIZED`, R13 `BLOCKED`.

**Gestione epistemica:** protocollo di correzione stilato DOPO la critica e i primi controcalcoli; non presentare i residui come scoperta preregistrata. Conservare immutato il parent v1.02 e i documenti di Claude.
