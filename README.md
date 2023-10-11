## Mini Project 7 
[![CI](https://github.com/nogibjj/IDS706_miniproject7_Mutian/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_miniproject7_Mutian/actions/workflows/cicd.yml)

## Overview

Package a Python script with setuptools or a similar tool

Include a user guide on how to install and use the tool

Include communication with an external or internal database (NoSQL, SQL, etc)

## Database Functions
**ALL Database function can be found in mylib.dbfunc.py**
## Connect & Create
<img width="567" alt="image" src="https://github.com/nogibjj/IDS706_miniproject5_Mutian/assets/108935314/461de4e5-fc57-40f2-babc-ee625e55113f">

### Read 

<img width="463" alt="image" src="https://github.com/nogibjj/IDS706_miniproject5_Mutian/assets/108935314/bc2fa42c-95fe-48cb-aa50-f98d76969786">

### Update

<img width="537" alt="image" src="https://github.com/nogibjj/IDS706_miniproject5_Mutian/assets/108935314/615b3233-7302-47b6-8cc2-fb41a6889102">

### Delete

<img width="583" alt="image" src="https://github.com/nogibjj/IDS706_miniproject5_Mutian/assets/108935314/873146d6-3317-4bee-8037-6bb5f7014dbf">


### Insert 

<img width="667" alt="image" src="https://github.com/nogibjj/IDS706_miniproject5_Mutian/assets/108935314/e0df2b90-100a-4bc3-9dd3-504f2c98ee20">


## Demo

* Pass the database name to main and do basic operations:
  
  `python main.py <databasename>`
  
  <img width="827" alt="image" src="https://github.com/nogibjj/IDS706_miniproject7_Mutian/assets/108935314/a48c150c-b9ec-46ea-9e7f-f8e912c0ef6d">

* To see the guid run:

  `python main.py --help`

  <img width="638" alt="image" src="https://github.com/nogibjj/IDS706_miniproject7_Mutian/assets/108935314/ec8d1d13-7841-40b1-822d-f1e158496805">

* Error
  when arguments are incorrect
  
  <img width="520" alt="image" src="https://github.com/nogibjj/IDS706_miniproject7_Mutian/assets/108935314/c60d07f0-465e-42a5-a7e2-b39a3a61d337">
  
  <img width="621" alt="image" src="https://github.com/nogibjj/IDS706_miniproject7_Mutian/assets/108935314/f86aee7d-893f-4d3e-ac1a-fd4c3d60b16d">


## Test
<img width="1159" alt="image" src="https://github.com/nogibjj/IDS706_miniproject5_Mutian/assets/108935314/b620bd3c-befe-478d-85ac-ff909f3fef09">

## Run

### Makefile Commands 
`make install`

`make format`

`make lint`

`make test`

`make all`
