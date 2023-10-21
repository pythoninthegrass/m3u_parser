#!/usr/bin/env python3

import sys


class track():
    def __init__(self, length, title, path):
        self.length = length
        self.title = title
        self.path = path


def parsem3u(infile, verbose=True):
    """
    Parses an M3U playlist file into a list of track objects.

    NOTES
        All M3U files start with #EXTM3U.
        If the first line doesn't start with this, we're either
        not working with an M3U or the file we got is corrupted.

        The #EXTINF line is formatted like this:
        #EXTINF:<length>,<title>
        <length> is in seconds
        <title> is the title of the song

        All other, non-blank lines are paths to the files.
        (e.g., ../Minus The Bear - Planet of Ice/Minus The Bear_Planet of Ice_01_Burying Luck.mp3)
    """
    try:
        assert(type(infile) == '_io.TextIOWrapper')
    except AssertionError:
        infile = open(infile,'r', errors='replace')

    lines = infile.readlines()

    # TODO: add more internal field separators (e.g., "_")
    tracks = []
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith('#EXTINF:'):
            length, title = line.split('#EXTINF:')[1].split(',', 1)
            path = lines[i+1].strip()
            try:
                artist, title = title.split(' - ', 1)
                if verbose:
                    print(f"{artist} - {title} ({length}s)")
                track = {'title': title, 'artist': artist, 'length': length, 'path': path}
                tracks.append(track)
            except ValueError as e:
                print(f"Skipping track: {e}")
                pass

    if verbose:
        print(f"Parsed {len(tracks)} tracks from {infile.name}")

    return tracks


def main(filename=None, verbose=True):
    try:
        if filename:
            m3ufile = filename
        else:
            m3ufile = sys.argv[1]
    except IndexError:
        print("Usage: m3uparser.py <m3ufile>")
        sys.exit(1)

    return parsem3u(m3ufile, verbose=verbose)


if __name__ == '__main__':
    main()
