from wikitext_parser.wikitext_parser import parse_wikitext

def test_parse_wikitext():
    text = """
        {{also|-free}}
        ==English==

        ===Etymology===
        {{PIE root|en|preyH}}
        From {{inh|en|enm|free}}, {{m|enm|fre}}, {{m|enm|freo}}, from {{inh|en|ang|frēo||free}}, from {{inh|en|gem-pro|*frijaz||beloved, not in bondage}}, from {{inh|en|ine-pro|*priHós||dear, beloved}}, from {{m|ine-pro|*preyH-||to love, to please}}. Related to {{m|en|friend}}. Cognate with {{cog|fy|frij||free}}, {{cog|nl|vrij||free}}, {{cog|nds|free||free}}, {{cog|de|frei||free}}, {{m|de|Friede||peace}}, {{cog|da|-}}, {{cog|sv|-}} and {{cog|no|fri||free}}, {{cog|sa|प्रिय|tr=priyá}}.

        Germanic and Celtic are the only Indo-European language branches in which the PIE word with the meaning of &quot;dear, beloved&quot; acquired the additional meaning of &quot;free&quot; in the sense of &quot;not in bondage&quot;. This was an extension of the idea of &quot;characteristic of those who are dear and beloved&quot;, in other words friends and tribe members (in contrast to unfree inhabitants from other tribes and prisoners of war, many of which were among the slaves – compare the Latin use of [[liberi]] to mean both &quot;free persons&quot; and &quot;children of a family&quot;).&lt;ref&gt;{{R:Etymonline}}&lt;/ref&gt;&lt;ref&gt;[https://www.dwds.de/wb/frei &quot;frei&quot;] in Digitales Wörterbuch der deutschen Sprache&lt;/ref&gt;

        The verb comes from {{der|en|enm|freen}}, {{m|enm|freoȝen}}, from {{der|en|ang|frēon}}, {{m|ang|frēoġan||to free; make free}}.

        ===Pronunciation===
        * {{enPR|frē}}, {{IPA|en|/fɹiː/|[fɹɪi̯]}}
        * {{audio|en|en-us-free.ogg|Audio (US)}}
        * {{audio|en|En-uk-free.ogg|Audio (UK)}}
        * {{audio|en|LL-Q1860 (eng)-Nattes à chat-free.wav|Audio}}
        * {{rhymes|en|iː}}

        [[File:Free Beer.jpg|thumb|A sign advertising '''free''' beer (obtainable without payment), typically with some required purchase/catch.]]
        [[File:Buy one, get one free ^ - geograph.org.uk - 153952.jpg|thumb|A &quot;buy one get one '''free'''&quot; sign at a flower stand (obtainable without additional payment)]]
        [[File:Berkeley Farms Fat-Free Half &amp; Half.jpg|thumb|This food product is labelled &quot;fat '''free'''&quot;, meaning it contains no fat]]

        ===Adjective===
        {{en-adj|er}}

        # {{lb|en|social}} [[unconstrained|Unconstrained]].
        #: {{ux|en|He was given '''free''' rein to do whatever he wanted.}}
        #* '''1610-11?''', Shakespeare, {{w|The Tempest}}, Act V, scene i:
        #*: Quickly, spirit! / Thou shalt [[ere]] long be '''free'''.
        #* {{quote-book|en|year=1899|author={{w|Stephen Crane}}
        |title=[[s:Twelve O'Clock|Twelve O'Clock]]|chapter=1
        |passage=There was some laughter, and Roddle was left '''free''' to expand his ideas on the periodic visits of cowboys to the town. “Mason Rickets, he had ten big punkins a-sittin' in front of his store, an' them fellers from the Upside-down-F ranch shot 'em up […].”}}
        #* {{quote-journal|en|date=2013-08-10|volume=408|issue=8848|magazine={{w|The Economist}}|author=Schumpeter
        |title=[http://www.economist.com/news/business/21583242-businesspeople-have-become-too-influential-government-cronies-and-capitols Cronies and capitols]
        |passage=Policing the relationship between government and business in a '''free''' society is difficult. Businesspeople have every right to lobby governments, and civil servants to take jobs in the private sector.}}
        #: {{syn|en|unconstrained|unfettered|unhindered}}
        #: {{ant|en|constrained|restricted}}
        ## Not [[imprisoned]] or [[enslaved]].
        ##: {{ux|en|a '''free''' man}}
        ##: {{ant|en|bound|enslaved|imprisoned}}
        ## Unconstrained by [[timidity]] or [[distrust]]
        ##: {{syn|en|unreserved|frank|communicative}}
        ##* {{quote-book|en|author=Richard Milward| title=The Table Talk of {{w|John Selden}}| page=xxiv| year=1818| passage=Dr. Wilkins says, &quot;He was naturally of a serious temper, which was somewhat soured by his sufferings, so that he was '''free''' only with a few.&quot;}}
        ## [[generous|Generous]]; [[liberal]].
        ##: {{ux|en|He's very '''free''' with his money.}}
        ## {{lb|en|obsolete}} Clear of offence or crime; guiltless; innocent.
        ##* {{quote-book|en|author={{w|John Dryden}}|title=[[w:Oedipus (Dryden play)|Oedipus: A Tragedy]]| year=1679| page=59| passage=My hands are guilty, but my heart is '''free'''.}}
        ## Without [[obligation]]s.
        ##: {{ux|en|'''free''' time}}
        ## Thrown open, or made accessible, to all; to be enjoyed without limitations; unrestricted; not obstructed, engrossed, or appropriated; open; said of a thing to be possessed or enjoyed.
        ##: {{ux|en|a '''free''' school}}
        ##* {{quote-book|en|author={{w|William Shakespeare}}| title={{w|Taming of the Shrew}}, I, ii| year=1590-2| passage=Why, sir, I pray, are not the streets as '''free''' / For me as for you?}}
        ## Not arbitrary or despotic; assuring liberty; defending individual rights against encroachment by any person or class; instituted by a free people; said of a government, institutions, etc.
        ##: {{ux|en|This is a '''free''' country.}}
        ## {{lb|en|software}} With no or only freedom-preserving [[limitation]]s on distribution or modification.
        ##: {{ux|en|OpenOffice is [[free software|'''free''' software]].}}
        ##: {{syn|en|libre}}
        ##: {{ant|en|proprietary}}
        ## {{lb|en|software}} Intended for [[release]], as opposed to a [[checked]] version.
        # Obtainable without any [[payment]].
        #* {{quote-journal|en|date=2013-07-20|volume=408|issue=8845|magazine={{w|The Economist}}
        |title=[http://www.economist.com/news/http://www.economist.com/news/business/21582001-army-new-online-courses-scaring-wits-out-traditional-universities-can-they The attack of the MOOCs]
        |passage=Since the launch early last year of&amp;nbsp;[&amp;hellip;] two Silicon Valley start-ups offering '''free''' education through MOOCs, massive open online courses, the ivory towers of academia have been shaken to their foundations. University brands built in some cases over centuries have been forced to contemplate the possibility that information technology will rapidly make their existing business model obsolete.}}
        #: {{ux|en|The government provides '''free''' health care.}}
        #: {{ux|en|It's '''free''' real estate.}}
        #: {{syn|en|free of charge|gratis}}
        ## {{lb|en|by extension|chiefly|advertising slang}} [[complimentary]]
        ##: {{ux|en|Buy a TV to get a '''free''' DVD player!}}
        # {{lb|en|abstract}} [[unconstrained|Unconstrained]].
        ## {{lb|en|mathematics}} Unconstrained by [[relator]]s.
        ##: {{ux|en|the '''free''' group on three generators}}
        ## {{lb|en|mathematics|logic}} Unconstrained by [[quantifier]]s.
        ##: {{ux|en|&lt;math&gt;z&lt;/math&gt; is the '''free''' variable in &lt;math&gt;\forall x\exists y:xy=z&lt;/math&gt;.}}
        ##: {{ant|en|bound}}
        ## {{lb|en|programming}} Unconstrained of [[identifier]]s, not [[bound]].
        ##: {{syn|en|unbound}}
        ##: {{ant|en|bound}}
        ## {{lb|en|linguistics}} {{q|of a morpheme}} That can be used by itself, [[unattached]] to another [[morpheme]].
        # {{lb|en|physical}} [[unconstrained|Unconstrained]].
        ## Unobstructed, without [[blockage]]s.
        ##: {{ux|en|the drain was '''free'''}}
        ##: {{syn|en|clear|unobstructed}}
        ##: {{ant|en|blocked|obstructed}}
        ## Unattached or uncombined.
        ##: {{ux|en|a '''free''' radical}}
        ##: {{syn|en|loose|unfastened|Thesaurus:loose}}
        ## Not currently in use; not taken; unoccupied.
        ##: {{ux|en|You can sit on this chair; it's '''free'''.}}
        ## {{lb|en|botany|mycology}} Not [[attached]]; [[loose]].
        ##: {{ux|en|In this group of mushrooms, the gills are '''free'''.}}
        ##* {{RQ:Schuster Hepaticae|volume=V|page=7|text=Furthermore, the '''free''' anterior margin of the lobule is arched toward the lobe and is often involute{{...}}}}
        # Without; not containing (what is specified); exempt; clear; liberated.
        #: {{ux|en|We had a wholesome, filling meal, '''free''' of meat.&amp;emsp; I would like to live '''free''' from care in the mountains.}}
        #* {{quote-book|en|author={{w|Gilbert Burnet}}| title=The History of the Reformation of the Church of England| year=1679-1715| passage=princes declaring themselves '''free''' from the obligations of their treaties}}
        #* {{quote-book|en|year=1898|author={{w|Winston Churchill (novelist)|Winston Churchill}}| title={{w|The Celebrity}}| chapter=4| passage=One morning I had been driven to the precarious refuge afforded by the steps of the inn, after rejecting offers from the Celebrity to join him in a variety of amusements. But even here I was not '''free''' from interruption, for he was seated on a horse-block below me, playing with a fox terrier.}}
        #: {{syn|en|without}}
        # {{lb|en|dated}} Ready; eager; acting without spurring or whipping; spirited.
        #: {{ux|en|a '''free''' horse}}
        # {{lb|en|dated}} Invested with a particular freedom or franchise; enjoying certain immunities or privileges; admitted to special rights; followed by ''of''.
        #* {{quote-book|en|author={{w|John Dryden}}| title={{w|The Hind and the Panther}}| year=1697| chapter=Part 3, line 1245| passage=He therefore makes all birds, of every sect, / '''Free''' of his farm.}}
        # {{lb|en|UK|legal|obsolete}} Certain or honourable; the opposite of ''[[base]]''.
        #: {{ux|en|'''free''' service;&amp;emsp; '''free''' socage}}
        #: {{rfquotek|en|Burrill}}
        # {{lb|en|legal}} Privileged or individual; the opposite of ''[[common]]''.
        #: {{ux|en|a '''free''' fishery;&amp;emsp; a '''free''' warren}}
        #: {{rfquotek|en|Burrill}}

        ====Antonyms====
        {{checksense|en}}
        * {{l|en|unfree}}

        ====Hyponyms====
        {{checksense|en}}
        * {{l|en|-free}}

        ====Derived terms====
        {{der4|en
        |break free
        |cloud-free
        |freeball
        |freebooter
        |freedom
        |freehood
        |freelance
        |freeloader
        |freely
        |Freemason
        |free-spoken
        |free-thinker
        |freeware
        |freeway
        |freewheel
        }}

        ====Related terms====
        {{rel4|en|title=Related terms of ''free''
        |[[free Abelian group]]&lt;!--UK spelling--&gt;, [[free abelian group]]&lt;!--US spelling--&gt;
        |free algebra
        |free and clear
        |free and easy
        |free as a bird
        |free fall
        |free group
        |free lunch
        |free market
        |free marketeer
        |free module
        |free object
        |free of charge
        |free of the city
        |free rein
        |free ride
        |free rider
        |free semigroup
        |free speech
        |free spirit
        |free time
        |free variable
        |free vote
        |free will
        |friend
        }}

        ====Translations====
        {{trans-top|not imprisoned}}
        * Afrikaans: {{t+|af|vrye}}
        * Albanian: {{t+|sq|lirë}} (i/e)
        * Amharic: {{t|am|ነፃ|sc=Ethi}}
        * Arabic: {{t+|ar|حُرّ}}
        *: Egyptian Arabic: {{t|arz|حر|tr=ḥurr}}
        * Armenian: {{t+|hy|արձակ}}, {{t+|hy|ազատ}}
        * Asturian: {{t|ast|llibre}}
        * Azerbaijani: {{t+|az|azad}}
        * Bambara: {{t|bm|hɔrɔn}}
        * Bashkir: {{t|ba|ирекле|sc=Cyrl}}
        * Belarusian: {{t|be|свабо́дны}}, {{t|be|во́льны}}
        * Bengali: {{t|bn|মুক্ত|sc=Beng}}
        * Bulgarian: {{t+|bg|свобо̀ден}}
        * Catalan: {{t+|ca|lliure}}
        * Chinese:
        *: Cantonese: {{t|yue|自由|tr=zi6 jau4|sc=Hani}}
        *: Mandarin: {{t+|cmn|自由|tr=zìyóu de|alt=自由的}}
        * Czech: {{t+|cs|svobodný}}, {{t+|cs|volný}}
        * Danish: {{t+|da|fri}}
        * Dutch: {{t+|nl|vrij}}, {{t+|nl|los}}
        * Esperanto: {{t+|eo|libera}}
        * Estonian: {{t+|et|vaba}}, {{t|et|prii}}
        * Finnish: {{t+|fi|vapaa}}
        * French: {{t+|fr|libre}}
        * Friulian: {{t|fur|libar}}
        * Galician: {{t+|gl|ceibo|m}}
        * Georgian: {{t|ka|თავისუფალი|sc=Geor}}
        * German: {{t+|de|frei}}, {{t|de|ungebunden}}
        * Gothic: {{t|got|𐍆𐍂𐌴𐌹𐍃}}
        * Greek: {{t+|el|ελεύθερος}}
        *: Ancient: {{t|grc|ἐλεύθερος}}
        * Haitian Creole: {{t|ht|lib}}
        * Hebrew: {{t|he|חופשי|tr=khofshí|alt=חופשי / חָפְשִׁי}}
        * Hindi: {{t+|hi|मुक्त}}, {{t+|hi|आज़ाद}}
        * Hungarian: {{t+|hu|szabad}}
        * Icelandic: {{t+|is|frjáls}}
        * Ido: {{t+|io|libera}}
        * Indonesian: {{t+|id|bebas}}
        * Interlingua: {{t+|ia|libere}}
        * Irish: {{t|ga|saor}}
        *: Old Irish: {{t|sga|sóer}}
        * Istriot: {{t|ist|leîbaro}}
        * Italian: {{t+|it|libero}}
        * Japanese: {{t+|ja|自由|tr=じゆう, jiyū}}
        * Jarai: {{t|jra|rơngai}}
        * Khmer: {{t+|km|សេរី|tr=seerəy|sc=Khmr}}
        * Korean: {{t+|ko|자유}}
        * Kurdish:
        *: Kurmanji: {{t+|kmr|azad}}, {{t+|kmr|serbest}}, {{t+|kmr|rizgar}}
        *: Sorani: {{t+|ku|ئازاد|tr=AzAd|sc=ku-Arab}}, {{t+|ku|ڕزگار|tr=RizgAr|sc=ku-Arab}}
        {{trans-mid}}
        * Latin: {{t+|la|līber}}
        * Latvian: {{t|lv|brīvs}}
        * Leonese: {{t|roa-leo|ḷḷibru}}
        * Limburgish: {{t+|li|vrie}}
        * Lithuanian: {{t+|lt|laisvas}}
        * Low German: {{t|nds|frii}}, {{t|nds|fri}}
        *: German Low German: {{t|nds-de|free}}
        * Luxembourgish: {{t|lb|fräi}}
        * Macedonian: {{t|mk|слободен}}
        * Malay: {{t|ms|bebas}}
        * Malayalam: {{t|ml|സ്വതന്ത്രം}}
        * Manchu: {{t|mnc|ᠰᡠᠯᡶᠠᠩᡤᠠ}}
        * Norman: {{t|nrf|libre}}
        * Norwegian: {{t+|no|fri}}
        * Novial: {{t|nov|liberi}}
        * Occitan: {{t+|oc|liure}}
        * Old English: {{t|ang|frēo}}, {{t|ang|frēolic}}
        * Persian: {{t+|fa|آزاد|tr=âzâd}}, {{t+|fa|رها|tr=rahâ}}
        * Polish: {{t+|pl|wolny}}
        * Portuguese: {{t+|pt|livre}}
        * Quechua: {{t+|qu|qispi}}
        * Romanian: {{t+|ro|liber}}, {{t+|ro|slobod}}
        * Russian: {{t+|ru|свобо́дный}}, {{t+|ru|во́льный}}
        * Sanskrit: {{t+|sa|मुक्त}}, {{t+|sa|स्वतन्त्र}}
        * Scottish Gaelic: {{t|gd|saor}}
        * Serbo-Croatian:
        *: Cyrillic: {{t|sh|слободан}}
        *: Roman: {{t+|sh|slobodan}}
        * Sindhi: {{t+|sd|آزاد|tr=āzād}}
        * Slovak: {{t|sk|slobodný}}, {{t|sk|voľný}}
        * Slovene: {{t+|sl|svoboden}}
        * Spanish: {{t+|es|libre}}
        * Swahili: {{t|sw|huru}}
        * Swedish: {{t+|sv|fri}}
        * Telugu: {{t+|te|విడుదల}}
        * Thai: {{t+|th|อิสระ}}
        * Turkish: {{t+|tr|özgür}}
        * Ukrainian: {{t+|uk|ві́льний}}
        * Urdu: {{t+|ur|آزاد|tr=āzād}}, {{t|ur|سوتنتر|tr=svatantra|sc=ur-Arab}}, {{t|ur|مکت|tr=mukt|sc=ur-Arab}}
        * Uyghur: {{t|ug|ئەركىن|sc=ug-Arab}}, {{t|ug|ھۆر|sc=ug-Arab}}
        * Vietnamese: {{t+|vi|tự do}}
        * Volapük: {{t+|vo|libik}}
        * Walloon: {{t+|wa|libe}}
        * Welsh: {{t+|cy|rhydd}}
        * West Frisian: {{t|fy|frijlitten}}, {{t|fy|frij}}
        * Yiddish: {{t|yi|פֿרײַ}}
        * Zazaki: {{t|zza|azad}}, {{t|zza|xoser}}
        {{trans-bottom}}

        {{trans-see|obtainable without payment|free of charge}}

        {{trans-top|unconstrained}}
        * Albanian: {{t+|sq|pafre}}
        * Amharic: {{t|am|ነፃ|sc=Ethi}}
        * Arabic: {{t+|ar|حُرّ}}
        *: Egyptian Arabic: {{t|arz|حر|tr=ḥurr}}
        * Armenian: {{t+|hy|ազատ}}
        * Asturian: {{t|ast|llibre}}
        * Azerbaijani: {{t+|az|sərbəst}}
        * Bambara: {{t|bm|hɔrɔn}}
        * Bashkir: {{t|ba|иркен|sc=Cyrl}}
        * Catalan: {{t+|ca|lliure}}
        * Chinese:
        *: Mandarin: {{t+|cmn|自由|tr=zìyóu de|alt=自由的}}
        * Czech: {{t+|cs|volný}}
        * Danish: {{t+|da|fri}}
        * Dutch: {{t+|nl|vrij}}, {{t+|nl|los}}, {{t+|nl|loslopend}}
        * Esperanto: {{t+|eo|libera}}
        * Estonian: {{t+|et|vaba}}, {{t|et|prii}}
        * Finnish: {{t+|fi|vapaa}}, {{t+|fi|rajoittamaton}}
        * French: {{t+|fr|libre}}
        * Galician: {{t+|gl|libre|m|f}}
        * German: {{t+|de|frei}}, {{t|de|ungebunden}}
        * Greek: {{t+|el|ελεύθερος}}, {{t+|el|ανεμπόδιστος}}
        * Hebrew: {{t|he|פָּנוּי|tr=panúy}}
        * Ido: {{t+|io|libera}}
        * Interlingua: {{t+|ia|libere}}, {{t+|ia|franc}}
        * Irish: {{t|ga|saor}}, {{t|ga|scaoilte}}, {{t|ga|éasca}}
        *: Old Irish: {{t|sga|sóer}}
        * Italian: {{t+|it|libero|m}}, {{t+|it|brado|m}}
        * Japanese: {{t+|ja|自由|tr=じゆう, jiyū}}
        * Khmer: {{t+|km|ស្រស់ស្រាយ|tr=srɑh sraay|sc=Khmr}}
        * Korean: {{t|ko|자유적}} ({{t|ko|自由的}})
        * Kurdish:
        *: Kurmanji: {{t+|kmr|berdayî}}
        *: Sorani: {{t+|ku|سه‌ربه‌ست|tr=sarbast|sc=ku-Arab}}
        {{trans-mid}}
        * Latin: {{t+|la|līber}}
        * Latvian: {{t|lv|brīvs}}
        * Limburgish: {{t+|li|vrie}}
        * Low German:
        *: German Low German: {{t|nds-de|free}}
        * Macedonian: {{t|mk|слободен}}
        * Malay: {{t+|ms|merdeka}}
        * Maori: {{t|mi|māhorahora}}
        * Norman: {{t|nrf|libre}}
        * Norwegian: {{t+|no|fri}}, {{t+|no|løs}}
        * Novial: {{t|nov|liberi}}
        * Old English: {{t|ang|frēo}}
        * Persian: {{t+|fa|آزاد|tr=âzâd}}
        * Polish: {{t+|pl|wolny}}, {{t+|pl|swobodny}}
        * Portuguese: {{t+|pt|livre}}
        * Romanian: {{t+|ro|liber}}, {{t|ro|neîmpiedicat}}
        * Russian: {{t+|ru|свобо́дный}}
        * Scottish Gaelic: {{t|gd|saor}}
        * Serbo-Croatian:
        *: Roman: {{t+|sh|povoljno}}, {{t+|sh|voljno}}, {{t+|sh|neograničen}}, {{t+|sh|slobodan}}
        * Sindhi: {{t|sd|چٽل}}
        * Sorbian:
        *: Lower Sorbian: {{t|dsb|lichy}}
        * Spanish: {{t+|es|libre}}
        * Swedish: {{t+|sv|fri}}
        * Turkish: {{t+|tr|serbest}}
        * Vietnamese: {{t+|vi|tự do}}
        * Welsh: {{t+|cy|rhydd}}
        * Yiddish: {{t|yi|פֿרײַ}}
        * Zazaki: {{t|zza|serbest}}
        {{trans-bottom}}

        {{trans-top|mathematics: unconstrained}}
        * Czech: {{t+|cs|volný}}
        * Finnish: {{t+|fi|vapaa}}
        * Norwegian: {{t+|no|fri}}
        {{trans-mid}}
        * Polish: {{t+|pl|wolny}}
        * Portuguese: {{t+|pt|livre}}
        * Romanian: {{t+|ro|liber}}, {{t|ro|nelegat}}
        {{trans-bottom}}

        {{trans-top|unobstructed}}
        * Albanian: {{t+|sq|lirë}}
        * Azerbaijani: {{t|az|maneə törədilməmiş}}
        * Catalan: {{t+|ca|lliure}}
        * Chinese:
        *: Mandarin: {{t+|cmn|通暢|alt=通暢的}}, {{t+|cmn|通畅|tr=tōngchàng de|alt=通畅的}}, {{t+|cmn|順暢|alt=順暢的}}, {{t+|cmn|順畅|tr=shùnchàng de|alt=順畅的}}
        * Czech: {{t+|cs|volný|m}}
        * Dutch: {{t+|nl|vrij}}, {{t+|nl|open}}
        * Esperanto: {{t+|eo|libera}}
        * Estonian: {{t|et|piiramatu}}, {{t|et|takistamatu}}
        * Finnish: {{t+|fi|auki}} {{qualifier|adverb}}, {{t|fi|aukinainen}}, {{t+|fi|avoin}}, {{t|fi|esteetön}}, {{t+|fi|selvä}}
        * French: {{t+|fr|libre}}
        * German: {{t+|de|frei}}
        * Greek: {{t+|el|ελεύθερος|m}}, {{t+|el|ανεμπόδιστος|m}}
        * Hebrew: {{t|he|פָּנוּי|tr=panúy}}
        * Hindi: {{t+|hi|खुला|sc=Deva}}
        * Ido: {{t+|io|libera}}
        * Interlingua: {{t+|ia|libere}}, {{t+|ia|franc}}
        * Italian: {{t+|it|libero|m}}
        * Japanese: {{t|ja|[[その]][[まま]]の|tr=sono mama no}}
        * Korean: {{t|ko|막힘|alt=막힘없는}}
        * Kurdish:
        *: Kurmanji: {{t+|kmr|vekirî}}, {{t+|kmr|vebûyî}}
        * Limburgish: {{t+|li|vrie}}
        {{trans-mid}}
        * Low German:
        *: German Low German: {{t|nds-de|free}}
        * Macedonian: {{t|mk|непречен}}
        * Maori: {{t|mi|māhorahora}}
        * Norman: {{t|nrf|libre}}
        * Norwegian: {{t+|no|åpen}}, {{t+|no|fri}}
        * Novial: {{t|nov|liberi}}
        * Polish: {{t+|pl|wolny}}, {{t+|pl|swobodny}}
        * Portuguese: {{t+|pt|livre}}
        * Romanian: {{t+|ro|liber}}, {{t|ro|neîmpiedicat}}
        * Russian: {{t+|ru|беспрепя́тственный}}, {{t+|ru|свобо́дный}}
        * Scottish Gaelic: {{t|gd|saor}}
        * Serbo-Croatian:
        *: Roman: {{t+|sh|slobodan}}, {{t+|sh|otvoren}}
        * Sindhi: {{t|sd|خلاصو}}
        * Slovene: {{t+|sl|prost}}
        * Sorbian:
        *: Lower Sorbian: {{t|dsb|lichy}}
        * Spanish: {{t+|es|libre}}, {{t+|es|obstáculo|alt=sin obstáculos}}, {{t+|es|despejado}}
        * Telugu: {{t|te|అడ్డగించని}}
        * Turkish: {{t+|tr|engellenmemiş}}
        * Yiddish: {{t|yi|פֿרײַ}}
        {{trans-bottom}}

        {{trans-top|not in use}}
        * Arabic: {{t|ar|شَاغِر}}
        *: Egyptian Arabic: {{t|arz|فاضى|tr=fāḍi}}
        * Armenian: {{t+|hy|ազատ}}
        * Azerbaijani: {{t+|az|boş}}
        * Bashkir: {{t|ba|буш|sc=Cyrl}}
        * Bulgarian: {{t+|bg|незает|sc=Cyrl}}, {{t+|bg|неизползван|sc=Cyrl}}
        * Burmese: {{t+|my|အား|sc=Mymr}}
        * Catalan: {{t|ca|desocupat}}
        * Czech: {{t+|cs|volný}}
        * Finnish: {{t+|fi|vapaa}}
        * French: {{t+|fr|libre}}, {{t+|fr|disponible}}
        * German: {{t+|de|frei}}, {{t|de|unbesetzt}}
        * Greek: {{t+|el|ελεύθερος|m}}
        * Latvian: {{t|lv|brīvs}}
        {{trans-mid}}
        * Macedonian: {{t|mk|слободен}}
        * Norman: {{t|nrf|libre}}
        * Norwegian: {{t|no|ledig}}
        * Persian: {{t+|fa|آزاد|tr=âzâd}}, {{t+|fa|بی کار|tr=bikâr}}
        * Polish: {{t+|pl|wolny}}
        * Portuguese: {{t+|pt|vago}}, {{t+|pt|livre}}, {{t+|pt|desocupado}}
        * Romanian: {{t+|ro|liber}}, {{t+|ro|neocupat}}
        * Russian: {{t+|ru|свобо́дный}}, {{t+|ru|неза́нятый}}
        * Spanish: {{t+|es|libre}}, {{t+|es|desocupado}}
        * Swedish: {{t+|sv|ledig}}
        * Telugu: {{t|te|ఉపయోగించని}}
        * Thai: {{t+|th|ว่าง}}
        * Turkish: {{t+|tr|boş}}
        * Yiddish: {{t|yi|פֿרײַ}}
        * Zazaki: {{t|zza|veng}}, {{t|zza|bêkar}}, {{t|zza|azad}}
        {{trans-bottom}}

        {{trans-top|without obligations}}
        * Albanian: {{t+|sq|pazënë}}
        * Armenian: {{t+|hy|ազատ}}
        * Azerbaijani: {{t|az|çətininsiz}}
        * Bambara: {{t|bm|hɔrɔn}}
        * Bashkir: {{t|ba|буш|sc=Cyrl}}, {{t|ba|ирекле|sc=Cyrl}}
        * Bulgarian: {{t+|bg|свободен|sc=Cyrl}}
        * Burmese: {{t+|my|အား|sc=Mymr}}
        * Catalan: {{t+|ca|lliure}}
        * Chinese:
        *: Mandarin: {{t+|cmn|自由|tr=zìyóu de|alt=自由的}}, {{t+|cmn|空閒}}, {{t+|cmn|空閑}}, {{t+|cmn|空闲|tr=kòngxián}}
        * Czech: {{t+|cs|volný}}
        * Danish: {{t+|da|fri}}
        * Dutch: {{t+|nl|vrij}}, {{t+|nl|ongedwongen}}
        * Esperanto: {{t+|eo|libera}}
        * Estonian: {{t+|et|vaba}}
        * Finnish: {{t+|fi|vapaa}}
        * French: {{t+|fr|libre}}
        * German: {{t+|de|frei}}, {{t|de|ungebunden}}
        * Greek: {{t+|el|ελεύθερος|m}}
        * Hebrew: {{t|he|פָּנוּי|tr=panúy}}, {{t|he|חופשי|tr=khofshí|alt=חופשי / חָפְשִׁי}}
        * Hungarian: {{t+|hu|szabad}}
        * Ido: {{t+|io|libera}}
        * Interlingua: {{t+|ia|libere}}
        * Irish: {{t|ga|saor}}
        *: Old Irish: {{t|sga|sóer}}
        * Italian: {{t+|it|libero}}
        * Japanese: {{t+|ja|自由|tr=じゆうな, jiyū na|alt=自由な}}
        * Korean: {{t+|ko|자의}}, {{t+|ko|자유롭다}}
        * Kurdish:
        *: Kurmanji: {{t+|kmr|azad}}, {{t+|kmr|serbest}}
        {{trans-mid}}
        * Latvian: {{t|lv|brīvs}}
        * Limburgish: {{t+|li|vrie}}
        * Macedonian: {{t|mk|слободен}}
        * Maori: {{t|mi|māhorahora}}
        * Ngazidja Comorian: {{t|zdj|nafasi|alt=na nafasi}}
        * Norman: {{t|nrf|libre|m|f}}
        * Norwegian: {{t+|no|fri}}, {{t|no|ledig}}
        * Novial: {{t|nov|liberi}}
        * Old English: {{t|ang|frēo}}
        * Polish: {{t+|pl|wolny}}
        * Portuguese: {{t+|pt|livre}}
        * Quechua: {{t|qu|qasi}}
        * Romanian: {{t+|ro|liber|m}}
        * Russian: {{t+|ru|свобо́дный}}
        * Scottish Gaelic: {{t|gd|saor}}
        * Serbo-Croatian:
        *: Roman: {{t|sh|bezobavezno}}, {{t+|sh|slobodan}}
        * Sindhi: {{t|sd|فارِغ}}, {{t+|sd|واندو}}
        * Slovene: {{t+|sl|prost}}
        * Sorbian:
        *: Lower Sorbian: {{t|dsb|lichy}}
        * Spanish: {{t+|es|libre}}, {{t+|es|exento}}
        * Swedish: {{t+|sv|fri}}
        * Telugu: {{t|te|నిబంధన లేని}}
        * Thai: {{t+|th|ว่าง}}
        * Turkish: {{t+|tr|serbest}}, {{t|tr|zorunsuz}}
        * Vietnamese: {{t+|vi|rỗi}}
        * Yiddish: {{t|yi|פֿרײַ}}
        {{trans-bottom}}

        {{trans-top|software: with very few limitations on distribution or improvement}}
        * Albanian: {{t|sq|lejuar}}
        * Azerbaijani: {{t+|az|azad}}
        * Bambara: {{t|bm|hɔrɔn}}
        * Bashkir: {{t|ba|түләүһеҙ|sc=Cyrl}}
        * Bulgarian: {{t+|bg|безплатен|sc=Cyrl}}
        * Catalan: {{t+|ca|lliure}}
        * Chinese:
        *: Mandarin: {{t+|cmn|自由|tr=zìyóu de|alt=自由的}}
        * Czech: {{t+|cs|svobodný}}
        * Danish: {{t+|da|fri}}
        * Dutch: {{t+|nl|vrij}}, {{t+|nl|vrije}}
        * Esperanto: {{t+|eo|libera}}
        * Estonian: {{t+|et|vaba}}
        * Finnish: {{t+|fi|avoin}}, {{t+|fi|vapaa}}
        * French: {{t+|fr|libre}}
        * German: {{t+|de|frei}}
        * Greek: {{t+|el|ελεύθερος}}
        * Hebrew: {{t|he|חופשי|tr=khofshí|alt=חופשי / חָפְשִׁי}}
        * Ido: {{t+|io|libera}}
        * Interlingua: {{t+|ia|libere}}
        * Irish: {{t|ga|saor}}
        * Italian: {{t+|it|libero}}, {{t+|it|free}}, {{t+|it|libre}} {{gloss|software}}
        {{trans-mid}}
        * Japanese: {{t+|ja|フリー|tr=furī}}
        * Korean: {{t+|ko|자유}}
        * Kurdish:
        *: Kurmanji: {{t+|kmr|azad}}, {{t+|kmr|vekirî}}, {{t+|kmr|serbest}}
        * Limburgish: {{t+|li|vrie}}
        * Lithuanian: {{t+|lt|nemokama}}
        * Macedonian: {{t|mk|слободен}}
        * Norwegian: {{t+|no|fri}}
        * Novial: {{t|nov|liberi}}
        * Polish: {{t+|pl|wolny}}
        * Portuguese: {{t+|pt|livre}}
        * Romanian: {{t+|ro|gratuit}}, {{t+|ro|liber}}
        * Russian: {{t+|ru|свободный}}
        * Serbo-Croatian:
        *: Roman: {{t+|sh|slobodan}}
        * Sindhi: {{t|sd|کليل}}
        * Spanish: {{t+|es|libre}}
        * Swedish: {{t+|sv|fri}}
        * Telugu: {{t|te|ఉచిత దిగుమతి}}
        * Turkish: {{t+|tr|özgür}}
        * Zazaki: {{t|zza|xoser}}
        {{trans-bottom}}

        {{trans-top|without}}
        * Armenian: {{t+|hy|ազատ}}
        * Bashkir: {{t|ba|-һыҙ|sc=Cyrl}} / {{t|ba|-һеҙ|sc=Cyrl}}, {{t|ba|-һоҙ|sc=Cyrl}} / {{t|ba|-һөҙ|sc=Cyrl}}
        * Burmese: {{t+|my|လွတ်လပ်|sc=Mymr}}
        * Czech: {{t+|cs|prostý}}
        * Dutch: {{t+|nl|zonder}}, {{t|nl|-vrij}}
        * Finnish: {{t+|fi|-ton}}, {{t|fi|[[ilman]] ([[jotakin]])}}, {{t+|fi|vapaa|alt=-vapaa}}
        * French: {{t+|fr|sans}}
        * German: {{t+|de|frei}}
        * Hebrew: {{t+|he|בְּלְי|sc=Hebr}}
        * Indonesian: {{t+|id|bebas}}, {{t+|id|tanpa}}
        * Irish: {{t+|ga|gan}}
        {{trans-mid}}
        * Low German:
        *: German Low German: {{t|nds-de|free}}
        * Macedonian: {{t|mk|без-}}, {{t|mk|бес-}}
        * Malay: {{t|ms|tanpa}}
        * Norwegian: {{t+|no|fri}}, {{t+|no|uten}}
        * Persian: {{t+|fa|بدون|sc=fa-Arab}}
        * Polish: {{t+|pl|bez}}, {{t+|pl|wolny}}
        * Portuguese: {{t+|pt|semideus}}
        * Sorbian:
        *: Lower Sorbian: {{t|dsb|lichy}}
        * Telugu: {{t+|te|లేకుండా}}
        * Zazaki: {{t|zza|berdos}}
        {{trans-bottom}}

        {{trans-top|programming: not bound}}
        * Czech: {{t+|cs|volný}}
        * Finnish: {{t+|fi|riippumaton}}
        {{trans-mid}}
        * Portuguese: {{t+|pt|livre}}
        * Telugu: {{t|te|పరిమితి లేని}}
        {{trans-bottom}}

        {{trans-top|mycology: not attached to the stipe}}
        * Azerbaijani: {{t+|az|zəif}}
        * Finnish: {{t|fi|irtonainen}}
        {{trans-mid}}
        * Turkish: {{t+|tr|gevşek}}
        * Zazaki: {{t|zza|sıst}}
        {{trans-bottom}}

        {{checktrans-top}}
        * Albanian: {{qualifier|i/e}} {{t+check|sq|lirë}}, {{t+check|sq|pa}}
        * German: {{t+check|de|entlassen}}, {{t+check|de|befreit}}, {{t-check|de|frei von}}
        * Interlingua: {{t+check|ia|libere}}
        * Italian: {{t+check|it|senza}}
        * Lithuanian: {{qualifier|3}} {{t+check|lt|be}}, {{qualifier|4}} {{t-check|lt|neribotas}}
        * Low German: {{t-check|nds|leddig}}, {{t-check|nds|ledig}}
        * Occitan: {{qualifier|1,3}} {{t+check|oc|liure}}, {{qualifier|2}} {{t+check|oc|dobèrt}}, {{qualifier|5}} {{t-check|oc|gratis}}, {{qualifier|5}} {{t-check|oc|gratuït}}
        {{trans-mid}}
        * Serbo-Croatian:
        *: Roman: {{t+check|sh|slobodan}} {{q|1}}, {{t+check|sh|besplatan}} {{q|5}}, {{t-check|sh|oslobođen}}, {{t+check|sh|pušten}}
        * Slovak: {{t-check|sk|slobodný}}, {{t+check|sk|bezplatný}}, {{qualifier|1}} {{t-check|sk|slobodný}}, {{qualifier|1|2|4}} {{t-check|sk|voľný}}, {{qualifier|5}} {{t+check|sk|bezplatný}}
        * Swedish: {{t+check|sv|fri}}, {{t+check|sv|lös}}, {{t+check|sv|släppt}}
        * Tamil: {{t+check|ta|இலவசம்}}
        * Volapük: {{t+check|vo|libik}}, {{t+check|vo|livik}}
        * West Frisian: {{t-check|fy|frijlitten}}, {{t-check|fy|befrijt}}
        {{trans-bottom}}

        ===Adverb===
        {{en-adv}}

        # Without needing to [[pay]].
        #: {{ux|en|I got this bike '''free'''.}}
        #: {{syn|en|for free|for nothing}}
        # {{lb|en|obsolete}} Freely; willingly.
        #* {{quote-book|en|title=[[w:Henry VIII (play)|Henry VIII]]|authorlink=William Shakespeare|year=c. 1601–1602|year_published=1623|passage=I as '''free''' forgive you / As I would be forgiven.}}

        ====Translations====
        {{trans-top|without needing to pay}}
        * Albanian: {{t+|sq|falas}}
        * Armenian: {{t+|hy|անվճար}}, {{t+|hy|ձրի}}
        * Bulgarian: {{t+|bg|безплатно|sc=Cyrl}}
        * Catalan: {{t+|ca|gratis}}, {{t+|ca|gratuïtament}}
        * Chukchi: {{t|ckt|эркуркэ|tr=ėrkurkė}}
        * Czech: {{t|cs|zadarmo}}
        * Danish: {{t+|da|gratis}}
        * Dutch: {{t+|nl|gratis}}
        * Finnish: {{t+|fi|ilmaiseksi}}
        * French: {{t+|fr|gratuitement}}, &lt;!--{{qualifier|informal}}--&gt; {{t+|fr|gratis}}, &lt;!--{{qualifier|informal}}--&gt; {{t+|fr|gratos}}
        * German: {{t+|de|gratis}}, {{t+|de|umsonst}}
        * Hindi: {{t|hi|मुफ़्त|sc=Deva}}
        * Hungarian: {{t+|hu|ingyen}}
        * Icelandic: {{t+|is|ókeypis}}
        * Indonesian: {{t+|id|gratis}}, {{t+|id|cuma-cuma}}
        * Irish: {{t|ga|saor}}
        * Italian: {{t+|it|gratuitamente}}
        * Kabuverdianu: {{t|kea|fabal}}
        {{trans-mid}}
        * Latin: {{t|la|grātīs}}
        * Latvian: {{t|lv|bezmaksas}}
        * Macedonian: {{t|mk|бесплатно}}
        * Maori: {{t+|mi|utukore}}
        * Navajo: {{t|nv|tʼáá jííkʼe}}, {{t|nv|tʼáadoo bą́ą́h ílíní da}}
        * Norwegian: {{t+|no|gratis}}
        * Polish: {{t+|pl|za darmo}}, {{t+|pl|bezpłatnie}}
        * Portuguese: {{t+|pt|grátis}}, {{t|pt|de graça}}, {{t+|pt|gratuitamente}}
        * Russian: {{t+|ru|беспла́тно}}, {{t+|ru|да́ром}}
        * Scottish Gaelic: {{t|gd|an asgaidh}}
        * Spanish: {{t+|es|gratis}}
        * Swedish: {{t+|sv|gratis}}
        * Telugu: {{t|te|చెల్లించనవసరం లేని}}
        * Thai: {{t+|th|ฟรี}}
        * Turkish: {{t+|tr|bedava}}
        * Yiddish: {{t|yi|בחינם|tr=bkhinem|sc=Hebr}}
        * Zazaki: {{t|zza|berdos}}
        {{trans-bottom}}

        ===Verb===
        [[File:Peter Paul Rubens - Perseus Freeing Andromeda - WGA20306.jpg|thumb|A painting depicting mythical Greek hero Perseus '''freeing''' Andromeda, who was imprisoned by a sea monster]]
        {{en-verb|d}}

        # {{lb|en|transitive}} To make free; set at [[liberty]]; [[release]].
        #* {{RQ:Shakespeare Tempest|I|ii|page=5|passage={{w|Prospero|''Pro.''}}{{...}}{{w|Ariel (The Tempest)|Spirit}}, fine ſpirit, [[I'll|Ile]] '''free''' thee / Within two dayes for this.}}
        # {{lb|en|transitive}} To [[rid]] of something that confines or oppresses.
        #* '''1885''', {{w|Richard F. Burton}}, ''{{w|The Book of the Thousand Nights and a Night}}'', Night 564:
        #*: Then I walked about, till I found on the further side, a great river of sweet water, running with a strong current; whereupon I called to mind the boat-raft I had made aforetime and said to myself, &quot;Needs must I make another; haply I may '''free''' me from this strait. If I escape, I have my desire and I vow to Allah Almighty to forswear travel; and if I perish I shall be at peace and shall rest from toil and moil.&quot;

        ====Derived terms====
        * {{l|en|befree}}

        ====Synonyms====
        * {{l|en|befree}}
        * {{l|en|emancipate}}
        * {{l|en|let loose}}
        * {{l|en|liberate}}
        * {{l|en|manumit}}
        * {{l|en|release}}
        * {{l|en|unchain}}
        * {{l|en|unfetter}}
        * {{l|en|unshackle}}

        ====Translations====
        {{trans-top|make free}}
        * Afrikaans: {{t|af|bevry}}, {{t|af|loslaat}}, {{t|af|laat gaan}}
        * Albanian: {{t+|sq|liroj}}
        * Arabic: {{t+|ar|حَرَّرَ}}
        *: Egyptian Arabic: {{t|arz|يحرر|tr=yeḥarrar}}
        * Armenian: {{t+|hy|ազատել}}
        * Belarusian: {{t|be|вызваля́ць|impf}}, {{t|be|вы́зваліць|pf}}
        * Bulgarian: {{t+|bg|освобожда́вам|impf}}, {{t|bg|освободя́|pf}}
        * Catalan: {{t+|ca|alliberar}}
        * Chinese:
        *: Mandarin: {{t+|cmn|解放|tr=jiěfàng|sc=Hani}}
        * Czech: {{t|cs|osvobozovat|impf}}, {{t+|cs|osvobodit|pf}}
        * Danish: {{t|da|befri}}, {{t|da|fritage}}, {{t|da|løslade}}
        * Dutch: {{t+|nl|bevrijden}}, {{t+|nl|loslaten}}, {{t|nl|laten gaan}}
        * Esperanto: {{t|eo|liberi}}, {{t|eo|liberigi}}
        * Estonian: {{t+|et|vabastama}}, {{t|et|vabaks laskma}}
        * Finnish: {{t+|fi|vapauttaa}}, {{t|fi|[[päästää]] [[vapaa|vapaaksi]]}}
        * French: {{t+|fr|libérer}}, {{t+|fr|dégager}}, {{t+|fr|affranchir}}
        * Galician: {{t+|gl|liberar}}
        * German: {{t+|de|befreien}}, {{t+|de|freisetzen}} {{qualifier|free someone from prison}}
        * Greek: {{t+|el|ελευθερώνω}}
        * Hebrew: {{t+|he|שחרר|tr=shikhrér|alt=שיחרר / שִׁחְרֵר}}
        * Hindi: {{t|hi|मुक्त करना}}
        * Ido: {{t+|io|libereskar}}
        * Indonesian: {{t+|id|membebaskan}}, {{t+|id|memerdekakan}}
        * Interlingua: {{t|ia|liberar}}
        * Irish: {{t|ga|saoraigh}}
        * Italian: {{t+|it|liberare}}
        * Japanese: {{t+|ja|解放|tr=かいほうする, kaihō suru|alt=解放する}}
        * Korean: {{t+|ko|해방하다}} ({{t+|ko|解放}} + {{t+|ko|하다}})
        * Kurdish:
        *: Sorani: {{t+|ku|ڕزگار کردن|sc=Arab}}
        {{trans-mid}}
        * Latin: {{t|la|liberare}}
        * Latvian: {{t|lv|atbrīvot}}, {{t|lv|atsvabināt}}
        * Lithuanian: {{t|lt|išlaisvinti}}
        * Macedonian: {{t|mk|ослободува|impf}}, {{t|mk|ослободи|pf}}
        * Maori: {{t+|mi|whakawātea}}, {{t|mi|wewete}}, {{t|mi|kokiro}} {{qualifier|from a spell or ritual }}
        * Norman: {{t|nrf|libéther}}
        * Norwegian: {{t+|no|frigjøre}}, {{t|no|frigi}}, {{t|no|befri}}, {{t|no|løslate}}
        * Occitan: {{t+|oc|desliurar}}
        * Old English: {{t|ang|frēoġan}}
        * Persian: {{t|fa|آزاد ساختن|tr=âzâd sâxtan}}, {{t+|fa|آزاد کردن|tr=âzâd kardan|sc=fa-Arab}}
        * Polish: {{t+|pl|uwalniać|impf}}, {{t+|pl|uwolnić|pf}}, {{t+|pl|wyzwalać|impf}}, {{t+|pl|wyzwolić|pf}}, {{t|pl|oswabadzać|impf}}, {{t|pl|oswobodzić|pf}}
        * Portuguese: {{t+|pt|libertar}}, {{t+|pt|livrar}}, {{t+|pt|soltar}}
        * Romanian: {{t+|ro|elibera}}
        * Russian: {{t+|ru|освобожда́ть|impf}}, {{t+|ru|освободи́ть|pf}}, {{t+|ru|вызволя́ть|impf}}, {{t+|ru|вы́зволить|pf}}
        * Serbo-Croatian:
        *: Cyrillic: {{t|sh|ослобађати|impf}}, {{t|sh|ослободити|pf}}
        *: Roman: {{t+|sh|oslobađati|impf}}, {{t+|sh|osloboditi|pf}}
        * Slovak: {{t|sk|oslobodzovať|impf}}, {{t+|sk|oslobodiť|pf}}
        * Slovene: {{t|sl|osvobajati|impf}}, {{t|sl|osvoboditi|pf}}
        * Spanish: {{t+|es|librar}}
        * Swedish: {{t+|sv|frigöra}}, {{t+|sv|befria}}, {{t+|sv|frita}}(ga) &lt;!--{{t+|sv|fria}}: Someone please give an example of this?---&gt;
        * Telugu: {{t|te|విడుదల చేయు}}
        * Thai: {{t+|th|ปลดปล่อย}}
        * Turkish: {{t+|tr|serbest bırakmak}}
        * Ukrainian: {{t|uk|звільня́ти|impf}}, {{t|uk|звільни́ти|pf}}, {{t|uk|визволя́ти|impf}}, {{t|uk|ви́зволити|pf}}
        * Vietnamese: {{t+|vi|giải phóng}} ({{t|vi|解放}})
        * Welsh: {{t+|cy|rhyddhau}}
        * Westrobothnian: {{t|gmq-bot|frij}}
        * Yiddish: {{t|yi|באַפֿרײַען|sc=Hebr}}
        {{trans-bottom}}

        ===Noun===
        {{en-noun}}

        # {{lb|en|Australian rules football|Gaelic football}} {{abbreviation of|en|free kick}}
        #* '''2006''', [http://footballlegends.org/daryn_cresswell.htm]:
        #*: Whether deserved or not, the '''free''' gave Cresswell the chance to cover himself in glory with a shot on goal after the siren. &lt;!-- a typical, but not especially notable usage here, feel '''free''' (pun intended) to replace with a better one --&gt;
        # [[free transfer]]
        #* {{quote-journal
        |en
        |date=September 21, 2011
        |author=Sam Lyon
        |title=Man City 2 - 0 Birmingham
        |work=BBC Sport
        |url=http://news.bbc.co.uk/sport2/hi/football/14910208.stm
        |page=
        |passage=Hargreaves, who left Manchester United on a '''free''' during the summer, drilled a 22-yard beauty to open the scoring.}}
        # {{lb|en|hurling}} The usual means of restarting play after a foul is committed, where the non-offending team restarts from where the foul was committed.

        ====Translations====
        &lt;!-- Only abbreviated forms here (if they exist), please --&gt;
        {{trans-top|abbreviation of free kick}}
        * Finnish: {{t+|fi|vapari}}
        {{trans-mid}}
        * German: {{t+|de|Freistoss}}
        {{trans-bottom}}

        {{trans-top|hurling}}
        * Irish: {{qualifier|hurling}} {{t|ga|poc saor|m}}
        {{trans-mid}}
        {{trans-bottom}}

        {{checktrans-top}}
        * Ghotuo: {{t|aaa|koola}}&lt;!--was in the &quot;abbrev of free kick&quot; section, but I suspect it and other aaa translations may have been added as nonsense using the trans-adder; it was added by an IP from India; restore it if you can verify it; -sche--&gt;
        {{trans-mid}}
        {{trans-bottom}}

        ===References===
        &lt;references/&gt;

        ===Anagrams===
        * {{anagrams|en|a=eefr|feer|fere|reef}}

        [[Category:English basic words]]
        [[Category:en:Money]]

        ----

        ==Galician==

        ===Verb===
        {{gl-verb-form}}

        # {{inflection of|gl|frear||1|s|pres|subj}}
        # {{inflection of|gl|frear||3|s|pres|subj}}

        ----

        ==Low German==

        ===Alternative forms===
        * {{l|nds|frie}} {{q|more common}}

        ===Etymology===
        From {{inh|nds|gml|vrîe}}, variant of {{m|gml|vrî}}, from {{der|nds|osx|frī}}, from {{der|nds|gem-pro|*frijaz}}, from {{der|nds|ine-pro|*prey||new}}. Compare {{cog|nl|vrij}}, {{cog|fy|frij}}, {{cog|en|free}}, {{cog|de|frei}}.

        ===Adjective===
        {{head|nds|adjective|comparative|fre'er|superlative|freest}}

        # {{lb|nds|rather rare}} [[free]]

        ====Declension====
        {{nds-decl-adj|head=free|free|fre'|Fre'e|fre'er|freest|Freest}}

        ====Derived terms====
        * {{l|nds|Freeheit}}
        """
    expected = {'pos': {
        'adjective': ['unconstrained.', 'Obtainable without any payment.', 'Without; not containing (what is specified); exempt; clear; liberated.', 'Ready; eager; acting without spurring or whipping; spirited.', 'Invested with a particular freedom or franchise; enjoying certain immunities or privileges; admitted to special rights; followed by of.', 'Certain or honourable; the opposite of base.', 'Privileged or individual; the opposite of common.'], 
        'adverb': ['Without needing to pay.', 'Freely; willingly.'], 
        'verb': ['To make free; set at liberty; release.', 'To rid of something that confines or oppresses.'], 
        'noun': ['free transfer', 'The usual means of restarting play after a foul is committed, where the non-offending team restarts from where the foul was committed.']
        }, 
        'IPA': 'fɹiː', 
        'File': 'Free Beer.jpg'}
    actual = parse_wikitext(text, 'IPA', 'en', 'File') 
    assert actual == expected


