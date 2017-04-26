# MediaWiki Wikibase

This package provides basic functionality for processing and normalizing
Wikidata Entity JSON.  

## Usage

```python
>>> import mwbase
>>> import requests
>>>
>>> wb_doc = requests.get(
...     "https://wikidata.org/wiki/Special:EntityData/Q42.json").json()
>>>
>>> entity = mwbase.Entity.from_json(wb_doc['entities']['Q42'])
>>>
>>> entity.labels['en']
'Douglas Adams'
>>> entity.claims.keys()
dict_keys(['P949', 'P21', 'P551', 'P1442', 'P69', 'P1368', 'P1303', 'P856',
'P2188', 'P434', 'P396', 'P509', 'P269', 'P1617', 'P1559', 'P2387', 'P1284',
'P734', 'P1695', 'P1375', 'P2435', 'P1266', 'P20', 'P1816', 'P950', 'P1411',
'P800', 'P31', 'P172', 'P906', 'P3106', 'P646', 'P570', 'P648', 'P2605',
'P866', 'P40', 'P271', 'P998', 'P1273', 'P103', 'P2963', 'P3430', 'P244',
'P2469', 'P2163', 'P2611', 'P2019', 'P910', 'P2626', 'P1005', 'P140', 'P569',
'P349', 'P1258', 'P25', 'P1412', 'P947', 'P18', 'P1207', 'P1015', 'P119',
'P214', 'P1670', 'P1003', 'P1233', 'P373', 'P2191', 'P26', 'P409', 'P1953',
'P22', 'P1006', 'P1477', 'P1263', 'P345', 'P535', 'P268', 'P691', 'P1196',
'P213', 'P27', 'P1417', 'P19', 'P735', 'P2168', 'P1315', 'P3373', 'P108',
'P3417', 'P227', 'P106', 'P2604', 'P1415', 'P3762'])
>>> entity.sitelinks.keys()
dict_keys(['cswiki', 'skwikiquote', 'elwiki', 'bgwiki', 'eowiki',
'simplewiki', 'trwikiquote', 'svwikiquote', 'idwiki', 'azwiki',
'etwikiquote', 'cswikiquote', 'gawiki', 'be_x_oldwiki', 'elwikiquote',
'itwikiquote', 'shwiki', 'ukwiki', 'skwiki', 'fawiki', 'arwiki', 'lvwiki',
'zhwikiquote', 'eswikiquote', 'fiwiki', 'mlwiki', 'mrwiki', 'dawiki',
'frwikiquote', 'bgwikiquote', 'plwikiquote', 'bswiki', 'warwiki', 'frwiki',
'cywiki', 'kawiki', 'hywikiquote', 'ocwiki', 'zhwiki', 'simplewikiquote',
'itwiki', 'lawiki', 'astwiki', 'dewikiquote', 'bnwiki', 'mgwiki', 'kowiki',
'plwiki', 'slwiki', 'huwikiquote', 'urwiki', 'hywiki', 'huwiki', 'sqwiki',
'nlwiki', 'trwiki', 'jvwiki', 'barwiki', 'iowiki', 'glwikiquote',
'thwikiquote', 'euwiki', 'hewikiquote', 'eowikiquote', 'eswiki',
'ltwikiquote', 'hrwiki', 'svwiki', 'cawiki', 'hewiki', 'viwiki',
'liwikiquote', 'tawiki', 'rowiki', 'bewiki', 'ruwiki', 'mkwiki', 'glwiki',
'mrjwiki', 'ruwikiquote', 'srwiki', 'fawikiquote', 'jawiki', 'fiwikiquote',
'bswikiquote', 'dewiki', 'nlwikiquote', 'scowiki', 'nowiki', 'iswiki',
'ptwikiquote', 'nnwiki', 'arzwiki', 'vepwiki', 'azwikiquote', 'ptwiki',
'enwiki', 'enwikiquote', 'etwiki'])
```
