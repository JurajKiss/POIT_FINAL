# Systém monitorovania a riadenia signálov IoT

Tento projekt je súčasťou predmetu Pokročilé informačné technológie na Slovenskej technickej univerzite v Bratislave. Cieľom je monitorovať a riadiť signály z reálnych senzorov alebo simulačných prostredí pomocou webovej aplikácie, v súlade s koncepciou IoT.

## Obsah
1. [Popis projektu](#popis-projektu)
2. [Architektúra systému](#architektúra-systému)
3. [Inštalácia a nastavenie](#inštalácia-a-nastavenie)
4. [Použitie](#použitie)
5. [Komponenty](#komponenty)
6. [Prispievanie](#prispievanie)
7. [Licencia](#licencia)

## Popis projektu

Cieľom projektu je monitorovať a riadiť signály získané z reálnych senzorov alebo simulačných a virtuálnych prostredí. Monitorovanie a riadenie sa uskutočňuje prostredníctvom webovej aplikácie. Používame 10kΩ potenciometer ako senzor, zelenú LED diódu a 230Ω rezistor. Mikrokontrolér použitý v projekte je NodeMCU 1.0. Analógový signál z potenciometra je posielaný cez sériovú linku do virtuálnej mašiny s Raspberry OS, kde je zobrazovaný na webovej stránke.

## Architektúra systému

Projekt je rozdelený do troch hlavných častí:
1. **Serverová časť**: 
   - Používa Python s Flask na spracovanie webových požiadaviek a komunikáciu s mikrokontrolérom cez sériové pripojenie.
2. **Klientská časť**:
   - Webové rozhranie s tlačidlami na spustenie a zastavenie merania signálu a vizualizáciu dát.
3. **Mikrokontrolér**:
   - NodeMCU 1.0, ktorý číta analógový signál z potenciometra a posiela dáta cez sériovú komunikáciu.

### Diagramy a zapojenie

- **UML diagram**: Zobrazuje tok dát cez komunikačné kanály.
- **Stavový diagram**: Ilustruje stavy systému.
- **Schéma zapojenia**: Zobrazuje pripojenie komponentov.

## Inštalácia a nastavenie

### Predpoklady

- NodeMCU 1.0
- Virtuálna mašina s Raspberry OS
- Python 3.x
- Flask knižnica
- Serial knižnica

### Kroky

1. Pripojte NodeMCU k počítaču.
2. Otvorte terminál vo virtuálnej mašine s Raspberry OS.
3. Pomocou príkazu `cd` prejdite do priečinka, kde je uložený súbor `Zaverecne_Zadanie.py`.
4. Spustite server príkazom:
   ```bash
   sudo python3 'Zaverecne_Zadanie.py'
5. Otvorte webový prehliadač a prejdite na `http://0.0.0.0`.

## Použitie

1. **Zapnúť meranie**: Kliknite na tlačidlo "Turn On" na webovej stránke na spustenie merania signálu.
2. **Vizualizácia**: Prepnite medzi kartami na zobrazenie dát v rôznych formátoch (graf, ciferník, atď.).
3. **Vypnúť meranie**: Kliknite na tlačidlo "Turn Off" na zastavenie merania.
4. **Odpojenie**: Kliknite na tlačidlo "Disconnect" na ukončenie relácie.
5. **Zastavenie servera**: V termináli stlačte `CTRL + C` na zastavenie servera.

## Komponenty

### Hardvér
- **Potenciometer (10kΩ)**
- **Zelená LED dióda**
- **Rezistor (230Ω)**
- **NodeMCU 1.0**

### Softvér
- **Server**: Python, Flask
- **Klient**: HTML, CSS, JavaScript
- **Kód mikrokontroléra**: C/C++

## Licencia

Tento projekt je licencovaný pod MIT licenciou - viď súbor [LICENSE](LICENSE) pre detaily.
