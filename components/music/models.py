import peewee
import datetime

from app.app import db

#artist
class Artist(peewee.Model):
    name = peewee.CharField()
    about = peewee.TextField()
    image = peewee.CharField(max_length=512)
    birth_date = peewee.DateField()

    @property
    def age(self):
        artist_age = int(datetime.datetime.now().date().strftime("%Y")) - int(self.birth_date.year)

        return artist_age

    class Meta:
        database = db


#album
class Album(peewee.Model):
    name = peewee.CharField()
    artist = peewee.ForeignKeyField(Artist, backref="albums")
    cover = peewee.CharField(max_length=512)
    release_date = peewee.DateField()
    about = peewee.CharField()
    
    @property
    def total_length(self):
        length = 0

        for song in self.songs:
            length += song.length
    
        return length


    class Meta:
        database = db


#song
class Song(peewee.Model):
    name = peewee.CharField()
    artist = peewee.ForeignKeyField(Artist, backref="songs")
    album = peewee.ForeignKeyField(Album, backref="songs")
    cover = peewee.CharField(max_length=512)
    release_date = peewee.DateField()
    length = peewee.IntegerField()

    @property
    def minutes(self):
        return int(self.length / 60)
    
    class Meta:
        database = db