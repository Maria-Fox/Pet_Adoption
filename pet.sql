DROP DATABASE IF EXISTS adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets(
  id SERIAL PRIMARY KEY, 
  pet_name TEXT not null,
  species TEXT not null,
  photo_url TEXT,
  age INTEGER,
  notes TEXT,
  available boolean not null
);


INSERT INTO pets (pet_name, species, available) VALUES 
('Emery','dog', 'True'),
('Kitty','cat', 'True')
;

