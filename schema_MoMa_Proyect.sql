Tabla padre 
CREATE TABLE Artists (
    ConstituentID   VARCHAR(50) PRIMARY KEY,
    DisplayName VARCHAR(200),
    ArtistBio VARCHAR(100),
    Nationality VARCHAR(50),
    Gender VARCHAR (50)
);

Tabla hija
CREATE TABLE Artworks (
    Title VARCHAR(800),
    ConstituentID VARCHAR(50),
    Date DATE,
    Medium VARCHAR(1200),
    CreditLine VARCHAR(800),
    AccessionNumber VARCHAR(50),
    Classification VARCHAR(50),
    Department VARCHAR(50),
    DateAcquired DATE,
    Cataloged VARCHAR(5),
    OnView VARCHAR(50),
    ObjectID VARCHAR(50) PRIMARY KEY,
    FOREIGN KEY (ConstituentID) REFERENCES Artists(ConstituentID)
);