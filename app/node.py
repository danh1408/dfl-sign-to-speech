import os
import time

node_id = os.getenv('NODE_ID', 'Unknown')
print(f"--- Hello! This is DFL Node {node_id} starting up ---", flush = True)

while True:
    print(f"Node {node_id} is waiting for gossip...")
    time.sleep(10)