---
slug: paella
tags: [operadors, aritmetics]
---
# Paella

Suposant que una paella es pot cuinar exclusivament amb arròs i gambes (que es molt suposar), i que per cada 4 persones s'utilitza mig kilo d'arròs i un quart de kilo de gambes, escriu un programa que llegeixi el número de comensals, el preu per kilo d'arròs i el preu per kilo de gambes, i mostri les quantitats necessàries i el cost de cada ingredient, i el cost total de la paella.

## Input

Un enter <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.766ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 760.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M50 252Q50 367 117 473T286 641T490 704Q580 704 633 653Q642 643 648 636T656 626L657 623Q660 623 684 649Q691 655 699 663T715 679T725 690L740 705H746Q760 705 760 698Q760 694 728 561Q692 422 692 421Q690 416 687 415T669 413H653Q647 419 647 422Q647 423 648 429T650 449T651 481Q651 552 619 605T510 659Q484 659 454 652T382 628T299 572T226 479Q194 422 175 346T156 222Q156 108 232 58Q280 24 350 24Q441 24 512 92T606 240Q610 253 612 255T628 257Q648 257 648 248Q648 243 647 239Q618 132 523 55T319 -22Q206 -22 128 53T50 252Z"></path></g></svg></span> indicant el número de comensals.

Un float <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.743ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 750.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M208 74Q208 50 254 46Q272 46 272 35Q272 34 270 22Q267 8 264 4T251 0Q249 0 239 0T205 1T141 2Q70 2 50 0H42Q35 7 35 11Q37 38 48 46H62Q132 49 164 96Q170 102 345 401T523 704Q530 716 547 716H555H572Q578 707 578 706L606 383Q634 60 636 57Q641 46 701 46Q726 46 726 36Q726 34 723 22Q720 7 718 4T704 0Q701 0 690 0T651 1T578 2Q484 2 455 0H443Q437 6 437 9T439 27Q443 40 445 43L449 46H469Q523 49 533 63L521 213H283L249 155Q208 86 208 74ZM516 260Q516 271 504 416T490 562L463 519Q447 492 400 412L310 260L413 259Q516 259 516 260Z"></path></g></svg></span> indicant el preu per kilo d'arròs.

Un float <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-3-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.827ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 786.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M50 252Q50 367 117 473T286 641T490 704Q580 704 633 653Q642 643 648 636T656 626L657 623Q660 623 684 649Q691 655 699 663T715 679T725 690L740 705H746Q760 705 760 698Q760 694 728 561Q692 422 692 421Q690 416 687 415T669 413H653Q647 419 647 422Q647 423 648 429T650 449T651 481Q651 552 619 605T510 659Q492 659 471 656T418 643T357 615T294 567T236 496T189 394T158 260Q156 242 156 221Q156 173 170 136T206 79T256 45T308 28T353 24Q407 24 452 47T514 106Q517 114 529 161T541 214Q541 222 528 224T468 227H431Q425 233 425 235T427 254Q431 267 437 273H454Q494 271 594 271Q634 271 659 271T695 272T707 272Q721 272 721 263Q721 261 719 249Q714 230 709 228Q706 227 694 227Q674 227 653 224Q646 221 643 215T629 164Q620 131 614 108Q589 6 586 3Q584 1 581 1Q571 1 553 21T530 52Q530 53 528 52T522 47Q448 -22 322 -22Q201 -22 126 55T50 252Z"></path></g></svg></span> indicant el preu per kilo de gambes.

## Output

El programa imprimeix:

- La quantitat d'arròs necessària expressada en kilos.
- La quantitat de gambes necessàrias expressada en kilos.
- El preu de l'arròs necessari per a la paella.
- El preu de les gambes necessàries per a la paella.
- El cost total de la paella.

amb el format següent:

```
0.5 kg arros
0.25 kg gambes
0.5 euros arros
3.0 euros gambes
TOTAL: 3.5 euros
```

## Tests

### Test
```input
4
1.00
12.00
```
```output
0.5 kg arros
0.25 kg gambes
0.5 euros arros
3.0 euros gambes
TOTAL: 3.5 euros
```

### Test
```input
8
1.5
15
```
```output
1.0 kg arros
0.5 kg gambes
1.5 euros arros
7.5 euros gambes
TOTAL: 9.0 euros
```

### Test
```input
22
2
20
```
```output
2.75 kg arros
1.375 kg gambes
5.5 euros arros
27.5 euros gambes
TOTAL: 33.0 euros
```

### Test private
```input
24
16
8
```
```output
3.0 kg arros
1.5 kg gambes
48.0 euros arros
12.0 euros gambes
TOTAL: 60.0 euros
```
