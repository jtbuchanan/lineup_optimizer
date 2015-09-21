lineup_optimizer
================

### optimize.py

Optimizes Daily Fantasy Football Lineups

To operate:

```python optimize.py magic.csv 10```

Will return the 10 best lineups based on that csv of predictions

* * *

### makeCSV.py

Generates the magic.csv file required as an input for optimize.py

makeCSV.py requires the following three inputs (Rotowire subscription needed):

1. rw_QbRbWrTe.csv

   - To generate go to: http://www.rotowire.com/football/weekly-projections.htm
   - In Position drop down choose QB/RB/WR/TE
   - League Type PPR
   - Choose the appropriate week
   - Export to Excel
   - Open Excel save file as MS-DOS Comma Separated (.csv)
   - Use the name rw_QbRbWrTe.csv

1. rw_K.csv

   - While still on Rotowire, change Position drop down to K
   - Export to Excel, save as CSV, use the name rw_K.csv

1. fd.csv

   - Go tp FanDuel.com, start creating a lineup
   - Click the "Download players list" button
   - Change downloaded file name to fd.csv

Save all three .csv files in the same folder as makeCSV.py and then run

```python makeCSV.py```
