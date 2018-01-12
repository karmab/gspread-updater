
# this updates a google spreadsheet with provided line

to test on docker, use the following, separating the column content with *+*

```
docker run --rm -it -v /Users/kboumedh/.credentials/:/root/.credentials karmab/gspread-updater BLA+BLA+BLA2
```
