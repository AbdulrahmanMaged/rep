import rpc1

# Fix the identities of channel, server, and client
channelID = 1
serverID  = 10
clientID  = 20

def client(channelID, clientID, serverID):
    c = rpc1.Client(channelID, clientID, serverID) # Create client stub
    s1 = rpc1.DBList((1,2))      # Create a local list
    s2 = c.append('c',s1)        # Pass local list to stub and wait for result
    print("Value s1:", s1.value) # This is what client started with
    print("Value s2:", s2.value) # This is what the server did after call to append
    c.stop()

if __name__ == "__main__":
    client(channelID, clientID, serverID)
