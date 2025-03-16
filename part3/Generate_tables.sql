-- Script that creates User, Place, Review, Amenity, and Place_Amenity tables.

-- Query that creates user table.
CREATE TABLE IF NOT EXISTS user (
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    is_admin TINYINT(1) DEFAULT 0
);

-- Query that creates place table.
CREATE TABLE IF NOT EXISTS place (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2),
    latitude FLOAT,
    longitude FLOAT,
    owner_id CHAR(36),
    FOREIGN KEY (owner_id) REFERENCES user(id) ON DELETE CASCADE
);

-- Query that creates review table.
CREATE TABLE IF NOT EXISTS review (
    id CHAR(36) PRIMARY KEY,
    text TEXT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    user_id CHAR(36),
    place_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES place(id) ON DELETE CASCADE,
    UNIQUE (user_id, place_id)
);

-- Query that creates amenity table.
CREATE TABLE IF NOT EXISTS amenity (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

-- Query that creates place_amenity table.
CREATE TABLE IF NOT EXISTS place_amenity (
    place_id CHAR(36),
    amenity_id CHAR(36),
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES place(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenity(id) ON DELETE CASCADE
);
