from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#
class Venue_Genre(db.Model):
    __tablename__ = "venue_genres"
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(
        db.Integer, db.ForeignKey("venues.id", ondelete="CASCADE"), nullable=False
    )
    genre = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Venue_Genre venue_id:{self.venue_id} genre: {self.genre}>"


class Venue(db.Model):
    __tablename__ = "venues"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    genres = db.relationship(
        "Venue_Genre", passive_deletes=True, backref="venue", lazy=True,
    )
    seeking_talent = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(120), nullable=True)
    image_link = db.Column(
        db.String(500),
        nullable=True,
        default="https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
    )
    facebook_link = db.Column(db.String(120), nullable=True, default="")
    website = db.Column(db.String(120), nullable=True)


class Show(db.Model):
    __tablename__ = "shows"
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), primary_key=True)
    venue_id = db.Column(
        db.Integer, db.ForeignKey("venues.id", ondelete="CASCADE"), primary_key=True
    )
    start_time = db.Column(db.DateTime, nullable=False)


class Artist_Genre(db.Model):
    __tablename__ = "artist_genres"
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)
    genre = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Artist_Genre artist_id:{self.artist_id} genre: {self.genre}>"


class Artist(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.relationship("Artist_Genre", backref="artist", lazy=True)
    image_link = db.Column(
        db.String(500),
        nullable=True,
        default="https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
    )
    facebook_link = db.Column(db.String(120), nullable=True)
    venues = db.relationship(
        "Venue", secondary="shows", backref=db.backref("artists", lazy=True)
    )
    seeking_venue = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(), nullable=True, default="")
