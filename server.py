import multiprocessing
from time import sleep
import channel
import rpc1

# Fix the identities of channel, server, and client
channelID = 1
serverID  = 10
clientID  = 20

def server(channelID, serverID):
    s = rpc1.Server(channelID, serverID) 
    c = multiprocessing.Process(target=client,args=(channelID, clientID, serverID,))
    sleep(2)  # Simple wait so that client can get into the system
    c.start() # Now start the client
    s.run()   # In particular, get the server into a loop

if __name__ == "__main__":
    chan = channel.Channel(channelID, True)
    s = multiprocessing.Process(target=server,args=(channelID,serverID,))
    
    s.start()
    s.join()
