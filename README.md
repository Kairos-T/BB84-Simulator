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