# 参数寻优汇总报告 (parameter_optimization_strategy.md)

## 🟢 多空共振参数列表 (同一指标参数在多空方向盈亏差均 > 0)

| 周期              | 指标                 |   多头差值 |   空头差值 |   共振总差值 |
|:----------------|:-------------------|-------:|-------:|--------:|
| SOLUSDT_30m.csv | EMA(19,27)         |     13 |      1 |      14 |
| SOLUSDT_30m.csv | EMA(18,28)         |     13 |      1 |      14 |
| SOLUSDT_30m.csv | EMA(20,32)         |     13 |      1 |      14 |
| SOLUSDT_30m.csv | EMA(18,37)         |     11 |      1 |      12 |
| SOLUSDT_30m.csv | EMA(21,32)         |     11 |      1 |      12 |
| SOLUSDT_30m.csv | EMA(20,34)         |     11 |      1 |      12 |
| SOLUSDT_30m.csv | EMA(19,35)         |     11 |      1 |      12 |
| SOLUSDT_1h.csv  | SuperTrend(11,2.0) |      4 |      2 |       6 |
| SOLUSDT_1h.csv  | SuperTrend(10,2.0) |      4 |      2 |       6 |
| SOLUSDT_1h.csv  | SuperTrend(12,2.0) |      4 |      2 |       6 |
| SOLUSDT_4h.csv  | EMA(14,21)         |      3 |      2 |       5 |
| SOLUSDT_4h.csv  | EMA(16,19)         |      3 |      2 |       5 |
| SOLUSDT_4h.csv  | EMA(15,20)         |      3 |      2 |       5 |
| SOLUSDT_4h.csv  | EMA(13,21)         |      3 |      2 |       5 |
| SOLUSDT_4h.csv  | EMA(13,22)         |      3 |      2 |       5 |
| SOLUSDT_4h.csv  | EMA(15,19)         |      3 |      2 |       5 |
| SOLUSDT_4h.csv  | EMA(11,25)         |      4 |      1 |       5 |
| SOLUSDT_4h.csv  | EMA(14,20)         |      3 |      2 |       5 |
| SOLUSDT_4h.csv  | EMA(11,26)         |      3 |      2 |       5 |
| SOLUSDT_4h.csv  | EMA(12,23)         |      3 |      2 |       5 |
| SOLUSDT_1h.csv  | SuperTrend(9,2.2)  |      3 |      1 |       4 |
| SOLUSDT_1h.csv  | SuperTrend(10,2.2) |      3 |      1 |       4 |
| SOLUSDT_1h.csv  | SuperTrend(10,2.4) |      3 |      1 |       4 |
| SOLUSDT_1h.csv  | SuperTrend(12,2.2) |      3 |      1 |       4 |
| SOLUSDT_1h.csv  | SuperTrend(11,2.2) |      3 |      1 |       4 |
| SOLUSDT_1h.csv  | SuperTrend(9,2.4)  |      3 |      1 |       4 |
| SOLUSDT_1h.csv  | SuperTrend(12,2.6) |      2 |      2 |       4 |
| SOLUSDT_1h.csv  | SuperTrend(9,2.0)  |      3 |      1 |       4 |
| SOLUSDT_4h.csv  | EMA(12,24)         |      2 |      1 |       3 |
| SOLUSDT_4h.csv  | EMA(13,23)         |      1 |      2 |       3 |
| SOLUSDT_4h.csv  | EMA(10,30)         |      1 |      2 |       3 |
| SOLUSDT_4h.csv  | EMA(10,27)         |      1 |      2 |       3 |
| SOLUSDT_4h.csv  | EMA(10,29)         |      1 |      2 |       3 |
| SOLUSDT_4h.csv  | EMA(14,22)         |      1 |      2 |       3 |
| SOLUSDT_4h.csv  | EMA(11,28)         |      1 |      2 |       3 |
| SOLUSDT_4h.csv  | EMA(11,27)         |      1 |      2 |       3 |
| SOLUSDT_1h.csv  | SuperTrend(11,2.6) |      1 |      1 |       2 |
| SOLUSDT_1h.csv  | SuperTrend(12,2.4) |      1 |      1 |       2 |
| SOLUSDT_2h.csv  | SuperTrend(10,2.4) |      1 |      1 |       2 |
| SOLUSDT_4h.csv  | SuperTrend(11,2.6) |      1 |      1 |       2 |
| SOLUSDT_4h.csv  | SuperTrend(12,2.6) |      1 |      1 |       2 |

## 📊 指标优选详情 (各指标各方向仅保留 Top 20)

