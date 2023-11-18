# bb84-simulation
This repository contains a Python script that simulates Quantum Key Distribution (QKD) using the BB84 protocol as part of my group's cryptography assignment. The BB84 protocol is a quantum key distribution scheme that allows two parties (Alice and Bob) to securely exchange cryptographic keys. 

## Getting Started

1. Clone this repository:
```bash
git clone https://github.com/Kairos-T/bb84-simulation
cd bb84-simulation
```

2. (Optional): Create a Python virtual environment
```bash
sudo python3 -m venv venv
source venv/bin/activate
```

3. Install required dependencies
```bash
pip install -r requirements.txt
```

4. Run the script:
```bash
python3 main.py
```


## Simulation Options
1. **Simulate with 0 error**: Simulate quantum communication with no errors.
2. **Simulate with low error rate**: Simulate quantum communication with a low error rate.
3. **Simulate with high error rate**: Simulate quantum communication with a high error rate.
4. **Simulate eavesdropping attempt**: Simulate an eavesdropper intercepting and measuring a quantum message.

## Simulation Results (Sample)

### Main Menu
```
--------------------------------------------------


 ____   ____    ___   _  _   
| __ ) | __ )  ( _ ) | || |  
|  _ \ |  _ \  / _ \ | || |_ 
| |_) || |_) || (_) ||__   _|
|____/ |____/  \___/    |_|  
                             

--------------------------------------------------
CTG Assignment CSF02 2023

This script simulates QKD using the BB84 protocol.
It includes functions for generating random bits,
encoding messages with qubits,simulating a quantum
channel with errors, measuring quantum messages,
and removing bits measured in different bases.
Users can choose between simulating communication
with no error, low error rate, high error rate,
or simulating an eavesdropping attempt to observe
the effects on the integrity of the 
data transferred.
--------------------------------------------------
```

### Simulation with 0 error
```
Enter your choice (1/2/3/4/5): 1

Alice's key:  [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0]
Bob's key:  [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0]
Keys are the same and secure.

Alice's key:  [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
Bob's key:  [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
Keys are the same and secure.

Alice's key:  [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
Bob's key:  [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
Keys are the same and secure.

Alice's key:  [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
Bob's key:  [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
Keys are the same and secure.

Alice's key:  [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
Bob's key:  [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]
Keys are the same and secure.
```

### Simulation with low error rate
```
Enter your choice (1/2/3/4/5): 2

Alice's key:  [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]
Bob's key:  [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]
Keys are the same and secure.

Alice's key:  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0]
Bob's key:  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0]
Error: keys are different.

Alice's key:  [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1]
Bob's key:  [0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1]
Error: keys are different.

Alice's key:  [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1]
Bob's key:  [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1]
Keys are the same and secure.

Alice's key:  [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
Bob's key:  [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
Keys are the same and secure.
```

### Simulation with high error rate
```
Enter your choice (1/2/3/4/5): 3

Alice's key:  [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1]
Bob's key:  [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1]
Error: keys are different.

Alice's key:  [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1]
Bob's key:  [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1]
Keys are the same and secure.

Alice's key:  [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
Bob's key:  [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
Error: keys are different.

Alice's key:  [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
Bob's key:  [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0]
Error: keys are different.

Alice's key:  [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1]
Bob's key:  [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1]
Error: keys are different.
```

### Simulation with eavesdropping attempt
```
Enter your choice (1/2/3/4/5): 4

Alice's key:  [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0]
Bob's key:  [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0]
Error: keys are different.

Alice's key:  [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]
Bob's key:  [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
Error: keys are different.

Alice's key:  [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
Bob's key:  [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1]
Error: keys are different.

Alice's key:  [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1]
Bob's key:  [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1]
Error: keys are different.

Alice's key:  [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0]
Bob's key:  [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
Error: keys are different.
```