def test_free_noun():
    text = """
            ===Noun===
            {{en-noun}}
    
            # {{lb|en|Australian rules football|Gaelic football}} {{abbreviation of|en|free kick}}
            #* '''2006''', [http://footballlegends.org/daryn_cresswell.htm]:
            #*: Whether deserved or not, the '''free''' gave Cresswell the chance to cover himself in glory with a shot on goal after the siren. &lt;!-- a typical, but not especially notable usage here, feel '''free''' (pun intended) to replace with a better one --&gt;
            # [[free transfer]]
            #* {{quote-journal
            |en
            |date=September 21, 2011
            |author=Sam Lyon
            |title=Man City 2 - 0 Birmingham
            |work=BBC Sport
            |url=http://news.bbc.co.uk/sport2/hi/football/14910208.stm
            |page=
            |passage=Hargreaves, who left Manchester United on a '''free''' during the summer, drilled a 22-yard beauty to open the scoring.}}
            # {{lb|en|hurling}} The usual means of restarting play after a foul is committed, where the non-offending team restarts from where the foul was committed.
    
            ====Translations====
    """
    actual = parse_wikitext(text, 'IPA', 'en', 'File') 
    assert actual == {'pos': {
        'noun': ['free transfer', 'The usual means of restarting play after a foul is committed, where the non-offending team restarts from where the foul was committed.']
    }}

