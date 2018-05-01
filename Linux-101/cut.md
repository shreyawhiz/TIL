````javascript
$ cat state.txt
$ Andhra Pradesh
$ Arunachal Pradesh
$ Assam
$ Bihar
$ Chhattisgarh
````

#### -b(byte): To extract the specific bytes

````javascript
$ cut -b 1 state.txt
$ A
$ A
$ A
$ B
$ C

List without ranges
$ cut -b 1,2,3 state.txt
$ And
$ Aru
$ Ass
$ Bih
$ Chh

In this, 1- indicate from 1st byte to end byte of a line
$ cut -b 1- state.txt
$ Andhra Pradesh
$ Arunachal Pradesh
$ Assam
$ Bihar
$ Chhattisgarh

In this, -3 indicate from 1st byte to 3rd byte of a line
$ cut -b 3- state.txt
$ Andhra Pradesh
$ Arunachal Pradesh
$ Assam
$ Bihar
$ Chhattisgarh
````