| 周期              | 指标类型       | 参数组合     | 方向   |   锚定次数 | 盈亏比(损:盈)   |   盈亏差值 |
|:----------------|:-----------|:---------|:-----|-------:|:-----------|-------:|
| SOLUSDT_15m.csv | EMA        | 7,21     | 多头   |    144 | 46:98      |     52 |
| SOLUSDT_15m.csv | EMA        | 8,19     | 多头   |    142 | 47:95      |     48 |
| SOLUSDT_15m.csv | EMA        | 7,22     | 多头   |    134 | 44:90      |     46 |
| SOLUSDT_15m.csv | EMA        | 8,17     | 多头   |    154 | 54:100     |     46 |
| SOLUSDT_15m.csv | EMA        | 7,20     | 多头   |    151 | 53:98      |     45 |
| SOLUSDT_15m.csv | EMA        | 8,18     | 多头   |    147 | 51:96      |     45 |
| SOLUSDT_15m.csv | EMA        | 7,18     | 多头   |    164 | 60:104     |     44 |
| SOLUSDT_15m.csv | EMA        | 7,19     | 多头   |    156 | 56:100     |     44 |
| SOLUSDT_15m.csv | EMA        | 8,20     | 多头   |    132 | 44:88      |     44 |
| SOLUSDT_15m.csv | EMA        | 9,18     | 多头   |    134 | 45:89      |     44 |
| SOLUSDT_15m.csv | EMA        | 8,16     | 多头   |    159 | 58:101     |     43 |
| SOLUSDT_15m.csv | EMA        | 9,19     | 多头   |    129 | 43:86      |     43 |
| SOLUSDT_15m.csv | EMA        | 10,18    | 多头   |    125 | 41:84      |     43 |
| SOLUSDT_15m.csv | EMA        | 7,23     | 多头   |    130 | 44:86      |     42 |
| SOLUSDT_15m.csv | EMA        | 10,17    | 多头   |    130 | 44:86      |     42 |
| SOLUSDT_15m.csv | EMA        | 11,17    | 多头   |    122 | 40:82      |     42 |
| SOLUSDT_15m.csv | EMA        | 12,16    | 多头   |    120 | 39:81      |     42 |
| SOLUSDT_15m.csv | EMA        | 7,16     | 多头   |    175 | 67:108     |     41 |
| SOLUSDT_15m.csv | EMA        | 8,22     | 多头   |    125 | 42:83      |     41 |
| SOLUSDT_15m.csv | EMA        | 10,16    | 多头   |    137 | 48:89      |     41 |
| SOLUSDT_15m.csv | MACD       | 9,29,8   | 多头   |    267 | 95:172     |     77 |
| SOLUSDT_15m.csv | MACD       | 9,22,8   | 多头   |    277 | 101:176    |     75 |
| SOLUSDT_15m.csv | MACD       | 10,35,8  | 多头   |    243 | 84:159     |     75 |
| SOLUSDT_15m.csv | MACD       | 9,21,8   | 多头   |    278 | 102:176    |     74 |
| SOLUSDT_15m.csv | MACD       | 9,28,8   | 多头   |    264 | 95:169     |     74 |
| SOLUSDT_15m.csv | MACD       | 9,30,8   | 多头   |    260 | 93:167     |     74 |
| SOLUSDT_15m.csv | MACD       | 10,27,10 | 多头   |    227 | 77:150     |     73 |
| SOLUSDT_15m.csv | MACD       | 10,28,10 | 多头   |    229 | 78:151     |     73 |
| SOLUSDT_15m.csv | MACD       | 13,22,10 | 多头   |    225 | 76:149     |     73 |
| SOLUSDT_15m.csv | MACD       | 14,21,10 | 多头   |    221 | 74:147     |     73 |
| SOLUSDT_15m.csv | MACD       | 14,22,10 | 多头   |    219 | 73:146     |     73 |
| SOLUSDT_15m.csv | MACD       | 11,27,9  | 多头   |    228 | 78:150     |     72 |
| SOLUSDT_15m.csv | MACD       | 11,29,9  | 多头   |    232 | 80:152     |     72 |
| SOLUSDT_15m.csv | MACD       | 11,34,8  | 多头   |    234 | 81:153     |     72 |
| SOLUSDT_15m.csv | MACD       | 12,24,10 | 多头   |    226 | 77:149     |     72 |
| SOLUSDT_15m.csv | MACD       | 12,26,10 | 多头   |    220 | 74:146     |     72 |
| SOLUSDT_15m.csv | MACD       | 13,24,10 | 多头   |    218 | 73:145     |     72 |
| SOLUSDT_15m.csv | MACD       | 14,23,9  | 多头   |    222 | 75:147     |     72 |
| SOLUSDT_15m.csv | MACD       | 15,21,9  | 多头   |    226 | 77:149     |     72 |
| SOLUSDT_15m.csv | MACD       | 9,23,8   | 多头   |    275 | 102:173    |     71 |
| SOLUSDT_15m.csv | SuperTrend | 10,2.0   | 多头   |     31 | 10:21      |     11 |
| SOLUSDT_15m.csv | SuperTrend | 11,2.0   | 多头   |     28 | 9:19       |     10 |
| SOLUSDT_15m.csv | SuperTrend | 12,2.0   | 多头   |     28 | 9:19       |     10 |
| SOLUSDT_15m.csv | SuperTrend | 12,2.2   | 多头   |     26 | 9:17       |      8 |
| SOLUSDT_15m.csv | SuperTrend | 9,2.0    | 多头   |     31 | 12:19      |      7 |
| SOLUSDT_15m.csv | SuperTrend | 9,2.2    | 多头   |     22 | 8:14       |      6 |
| SOLUSDT_15m.csv | SuperTrend | 10,2.2   | 多头   |     22 | 8:14       |      6 |
| SOLUSDT_15m.csv | SuperTrend | 11,2.2   | 多头   |     23 | 9:14       |      5 |
| SOLUSDT_15m.csv | SuperTrend | 9,2.4    | 多头   |     16 | 6:10       |      4 |
| SOLUSDT_15m.csv | SuperTrend | 10,2.4   | 多头   |     16 | 6:10       |      4 |
| SOLUSDT_15m.csv | SuperTrend | 11,2.4   | 多头   |     15 | 6:9        |      3 |
| SOLUSDT_15m.csv | SuperTrend | 12,2.4   | 多头   |     16 | 7:9        |      2 |
| SOLUSDT_15m.csv | SuperTrend | 9,2.8    | 空头   |     10 | 3:7        |      4 |
| SOLUSDT_15m.csv | SuperTrend | 10,2.8   | 空头   |     11 | 4:7        |      3 |
| SOLUSDT_15m.csv | SuperTrend | 12,3.0   | 空头   |      9 | 3:6        |      3 |
| SOLUSDT_15m.csv | SuperTrend | 11,2.8   | 空头   |     11 | 4:7        |      3 |
| SOLUSDT_15m.csv | SuperTrend | 12,2.8   | 空头   |     10 | 4:6        |      2 |
| SOLUSDT_15m.csv | SuperTrend | 9,2.6    | 空头   |     13 | 6:7        |      1 |
| SOLUSDT_15m.csv | SuperTrend | 10,3.0   | 空头   |      9 | 4:5        |      1 |
| SOLUSDT_15m.csv | SuperTrend | 9,3.2    | 空头   |      9 | 4:5        |      1 |
| SOLUSDT_15m.csv | SuperTrend | 9,3.0    | 空头   |      9 | 4:5        |      1 |
| SOLUSDT_15m.csv | SuperTrend | 11,3.0   | 空头   |      9 | 4:5        |      1 |
| SOLUSDT_1h.csv  | EMA        | 7,23     | 多头   |     36 | 9:27       |     18 |
| SOLUSDT_1h.csv  | EMA        | 8,22     | 多头   |     38 | 10:28      |     18 |
| SOLUSDT_1h.csv  | EMA        | 9,21     | 多头   |     36 | 9:27       |     18 |
| SOLUSDT_1h.csv  | EMA        | 7,18     | 多头   |     41 | 12:29      |     17 |
| SOLUSDT_1h.csv  | EMA        | 8,23     | 多头   |     35 | 9:26       |     17 |
| SOLUSDT_1h.csv  | EMA        | 10,17    | 多头   |     37 | 10:27      |     17 |
| SOLUSDT_1h.csv  | EMA        | 10,19    | 多头   |     35 | 9:26       |     17 |
| SOLUSDT_1h.csv  | EMA        | 11,18    | 多头   |     35 | 9:26       |     17 |
| SOLUSDT_1h.csv  | EMA        | 7,15     | 多头   |     44 | 14:30      |     16 |
| SOLUSDT_1h.csv  | EMA        | 7,19     | 多头   |     40 | 12:28      |     16 |
| SOLUSDT_1h.csv  | EMA        | 7,24     | 多头   |     36 | 10:26      |     16 |
| SOLUSDT_1h.csv  | EMA        | 8,17     | 多头   |     40 | 12:28      |     16 |
| SOLUSDT_1h.csv  | EMA        | 8,18     | 多头   |     40 | 12:28      |     16 |
| SOLUSDT_1h.csv  | EMA        | 9,15     | 多头   |     40 | 12:28      |     16 |
| SOLUSDT_1h.csv  | EMA        | 9,18     | 多头   |     36 | 10:26      |     16 |
| SOLUSDT_1h.csv  | EMA        | 9,20     | 多头   |     36 | 10:26      |     16 |
| SOLUSDT_1h.csv  | EMA        | 11,16    | 多头   |     36 | 10:26      |     16 |
| SOLUSDT_1h.csv  | EMA        | 12,17    | 多头   |     34 | 9:25       |     16 |
| SOLUSDT_1h.csv  | EMA        | 13,16    | 多头   |     34 | 9:25       |     16 |
| SOLUSDT_1h.csv  | EMA        | 7,20     | 多头   |     39 | 12:27      |     15 |
| SOLUSDT_1h.csv  | MACD       | 9,26,8   | 多头   |     66 | 22:44      |     22 |
| SOLUSDT_1h.csv  | MACD       | 9,30,8   | 多头   |     66 | 22:44      |     22 |
| SOLUSDT_1h.csv  | MACD       | 9,27,8   | 多头   |     65 | 22:43      |     21 |
| SOLUSDT_1h.csv  | MACD       | 9,28,8   | 多头   |     65 | 22:43      |     21 |
| SOLUSDT_1h.csv  | MACD       | 9,29,8   | 多头   |     67 | 23:44      |     21 |
| SOLUSDT_1h.csv  | MACD       | 10,27,8  | 多头   |     63 | 21:42      |     21 |
| SOLUSDT_1h.csv  | MACD       | 9,25,8   | 多头   |     66 | 23:43      |     20 |
| SOLUSDT_1h.csv  | MACD       | 9,29,9   | 多头   |     64 | 22:42      |     20 |
| SOLUSDT_1h.csv  | MACD       | 10,29,8  | 多头   |     64 | 22:42      |     20 |
| SOLUSDT_1h.csv  | MACD       | 15,31,9  | 多头   |     48 | 14:34      |     20 |
| SOLUSDT_1h.csv  | MACD       | 9,23,8   | 多头   |     67 | 24:43      |     19 |
| SOLUSDT_1h.csv  | MACD       | 9,24,9   | 多头   |     65 | 23:42      |     19 |
| SOLUSDT_1h.csv  | MACD       | 9,26,9   | 多头   |     63 | 22:41      |     19 |
| SOLUSDT_1h.csv  | MACD       | 9,30,9   | 多头   |     65 | 23:42      |     19 |
| SOLUSDT_1h.csv  | MACD       | 9,33,8   | 多头   |     65 | 23:42      |     19 |
| SOLUSDT_1h.csv  | MACD       | 9,34,8   | 多头   |     65 | 23:42      |     19 |
| SOLUSDT_1h.csv  | MACD       | 9,35,8   | 多头   |     65 | 23:42      |     19 |
| SOLUSDT_1h.csv  | MACD       | 10,23,8  | 多头   |     65 | 23:42      |     19 |
| SOLUSDT_1h.csv  | MACD       | 10,24,8  | 多头   |     65 | 23:42      |     19 |
| SOLUSDT_1h.csv  | MACD       | 10,26,8  | 多头   |     63 | 22:41      |     19 |
| SOLUSDT_1h.csv  | SuperTrend | 10,2.0   | 多头   |      8 | 2:6        |      4 |
| SOLUSDT_1h.csv  | SuperTrend | 11,2.0   | 多头   |      8 | 2:6        |      4 |
| SOLUSDT_1h.csv  | SuperTrend | 12,2.0   | 多头   |      8 | 2:6        |      4 |
| SOLUSDT_1h.csv  | SuperTrend | 9,2.4    | 多头   |      7 | 2:5        |      3 |
| SOLUSDT_1h.csv  | SuperTrend | 9,2.2    | 多头   |      7 | 2:5        |      3 |
| SOLUSDT_1h.csv  | SuperTrend | 9,2.0    | 多头   |      7 | 2:5        |      3 |
| SOLUSDT_1h.csv  | SuperTrend | 12,2.2   | 多头   |      7 | 2:5        |      3 |
| SOLUSDT_1h.csv  | SuperTrend | 10,2.2   | 多头   |      7 | 2:5        |      3 |
| SOLUSDT_1h.csv  | SuperTrend | 11,2.2   | 多头   |      7 | 2:5        |      3 |
| SOLUSDT_1h.csv  | SuperTrend | 10,2.4   | 多头   |      7 | 2:5        |      3 |
| SOLUSDT_1h.csv  | SuperTrend | 9,3.2    | 多头   |      2 | 0:2        |      2 |
| SOLUSDT_1h.csv  | SuperTrend | 12,2.6   | 多头   |      6 | 2:4        |      2 |
| SOLUSDT_1h.csv  | SuperTrend | 11,2.6   | 多头   |      5 | 2:3        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 12,2.4   | 多头   |      7 | 3:4        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 10,2.0   | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_1h.csv  | SuperTrend | 12,2.6   | 空头   |      6 | 2:4        |      2 |
| SOLUSDT_1h.csv  | SuperTrend | 11,2.4   | 空头   |      6 | 2:4        |      2 |
| SOLUSDT_1h.csv  | SuperTrend | 11,2.0   | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_1h.csv  | SuperTrend | 12,2.0   | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_1h.csv  | SuperTrend | 9,2.0    | 空头   |      7 | 3:4        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 9,2.4    | 空头   |      7 | 3:4        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 9,2.2    | 空头   |      7 | 3:4        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 10,2.6   | 空头   |      3 | 1:2        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 10,2.4   | 空头   |      7 | 3:4        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 10,2.2   | 空头   |      7 | 3:4        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 9,2.6    | 空头   |      3 | 1:2        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 11,2.6   | 空头   |      5 | 2:3        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 11,2.2   | 空头   |      7 | 3:4        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 12,2.2   | 空头   |      7 | 3:4        |      1 |
| SOLUSDT_1h.csv  | SuperTrend | 12,2.4   | 空头   |      7 | 3:4        |      1 |
| SOLUSDT_2h.csv  | EMA        | 9,41     | 多头   |     18 | 4:14       |     10 |
| SOLUSDT_2h.csv  | EMA        | 10,40    | 多头   |     18 | 4:14       |     10 |
| SOLUSDT_2h.csv  | EMA        | 7,15     | 多头   |     25 | 8:17       |      9 |
| SOLUSDT_2h.csv  | EMA        | 9,42     | 多头   |     17 | 4:13       |      9 |
| SOLUSDT_2h.csv  | EMA        | 7,16     | 多头   |     24 | 8:16       |      8 |
| SOLUSDT_2h.csv  | EMA        | 8,15     | 多头   |     22 | 7:15       |      8 |
| SOLUSDT_2h.csv  | EMA        | 21,26    | 多头   |     18 | 5:13       |      8 |
| SOLUSDT_2h.csv  | EMA        | 7,17     | 多头   |     23 | 8:15       |      7 |
| SOLUSDT_2h.csv  | EMA        | 7,42     | 多头   |     19 | 6:13       |      7 |
| SOLUSDT_2h.csv  | EMA        | 7,43     | 多头   |     19 | 6:13       |      7 |
| SOLUSDT_2h.csv  | EMA        | 8,16     | 多头   |     21 | 7:14       |      7 |
| SOLUSDT_2h.csv  | EMA        | 8,17     | 多头   |     21 | 7:14       |      7 |
| SOLUSDT_2h.csv  | EMA        | 9,43     | 多头   |     15 | 4:11       |      7 |
| SOLUSDT_2h.csv  | EMA        | 9,44     | 多头   |     15 | 4:11       |      7 |
| SOLUSDT_2h.csv  | EMA        | 9,45     | 多头   |     15 | 4:11       |      7 |
| SOLUSDT_2h.csv  | EMA        | 13,34    | 多头   |     17 | 5:12       |      7 |
| SOLUSDT_2h.csv  | EMA        | 13,36    | 多头   |     17 | 5:12       |      7 |
| SOLUSDT_2h.csv  | EMA        | 14,33    | 多头   |     17 | 5:12       |      7 |
| SOLUSDT_2h.csv  | EMA        | 15,32    | 多头   |     17 | 5:12       |      7 |
| SOLUSDT_2h.csv  | EMA        | 15,34    | 多头   |     15 | 4:11       |      7 |
| SOLUSDT_2h.csv  | MACD       | 9,25,8   | 多头   |     31 | 7:24       |     17 |
| SOLUSDT_2h.csv  | MACD       | 15,32,10 | 多头   |     27 | 5:22       |     17 |
| SOLUSDT_2h.csv  | MACD       | 9,23,8   | 多头   |     30 | 7:23       |     16 |
| SOLUSDT_2h.csv  | MACD       | 9,24,8   | 多头   |     30 | 7:23       |     16 |
| SOLUSDT_2h.csv  | MACD       | 9,24,10  | 多头   |     28 | 6:22       |     16 |
| SOLUSDT_2h.csv  | MACD       | 9,27,9   | 多头   |     28 | 6:22       |     16 |
| SOLUSDT_2h.csv  | MACD       | 9,30,9   | 多头   |     26 | 5:21       |     16 |
| SOLUSDT_2h.csv  | MACD       | 10,20,8  | 多头   |     30 | 7:23       |     16 |
| SOLUSDT_2h.csv  | MACD       | 10,24,9  | 多头   |     28 | 6:22       |     16 |
| SOLUSDT_2h.csv  | MACD       | 11,25,8  | 多头   |     28 | 6:22       |     16 |
| SOLUSDT_2h.csv  | MACD       | 12,22,8  | 多头   |     28 | 6:22       |     16 |
| SOLUSDT_2h.csv  | MACD       | 12,23,8  | 多头   |     28 | 6:22       |     16 |
| SOLUSDT_2h.csv  | MACD       | 14,34,10 | 多头   |     26 | 5:21       |     16 |
| SOLUSDT_2h.csv  | MACD       | 14,35,10 | 多头   |     26 | 5:21       |     16 |
| SOLUSDT_2h.csv  | MACD       | 15,33,10 | 多头   |     26 | 5:21       |     16 |
| SOLUSDT_2h.csv  | MACD       | 15,34,10 | 多头   |     26 | 5:21       |     16 |
| SOLUSDT_2h.csv  | MACD       | 9,23,10  | 多头   |     29 | 7:22       |     15 |
| SOLUSDT_2h.csv  | MACD       | 9,24,9   | 多头   |     29 | 7:22       |     15 |
| SOLUSDT_2h.csv  | MACD       | 9,25,9   | 多头   |     29 | 7:22       |     15 |
| SOLUSDT_2h.csv  | MACD       | 9,26,9   | 多头   |     29 | 7:22       |     15 |
| SOLUSDT_2h.csv  | SuperTrend | 9,3.2    | 多头   |      1 | 0:1        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 10,2.4   | 多头   |      3 | 1:2        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 10,2.6   | 多头   |      3 | 1:2        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 10,3.2   | 多头   |      1 | 0:1        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 11,2.4   | 多头   |      3 | 1:2        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 11,2.6   | 多头   |      3 | 1:2        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 11,3.2   | 多头   |      1 | 0:1        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 12,2.6   | 多头   |      3 | 1:2        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 12,3.2   | 多头   |      1 | 0:1        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 9,2.2    | 空头   |      3 | 1:2        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 10,2.2   | 空头   |      3 | 1:2        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 10,2.4   | 空头   |      3 | 1:2        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 11,2.2   | 空头   |      3 | 1:2        |      1 |
| SOLUSDT_2h.csv  | SuperTrend | 12,2.2   | 空头   |      3 | 1:2        |      1 |
| SOLUSDT_30m.csv | EMA        | 7,43     | 多头   |     56 | 14:42      |     28 |
| SOLUSDT_30m.csv | EMA        | 7,33     | 多头   |     59 | 16:43      |     27 |
| SOLUSDT_30m.csv | EMA        | 7,34     | 多头   |     57 | 15:42      |     27 |
| SOLUSDT_30m.csv | EMA        | 7,18     | 多头   |     80 | 27:53      |     26 |
| SOLUSDT_30m.csv | EMA        | 7,19     | 多头   |     74 | 24:50      |     26 |
| SOLUSDT_30m.csv | EMA        | 8,16     | 多头   |     76 | 25:51      |     26 |
| SOLUSDT_30m.csv | EMA        | 8,17     | 多头   |     72 | 23:49      |     26 |
| SOLUSDT_30m.csv | EMA        | 7,40     | 多头   |     53 | 14:39      |     25 |
| SOLUSDT_30m.csv | EMA        | 7,42     | 多头   |     55 | 15:40      |     25 |
| SOLUSDT_30m.csv | EMA        | 7,27     | 多头   |     62 | 19:43      |     24 |
| SOLUSDT_30m.csv | EMA        | 7,38     | 多头   |     54 | 15:39      |     24 |
| SOLUSDT_30m.csv | EMA        | 7,39     | 多头   |     54 | 15:39      |     24 |
| SOLUSDT_30m.csv | EMA        | 7,41     | 多头   |     54 | 15:39      |     24 |
| SOLUSDT_30m.csv | EMA        | 7,44     | 多头   |     56 | 16:40      |     24 |
| SOLUSDT_30m.csv | EMA        | 8,19     | 多头   |     70 | 23:47      |     24 |
| SOLUSDT_30m.csv | EMA        | 8,26     | 多头   |     62 | 19:43      |     24 |
| SOLUSDT_30m.csv | EMA        | 8,32     | 多头   |     58 | 17:41      |     24 |
| SOLUSDT_30m.csv | EMA        | 9,15     | 多头   |     72 | 24:48      |     24 |
| SOLUSDT_30m.csv | EMA        | 9,24     | 多头   |     60 | 18:42      |     24 |
| SOLUSDT_30m.csv | EMA        | 7,15     | 多头   |     83 | 30:53      |     23 |
| SOLUSDT_30m.csv | EMA        | 18,28    | 空头   |     41 | 20:21      |      1 |
| SOLUSDT_30m.csv | EMA        | 18,37    | 空头   |     35 | 17:18      |      1 |
| SOLUSDT_30m.csv | EMA        | 19,27    | 空头   |     41 | 20:21      |      1 |
| SOLUSDT_30m.csv | EMA        | 19,35    | 空头   |     35 | 17:18      |      1 |
| SOLUSDT_30m.csv | EMA        | 20,32    | 空头   |     35 | 17:18      |      1 |
| SOLUSDT_30m.csv | EMA        | 20,34    | 空头   |     35 | 17:18      |      1 |
| SOLUSDT_30m.csv | EMA        | 21,32    | 空头   |     35 | 17:18      |      1 |
| SOLUSDT_30m.csv | MACD       | 9,20,8   | 多头   |    139 | 56:83      |     27 |
| SOLUSDT_30m.csv | MACD       | 9,21,8   | 多头   |    137 | 58:79      |     21 |
| SOLUSDT_30m.csv | MACD       | 15,34,10 | 多头   |     93 | 36:57      |     21 |
| SOLUSDT_30m.csv | MACD       | 9,22,8   | 多头   |    136 | 58:78      |     20 |
| SOLUSDT_30m.csv | MACD       | 15,33,10 | 多头   |     94 | 37:57      |     20 |
| SOLUSDT_30m.csv | MACD       | 9,21,9   | 多头   |    131 | 56:75      |     19 |
| SOLUSDT_30m.csv | MACD       | 12,28,10 | 多头   |    113 | 47:66      |     19 |
| SOLUSDT_30m.csv | MACD       | 13,29,9  | 多头   |    113 | 47:66      |     19 |
| SOLUSDT_30m.csv | MACD       | 14,29,8  | 多头   |    113 | 47:66      |     19 |
| SOLUSDT_30m.csv | MACD       | 14,31,8  | 多头   |    115 | 48:67      |     19 |
| SOLUSDT_30m.csv | MACD       | 15,27,8  | 多头   |    113 | 47:66      |     19 |
| SOLUSDT_30m.csv | MACD       | 15,35,10 | 多头   |     91 | 36:55      |     19 |
| SOLUSDT_30m.csv | MACD       | 9,20,9   | 多头   |    136 | 59:77      |     18 |
| SOLUSDT_30m.csv | MACD       | 9,23,8   | 多头   |    134 | 58:76      |     18 |
| SOLUSDT_30m.csv | MACD       | 10,20,8  | 多头   |    136 | 59:77      |     18 |
| SOLUSDT_30m.csv | MACD       | 12,29,10 | 多头   |    114 | 48:66      |     18 |
| SOLUSDT_30m.csv | MACD       | 13,28,9  | 多头   |    112 | 47:65      |     18 |
| SOLUSDT_30m.csv | MACD       | 13,31,9  | 多头   |    116 | 49:67      |     18 |
| SOLUSDT_30m.csv | MACD       | 14,27,9  | 多头   |    114 | 48:66      |     18 |
| SOLUSDT_30m.csv | MACD       | 14,28,10 | 多头   |    108 | 45:63      |     18 |
| SOLUSDT_30m.csv | SuperTrend | 9,2.6    | 空头   |      9 | 4:5        |      1 |
| SOLUSDT_30m.csv | SuperTrend | 10,2.6   | 空头   |      7 | 3:4        |      1 |
| SOLUSDT_30m.csv | SuperTrend | 12,2.2   | 空头   |     15 | 7:8        |      1 |
| SOLUSDT_4h.csv  | EMA        | 7,19     | 多头   |     12 | 3:9        |      6 |
| SOLUSDT_4h.csv  | EMA        | 8,17     | 多头   |     12 | 3:9        |      6 |
| SOLUSDT_4h.csv  | EMA        | 9,15     | 多头   |     14 | 4:10       |      6 |
| SOLUSDT_4h.csv  | EMA        | 7,18     | 多头   |     13 | 4:9        |      5 |
| SOLUSDT_4h.csv  | EMA        | 9,16     | 多头   |     11 | 3:8        |      5 |
| SOLUSDT_4h.csv  | EMA        | 10,15    | 多头   |     11 | 3:8        |      5 |
| SOLUSDT_4h.csv  | EMA        | 19,39    | 多头   |      7 | 1:6        |      5 |
| SOLUSDT_4h.csv  | EMA        | 20,36    | 多头   |      7 | 1:6        |      5 |
| SOLUSDT_4h.csv  | EMA        | 21,34    | 多头   |      7 | 1:6        |      5 |
| SOLUSDT_4h.csv  | EMA        | 7,17     | 多头   |     14 | 5:9        |      4 |
| SOLUSDT_4h.csv  | EMA        | 7,20     | 多头   |     12 | 4:8        |      4 |
| SOLUSDT_4h.csv  | EMA        | 8,16     | 多头   |     14 | 5:9        |      4 |
| SOLUSDT_4h.csv  | EMA        | 8,27     | 多头   |     10 | 3:7        |      4 |
| SOLUSDT_4h.csv  | EMA        | 9,26     | 多头   |     10 | 3:7        |      4 |
| SOLUSDT_4h.csv  | EMA        | 11,25    | 多头   |     10 | 3:7        |      4 |
| SOLUSDT_4h.csv  | EMA        | 18,44    | 多头   |      6 | 1:5        |      4 |
| SOLUSDT_4h.csv  | EMA        | 18,45    | 多头   |      6 | 1:5        |      4 |
| SOLUSDT_4h.csv  | EMA        | 19,40    | 多头   |      6 | 1:5        |      4 |
| SOLUSDT_4h.csv  | EMA        | 20,30    | 多头   |      8 | 2:6        |      4 |
| SOLUSDT_4h.csv  | EMA        | 20,37    | 多头   |      6 | 1:5        |      4 |
| SOLUSDT_4h.csv  | EMA        | 8,34     | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 8,35     | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 9,30     | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 9,31     | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 9,32     | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 9,33     | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 10,27    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 10,28    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 10,29    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 10,30    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 11,26    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 11,27    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 11,28    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 12,23    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 12,25    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 12,26    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 13,21    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 13,22    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 13,23    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | EMA        | 13,24    | 空头   |      8 | 3:5        |      2 |
| SOLUSDT_4h.csv  | MACD       | 9,22,8   | 多头   |     21 | 5:16       |     11 |
| SOLUSDT_4h.csv  | MACD       | 9,23,8   | 多头   |     21 | 5:16       |     11 |
| SOLUSDT_4h.csv  | MACD       | 9,20,9   | 多头   |     22 | 6:16       |     10 |
| SOLUSDT_4h.csv  | MACD       | 9,32,8   | 多头   |     22 | 6:16       |     10 |
| SOLUSDT_4h.csv  | MACD       | 9,33,8   | 多头   |     22 | 6:16       |     10 |
| SOLUSDT_4h.csv  | MACD       | 9,34,8   | 多头   |     22 | 6:16       |     10 |
| SOLUSDT_4h.csv  | MACD       | 9,35,8   | 多头   |     22 | 6:16       |     10 |
| SOLUSDT_4h.csv  | MACD       | 10,20,8  | 多头   |     22 | 6:16       |     10 |
| SOLUSDT_4h.csv  | MACD       | 10,30,8  | 多头   |     22 | 6:16       |     10 |
| SOLUSDT_4h.csv  | MACD       | 10,31,8  | 多头   |     22 | 6:16       |     10 |
| SOLUSDT_4h.csv  | MACD       | 9,21,9   | 多头   |     21 | 6:15       |      9 |
| SOLUSDT_4h.csv  | MACD       | 9,29,8   | 多头   |     21 | 6:15       |      9 |
| SOLUSDT_4h.csv  | MACD       | 9,30,8   | 多头   |     21 | 6:15       |      9 |
| SOLUSDT_4h.csv  | MACD       | 9,31,8   | 多头   |     21 | 6:15       |      9 |
| SOLUSDT_4h.csv  | MACD       | 10,21,8  | 多头   |     21 | 6:15       |      9 |
| SOLUSDT_4h.csv  | MACD       | 10,28,8  | 多头   |     21 | 6:15       |      9 |
| SOLUSDT_4h.csv  | MACD       | 10,29,8  | 多头   |     21 | 6:15       |      9 |
| SOLUSDT_4h.csv  | MACD       | 10,33,8  | 多头   |     21 | 6:15       |      9 |
| SOLUSDT_4h.csv  | MACD       | 10,34,8  | 多头   |     21 | 6:15       |      9 |
| SOLUSDT_4h.csv  | MACD       | 10,35,8  | 多头   |     21 | 6:15       |      9 |
| SOLUSDT_4h.csv  | SuperTrend | 11,2.6   | 多头   |      1 | 0:1        |      1 |
| SOLUSDT_4h.csv  | SuperTrend | 12,2.6   | 多头   |      1 | 0:1        |      1 |
| SOLUSDT_4h.csv  | SuperTrend | 9,2.4    | 空头   |      1 | 0:1        |      1 |
| SOLUSDT_4h.csv  | SuperTrend | 11,2.6   | 空头   |      1 | 0:1        |      1 |
| SOLUSDT_4h.csv  | SuperTrend | 12,2.6   | 空头   |      1 | 0:1        |      1 |