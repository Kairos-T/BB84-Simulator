from qiskit import QuantumCircuit, execute, Aer
from numpy.random import randint
import numpy as np
from art import *

NUM_QUBITS = 32


def generate_bits(n: int) -> np.ndarray:
    """
    Generate an array of random bits.

    Parameters:
    n (int): The number of bits to generate.

    Returns:
    np.ndarray: An array of random bits.
    """
    return randint(2, size=n)


def encode_message(bits: np.ndarray, basis: np.ndarray) -> list:
    """
    Encode a message using quantum bits.

    Parameters:
    bits (np.ndarray): The bits to encode.
    basis (np.ndarray): The basis to use for encoding.

    Returns:
    list: A list of QuantumCircuit objects representing the encoded message.
    """
    message = []
    for i in range(NUM_QUBITS):
        qc = QuantumCircuit(1, 1) # 1 qubit and 1 classical bit - message and measurement respectively
        if basis[i] == 0:  # Prepare qubit in Z-basis (i.e. |0> or |1>)
            if bits[i] == 1:
                qc.x(0) # Bit flip (Pauli-X gate)
        else:  # Prepare qubit in X-basis (i.e. |+> or |->)
            if bits[i] == 0:
                qc.h(0) # Hadamard gate
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        message.append(qc)
    return message


def simulate_quantum_channel(message: list, error_rate: float) -> list:
    """
    Simulate a quantum channel with a given error rate.

    Parameters:
    message (list): The original quantum message to be transmitted.
    error_rate (float): The rate at which errors occur during transmission.

    Returns:
    list: The noisy message after transmission through the quantum channel.
    """
    noisy_message = []
    for qc in message:
        if np.random.random() < error_rate:  # Bit flip with given error rate
            qc.x(0)
        noisy_message.append(qc)
    return noisy_message


def measure_message(message: list, basis: np.ndarray) -> list:
    """
    Measure a quantum message using a given basis.

    Parameters:
    message (list): The quantum message to be measured.
    basis (np.ndarray): The basis to use for measurement.

    Returns:
    list: The measurements results.
    """
    backend = Aer.get_backend("qasm_simulator")
    measurements = []
    for q in range(NUM_QUBITS):
        if basis[q] == 1:  # Measuring in X-basis
            message[q].h(0)
        message[q].measure(0, 0)
        result = execute(message[q], backend, shots=1, memory=True).result()
        measurements.append(int(result.get_memory()[0]))
    return measurements


def remove_garbage(a_basis: np.ndarray, b_basis: np.ndarray, bits: np.ndarray) -> list:
    """
    Remove bits that were measured in different bases.

    Parameters:
    a_basis (np.ndarray): The basis used by the first party.
    b_basis (np.ndarray): The basis used by the second party.
    bits (np.ndarray): The bits to be filtered.

    Returns:
    list: The filtered bits.
    """
    return [bits[q] for q in range(NUM_QUBITS) if a_basis[q] == b_basis[q]]  # Removes bits that do not match


def check_keys(key1: list, key2: list) -> None:
    """
    Check if two keys are the same.

    Parameters:
    key1 (list): The first key to be compared.
    key2 (list): The second key to be compared.

    Returns:
    None
    """
    print("\nAlice's key: ", key1)
    print("Bob's key:   ", key2)
    if key1 == key2:
        print("Keys are the same and secure.")
    else:
        print("Error: keys are different.")


def quantum_communication(error_rate: float, num_iterations: int):
    """
    Simulate quantum communication between two parties (Alice and Bob).

    Parameters:
    error_rate (float): The rate at which errors occur during transmission.
    num_iterations (int): The number of times to run the simulation.

    Returns:
    None
    """
    for i in range(num_iterations):
        alice_bits = generate_bits(NUM_QUBITS)
        alice_basis = generate_bits(NUM_QUBITS)
        message = encode_message(alice_bits, alice_basis)
        message = simulate_quantum_channel(message, error_rate)
        bob_basis = generate_bits(NUM_QUBITS)
        bob_results = measure_message(message, bob_basis)
        alice_key = remove_garbage(alice_basis, bob_basis, alice_bits)
        bob_key = remove_garbage(alice_basis, bob_basis, bob_results)
        check_keys(alice_key, bob_key)


def simulate_eavesdropping(
    message: list, eavesdropper_basis: np.ndarray, error_rate: float
) -> list:
    """
    Simulate an eavesdropper intercepting and measuring a quantum message.

    Parameters:
    message (list): The quantum message to be intercepted.
    eavesdropper_basis (np.ndarray): The basis used by the eavesdropper for measurement.
    error_rate (float): The rate at which the eavesdropper introduces errors.

    Returns:
    list: The intercepted message after measurement and introduction of errors.
    """
    for i in range(len(message)):
        qc = message[i]
        # Eavesdropper intercepts the qubit and measures it in a random basis
        if np.random.random() < 0.5:  # Measure in Z-basis with 50% probability
            qc.measure(0, 0)
        else:  # Measure in X-basis with 50% probability
            qc.h(0)
            qc.measure(0, 0)

        # Eavesdropper introduces errors with the given error rate
        if np.random.random() < error_rate:
            qc.x(0)  # Apply a bit flip error
    return message


def main():
    """
    Main function to simulate quantum communication with different error rates and eavesdropping attempts.

    The function provides a menu for the user to choose from different simulation options.
    The user can choose to simulate quantum communication with no error, low error rate, high error rate, or simulate an eavesdropping attempt.

    Returns:
    None
    """

    print("-" * 50 + "\n")
    print(text2art("BB84", font="small"))
    print("-" * 50)
    print("CTG Assignment CSF02 2023\n")
    print(
        "This script simulates QKD using the BB84 protocol.\n"
        "It includes functions for generating random bits,\n"
        "encoding messages with qubits,simulating a quantum\n"
        "channel with errors, measuring quantum messages,\nand removing bits measured in different bases.\n"
        "Users can choose between simulating communication\nwith no error, low error rate, high error rate,\n"
        "or simulating an eavesdropping attempt to observe\nthe effects on the integrity of the \n"
        "data transferred."
    )

    print("-" * 50 + "\n\n")

    num_iterations = 5  # Set the number of iterations
    while True:
        print("Choose an option:")
        print("[1] Simulate with 0 error")
        print("[2] Simulate with low error rate")
        print("[3] Simulate with high error rate")
        print("[4] Simulate eavesdropping attempt")
        print("[5] Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            quantum_communication(0.0, num_iterations)
            print()

        elif choice == "2":
            quantum_communication(0.05, num_iterations)
            print()
        elif choice == "3":
            quantum_communication(0.2, num_iterations)
            print()
        elif choice == "4":
            for _ in range(num_iterations):
                alice_bits = generate_bits(NUM_QUBITS)
                alice_basis = generate_bits(NUM_QUBITS)
                message = encode_message(alice_bits, alice_basis)
                eavesdropper_basis = generate_bits(NUM_QUBITS)
                message = simulate_eavesdropping(
                    message, eavesdropper_basis, 0.1)
                bob_basis = generate_bits(NUM_QUBITS)
                bob_results = measure_message(message, bob_basis)
                alice_key = remove_garbage(alice_basis, bob_basis, alice_bits)
                bob_key = remove_garbage(alice_basis, bob_basis, bob_results)

                check_keys(alice_key, bob_key)
            print()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