def test_simple_text():
    text = """
==English==

===Alternative forms===
* {{l|en|Pope July}}
* {{l|en|Pope Julio}}

===Etymology===
Unknown. Presumably named after [[w:Pope Julius II|Pope Julius II]], the Warrior Pope.

===Proper noun===
{{en-proper noun}}

# {{lb|en|obsolete}} A sixteenth-century [[gambling]] [[card game]] about which little is known.
#* {{quote-book|en|year=1525|author=[[w:John Skelton|John Skelton]]|url=http://books.google.com/books?id=H1g1AAAAMAAJ|title=Speke, Parrot
|passage=Of '''Pope Julius''' cardys he ys chefe cardynall.}}
#* {{quote-book|en|date=November 30, 1532|title=Privy Purse Expences of King Henry VIII, 30 Novembre 1532
|passage=Item the laste day delived unto the kings grace whiche his grace lost at '''pope July''' game wt my lady marquess and m Weston xvj cor}}
#* {{quote-book|en|year={{circa2|1596|short=yes}}|author=Sir John Harington|title=A Treatise on Playe|quoted_in=Nugae antiquae|year_published=1804
|passage='''Pope Julio''' (if I fail not in the name, and sure I am that there is a game of the cards after his name) was a great and wary player, a great vertue in a man of his profession}}

[[Category:en:Card games]]
"""
    actual = parse_wikitext(text, 'IPA', 'en', 'File') 
    expected = {'pos': {'proper noun': ['A sixteenth-century gambling card game about which little is known.']}}
    assert actual == expected

