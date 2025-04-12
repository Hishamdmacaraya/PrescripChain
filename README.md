
# PrescripChain

**PrescripChain** is a simple AI-driven blockchain application designed to securely track medical prescriptions and detect potential misuse. It combines two main components:

1. **Blockchain** – To store and protect prescription data in a tamper-resistant ledger.
2. **Logistic Regression Model** – To predict and flag potentially suspicious (misuse) prescriptions.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites and Installation](#prerequisites-and-installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
  - [AI Model](#ai-model)
  - [Blockchain](#blockchain)
- [Example Output](#example-output)
- [Validation](#validation)
- [License](#license)

---

## Overview

Medical prescription misuse is a critical problem in healthcare. **PrescripChain** aims to mitigate this by leveraging:

- **AI** to detect and flag suspicious prescriptions before they are officially recorded.
- **Blockchain** to store legitimate prescription data immutably, ensuring transparency and trust.

### Use Cases

- **Healthcare Facilities**: Hospitals and clinics can use this system to track prescriptions and detect potential misuse in real time.
- **Pharmacies**: Validate incoming prescriptions against a secure ledger and flag anomalies.
- **Research**: Demonstrate how AI and blockchain can be integrated for healthcare applications.

---

## Features

1. **AI-Enhanced Verification**  
   - A trained logistic regression model checks if new prescriptions are likely to be misused.

2. **Immutable Ledger**  
   - Valid (legitimate) prescriptions are appended to a blockchain, ensuring no retroactive tampering.

3. **Auditable and Transparent**  
   - Anyone with access can verify the integrity of the prescription data by validating the blockchain.

4. **Easy to Extend**  
   - The code structure allows replacing or upgrading the AI component and scaling the blockchain functionality.

---

## Project Structure

```
.
├── ai_blockchain.py           # Main script containing the Blockchain class, AI model, and example usage
├── README.md                  # This README documentation
└── requirements.txt           # Contains a list of Python dependencies
```

- **ai_blockchain.py**:  
  - **Blockchain** class: Methods for creating, appending, and validating blocks.
  - **train_ai_model** function: Builds and trains the logistic regression model.
  - **check_prescription** function: Uses the trained model to predict misuse vs. legitimate prescriptions.
  - **main** function: Demonstrates how to integrate the AI model and blockchain in practice.

---

## Prerequisites and Installation

1. **Python 3.x** installed.
2. The following Python libraries:
   - `numpy`
   - `scikit-learn`

You can install the necessary packages by running:
```bash
pip install numpy scikit-learn
```
Or with a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## Usage

1. **Clone or Download** this repository.

2. **Install Dependencies** using:
   ```bash
   pip install numpy scikit-learn
   ```
   or:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   ```bash
   python ai_blockchain.py
   ```

4. **Observe** the console output to see:
   - Flagged prescriptions
   - Added blocks
   - Final blockchain validity

---

## How It Works

### AI Model

#### Training Data
- A small synthetic dataset represents:  
  `[number_of_prescriptions, dosage, misuse_label]`
- The logistic regression model is trained to distinguish:
  - `0 = legitimate`
  - `1 = misuse`

#### Prediction
- When a new prescription arrives, its features (`quantity`, `dosage`) are fed into the model.
- If the model predicts misuse:
  - It is flagged and **not added** to the blockchain.
- Otherwise:
  - It is stored on the blockchain as a valid block.

---

### Blockchain

#### Structure
Each block in the chain holds:
- `data`: A dictionary containing the prescription (patient ID, medication, quantity, dosage, etc.)
- `timestamp`: When the block was added.
- `previous_hash`: Hash of the preceding block.
- `hash`: The SHA-256 hash of the current block’s content.

#### Adding a Block
- A new block is created by combining:
  - Prescription data
  - Previous block’s hash
- The block is then:
  - Serialized
  - Hashed using SHA-256
  - Appended to the chain

---

## Example Output

Below is a sample console output after running `ai_blockchain.py`:


![Screenshot 2025-04-12 080716](https://github.com/user-attachments/assets/5b092959-52ac-4608-87b2-a770e4d56023)

---

## Validation

To confirm the integrity of your data, **PrescripChain** uses its `is_valid()` method:

- Calculates the hash of each block and compares it to the stored hash.
- Ensures that each block’s `previous_hash` matches the `hash` of the block before it.
- If **any discrepancy** is found, the blockchain is considered **invalid**.

---

## License

MIT License

---

Enjoy building and expanding upon **PrescripChain**!
