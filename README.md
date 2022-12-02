# GitHub Repository von Hanna Misera


## Masterarbeit 

##### zur Erlangung des akademischen Grades Master of Arts (MA) 

##### an der Karl-Franzens-Universität Graz 
##### am Institut "Zentrum für Informationsmodellierung - Austrian Centre for Digital Humanities"

#


## Inhalt und Aufbau von Stellenanzeigen des 19. und 20. Jahrhunderts. Iterative Erarbeitung eines Skripts zur Strukturierung von Stellenanzeigen, mittels regulärer Ausdrücke" 



##### Begutachter: [Georg Vogeler](https://online.uni-graz.at/kfu_online/visitenkarte.show_vcard?pPersonenGruppe=3&pPersonenId=27A89EA24D11359E)
#



## Abstract DE
Diese Arbeit ist eingebettet in ein FWF-gefördertes Forschungsprojekt mit dem Titel „The making of the incredibly differentiated labor market: Evidence from job offers from ten decades“. Ziel dieses Forschungsprojekts ist es, Informationen zur Arbeitssuche, zum Arbeitsangebot sowie der Vermittlung von Angebot und Nachfrage aus digitalisierten historischen Zeitungen zu extrahieren. Hierfür werden Stellenanzeigen des 19. und 20. Jahrhunderts untersucht. Diese Arbeit soll einen Beitrag für die anschließende, inhaltliche Textanalyse darstellen.
Die Datengrundlage sind Stellenanzeigen, welche aus Zeitungsscans des ANNO-Korpus extrahiert und mit Hilfe von OCR transkribiert wurden. Die digitale Analyse dieser Quellen birgt ein enormes Potenzial durch die Verarbeitung von sehr großen Datenmengen. 
Doch zeigen Untersuchen dieser Arbeit, dass die computerbasierte und automatisierte Verarbeitung von Stellenanzeigen von großen Hürden begleitet sind. Die sehr kurzen Texte, eine fehlerhafte OCR-Transkription und die reduzierte Grammatik erschweren deskriptive und strukturelle Analysen. Daraus ergibt sich die Frage, ob die Strukturierung durch Annotation von Stellenanzeigen bei deskriptiven und strukturellen Analysen helfen kann. 
Durch Literaturrecherche und Experimente wird gezeigt, dass Stellenanzeigen über eine innere Struktur verfügen, welche sich nicht immer durch Grammatik oder Formatierung ableiten lässt.
Aus diesem Grund ist die Annotation von Stellenanzeigen auf der Grundlage starrer Regeln nur bedingt möglich. 
Deshalb besteht der Vorschlag dieser Arbeit darin, Stellenanzeigen nicht ausschließlich durch reguläre Ausdrücke zu annotieren. Ergebnis ist ein Skript, das eine Annotation von Stellenanzeigen vorschlägt, jedoch eine individuelle Fehlerkorrektur ermöglicht.

## Abstract EN
This work forms part of an FWF-funded research project entitled "The making of the incredibly differentiated labor market: Evidence from job offers from ten decades". The aim of this research project is to extract information on job seeking, job offers, and the conveyance of supply and demand from digitized historical newspapers. For this purpose, 19th and 20th century job advertisements are examined. This work is intended as a contribution to the subsequent textual analysis.
The data basis consists of digitized job advertisements extracted from newspaper scans of the ANNO corpus and transcribed with the help of OCR. Digital analysis of such sources holds enormous potential because huge amounts of data can be processed. 
However, ressults of this study show that computer-based and automated processing of job advertisements is accompanied by major hurdles. Short texts, faulty OCR transcription, and reduced grammar make descriptive and structural analyses difficult. This raises the question of whether structuring job advertisements by way of annotation can help with descriptive and structural analyses. 
Literature research and experiments show that job advertisements have an internal structure that cannot always be derived from grammar or formatting.
For this reason, annotating job advertisements based on rigid rules is only possible to a limited extent. 
Hence, the proposal of this thesis is to avoid annotating job advertisements exclusively by regular expressions. Rather, this thesis presents a script which (i) proposes an annotation of job advertisements, and (ii) allows for correction of any error which may be present in the proposed annotation.


## Inhalt dieses Repositories 
Dieses Repository beinhaltet alle Notebooks, die für die Masterarbeit erstellt wurden. 
Die Notebooks wurden nach den Kapiteln der Thesis benannt, in denen der Code vorkommt und verwendet wird. 
Die Notebooks enthalten Analysen, um Struktur und Inhalt von Stellenanzeigen näher  zu. beschreiben. Davon abgeleitet, wurden RegEx-Muster erstellt, um Stellenanzeigen leichter zu annotieren. Dieses Annotationsskript, findet sich in der PY-Datei. 

Die Masterarbeit verweist auf das Skript 5.2.2_regex_annotation_skript.py, da der Code des Annotationsskript nicht separat in der Arbeit abgedruckt wird. Auch das Flow Chart ist im Repository zu finden, da die Datei hier etwas größer abgespeichert werden kann. 


## Daten 
Die OCR-transkribierten Stellenanzeigen stammen aus dem ANNO-Korpus der ÖNB. Das ANNO-Korpus findet sich hier: https://anno.onb.ac.at 

In der Vorarbeit des FWF-Forschungsprojekts wurde bereits ein kleiner Korpus, bestehend aus 13493 Stellenanzeigen identifiziert und mit einem Tesseract-Modell transkribiert. Ebenfalls wurde ein Teil der Stellenanzeigen per Hand transkribiert. Dieser Goldstandard ermöglicht es, die Qualität des QCR einzuschätzen.
Diese Korpora werden aus Datenschutz rechtlichen Gründen nicht auf GitHub zur Verfügung gestellt. Bei Interesse lohnt sich eine Kontaktaufnahme mit den Hautverantwortlichen des [Forschungsprojekts](https://online.uni-graz.at/kfu_online/wbForschungsportal.cbShowPortal?pPersonNr=80075&pMode=E&pCallType=PROJ&pLevel=PERS). 
Hierfür wenden Sie sich bitte an [Jörn Kleinert](https://online.uni-graz.at/kfu_online/visitenkarte.show_vcard?pPersonenId=3C898C155E0707D9&pPersonenGruppe=3). 
