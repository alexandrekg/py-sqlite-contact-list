CREATE TABLE contato (
    id integer primary key,
    name text NOT NULL,
    email text,
    phone text
);

INSERT INTO contato (name, email, phone) VALUES ('Teste1', 'teste1@gmail.com', '5199993939393');
