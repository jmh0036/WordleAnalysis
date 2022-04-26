# WordleAnalysis

This is some initial analysis on Wordle.  Since a NYTimes dictionary could not be found, we are using a library found here: [https://github.com/fogleman/TWL06](https://github.com/fogleman/TWL06).

# Shell Output

The shell output of the Wordle analysis is:

```console
Five Letter Words: 8938

Occurrences of each letter Accounting for duplication within a word:    [3991, 1097, 1485, 1730, 4586, 791, 1115, 1217, 2638, 186, 961, 2442, 1342, 2033, 2986, 1393, 79, 2918, 4649, 2321, 1699, 476, 693, 210, 1403, 249]
Occurrences of each letter Not Accounting or duplication within a word: [3620, 1023, 1412, 1617, 3993, 708, 1052, 1188, 2516, 184, 924, 2231, 1270, 1922, 2632, 1310, 79, 2753, 4124, 2139, 1657, 465, 689, 209, 1372, 227]

The letter s achieves occurs 4649 times, which is the maximum amount accounting for letters occurring multiple times in a single word.
     Letter Order accounting for letters occurring multiple times in a single word: s, e, a, o, r, i, l, t, n, d, u, c, y, p, m, h, g, b, k, f, w, v, z, x, j, q

The letter s achieves occurs 4124 times, which is the maximum amount without accounting for letters occurring multiple times in a single word.
     Letter Order without accounting for letters occurring multiple times in a single word: s, e, a, r, o, i, l, t, n, u, d, c, y, p, m, h, g, b, k, f, w, v, z, x, j, q

Position 0:
     Distribution: [513, 621, 681, 470, 198, 441, 433, 349, 120, 139, 220, 416, 460, 208, 185, 581, 56, 434, 1084, 567, 123, 167, 303, 13, 100, 56]
     Max in Dist:  1084
     Max Letter:   s
     Letter Order: s, c, b, p, t, a, d, m, f, r, g, l, h, w, k, n, e, o, v, j, u, i, y, z, q, x

Position 1:
     Distribution: [1530, 56, 124, 61, 1110, 14, 51, 391, 1001, 7, 58, 519, 122, 251, 1384, 153, 12, 663, 66, 170, 822, 40, 99, 45, 173, 16]
     Max in Dist:  1530
     Max Letter:   a
     Letter Order: a, o, e, i, u, r, l, h, n, y, t, p, c, m, w, s, d, k, b, g, x, v, z, f, q, j

Position 2:
     Distribution: [866, 231, 286, 285, 580, 126, 253, 70, 763, 26, 158, 609, 353, 659, 696, 255, 8, 822, 354, 450, 456, 169, 159, 94, 123, 87]
     Max in Dist:  866
     Max Letter:   a
     Letter Order: a, r, i, o, n, l, e, u, t, s, m, c, d, p, g, b, v, w, k, f, y, x, z, h, j, q

Position 3:
     Distribution: [693, 151, 295, 319, 1749, 155, 285, 148, 601, 14, 338, 543, 279, 535, 482, 281, 1, 467, 360, 643, 265, 98, 92, 8, 67, 69]
     Max in Dist:  1749
     Max Letter:   e
     Letter Order: e, a, t, i, l, n, o, r, s, k, d, c, g, p, m, u, f, b, h, v, w, z, y, j, x, q

Position 4:
     Distribution: [389, 38, 99, 595, 949, 55, 93, 259, 153, 0, 187, 355, 128, 380, 239, 123, 2, 532, 2785, 491, 33, 2, 40, 50, 940, 21]
     Max in Dist:  2785
     Max Letter:   s
     Letter Order: s, e, y, d, r, t, a, n, l, h, o, k, i, m, p, c, g, f, x, w, b, u, z, v, q, j
```

# Graphics

The following is a graphical depiction of the data found in the code.  

The bar graph shows the number of times a letter appears in the dictionary:
![Letter Count Accounting for Multiplicity](https://github.com/jmh0036/WordleAnalysis/blob/main/LettersAccountingForMultiplicity.png?raw=true)

The bar graph shows the number of times there exists a word that contains that letter in the dictionary":
![Letter Count Accounting for Multiplicity](https://github.com/jmh0036/WordleAnalysis/blob/main/LettersNotAccountingForMultiplicity.png?raw=true)

Letter Distribution Position 0 (First Letter)
![Letter Distribution for First Letter](https://github.com/jmh0036/WordleAnalysis/blob/main/LetterDistributionPosition0.png?raw=true)

Letter Distribution Position 1 (Second Letter)
![Letter Distribution for Seconnd Letter](https://github.com/jmh0036/WordleAnalysis/blob/main/LetterDistributionPosition1.png?raw=true)

Letter Distribution Position 2 (Third Letter)
![Letter Distribution for Third Letter](https://github.com/jmh0036/WordleAnalysis/blob/main/LetterDistributionPosition2.png?raw=true)

Letter Distribution Position 3 (Fourth Letter)
![Letter Distribution for Fourth Letter](https://github.com/jmh0036/WordleAnalysis/blob/main/LetterDistributionPosition3.png?raw=true)

Letter Distribution Position 4 (Fifth Letter)
![Letter Distribution for Fifth Letter](https://github.com/jmh0036/WordleAnalysis/blob/main/LetterDistributionPosition4.png?raw=true)