# Bibliotech_Hackathon_AnjouBible


## Collection description | TEAM 1: Bible of Anjou

 
This illuminated Bible, known as the Anjou Bible or Bible Angevine, is an absolute masterpiece from the 14th century. It is richly adorned and was created in Naples around the year 1340 at the court of Robert of Anjou. It consists of 338 folios with two miniatures covering entire pages and over 160 smaller miniatures. After many journeys, the manuscript ended up in the archiepiscopal seminary of Mechlin in the 19th century, until it was deposited in the Maurits Sabbe Library in 1974. In 2008, following the 'Masterpieces Decree', the Flemish Community granted it the title of Flemish Masterpiece.

View our poster at https://zenodo.org/record/7762363#.ZB15T3bMJPY

<img src="https://github.com/SuzannaLin/Bibliotech_Hackathon_AnjouBible/blob/main/Character%20Animation%2001_test.gif" width="50%" height="50%">

## Goals and Output

	
Catalogue the contents of the book in machine readable format including information about the chapters, illustrations, and illuminated initials categorised by size.
	
Extract illustrations from the manuscript using computational methods and making these available for re-use.
	
Create an interactive website that makes it possible for the general public to interact with the illustrations in a new way.
	
Create a character set based on the illuminated initials that will be displayed on the website and can be used for other projects.

<img src="https://github.com/SuzannaLin/Bibliotech_Hackathon_AnjouBible/blob/main/Anjou/199_wo_bg_bigA.png" width="40%" height="40%">


## Methodology


To extract images from each page, we first use a Selective Search algorithm to locate “interesting” regions. We filter out the text regions using a color mask. 
	
Then, for each region, the background is removed. These snippets contain illustrations of animals, people, swirls, and decorated initials. 
	
Using a classification network, we can filter out specific categories such as horses. 
	
The website uses Bootstrap, an open source development framework, and displays the illustrations of the Anjou Bible grouped in collections (letters, animals, etc.)


<img src="https://github.com/SuzannaLin/Bibliotech_Hackathon_AnjouBible/blob/main/Anjou/101_wo_bg_dragon.png" width="40%" height="40%">


## Anjou Bible Timeline

1340 - A bible (now known as the 'Anjou Bible') is commissioned by Robert, King of Naples, also known as Robert I of Anjou (Italian: Roberto d'Angiò) as a wedding present for his granddaughter Joanna and her Hungarian fiancé Andrew of Hungary
1345 (?) - Anjou Bible comes into the possession of Nicolo d'Alifio, an advisor to Robert and Joanna, probably as a gift from Queen Joanna or given to him when the queen fled to France (cf. f308r)
1402 - Anjou Bible is mentioned in an inventory of the books of John, Duke of Berry
1418 - Anjou Bible is sold for well below its estimated value for 125 livre tournois in an auction to Galiache Pinel, a merchant
150x - Anjou Bible ends up in the possession of Nicolas Le Ruistre, bishop of Arras (1502-1509) and chancellor at the University of Leuven and was kept at Arras College in Leuven until the end of the French Revolution
1547 - The Anjou Bible entered a list of Bibles used to compile the Biblia vulgata Lovaniensis
1797 - Anjou Bible is apparently transferred to the grand seminary in Mechelen (Hence why it's sometimes also called Malines Bible)
1969 - Anjou Bible deposited in the Maurits Sabbe Library of KU Leuven
2010 - Anjou Bible is exhibited to the public for twelve weeks at Museum M in Leuven


<img src="https://github.com/SuzannaLin/Bibliotech_Hackathon_AnjouBible/blob/main/Anjou/199_wo_bg_swirl.png" >


## Team members
Agni Vourtsi
Austine Jesuvera Crasta
Courtney Van de Mosselaer
Joachim Bovin (TL)
Ni Li
Sandra Elpers
Suzanna Cuypers
Yun Liu (TL)
