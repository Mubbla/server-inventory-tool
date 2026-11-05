# Reflektioner

## Val av parameter eller global lista

 Ett designval jag behövde ta ställning till var hur listan med servrar skulle användas i programmet. Ett alternativ var att läsa in listan från JSON-filen i meny.py och sedan låta alla funktioner i filen använda samma globala variabel. Det alternativet kräver mindre kod eftersom listan redan finns tillgänglig för funktionerna.

 Jag valde istället att låta funktionerna ta emot listan med servrar som parameter. Exempelvis kan starta_meny(servrar) och visa_servrar(servrar) få listan skickad till sig från main.py. På så sätt blir det tydligt vilka data varje funktion behöver för att kunna utföra sin uppgift.

Fördelen med denna lösning är att funktionerna blir mindre beroende av globala variabler. De blir också enklare att återanvända och testa eftersom de inte förutsätter att en viss variabel redan finns i modulen. Lösningen följer dessutom kursens riktlinje att funktioner ska ta emot det de behöver som parametrar.

 Nackdelen är att samma parameter ibland måste skickas vidare mellan flera funktioner, vilket kan upplevas som lite omständligt och innebära några extra kodrader.

 Om programmet hade varit mycket litet hade jag kunnat välja en global lista för att göra koden kortare. Eftersom projektet är uppdelat i flera moduler och ska kunna byggas ut med fler funktioner bedömde jag att parameterlösningen är mer strukturerad och lättare att underhålla på sikt.
