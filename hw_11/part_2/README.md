## Домашняя работа №13: Использование neo4j

Поднял базу в доккере

```
docker run -p7474:7474 -p7687:7687 neo4j
```

Создадим данные для задания.
Я вбил в поисковике `самые популярные туроператоры` и пошёл на сайты первых четырёх. Если честно, то убив несколько часов в попытках достать информацию, я где-то начал фантазировать - например, у турков там чуть ли не в каждом городе какой-то аэропорт, поэтому я в лоб создал два города - Стамбул и Анкара, как ближайшие к куротам. Какой из них ближе к какому на самом деле, я даже не знаю. Не стал заморачиваться по поводу коннекта с хабами - можно было properties у отношения между городами хабами сделать, скажем, с флагами: has_flights, has_bus, has_train, но я для простоты просто ввёл одно свойство - туpe и два значения, или flight, или bus.
Ниже команды создания данных для задания. 

```
create (anextour:Operator {name: "AnexTour"});
create (biblioglobus:Operator {name: "BiblioGlobus"});
create (coraltravel:Operator {name: "CoralTravel"});
create (sunmar:Operator {name: "Sunmar"});

create (egypt:Country {name: "Egypt"});
create (turkey:Country {name: "Turkey"});
create (uae:Country {name: "UAE"});
create (thailand:Country {name: "Thailand"});
create (cyprus:Country {name: "Cyprus"});
create (bahrain:Country {name: "Bahrain"});

MATCH (a:Operator {name:'AnexTour'}), (e:Country {name:'Egypt'}), (t:Country {name:'Turkey'}), (u:Country {name:'UAE'}), (th:Country {name:'Thailand'})
CREATE (a) -[:HAS_TOURS_TO]-> (e),
(a) -[:HAS_TOURS_TO]-> (t),
(a) -[:HAS_TOURS_TO]-> (u), 
(a) -[:HAS_TOURS_TO]-> (th);

MATCH (a:Operator {name:'BiblioGlobus'}), (e:Country {name:'Egypt'}), (t:Country {name:'Turkey'}), (u:Country {name:'UAE'}), (c:Country {name:'Cyprus'})
CREATE (a) -[:HAS_TOURS_TO]-> (e),
(a) -[:HAS_TOURS_TO]-> (t),
(a) -[:HAS_TOURS_TO]-> (u), 
(a) -[:HAS_TOURS_TO]-> (c);

MATCH (a:Operator {name:'CoralTravel'}), (e:Country {name:'Egypt'}), (t:Country {name:'Turkey'}), (b:Country {name:'Bahrain'}), (c:Country {name:'Cyprus'})
CREATE (a) -[:HAS_TOURS_TO]-> (e),
(a) -[:HAS_TOURS_TO]-> (t),
(a) -[:HAS_TOURS_TO]-> (b), 
(a) -[:HAS_TOURS_TO]-> (c);

MATCH (a:Operator {name:'Sunmar'}), (e:Country {name:'Egypt'}), (t:Country {name:'Turkey'}), (u:Country {name:'UAE'}), (th:Country {name:'Thailand'})
CREATE (a) -[:HAS_TOURS_TO]-> (e),
(a) -[:HAS_TOURS_TO]-> (t),
(a) -[:HAS_TOURS_TO]-> (u), 
(a) -[:HAS_TOURS_TO]-> (th);


create (sharmelsheikh:Destination {name: "SharmElSheikh"});
create (cairo:Destination {name: "Cairo"});
create (hurgarda:Destination {name: "Hurgarda"});
MATCH (e:Country {name:'Egypt'}), (sh:Destination {name:'SharmElSheikh'}), (c:Destination {name:'Cairo'}), (h:Destination {name:'Hurgarda'})
CREATE (e) -[:CONTAINS]-> (sh),
(e) -[:CONTAINS]-> (c),
(e) -[:CONTAINS]-> (h);



create (izmir:Destination {name: "Izmir"});
create (kundu:Destination {name: "Kundu"});
create (lara:Destination {name: "Lara"});
create (bodrum:Destination {name: "Bodrum"});
create (belek:Destination {name: "Belek"});
create (side:Destination {name: "Side"});
create (marmaris:Destination {name: "Marmaris"});
create (kemer:Destination {name: "Kemer"});
create (alania:Destination {name: "Alania"});
MATCH (turkey:Country {name:'Turkey'}), 
(izmir:Destination {name:'Izmir'}), 
(kundu:Destination {name: "Kundu"}),
(lara:Destination {name: "Lara"}),
(bodrum:Destination {name: "Bodrum"}),
(belek:Destination {name: "Belek"}),
(side:Destination {name: "Side"}),
(marmaris:Destination {name: "Marmaris"}),
(kemer:Destination {name: "Kemer"}),
(alania:Destination {name: "Alania"})
CREATE (turkey) -[:CONTAINS]-> (izmir),
(turkey) -[:CONTAINS]-> (kundu),
(turkey) -[:CONTAINS]-> (lara),
(turkey) -[:CONTAINS]-> (bodrum),
(turkey) -[:CONTAINS]-> (belek),
(turkey) -[:CONTAINS]-> (side),
(turkey) -[:CONTAINS]-> (marmaris),
(turkey) -[:CONTAINS]-> (alania),
(turkey) -[:CONTAINS]-> (kemer);


create (dubai:Destination {name: "Dubai"});
create (abudhabi:Destination {name: "AbuDhabi"});
MATCH (uae:Country {name:'UAE'}), 
(d:Destination {name:'Dubai'}), 
(a:Destination {name: "AbuDhabi"})
CREATE (uae) -[:CONTAINS]-> (d),
(uae) -[:CONTAINS]-> (a);

create (phukhet:Destination {name: "Phukhet"});
create (pattaya:Destination {name: "Pattaya"});
MATCH (th:Country {name:'Thailand'}), 
(ph:Destination {name:'Phukhet'}), 
(pt:Destination {name: "Pattaya"})
CREATE (th) -[:CONTAINS]-> (ph),
(th) -[:CONTAINS]-> (pt);


create (limassol:Destination {name: "Limassol"});
create (ayaianapa:Destination {name: "AyaiaNapa"});
create (paphos:Destination {name: "Paphos"});
create (polis:Destination {name: "Polis"});
MATCH (c:Country {name:'Cyprus'}), 
(l:Destination {name:'Limassol'}), 
(a:Destination {name: "AyaiaNapa"}),
(pa:Destination {name:'Paphos'}), 
(po:Destination {name: "Polis"})
CREATE (c) -[:CONTAINS]-> (l),
(c) -[:CONTAINS]-> (a),
(c) -[:CONTAINS]-> (pa),
(c) -[:CONTAINS]-> (po);



create (amwaj:Destination {name: "Amwaj"});
create (juffair:Destination {name: "Juffair"});
create (manama:Destination {name: "Manama"});
MATCH (b:Country {name:'Bahrain'}), 
(a:Destination {name:'Amwaj'}), 
(j:Destination {name: "Juffair"}),
(m:Destination {name:'Manama'})
CREATE (b) -[:CONTAINS]-> (a),
(b) -[:CONTAINS]-> (j),
(b) -[:CONTAINS]-> (m);

create (sharmhub:City {name: "SharmElSheikhHub"});
create (cairohub:City {name: "CairoHub"});
MATCH (shub:City {name:'SharmElSheikhHub'}), 
(chub:City {name:'CairoHub'}), 
(s:Destination {name: "SharmElSheikh"}),
(c:Destination {name:'Cairo'})
CREATE (s) -[:CLOTHEST_TO]-> (shub),
(c) -[:CLOTHEST_TO]-> (chub);


create (istambul:City {name: "Istambul"});
MATCH (istambul:City {name: "Istambul"}), 
(izmir:Destination {name:'Izmir'}), 
(kundu:Destination {name: "Kundu"}),
(lara:Destination {name:'Lara'}),
(bodrum:Destination {name:'Bodrum'}), 
(belek:Destination {name: "Belek"})
create (izmir) -[:CLOTHEST_TO]-> (istambul),
(kundu) -[:CLOTHEST_TO]-> (istambul),
(lara) -[:CLOTHEST_TO]-> (istambul),
(bodrum) -[:CLOTHEST_TO]-> (istambul),
(belek) -[:CLOTHEST_TO]-> (istambul);

create (ancara:City {name: "Ancara"});
MATCH (ancara:City {name: "Ancara"}), 
(side:Destination {name:'Side'}), 
(marmaris:Destination {name: "Marmaris"}),
(kemer:Destination {name:'Kemer'}),
(alania:Destination {name:'Alania'})
create (side) -[:CLOTHEST_TO]-> (ancara),
(marmaris)-[:CLOTHEST_TO]-> (ancara),
(kemer) -[:CLOTHEST_TO]-> (ancara),
(alania) -[:CLOTHEST_TO]-> (ancara);

create (dubaihub:City {name: "DubaiHub"});
create (abudhabihub:City {name: "AbuDhabiHub"});
MATCH (dubaihub:City {name: "DubaiHub"}), 
(abudhabihub:City {name: "AbuDhabiHub"}), 
(abudhabi:Destination {name: "Dubai"}),
(dubai:Destination {name:'AbuDhabi'})
create (abudhabi) -[:CLOTHEST_TO]-> (abudhabihub),
(dubai)-[:CLOTHEST_TO]-> (dubaihub);

create (bankogh:City {name: "Bankogh"});
MATCH (bankogh:City {name: "Bankogh"}), 
(phukhet:Destination {name: "Phukhet"}), 
(pattaya:Destination {name: "Pattaya"})
create (phukhet) -[:CLOTHEST_TO]-> (bankogh),
(pattaya) -[:CLOTHEST_TO]-> (bankogh);

create (larnaka:City {name: "Larnaka"});
create (paphoshub:City {name: "PaphosHub"}); 
MATCH (larnaka:City {name: "Larnaka"}), 
(paphoshub:City {name: "PaphosHub"}), 
(limassol:Destination {name: "Limassol"}), 
(ayaianapa:Destination {name: "AyaiaNapa"}), 
(paphos:Destination {name: "Paphos"}), 
(polis:Destination {name: "Polis"})
create (limassol) -[:CLOTHEST_TO]-> (larnaka),
(ayaianapa) -[:CLOTHEST_TO]-> (larnaka),
(paphos)-[:CLOTHEST_TO]-> (paphoshub),
(polis)-[:CLOTHEST_TO]-> (paphoshub);

create (muharraq:City {name: "Muharraq"});
MATCH (muharraq:City {name: "Muharraq"}), 
(amwaj:Destination {name: "Amwaj"}), 
(juffair:Destination {name: "Juffair"}),
(manama:Destination {name: "Manama"}) 
create (amwaj) -[:CLOTHEST_TO]-> (muharraq),
(juffair) -[:CLOTHEST_TO]-> (muharraq),
(manama) -[:CLOTHEST_TO]-> (muharraq);

MATCH (muharraq:City {name: "Muharraq"}),
(larnaka:City {name: "Larnaka"}), 
(paphoshub:City {name: "PaphosHub"}), 
(bankogh:City {name: "Bankogh"}),
(dubaihub:City {name: "DubaiHub"}),
(abudhabihub:City {name: "AbuDhabiHub"}),
(ancara:City {name: "Ancara"}),
(istambul:City {name: "Istambul"}),
(sharmhub:City {name: "SharmElSheikhHub"}),
(cairohub:City {name: "CairoHub"})
create (sharmhub) -[:HAS_CONNECTION_WITH {type: "bus"}]-> (cairohub),
(sharmhub) -[:HAS_CONNECTION_WITH {type: "flight"}]-> (istambul),
(istambul) -[:HAS_CONNECTION_WITH {type: "bus"}]-> (ancara),
(istambul) -[:HAS_CONNECTION_WITH {type: "flight"}]-> (dubaihub),
(istambul) -[:HAS_CONNECTION_WITH {type: "flight"}]-> (bankogh),
(ancara) -[:HAS_CONNECTION_WITH {type: "flight"}]-> (abudhabihub),
(dubaihub) -[:HAS_CONNECTION_WITH {type: "bus"}]-> (abudhabihub),
(dubaihub) -[:HAS_CONNECTION_WITH {type: "bus"}]-> (bankogh),
(larnaka) -[:HAS_CONNECTION_WITH {type: "bus"}]-> (paphoshub),
(ancara) -[:HAS_CONNECTION_WITH {type: "flight"}]-> (muharraq);
```
![](pics/Screen%20Shot%202022-08-26%20at%205.59.58%20pm.png)
Теперь поисковый запрос:
```
match (a:Destination {name:"Lara"})-[r]-(c:City)-[connect:HAS_CONNECTION_WITH]-(z:City)-[e]-(b:Destination {name:"Kemer"}) where connect.type <> "flight" return *
```
Я взял два турецких города, которые, типа, связаны через разные города, чтобы наглядней показать граф. 
![](pics/Screen%20Shot%202022-08-26%20at%205.58.41%20pm.png)