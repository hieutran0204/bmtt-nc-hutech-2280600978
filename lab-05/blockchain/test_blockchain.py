# from blockchain import Blockchain

# my_blockchain = Blockchain()
# # nhập bằng teminal 
# my_blockchain.add_transaction('Alice', 'Bob', 10)
# my_blockchain.add_transaction('Bob', 'Charlie', 5)
# my_blockchain.add_transaction('Charlie', 'Alice', 3)

# previous_block = my_blockchain.get_previous_block()
# previous_proof = previous_block.proof
# new_proof = my_blockchain.proof_of_work(previous_proof)
# previous_hash = previous_block.hash
# my_blockchain.add_transaction('Genesis', 'Miner', 1)
# new_block = my_blockchain.create_block(new_proof, previous_hash)

# for block in my_blockchain.chain:
#     print(f"Block #{block.index}")
#     print("Timestamp:", block.timestamp)
#     print("Transactions:", block.transactions)
#     print("Proof:", block.proof)
#     print("Previous Hash:", block.previous_hash)
#     print("Hash:", block.hash)
#     print("------------------------------")

# print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
from blockchain import Blockchain

my_blockchain = Blockchain()

# Nhập giao dịch từ terminal
num_tx = int(input("Nhập số lượng giao dịch bạn muốn thêm: "))

for i in range(num_tx):
    sender = input(f"Giao dịch #{i+1} - Nhập người gửi: ")
    receiver = input(f"Giao dịch #{i+1} - Nhập người nhận: ")
    amount = float(input(f"Giao dịch #{i+1} - Nhập số tiền: "))
    my_blockchain.add_transaction(sender, receiver, amount)

# Tạo block mới sau khi nhập giao dịch
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1)  # Thưởng block
new_block = my_blockchain.create_block(new_proof, previous_hash)

# In thông tin blockchain
for block in my_blockchain.chain:
    print(f"\nBlock #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("-" * 30)

print("\nIs Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
