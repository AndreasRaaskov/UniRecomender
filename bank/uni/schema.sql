CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username VARCHAR (60) UNIQUE,
    email VARCHAR (60) UNIQUE,
    user_password VARCHAR (60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Universities(
    id INTEGER PRIMARY KEY,
    university_name VARCHAR(60) UNIQUE,
    average_rating DECIMAL (1,1)
);

CREATE TABLE IF NOT EXISTS Reviews(
    id INTEGER PRIMARY KEY,
    rating integer NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment varchar(500),
    votes_no INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS gave_review (
    review_id INTEGER NOT NULL REFERENCES Reviews(id),
    user_id INTEGER NOT NULL REFERENCES Users(id) on delete CASCADE
);
ALTER TABLE gave_review ADD CONSTRAINT gr_01
    FOREIGN KEY (review_id) REFERENCES Reviews (id) ON DELETE CASCADE
;


CREATE TABLE IF NOT EXISTS review_of (
    review_id INTEGER REFERENCES Reviews (id),
    university_id INTEGER REFERENCES Universities (id)
);
ALTER TABLE review_of ADD CONSTRAINT ro_01
    FOREIGN KEY (review_id) REFERENCES Reviews (id) ON DELETE CASCADE
;

CREATE TABLE IF NOT EXISTS attended_university(
    user_id INTEGER REFERENCES Users (id) ON DELETE CASCADE,
    university_id INTEGER REFERENCES Universities (id) ON DELETE CASCADE
);
ALTER TABLE attended_university ADD CONSTRAINT au_01
    PRIMARY KEY (user_id, university_id)
;

CREATE TABLE IF NOT EXISTS review_vote (
    review_id INTEGER REFERENCES Reviews (id),
    user_id INTEGER REFERENCES Users (id) ON DELETE CASCADE
);
ALTER TABLE review_vote ADD CONSTRAINT rv_01
    PRIMARY KEY (review_id, user_id)
;