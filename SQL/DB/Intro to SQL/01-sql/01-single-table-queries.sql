-- 01. Querying data --

-- 단일 필드 조회
SELECT
    LastName
FROM   
    employees;

-- 다중 필드 조회
SELECT
    LastName, FirstName
FROM
    employees;

-- 모든 필드 조회
SELECT
    *
FROM
    employees;

-- 필드 이름 변경

SELECT
    FirstName AS '이름'
FROM
    employees;

SELECT
    Name, Milliseconds / 60000 AS '재생시간(분)'
FROM
    tracks;



-- 02. Sorting data -- 

SELECT
    FirstName
FROM
    employees
ORDER BY
    FirstName ASC;  -- 오름차순 조회
    -- FirstName DESC;  -- 내림차순 조회

SELECT
    Country, City
FROM
    customers
ORDER BY
    Country DESC,
    City ASC;

SELECT
    Name, Milliseconds
FROM
    tracks
ORDER BY
    Milliseconds DESC;

-- NULL 정렬 예시 --
SELECT
    ReportsTo
FROM
    employees
ORDER BY
    ReportsTo;


-- 03. Filtering data --
-- DISTINCT
SELECT DISTINCT
    Country
FROM
    customers
ORDER BY
    Country;

-- WHERE
SELECT LastName, FirstName, City
FROM customers
WHERE
    City = 'Prague';        -- 어떠한 값의 범위 / 포함관계 등
    -- City != 'Prague';        -- 어떠한 값의 범위 / 포함관계 등

SELECT 
    LastName, FirstName, Company
FROM
    customers
WHERE
    Company IS NULL         -- NULL인 부분을 찾기
    AND Country = 'USA'

-- 범위 조회
SELECT
    Name, Bytes
FROM
    tracks
WHERE
    Bytes BETWEEN 100000 AND 500000
ORDER BY
    Bytes;


SELECT
    LastName, FirstName, Country
FROM
    customers
WHERE
    -- Country = 'Canada'
    -- OR Country = 'Germany'
    -- OR Country = 'France'
    Country IN ('Canada', 'Germany', 'France');

SELECT
    LastName, FirstName
FROM
    customers
WHERE
    LastName LIKE 'Sson';

SELECT
    LastName, FirstName
FROM
    customers
WHERE
    LastName LIKE '___a';

-- LIMIT 연습
SELECT
    TrackId, Name, Bytes
FROM
    tracks
ORDER BY
    Bytes DESC
LIMIT 3, 4;



-- 04. Grouping data --
SELECT
    Country, COUNT(*)       -- COUNT : 집계 함수
FROM
    customers
GROUP BY
    Country;

SELECT 
    Composer, AVG(Bytes)
FROM
    tracks
GROUP BY
    Composer
ORDER BY
    AVG(Bytes) DESC;




-- 에러 --


-- 에러 해결 --

SELECT
    Composer,
    AVG(Milliseconds / 60000) AS avgOfMinute
FROM
    tracks
GROUP BY
    Composer
Having
    avgOfMinute < 10;