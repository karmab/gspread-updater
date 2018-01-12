
# this updates a google spreadsheet with provided line

## how to use

to test on docker, use the following, separating the column content with *+*

```
docker run --rm -it -v /Users/kboumedh/.credentials/:/root/.credentials -e doc="my secret document" karmab/gspread-updater bla1+bla2+bla3
```

using the frontend

```
curl -H "Content-Type: application/json" -X POST -d '{"row":"bla1+bla2+bla3","password":"secret"}' http://127.0.0.1:9000
```

## Todo

- send data this way ?
```
curl -X POST -d 'password=secret&row=bla1+bla2+bla3' 127.0.0.1:9000/
```

## Copyright

Copyright 2017 Karim Boumedhel

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Problems?

Send me a mail at [karimboumedhel@gmail.com](mailto:karimboumedhel@gmail.com) !

Mac Fly!!!

karmab
