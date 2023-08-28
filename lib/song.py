from config import CONN, CURSOR

class Song:
    def __init__(self, name, album, title, artist):
        self.id = None
        self.name = name
        self.album = album
        self.title = title
        self.artist = artist
    
    @classmethod
    def create_table(cls):
        sql = """ 

        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT,
            title TEXT,
            artist TEXT
        )
        """
        CURSOR.execute(sql)
    
    def save(self):
        sql = """ 
            INSERT INTO songs (name, album, title, artist)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album, self.title, self.artist))
        self.id = CURSOR.execute('SELECT last_insert_rowid() FROM songs ').fetchone()[0]
    
    @classmethod
    def create(cls, name, album, title, artist):
        song = Song(name, album, title, artist)
        song.save()
        return song
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM songs
        """

        all = CURSOR.execute(sql).fetchall()
        cls.all = [cls.new_from_db(row) for row in all]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM songs
            WHERE name = ?
            LIMIT 1
        """

        song = CURSOR.execute(sql, (name,)).fetchone()

        return cls.new_from_db(song)
    

    

hello = Song('Test', "New", "song", 'original')
hello.save()

songs = CURSOR.execute('SELECT * FROM songs')
[row for row in songs]


