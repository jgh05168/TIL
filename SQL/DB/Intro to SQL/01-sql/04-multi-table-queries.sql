SELECT * FROM articles;
SELECT * FROM users;

DROP TABLE articles;
DROP TABLE users;

CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50) NOT NULL
);

CREATE TABLE articles(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50) NOT NULL,
content VARCAHR(50) NOT NULL,
userId INTEGER NOT NULL,
FOREIGN KEY (userId)    -- userId 컬럼은 외래 키 제약 조건인데
    REFERENCES users(id) -- users 테이블의 id 컬럼값 침조
);

INSERT INTO
    users (name)
VALUES
    ('가나다'),
    ('라마바'),
    ('사아자');

INSERT INTO 
    articles (title, content, userId)
VALUES
    ('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 5),
    ('제목4', '내용4', 4),
    ('제목5', '내용5', 3);


-- 1번 게시글의 작성자 찾기
SELECT userId FROM articles WHERE id = 1;

SELECT name FROM users WHERE id = 1;

-- INNER JOIN
SELECT *
FROM articles
INNER JOIN users
    ON users.id = articles.userId;


-- LEFT JOIN
SELECT *
FROM articles
LEFT JOIN users
    ON users.id = articles.userId


-- 테이블 레코드 삭제 시
DELETE FROM users
WHERE id = 3;


-- 게시글을 작성한 이력이 없는 회원 정보 조회
SELECT *
FROM users
LEFT JOIN articles
    ON articles.userId = users.id
WHERE articles.userId IS NULL;



-- ex) 한명의 아티스트가 몇 개의 앨범을 냈는지 알고싶다.
-- 출력 데이터 : 앨범 개수, 아티스트 ID,  아티스트 이름

SELECT * FROM albums;
SELECT * FROM artists;

SELECT COUNT(*) as AlbumCount, artists.ArtistId, artists.Name as ArtistName
FROM albums
INNER JOIN artists
    ON artists.ArtistId = albums.ArtistId
GROUP BY
    artists.ArtistId;