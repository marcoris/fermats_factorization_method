# fermats_factorization_method
The way to generate the private key (id_rsa) is that the generation of the cryptography is weak. The difference of p and q is very small.  
The `id_rsa.pub` file has to be in the root directory of the script.  

## Kali
Preparations to run the script:  
```
python3 -m venv path/to/venv

path/to/venv/bin/python3 path/to/venv/bin/pip install pycryptodome
path/to/venv/bin/python3 path/to/venv/bin/pip install gmpy2
```

## Running the Fermat's Factorization Method
```
path/to/venv/bin/python3 rsa.py
```
