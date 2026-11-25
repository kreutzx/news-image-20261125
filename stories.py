# Story data for the 25 November 2026 front page.
# Every item was reported on Wednesday 25 November 2026 (any time zone)
# or happened that day. Certainty: CONFIRMED / REPORTED / CLAIM / FORECAST.
# Sources are the outlets whose reporting each item rests on (Reuters,
# BBC, Fox News, Newsreel, Times of India, Daily Debrief, UN, FIDE, UEFA).

HEROES = [
    {
        "kicker": "MONEY & TECH",
        "headline": "ASIA TUMBLES AS THE AI REBOUND STUMBLES",
        "deck": "Asian stocks slid Wednesday as fresh US tariff threats hit sentiment: MSCI Asia-Pacific fell 2.3%, Seoul 5.3% and Taiwan 5.1%, while Nvidia gave back 5.9% of its post-Huang surge.",
        "source": "REUTERS",
        "cert": "CONFIRMED",
        "icon": "chart",
    },
    {
        "kicker": "WORLD",
        "headline": "WARSAW DEMANDS US TROOPS",
        "deck": "A Russian drone crossed into Poland overnight — the second breach in four days, after Kh-101 missiles fell on Polish soil. Warsaw briefed the White House; NATO is sending AWACS.",
        "source": "FOX NEWS",
        "cert": "REPORTED",
        "icon": "radar",
    },
]

SECTIONS = [
    # (section, headline, deck, source, cert, icon or None)
    ("WORLD", "ISRAELI STRIKE KILLS HAMAS SECURITY CHIEF IN GAZA",
     "Naeem Abu Nahel, head of Hamas's internal security, was killed in Gaza City; medics say six more died.",
     "REUTERS", "REPORTED", "building"),
    ("WORLD", "NATO ANSWERS REPORTS OF A RUSSIAN NUCLEAR SATELLITE",
     "The alliance responds to reports of Russian nuclear activity in orbit.",
     "DAILY DEBRIEF", "REPORTED", "atom"),
    ("WORLD", "RUSSIA'S OWN FIGURES PUT ITS WAR DEAD NEAR 500,000",
     "Leaked data reported by the BBC suggests almost half a million Russian deaths in Ukraine.",
     "BBC", "REPORTED", None),
    ("WORLD", "CHINA INVESTIGATES SHANGHAI CHIEF IN XI'S LATEST PURGE",
     "Beijing investigates Politburo star Chen Jining, the Shanghai party chief.",
     "TIMES OF INDIA", "REPORTED", "stars"),
    ("WORLD", "DR CONGO MILITARY JET MISSING AMID REBEL CLAIMS",
     "A Congolese military aircraft is missing as rebels make claims.",
     "DAILY DEBRIEF", "REPORTED", None),
    ("MONEY & TECH", "HUAWEI GUILTY OF TRADE-SECRET THEFT IN US TRIAL",
     "A Brooklyn jury convicted Huawei on 10 of 12 counts; acquitted of racketeering, it plans to appeal.",
     "BBC", "CONFIRMED", "chip"),
    ("MONEY & TECH", "TRUMP READIES A NEW WAVE OF TARIFFS",
     "Washington prepares duties after a probe into 'excess industrial capacity' abroad.",
     "BBC", "CONFIRMED", "cart"),
    ("MONEY & TECH", "MICROSOFT DECLARES 'CODE RED' AFTER MAJOR OUTAGE",
     "Internal memos show a 'Code Red' declared as a major outage hit services.",
     "WIRE", "REPORTED", "shield"),
    ("MONEY & TECH", "SINGAPORE PROBES MEGASPEED OVER NVIDIA CHIP FLOWS",
     "Authorities investigate Megaspeed following the US prohibition on chip exports.",
     "WIRE", "REPORTED", "chip"),
    ("MONEY & TECH", "ANTHROPIC SLIPS 6.5%, BELOW ITS IPO PRICE",
     "The AI firm's shares fell below their IPO price as the tech rally fizzled.",
     "REUTERS", "CONFIRMED", "bank"),
    ("SCIENCE & PLANET", "SHENZHOU-24 LIFTS OFF WITH FIRST PAKISTANI ABOARD",
     "China's Shenzhou-24 carries the first Pakistani national into orbit.",
     "JAPAN TIMES", "CONFIRMED", "satellite"),
    ("SCIENCE & PLANET", "HEAT DEATHS IN ENGLAND HIT A RECORD HIGH IN 2026",
     "Official figures show heat-driven deaths at a record high this year.",
     "OFFICIAL FIGURES", "CONFIRMED", "smog"),
    ("SCIENCE & PLANET", "SPACEX FLIES A CLASSIFIED SPACE FORCE MISSION",
     "A classified US Space Force operation lifts off from California.",
     "US SPACE FORCE", "REPORTED", "jet"),
    ("SCIENCE & PLANET", "GLOBAL CLIMATE TALKS COLLAPSE WITHOUT A DEAL",
     "Negotiators leave without an agreement as the COP31 fallout deepens.",
     "NEWSREEL", "CONFIRMED", "globe"),
    ("SOCIETY & CULTURE", "IRANIAN SINGER GETS 74 LASHES OVER ONLINE CONCERT",
     "Parastoo Ahmadi was lashed 74 times for performing without a hijab on YouTube.",
     "NEWSREEL", "CONFIRMED", None),
    ("SOCIETY & CULTURE", "UN: 47,000 WOMEN KILLED BY PARTNERS OR KIN IN A YEAR",
     "About five women an hour died at the hands of partners or relatives in 2025.",
     "UN", "CONFIRMED", "shield"),
    ("SOCIETY & CULTURE", "TWO ARRESTED AFTER BREAK-IN AT WILLIAM AND KATE'S HOME",
     "Two men were held on suspicion of burglary at the couple's country residence.",
     "NEWSREEL", "CONFIRMED", None),
    ("SOCIETY & CULTURE", "TRUMP PARDONS TURKEYS FREEDOM AND FEATHERS",
     "The White House Thanksgiving pardon spared two turkeys, Freedom and Feathers.",
     "BBC", "CONFIRMED", None),
]

