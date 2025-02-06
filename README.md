### Simple manga recommendation based of off tf-idf & cosine similarity
right now it only makes recomemndations based off of synopsis similarity to user input

```
(new) PS C:\Users\obenn\OneDrive\Desktop\py> python nlp.py
   manga_id                                            title                                             genres                                             themes                                           synopsis
0         2                                          Berserk  ['Action', 'Adventure', 'Award Winning', 'Dram...  ['Gore', 'Military', 'Mythology', 'Psychologic...  Guts, a former mercenary now known as the "Bla...
1        13                                        One Piece                 ['Action', 'Adventure', 'Fantasy']                                                 []  Gol D. Roger, a man referred to as the "King o...
2      1706  JoJo no Kimyou na Bouken Part 7: Steel Ball Run  ['Action', 'Adventure', 'Mystery', 'Supernatur...                                     ['Historical']  In the American Old West, the world's greatest...
3      4632                                   Oyasumi Punpun                         ['Drama', 'Slice of Life']                                  ['Psychological']  Punpun Onodera is a normal 11-year-old boy liv...
4        25                              Fullmetal Alchemist  ['Action', 'Adventure', 'Award Winning', 'Dram...                                       ['Military']  Alchemists are knowledgeable and naturally tal...

Missing values in each column:
manga_id        0
title           0
genres          0
themes          0
synopsis    19923
dtype: int64

Number of duplicate rows:
0

Label distribution:
genres
['-----'] (nsfw)                                                                9046
['Romance']                                                               5305
['Boys Love', '------'] (nsfw)                                                  4632
[]                                                                        2412
['Comedy']                                                                2122
                                                                          ...
['Fantasy', 'Mystery', 'Slice of Life', 'Supernatural']                      1
['Comedy', '------', 'Sports']                                              1
['Action', 'Boys Love', 'Drama', 'Fantasy', 'Romance', 'Supernatural']       1
['Drama', 'Girls Love', 'Mystery']                                           1
['Fantasy', 'Mystery', 'Supernatural', 'Suspense']                           1
Name: count, Length: 1806, dtype: int64
Dropping rows with missing synopsis....

Missing values in each column:
manga_id    0
title       0
genres      0
themes      0
synopsis    0
dtype: int64
   manga_id                                            title  ...                                           synopsis                                             tokens
0         2                                          Berserk  ...  Guts, a former mercenary now known as the "Bla...  [guts, former, mercenary, known, black, swords...
1        13                                        One Piece  ...  Gol D. Roger, a man referred to as the "King o...  [gol, roger, man, referred, king, pirates, set...
2      1706  JoJo no Kimyou na Bouken Part 7: Steel Ball Run  ...  In the American Old West, the world's greatest...  [american, old, west, worlds, greatest, race, ...
3      4632                                   Oyasumi Punpun  ...  Punpun Onodera is a normal 11-year-old boy liv...  [punpun, onodera, normal, yearold, boy, living...
4        25                              Fullmetal Alchemist  ...  Alchemists are knowledgeable and naturally tal...  [alchemists, knowledgeable, naturally, talente...

[5 rows x 6 columns]
Enter a manga title or a brief synopsis to get recommendations: pirates on a journey to get treaure and fight along the way

Top 10 recommendations based on your input:
 - Gekijouban One Piece: Stampede
 - Love Flag★Girls!!
 - One Piece
 - Jolly Roger☆Fantasy
 - Kono Yo no Owari e no Tabi
 - One Piece Novel: Mugiwara Stories
 - Grenadier
 - Tramp.
 - Lodoss-tou Senki: Honoo no Majin
 - Seifuku Duty
```
