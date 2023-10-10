CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,       -- 기본 키 AUTOINCREMENT : 기본 키를 자동으로 증가하도록
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('examples');      -- 테이블의 정보를 확인하는 명령


-- 테이블 구조 변경 : 컬럼
ALTER TABLE
    examples
ADD COLUMN
    Country VARCHAR(100);

ALTER TABLE
    examples
ADD COLUMN
    Address VARCHAR(100);


-- 테이블 구조 이름 변경
ALTER TABLE
    examples
RENAME COLUMN Address to PostCode;

-- 테이블 구조 삭제  -  sqlite3으로 실행
ALTER TABLE
    examples
DROP COLUMN 
    PostCode;


-- 테이블 구조 변경 : 컬럼 추가 시 기본값 설정
ALTER TABLE
    examples
ADD COLUMN
    PostCode (VARCHAR(100) DEFAULT 'N' NOT NULL;