def test_simple_text_2():
    text = """
==English==

===Etymology===
From {{der|en|la|accendere||to kindle}}, formed from {{m|la|ad-}} + {{m|la|candere||to shine}}.

===Pronunciation===
* {{IPA|en|[ækˈsɛnd]}}

===Verb===
{{en-verb}}

# {{lb|en|transitive|obsolete}} To set on [[fire]]; to [[kindle]].

===Anagrams===
* {{anagrams|en|a=accden|Deccan}}

[[Category:English words prefixed with ad-]]
[[Category:en:Fire]]
"""
    actual = parse_wikitext(text, 'IPA', 'en', 'File') 
    expected = {'IPA': 'ækˈsɛnd', 'pos': {'verb': ['To set on fire; to kindle.']}}
    #print('debug: ', actual)
    assert actual == expected

def test_word_checkmate():
    text = """
==English==

===Etymology===
From {{inh|en|enm|chekmat}}, from {{der|en|fro|eschec mat}}, from {{der|en|ar|شَاهُ مَاتَ}}, from {{der|en|fa|شاه مات|tr=šâh mât|t=the king [is] amazed}}.

===Pronunciation===
* {{IPA|en|/ˈt͡ʃɛkmeɪt/}}
* {{audio|en|En-us-checkmate.ogg|Audio (US)}}
* {{rhymes|en|eɪt}}

===Interjection===
{{en-interj}}

# {{lb|en|chess}} Word called out by the [[victor]] when making a move that wins the game.

====Synonyms====
* {{sense|chess}} [[mate#Interjection|mate]]

====Translations====
{{trans-top|said when making the conclusive move in chess}}
* Albanian: {{t|sq|shah mat}}
* Arabic: {{t|ar|مَات|m}}, {{t|ar|كِش مَلِك|m}}
*: Egyptian Arabic: {{t|arz|كش ملك|tr=kešš malek}}
* Armenian: {{t|hy|շախ և մատ}}, {{t+|hy|մատ}}
* Bengali: {{t|bn|কিস্তিমাত}}
* Bulgarian: {{t|bg|мат}}
* Catalan: {{t|ca|escac i mat}}
* Chinese:
*: Mandarin: {{t+|cmn|將死|sc=Hani}}, {{t+|cmn|将死|tr=jiāngsǐ|sc=Hani}}
* Czech: {{t+|cs|mat}}, {{t|cs|šach mat|m}}
* Danish: {{t|da|skakmat|c}}
* Dutch: {{t+|nl|schaakmat|n}}, {{t+|nl|mat|n}}
* Estonian: {{t|et|šahh ja matt}}
* Faroese: {{t|fo|skák og mát}}
* Finnish: {{t|fi|shakki ja matti}}
* French: {{t+|fr|échec et mat}}
* Galician: {{t+|gl|xaque mate}}
* Georgian: {{t|ka|შამათი}}
* German: {{t+|de|schachmatt}}, {{t|de|schach und matt}}
* Greek: {{t+|el|ματ|sc=Grek}}
* Hebrew: {{t+|he|מט|tr=mat|sc=Hebr}}
* Hindi: {{t+|hi|मात|tr=māt|sc=Deva}}
* Hungarian: {{t+|hu|sakk-matt}}
{{trans-mid}}
* Italian: {{t+|it|scacco matto}}
* Japanese: {{t|ja|チェックメイト|tr=chekkumeito}}, {{t+|ja|詰み|tr=つみ, tsumi}}
* Kalmyk: {{t|xal|мад}}
* Khmer: {{t|km|ស្លាប់ក្រឡា|tr=slap krɑlaa}}
* Macedonian: {{t|mk|шах-мат}}, {{t|mk|мат}}
* Malay: {{t|ms|syahmat}}
* Maori: {{t|mi|whakamiere}}
* Norwegian: {{t|no|sjakkmatt}}
* Persian: {{t|fa|کیش و مات|tr=kiš-o-mât}}, {{t+|fa|شاه مات|tr=šâh mât}}, {{t+|fa|شهمات|tr=šahmât}}, {{t+|fa|مات|tr=mât}}
* Polish: {{t+|pl|mat|m}}, {{t|pl|szach mat}}, {{t|pl|szach i mat}}
* Portuguese: {{t+|pt|xeque-mate|m}}
* Romanian: {{t|ro|șah mat}}
* Russian: {{t+|ru|мат|m}}, {{t|ru|шах и мат}}
* Serbo-Croatian:
*: Cyrillic: {{t|sh|шах-мат|sc=Cyrl}}, {{t|sh|мат|sc=Cyrl}}
*: Roman: {{t+|sh|šah-mat}}, {{t+|sh|mat}}
* Slovene: {{t|sl|šah mat}}, {{t|sl|mat}}
* Spanish: {{t|es|jaque mate}}
* Swedish: {{t+|sv|schackmatt}}
* Tagalog: {{t+|tl|mate}}
* Turkish: {{t+|tr|şah mat}}
* Ukrainian: {{t|uk|мат|m}}, {{t|uk|шах і мат}}
* Yiddish: {{t|yi|מאַט}}
{{trans-bottom}}

===Noun===
{{wikipedia}}
{{en-noun}}

# The conclusive [[victory]] in a game of [[chess]] that occurs when an opponent's [[king]] is [[threaten]]ed with unavoidable [[capture]].
# {{lb|en|figuratively|by extension}} Any losing situation with no [[escape]]; utter defeat.

====Related terms====
* {{l|en|stalemate}}

====Translations====
{{trans-top|conclusive victory in a game of chess}}
* Arabic: {{t|ar|شَاه مَات}}
* Armenian: {{t+|hy|շախմատ}}
* Bulgarian: {{t|bg|мат|m}}
* Chinese:
*: Mandarin: {{t+|cmn|將死}}, {{t+|cmn|将死|tr=jiāngsǐ}}
* Czech: {{t+|cs|mat|m}}
* Danish: {{t|da|skakmat}}, {{t+|da|mat}}
* Dutch: {{t+|nl|schaakmat}}, {{t+|nl|mat}}
* Esperanto: {{t|eo|ŝakmato}}
* Estonian: {{t|et|matt}}
* Faroese: {{t|fo|mát|n}}
* Finnish: {{t+|fi|matti}}
* French: {{t+|fr|échec et mat|m}}
* Galician: {{t+|gl|xaque mate|m}}
* Georgian: {{t|ka|შამათი}}
* German: {{t+|de|Schachmatt|n}}
* Greek: {{t+|el|ματ|n}}
* Hebrew: {{t+|he|מט|tr=mat}}
* Hungarian: {{t+|hu|sakk-matt}}, {{t+|hu|matt}}
{{trans-mid}}
* Italian: {{t+|it|scacco matto|m}}
* Japanese: {{t+|ja|詰み|tr=つみ, tsumi}}, {{t|ja|チェックメイト|tr=chekkumeito}}
* Korean: {{t|ko|체크 메이트}}
* Maori: {{t|mi|whakamiere}}
* Norwegian:
*: Bokmål: {{t|nb|sjakkmatt}}
*: Nynorsk: {{t|nn|sjakkmatt}}
* Persian: {{t|fa|کیش و مات|tr=kiš-o-mât}}, {{t+|fa|شهمات|tr=šahmât}}, {{t+|fa|مات|tr=mât}}
* Polish: {{t+|pl|mat|m}}
* Portuguese: {{t+|pt|xeque-mate|m}}
* Romanian: {{t|ro|șah-mat|n}}
* Russian: {{t|ru|шах и мат|m}}, {{t+|ru|мат|m}}
* Scottish Gaelic: {{t|gd|clos|m}}
* Slovak: {{t|sk|mat|m}}
* Slovene: {{t|sl|šah mat|m}}, {{t|sl|mat|m}}
* Spanish: {{t|es|jaque mate|m}}, {{t+|es|mate|m}}
* Swedish: {{t+|sv|matt|c}}, {{t+|sv|schack matt|c}}
* Ukrainian: {{t|uk|мат|m|sc=Cyrl}}
{{trans-bottom}}

{{trans-top|losing situation with no escape}}
* Bulgarian: {{t|bg|мат|m}}
* Chinese:
*: Mandarin: {{t|cmn|[[徹底]][[失敗]]}}, {{t|cmn|[[彻底]][[失败]]|tr=chèdǐ shībài}}
* Czech: {{t|cs|matová situace|f}}
* Estonian: {{t|et|lüüasaamine}}
* Finnish: {{t+|fi|nurkka}}, {{t+|fi|umpikuja}}
{{trans-mid}}
* German: {{t+|de|Schachmatt|n}}, {{t+|de|Niederlage|f}}
* Hungarian: {{t+|hu|patthelyzet}}, {{t+|hu|zsákutca}}, {{t|hu|[[vesztes]]/[[reménytelen]]/[[kilátástalan]] [[helyzet]]}}
* Persian: {{t|fa|کیش و مات|tr=kiš-o-mât}}
* Portuguese: {{t+|pt|xeque-mate|m}}
* Russian: {{t-needed|ru}}
* Slovak: {{t|sk|matová situácia|f}}
{{trans-bottom}}

{{checktrans-top}}
* {{ttbc|ko}}: {{t-check|ko|외통 장군}}
{{trans-mid}}
* Latin: {{t-check|la|latrunculusque matum}}
{{trans-bottom}}

===Verb===
{{en-verb|checkmat}}

# {{lb|en|transitive|chess}} To put the [[king]] of an opponent into checkmate.
#: {{ux|en|That jerk '''checkmated''' me in four moves!}}
# {{lb|en|transitive|by extension}} To place in a losing situation that has no escape.

====Translations====
{{trans-top|to put an opponent into checkmate}}
* Bulgarian: {{t+|bg|мати́рам}}
* Chinese:
*: Mandarin: {{t|cmn|[[把]]...[[將死]]}}, {{t|cmn|[[把]]...[[将死]]|tr=bǎ...jiāngsǐ}}
* Czech: {{t|cs|matovat}}, {{t|cs|dát mat}}
* Esperanto: {{t|eo|ŝakmatigi}}
* Faroese: {{t|fo|máta}}
* Finnish: {{t|fi|matittaa}}, {{t|fi|[[tehdä]] [[matti]]}}
* French: {{t|fr|[[faire]] [[échec et mat]]}}
* Georgian: {{t|ka|დაშამათება}} {{qualifier|verbal noun}}, {{t|ka|აშამათებს}} {{qualifier|infinitive}}
* Hungarian: {{t|hu|mattot ad}}, {{t+|hu|megmattol}}
{{trans-mid}}
* Italian: {{t|it|[[dare]] [[scacco matto]]}}
* Maori: {{t|mi|whakamiere}}
* Persian: {{t|fa|شهمات کردن|tr=šahmāt kardan}}, {{t+|fa|مات کردن|tr=māt kardan}}
* Polish: {{t|pl|zamatować|pf}}, {{t|pl|dać mata|pf}}
* Portuguese: {{t|pt|[[dar]] ([[o]]) [[xeque-mate]]}}
* Russian: {{t|ru|ста́вить мат|impf}}, {{t|ru|поста́вить мат|pf}}
* Scottish Gaelic: {{t|gd|cuir clos air}}
* Slovak: {{t|sk|dať šach mat}}
* Slovene: {{t|sl|matirati}}
* Swedish: {{t+|sv|schackmatta}}, {{t|sv|sätta matt}}, {{t|sv|göra matt}}, {{t|sv|sätta schackmatt}}, {{t|sv|göra schackmatt}}
* Vietnamese: {{t|vi|chiếu bí}}
{{trans-bottom}}

{{trans-top|to lead to a situation of no escape}}
* Bulgarian: {{t+|bg|матирам}}
* Chinese:
*: Mandarin: {{t+|cmn|挫敗}}, {{t+|cmn|挫败|tr=cuòbài}}
* Finnish: {{t|fi|[[saattaa]] [[umpikuja|umpikujaan]]}}, {{t|fi|[[panna]] [[ahdas|ahtaalle]]}}
{{trans-mid}}
* Hungarian: {{t+|hu|sarokba szorít}}
* Portuguese: {{t|pt|[[dar]] ([[o]]) [[xeque-mate]]}}
* Russian: {{t-needed|ru}}
{{trans-bottom}}

{{checktrans-top}}
* Romanian: {{t-check|ro|șah mat}}
{{trans-mid}}
* Spanish: {{t-check|es|dar jaque mate}}, {{t-check|es|dar mate}}
{{trans-bottom}}

===References==="""
    actual = parse_wikitext(text, 'IPA', 'en', 'File') 
    expected = {'IPA': 'ˈt͡ʃɛkmeɪt', 
    'pos': {
        'interjection': ['Word called out by the victor when making a move that wins the game.'], 
        'noun': ['The conclusive victory in a game of chess that occurs when an opponents king is threatened with unavoidable capture.', 
            'Any losing situation with no escape; utter defeat.'], 
        'verb': ['To put the king of an opponent into checkmate.', 'To place in a losing situation that has no escape.']
        }
    }
    #print('debug: ', actual)
    assert actual == expected

