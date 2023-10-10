CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt DATE NOT NULL
    );

-- INSERT
INSERT INTO
    articles (title, content, createdAt)
VALUES
    ('hello', 'world1', '2000-01-01'),
    ('hello', 'world2', '2001-01-01'),
    ('hello', 'world3', DATE());

-- UPDATE
UPDATE 
    articles
SET
    title = 'update Title2',
    content = 'update Content2'
WHERE
    id = 2;

-- DELETE
DELETE FROM articles
WHERE
    id = 1;


-- 심화(서브 쿼리)
-- 제일 최근에 생성된 게시글을 골라서 하나만 삭제
DELETE FROM
    articles
WHERE id IN (
    SELECT id FROM articles
    ORDER BY
        createdAt DESC
    LIMIT 1
);