-- =========================================================
-- Codeforces Analytics Platform
-- Module : Table Creation
-- Table  : users
-- Description:
-- Stores profile information of Codeforces users.
-- =========================================================

USE codeforces_analytics;

-- =========================================================
-- TABLE 1 : USERS
-- =========================================================

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,

    -- Codeforces username
    handle VARCHAR(50) NOT NULL UNIQUE,

    -- Current and maximum rank
    current_rank VARCHAR(30),
    highest_rank VARCHAR(30),

    -- Current and maximum rating
    current_rating INT,
    highest_rating INT,

    -- User contribution score
    contribution INT UNSIGNED DEFAULT 0,

    -- Number of users who have added this user as a friend
    friend_count INT UNSIGNED DEFAULT 0,

    -- User information
    organization VARCHAR(150),
    country VARCHAR(100),
    city VARCHAR(100),

    -- Metadata
    source ENUM ('Codeforces', 'LeetCode', 'CodeChef', 'AtCoder')
        DEFAULT 'Codeforces',

    -- Time when the record was first inserted
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Time when the row was last modified
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    -- Time when data was last fetched from Codeforces API
    last_api_sync TIMESTAMP NULL,

    CHECK (current_rating >= 0),
    CHECK (highest_rating >= 0),
    CHECK (highest_rating >= current_rating)
);

drop table users;

-- =========================================================
-- TABLE 2 : CONTESTS
-- =========================================================

CREATE TABLE contests (

    -- Codeforces Contest ID
    contest_id INT PRIMARY KEY,

    -- Contest details
    contest_name VARCHAR(255) NOT NULL,

    contest_type ENUM(
        'CF',
        'IOI',
        'ICPC'
    ) NOT NULL,

    contest_phase ENUM(
        'BEFORE',
        'CODING',
        'PENDING_SYSTEM_TEST',
        'SYSTEM_TEST',
        'FINISHED'
    ) NOT NULL,

    is_frozen BOOLEAN NOT NULL,

    duration_seconds INT UNSIGNED NOT NULL,

    start_time TIMESTAMP NULL,

    -- Metadata
    source ENUM(
        'Codeforces',
        'LeetCode',
        'CodeChef',
        'AtCoder'
    ) DEFAULT 'Codeforces',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    last_api_sync TIMESTAMP NULL
);



-- =========================================================
-- TABLE 3 : PROBLEMS
-- =========================================================

CREATE TABLE problems (

    -- Internal Primary Key
    problem_id INT AUTO_INCREMENT PRIMARY KEY,

    -- Contest to which this problem belongs
    contest_id INT NOT NULL,

    -- Problem Index (A, B, C, D, E, F, A1...)
    problem_index CHAR(5) NOT NULL,

    -- Problem Name
    problem_name VARCHAR(255) NOT NULL,

    -- Problem Type
    problem_type ENUM(
        'PROGRAMMING',
        'QUESTION'
    ) DEFAULT 'PROGRAMMING',

    -- Problem Points
    points DECIMAL(6,2),

    -- Difficulty Rating
    problem_rating INT UNSIGNED,

    -- Whether the problem has an official rating
    is_rated BOOLEAN DEFAULT TRUE,

    -- Source Platform
    source ENUM(
        'Codeforces',
        'LeetCode',
        'CodeChef',
        'AtCoder'
    ) DEFAULT 'Codeforces',

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    last_api_sync TIMESTAMP NULL,

    -- Business Constraints
    CONSTRAINT uq_problem UNIQUE(contest_id, problem_index),

    CONSTRAINT chk_problem_rating
        CHECK (problem_rating IS NULL OR problem_rating >= 0),

    CONSTRAINT chk_problem_points
        CHECK (points IS NULL OR points >= 0)

);



-- =========================================================
-- TABLE 4 : TAGS
-- =========================================================

CREATE TABLE tags (

    tag_id INT AUTO_INCREMENT PRIMARY KEY,

    tag_name VARCHAR(100) NOT NULL UNIQUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- =========================================================
-- TABLE 5 : PROBLEM_TAGS
-- =========================================================

CREATE TABLE problem_tags (

    problem_id INT NOT NULL,

    tag_id INT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY(problem_id, tag_id)

);

-- =========================================================
-- TABLE 6 : SUBMISSIONS
-- =========================================================

CREATE TABLE submissions (

    -- Codeforces Submission ID
    submission_id BIGINT PRIMARY KEY,

    -- References
    user_id INT NOT NULL,
    contest_id INT NOT NULL,
    problem_id INT NOT NULL,

    -- Submission Details
    programming_language VARCHAR(100) NOT NULL,

    verdict ENUM(
        'OK',
        'WRONG_ANSWER',
        'TIME_LIMIT_EXCEEDED',
        'MEMORY_LIMIT_EXCEEDED',
        'RUNTIME_ERROR',
        'COMPILATION_ERROR',
        'PRESENTATION_ERROR',
        'IDLENESS_LIMIT_EXCEEDED',
        'CHALLENGED',
        'SKIPPED',
        'TESTING',
        'FAILED',
        'PARTIAL'
    ) NOT NULL,

    passed_test_count SMALLINT UNSIGNED DEFAULT 0,

    execution_time_ms INT UNSIGNED,

    memory_bytes INT UNSIGNED,

    submission_time TIMESTAMP NOT NULL,

    relative_time_seconds INT,

    source ENUM(
        'Codeforces',
        'LeetCode',
        'CodeChef',
        'AtCoder'
    ) DEFAULT 'Codeforces',

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    last_api_sync TIMESTAMP NULL,

    -- Validation
    CONSTRAINT chk_passed_tests
        CHECK (passed_test_count >= 0),

    CONSTRAINT chk_execution_time
        CHECK (execution_time_ms IS NULL OR execution_time_ms >= 0),

    CONSTRAINT chk_memory
        CHECK (memory_bytes IS NULL OR memory_bytes >= 0)

);


-- =========================================================
-- TABLE 7 : RATING_HISTORY
-- =========================================================

CREATE TABLE rating_history (

    rating_history_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    contest_id INT NOT NULL,

    contest_rank INT UNSIGNED NOT NULL,

    old_rating INT UNSIGNED NOT NULL,

    new_rating INT UNSIGNED NOT NULL,

    rating_change INT
        GENERATED ALWAYS AS (new_rating - old_rating) STORED,

    rating_update_time TIMESTAMP NOT NULL,

    source ENUM(
        'Codeforces',
        'LeetCode',
        'CodeChef',
        'AtCoder'
    ) DEFAULT 'Codeforces',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    last_api_sync TIMESTAMP NULL,

    CONSTRAINT chk_old_rating
        CHECK (old_rating >= 0),

    CONSTRAINT chk_new_rating
        CHECK (new_rating >= 0)

);


