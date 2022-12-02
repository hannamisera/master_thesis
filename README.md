# GitHub Repository von Hanna Misera


## Masterarbeit 

##### zur Erlangung des akademischen Grades Master of Arts (MA) 

##### an der Karl-Franzens-Universität Graz 
##### am Institut "Zentrum für Informationsmodellierung - Austrian Centre for Digital Humanities"

#


## Inhalt und Aufbau von Stellenanzeigen des 19. und 20. Jahrhunderts. Iterative Erarbeitung eines Skripts zur Strukturierung von Stellenanzeigen, mittels regulärer Ausdrücke" 



##### Begutachter: [Georg Vogeler](https://online.uni-graz.at/kfu_online/visitenkarte.show_vcard?pPersonenGruppe=3&pPersonenId=27A89EA24D11359E)
#



## Abstract
Diese Arbeit ist eingebettet in ein FWF-gefördertes Forschungsprojekt mit dem Titel „The making of the incredibly differentiated labor market: Evidence from job offers from ten decades“. Ziel dieses Forschungsprojekts ist es, Informationen zur Arbeitssuche, zum Arbeitsangebot und der Vermittlung von Angebot und Nachfrage, aus digitalisierten historischen Zeitungen zu extrahieren. Hierfür werden Stellenanzeigen des 19. und 20. Jahrhunderts untersucht. Diese Arbeit soll einen Beitrag für die anschließende, inhaltliche Textanalyse darstellen.
Die Datengrundlage sind Stellenanzeigen, welche aus Zeitungsscans des ANNO-Korpus extrahiert und mit Hilfe von OCR transkribiert wurden. Die digitale Analyse dieser Quellen birgt ein enormes Potenzial, durch die Verarbeitung von sehr großen Datenmengen. Denn computerbasierte Distant-Reading Methoden bieten die Chance, Einheiten in Texten wahrzunehmen und dadurch Erkenntnisse über ein Gesamtsystem abzuleiten. 
Die Analyse und Bearbeitung von Stellenanzeigen sind von großen Hürden begleitet. Die sehr kurzen Texte, eine fehlerhafte OCR-Transkription, sowie die reduzierte Grammatik, erschweren deskriptive und strukturelle Analysen. Daraus ergibt sich das Ziel, Stellenanzeigen in einem größeren Stil zu strukturieren. Anschließend wird untersucht, welche Potenziale und Risiken sich aus einer solchen Annotation ergeben.
Denn Stellenanzeigen verfügen über eine innere Struktur, welche sich nicht immer durch Grammatik oder Formatierung ableiten lässt. 
Untersuchungen dieser Arbeit zeigen, dass sich Stellenanzeigen mit Hilfe bestimmter Regeln in zwei Sinnabschnitte strukturieren lassen. Diese Regeln können  niemals auf sämtliche Stellenanzeigen angewendet werden. Deshalb besteht der Vorschlag dieser Arbeit darin, Stellenanzeigen mittels regulärer Ausdrücke zu annotieren. Ergebnis ist ein Annotation-Skript, das eine Annotation von Stellenanzeigen mit individueller Fehlerkorrektur, ermöglicht. 

## Inhalt dieses Repositories 
Dieses Repository beinhaltet alle Notebooks, die für die Masterarbeit erstellt wurden. 
Die Notebooks wurden nach den Kapiteln benannt, in denen der Code vorkommt und verwendet wird. 
Die Notebooks enthalten Analysen, um Struktur und Inhalt von Stellenanzeigen näher  zu. beschreiben. Davon abgeleitet, wurden RegEx-Muster erstellt, um Stellenanzeigen leichter zu annotieren. Dieses Annotationsskript, findet sich in der PY-Datei. 

Die Masterarbeit verweist auf das Skript 5.2.2_regex_annotation_skript.py, da der Code des Annotationsskript nicht separat in der Arbeit abgedruckt wird. Auch das Flow Chart ist lediglich im Repository zu finden, da die Datei zu groß ist. 


## Daten 
Die OCR-transkribierten Stellenanzeigen stammen aus dem ANNO-Korpus der ÖNB. Das ANNO-Korpus findet sich hier: https://anno.onb.ac.at 

In der Vorarbeit des FWF-Forschungsprojekts wurde bereits ein kleiner Korpus, bestehend aus 13493 Stellenanzeigen identifiziert und mit einem Tesseract-Modell transkribiert. Ebenfalls wurde ein Teil der Stellenanzeigen per Hand transkribiert. Dieser Goldstandard ermöglicht es, die Qualität des QCR einzuschätzen.
Diese Korpora werden aus Datenschutz rechtlichen Gründen nicht auf GitHub zur Verfügung gestellt. Bei Interesse lohnt sich eine Kontaktaufnahme mit den Hautverantwortlichen des [Forschungsprojekts](https://online.uni-graz.at/kfu_online/wbForschungsportal.cbShowPortal?pPersonNr=80075&pMode=E&pCallType=PROJ&pLevel=PERS). 
Hierfür wenden Sie sich bitte an [Jörn Kleinert](https://online.uni-graz.at/kfu_online/visitenkarte.show_vcard?pPersonenId=3C898C155E0707D9&pPersonenGruppe=3). 
