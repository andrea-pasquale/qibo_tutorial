# Practical Quantum Computing School 
This folder includes the following

* `exercise.ipynb` notebook with exercise for the students (only CPU)
* `solution.ipynb` notebook with exercise + solution
* `main.py` python script for GPU application

## Running the python script
The script `main.py` executes the exercise presented in `exercise.ipynb` following the supported configuration flags (check `python main.py -h`):

```
$ python main.py -h 

usage: main.py [-h] [--nqubits NQUBITS] [--backend BACKEND]
               [--platform PLATFORM]

optional arguments:
  -h, --help           show this help message and exit
  --nqubits NQUBITS    Number of qubits.
  --backend BACKEND    Qibo backend
  --platform PLATFORM  Qibo backend platform