def test_chinese_character():
    text = """
{{also|蠹}}
{{character info/new}}
==Translingual==

===Han character===
{{Han char|rn=142|rad=虫|as=16|sn=22|four=|canj=GBMI|ids=⿱𥑟䖵}}

# [[moth]]
# insects which eat into cloth

====References====
* {{Han ref|kx=1102.230|dkj=33824|dj=1565.290|hdz=42903.090|uh=8827|ud=34855}}

----

==Chinese==
{{zh-see|蠹|v}}

----

==Japanese==

===Kanji===
{{ja-kanji|grade=|rs=虫16}}

# {{rfdef|ja|sort=虫16}}

====Readings====
* {{ja-readings|on=と|kun=[[きくいむし,しみ|nanori=}}"""
    actual = parse_wikitext(text, 'IPA', 'en', 'File') 
    expected = {}
    #print('debug: ', actual)
    assert actual == expected


def test_empty_dict():
    text = """
==English==

===Alternative forms===
* {{l|en|Pope July}}
* {{l|en|Pope Julio}}

===Etymology===
Unknown. Presumably named after [[w:Pope Julius II|Pope Julius II]], the Warrior Pope.

===noun===
{{noun}}

# {{lb|en|obsolete}}
[[Category:en:Card games]]"""
    actual = parse_wikitext(text, 'IPA', 'en', 'File') 
    expected = {}
    #print('debug: ', actual)
    assert actual == expected

