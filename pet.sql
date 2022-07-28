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


INSERT INTO pets (pet_name, species, photo_url, available) VALUES 
('Emery','Dog', 'https://images.unsplash.com/photo-1552053831-71594a27632d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZG9nfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60','True'),
('Kitty','Cat', 'https://images.unsplash.com/photo-1573865526739-10659fec78a5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y2F0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60','True')
;

