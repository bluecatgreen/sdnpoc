import inotify.adapters

def _main():
    i = inotify.adapters.Inotify()

    i.add_watch('/home/VZADCLOUD/v545583/stats')

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

        print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
              path, filename, type_names))

if __name__ == '__main__':
    _main()
