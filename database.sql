CREATE TABLE ngrams (
  idngram serial PRIMARY KEY,
  gram varchar(100),
  length integer NOT NULL,
  absolut_frequency numeric NOT NULL,
  total integer NOT NULL,
  algorithm_idalgorithm integer NOT NULL,
  publication_idpublication integer NOT NULL
);
