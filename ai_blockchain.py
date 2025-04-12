# AI in Blockchain: Prescription Tracking

from datetime import datetime
import hashlib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

class Blockchain:
    """
    The Blockchain class maintains a chain of blocks, each holding:
      - data: Prescription details (patient_id, medication, quantity, dosage, etc.)
      - timestamp: When this block was created
      - previous_hash: The hash of the previous block in the chain
      - hash: The current block's hash, derived from its contents
    """

    def __init__(self):
        """
        Initialize an empty blockchain list.
        """
        self.chain = []

    def add_block(self, data):
        """
        Creates a new block with the given data, calculates its hash,
        and appends it to the chain.
        """
        if not self.chain:
            # No blocks yet, so previous_hash is '0'
            previous_hash = '0'
        else:
            # The hash of the last block in the chain
            previous_hash = self.chain[-1]['hash']
        
        # Construct the block
        block = {
            'data': data,
            'timestamp': str(datetime.now()),
            'previous_hash': previous_hash
        }
        
        # Serialize and hash the block
        block_string = str(block).encode()
        block_hash = hashlib.sha256(block_string).hexdigest()
        block['hash'] = block_hash

        # Append to the chain
        self.chain.append(block)

    def is_valid(self):
        """
        Checks the entire chain to ensure that no block has been tampered with:
          - The block's stored hash must match a newly computed hash.
          - The current block's previous_hash must match the previous block's hash.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Recompute the current block's hash
            current_block_string = str({
                'data': current_block['data'],
                'timestamp': current_block['timestamp'],
                'previous_hash': current_block['previous_hash']
            }).encode()
            current_hash = hashlib.sha256(current_block_string).hexdigest()
            
            if current_block['hash'] != current_hash:
                # If the hash doesn't match, it has been altered
                return False
            
            if current_block['previous_hash'] != previous_block['hash']:
                # If the chain links don't match, data integrity is compromised
                return False
        
        return True

    def display_chain(self):
        """
        Displays the entire chain: For each block, shows its hash, previous hash,
        the prescription data, and the timestamp.
        """
        for index, block in enumerate(self.chain):
            print(f"--- Block {index + 1} ---")
            print(f"Hash: {block['hash']}")
            print(f"Previous Hash: {block['previous_hash']}")
            print(f"Data: {block['data']}")
            print(f"Timestamp: {block['timestamp']}\n")


def train_ai_model():
    """
    Train a simple Logistic Regression model on synthetic data for prescription misuse detection.
    Data columns: [number_of_prescriptions, dosage, misuse_label(0 or 1)].
    """
    # Synthetic dataset
    data = np.array([
        [5, 10, 0],
        [3, 5, 0],
        [8, 20, 1],
        [4, 15, 0],
        [6, 18, 1],
        [7, 25, 1],
        [2, 5, 0],
        [9, 30, 1]
    ])
    
    X = data[:, :2]  # Features
    y = data[:, 2].astype(int)  # Labels
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Create and train the logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    return model

def check_prescription(ai_model, prescriptions):
    """
    Uses the AI model to predict whether each prescription is legitimate (0) or misuse (1).
    """
    predictions = ai_model.predict(prescriptions)
    return predictions

def main():
    # Initialize the Blockchain
    prescription_blockchain = Blockchain()

    # Train the AI Model
    ai_model = train_ai_model()

    # New prescription data: [quantity, dosage]
    new_prescriptions = np.array([
        [6, 15],  # Example
        [8, 22],  # Example
        [4, 10]   # Example
    ])

    # AI model predictions
    predictions = check_prescription(ai_model, new_prescriptions)

    # Attempt to add each prescription to the blockchain if legitimate
    for i, prescription in enumerate(new_prescriptions):
        status = 'legitimate' if predictions[i] == 0 else 'flagged'
        prescription_data = {
            'patient_id': f"patient_{i+1}",
            'medication': f"medication_{i+1}",
            'quantity': int(prescription[0]),
            'dosage': int(prescription[1]),
            'status': status
        }

        if status == 'legitimate':
            prescription_blockchain.add_block(prescription_data)
        else:
            print(f"Prescription {i+1} flagged for potential misuse. Not added to blockchain.")

    # Display the blockchain
    print("\n--- Blockchain Data ---")
    prescription_blockchain.display_chain()

    # Validate the blockchain integrity
    print(f"Is the blockchain valid? {prescription_blockchain.is_valid()}")

if __name__ == "__main__":
    main()

'''
This code simulates a blockchain for prescription tracking, integrating AI for misuse detection.
It creates a blockchain, trains a simple AI model, and checks new prescriptions against it.
The blockchain is validated for integrity, ensuring no tampering has occurred.
The AI model is a basic logistic regression model trained on synthetic data.
In a real-world scenario, the model would be trained on a larger dataset with more features.
The blockchain would also include more sophisticated security measures and data privacy considerations.
This code is for educational purposes and should not be used in a production environment without further enhancements.
Ensure all necessary libraries are installed in your Python environment.
'''