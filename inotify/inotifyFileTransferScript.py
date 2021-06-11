import inotify.adapters
import pulsar

def _main():
 
    client = pulsar.Client('pulsar://localhost:6650')
    producer  =  client.create_producer('my-topic')

    i = inotify.adapters.Inotify()

    i.add_watch('/home/VZADCLOUD/vx/stats')

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

        print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
              path, filename, type_names))
        if (type_names[0] == 'IN_CLOSE_WRITE'):
           print ("Sending filename and path to pulsar")
           f = open(path+ '/' + filename, "r")
           filecontent  = f.read() 
           producer.send(filecontent.encode('utf-8'))
           f.close()

if __name__ == '__main__':
    _main()
