import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name  TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name  TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title  TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len  INTEGER,  rating INTEGER,  count INTEGER
    );
''')

handle = open('tracks.csv')

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103, Rock
#   0                          1      2           3  4   5      6

for line in handle:
    line = line.strip();
    #print(line)
    pieces = line.split(',')
    if len(pieces) < 7 : continue

    name = pieces[0].strip()
    artist = pieces[1].strip()
    album = pieces[2].strip()
    count = pieces[3].strip()
    rating = pieces[4].strip()
    length = pieces[5].strip()
    genreName = pieces[6].strip()

    #print(name, artist, album, count, rating, length, genreName)
    # if name is None or artist is None or album is None or count is None or rating is None or genreName is None:
    #     continue
    
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genreName, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genreName, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )
    
conn.commit()

#read data
sqlstar = '''SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track
    JOIN Genre ON Track.genre_id = Genre.id
    JOIN Album ON Track.album_id = Album.id
    JOIN Artist ON Album.artist_id = Artist.id
    ORDER BY Artist.name, Track.title
    LIMIT 3'''

html = "<table border='1'><tr><td>Track</td><td>Artist</td><td>Album</td><td>Genre</td><td></tr>"
for row in cur.execute(sqlstar):
    print(str(row))
    html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>"
html += "</table>"
print(html)

cur.close()