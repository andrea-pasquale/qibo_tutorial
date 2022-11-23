import argparse
import time
import numpy as np
import matplotlib.pyplot as plt
from qibo import models, gates, set_backend

def create_superposition(nqubits):
    """Create circuit for superposition"""
    superposition = models.Circuit(nqubits+1)
    for i in range(nqubits):
        superposition.add(gates.H(i))
    superposition.add(gates.X(nqubits))
    superposition.add(gates.H(nqubits))

    return superposition

def create_oracle(nqubits):
    """Oracle"""
    oracle = models.Circuit(nqubits+1)
    oracle.add(gates.X(nqubits).controlled_by(*range(nqubits)))
    return oracle

def create_diffuser(nqubits):
    diffuser = models.Circuit(nqubits+1)
    for i in range(nqubits):
        diffuser.add(gates.H(i))
    for i in range(nqubits):
        diffuser.add(gates.X(i))
    diffuser.add(gates.Z(0).controlled_by(*range(1,nqubits)))
    for i in range(nqubits):
        diffuser.add(gates.X(i))
    for i in range(nqubits):
        diffuser.add(gates.H(i))
    return diffuser

def create_grover(nqubits, iterations):
    """Complete circuit that implements Grover's algorithm.
    
    Args:
        nqubits (int): Number of qubits in the circuit / target state.
        iterations (int): Number of times the oracle + diffuser operation is repeated.
    """
    superposition = create_superposition(nqubits)
    oracle = create_oracle(nqubits)
    diffuser = create_diffuser(nqubits)
    
    grover = models.Circuit(nqubits+1)
    grover += superposition
    for _ in range(iterations):
        grover += oracle + diffuser
    # measure all qubits
    grover.add([ gates.M(i) for i in range(nqubits)])
    return grover

def grover_iterations(nqubits, nsol=1):
    return int((np.pi/4)*np.sqrt((2**nqubits)/nsol))

def performance(backend, nqubits, platform=None):

    if platform is None:
        set_backend(backend)
    else:
        set_backend(backend, platform=platform)
    
    iterations = grover_iterations(nqubits,1)
    print("nqubits", nqubits, end="")
    circuit = create_grover(nqubits, iterations)
    start = time.time()
    result = circuit(nshots=1000)
    end = time.time()
    print(f"\tTime = {end-start}")
    # Frequency of the target bitstring
    freq = result.frequencies().get(nqubits * '1')
    print("Frequency =", freq)
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--nqubits", default=10, type=int, help="Number of qubits.")
    parser.add_argument("--backend", default="numpy", type=str, help="Qibo backend")
    parser.add_argument("--platform", default=None, type=str, help="Qibo backend platform")
    args = vars(parser.parse_args())
    performance(**args)