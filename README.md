
# this updates a given google spreadsheet adding the provided line at the end of the last sheet

## requisites

- DOC env variable pointing to the document name to update
- PASSWORD env variable is defined on server side (only for frontend)

## how to use

to test on docker, use the following, separating the column content with *+*

```
docker run --rm -it -v ~/gspread:/root/.credentials -e DOC="$DOC" karmab/gspread-updater bla1+bla2+bla4
```

## using the frontend

alternatively, one can set the frontend and have people sending curl with the content
an environment variable PASSWORD can be set on the server and then needed on client side for updates to occur


launch the server using docker:

```
docker run --rm -it -p 9000:9000 -v ~/gspread:/root/.credentials -e DOC="$DOC" -e PASSWORD=$PASSWORD karmab/gspread-updater-fe
```

on openshift, we use two secrets:

- gspread-credentials to hold google credentials
- gspread-secret to specify a password (this is optional)

```
oc create secret generic gspread-credentials --from-file=client_secret.json
oc create secret generic gspread-password --from-literal=password=$PASSWORD
oc create -f gspread-updater-fe.yml
```

client side 
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