SPORT = [
    ("CHESS", "GAME 2 IN GENEVA: GUKESH TAKES WHITE",
     "After escaping a time crisis to draw Game 1, Gukesh plays White in Game 2 of the world title match.",
     "FIDE", "FORECAST"),
    ("FOOTBALL", "REAL MADRID ROUT PSV 5-1 AT THE BERNABEU",
     "Madrid's five-goal night headlined Matchday 5 of the Champions League.",
     "UEFA", "CONFIRMED"),
    ("FOOTBALL", "CITY HELD 2-2 BY NAPOLI; ARSENAL DRAW 1-1",
     "City and Napoli shared four goals; Dortmund held Arsenal at the Emirates.",
     "UEFA", "CONFIRMED"),
    ("FOOTBALL", "TONIGHT: BARCELONA AT SABAH, PSG HOST ROMA",
     "Matchday 5 concludes with nine fixtures, including Sporting v Manchester United.",
     "UEFA", "FORECAST"),
]

NUMBERS = [
    ("-5.3%", "South Korea's fall, Asia's worst in the rout"),
    ("47,000", "women killed by partners or kin in a year — UN"),
    ("500,000", "Russian war dead, by its own figures"),
    ("12,000", "evacuated from UK concert gas alert"),
]

MARKETS = [
    ("ASIA", "MSCI APAC -2.3% · KOSPI -5.3% · Nikkei -2.9%"),
    ("CHIPS", "Nvidia -5.9% · Anthropic -6.5% · S&P futures -0.3%"),
    ("WEATHER", "England heat deaths at a record high in 2026"),
]

WIRE = [
    ("MEXICO TROOPS CAPTURE CARTEL LEADER 'EL CHAPO ISIDRO'", "REPORTED"),
    ("GUNMEN HOLD HOSTAGES IN COLOMBIA SUPERMARKET RAID", "REPORTED"),
    ("INDONESIA CHARGES FORMER POLICE CHIEF WITH TREASON", "REPORTED"),
    ("PUTIN VOWS REPRISALS OVER STRIKES ON RUSSIAN OIL SITES", "REPORTED"),
    ("FORT HOOD SHOOTER HASAN SEEKS STAY OF EXECUTION", "REPORTED"),
]

TIMELINE = [
    ("01:09", "UK sanctions Houthi leaders"),
    ("01:11", "Indonesia treason charge"),
    ("01:40", "Singapore probes Megaspeed"),
    ("02:42", "Hasan seeks execution stay"),
    ("02:58", "UN: 47,000 femicide toll"),
    ("03:02", "SpaceX classified launch"),
]

DATE_LINE = "WEDNESDAY 25 NOVEMBER 2026"
ACCOUNTING = "36 STORIES · 8 REGIONS · 5 FIELDS · ALL FROM WEDNESDAY 25 NOVEMBER 2026"
FIELD_COUNTS = "WORLD 6 · MONEY & TECH 6 · SCIENCE & PLANET 4 · SOCIETY & CULTURE 4 · SPORT 4 · BY THE NUMBERS 4 · MARKETS & WEATHER 3 · LATE WIRE 5"
