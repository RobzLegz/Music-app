import peewee

class Artist(peewee.Model):
    name = peewee.CharField()

    class Meta:
        pass