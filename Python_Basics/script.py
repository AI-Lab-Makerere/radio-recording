from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},{'amount': '55', 'sender':'bob', 'receiver':'alice'}]
 my_blockchain = Blockchain()
 my_blockchain.add_block(new_transactions)
 my_blockchain.print_blocks()
 my_blockchain.chain[1].transactions = 'fake_transactions'
 my_blockchain.validate_chain()









# transaction1 = {
#   'amount': '30',
#   'sender': 'Alice',
#   'receiver': 'Bob'}
# transaction2 = {
#   'amount': '200',
#   'sender': 'Bob',
#   'receiver': 'Alice'}
# transaction3 = {
#   'amount': '300',
#   'sender': 'Alice',
#   'receiver': 'Timothy' }
# transaction4 = {
#   'amount': '300',
#   'sender': 'Rodrigo',
#   'receiver': 'Thomas' }
# transaction5 = {
#   'amount': '200',
#   'sender': 'Timothy',
#   'receiver': 'Thomas' }
# transaction6 = {
#   'amount': '400',
#   'sender': 'Tiffany',
#   'receiver': 'Xavier' }
#
# mempool = [transaction1, transaction2,
#            transaction3, transaction4,
#            transaction5, transaction6]
#
# # add your code below
# my_transaction = {
#   'amount': '500',
#   'sender': 'name_1',
#   'receiver': 'name_2'
# }
#
# mempool.append(my_transaction)
#
# block_transactions = [transaction1, transaction3, my_transaction]
#
#
#









