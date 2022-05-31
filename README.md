Wipe file data via python  
  
install dependencies: ``` pip install -r requirements.txt ```
 
usage: ``` python pyshred.py [-h] [-z] [-r] [-i int] [-x] destination```
  
options:  
  -h, --help   show this help message and exit  
  -z           replace data with null-bytes  
  -r           replace data with randomly generated output  
  -i int       iterate a number of times  
  -x           remove file after shredding  
  
required:  
  destination  path to wipe  
  
Requires python >= 3.9
