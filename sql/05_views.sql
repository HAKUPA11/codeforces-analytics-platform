-- =========================================================
-- Codeforces Analytics Platform
-- File : 05_views.sql
-- Description : Database Views
-- =========================================================

USE codeforces_analytics;

-- =========================================================
-- VIEW 1 : USER PROFILE
-- =========================================================

DROP VIEW IF EXISTS vw_user_profile;

CREATE VIEW vw_user_profile AS

SELECT

    user_id,
    handle,

    current_rank,
    highest_rank,

    current_rating,
    highest_rating,

    contribution,
    friend_count,

    organization,
    country,
    city,

    source

FROM users;

-- =========================================================
-- VIEW 2 : PROBLEM DETAILS
-- =========================================================

DROP VIEW IF EXISTS vw_problem_details;

CREATE VIEW vw_problem_details AS

SELECT

    p.problem_id,

    p.problem_name,

    p.problem_index,

    p.problem_rating,

    p.points,

    p.problem_type,

    c.contest_id,

    c.contest_name,

    c.contest_type,

    c.start_time,

    p.source

FROM problems p

JOIN contests c

ON p.contest_id = c.contest_id;

-- =========================================================
-- VIEW 3 : SUBMISSION DETAILS
-- =========================================================

DROP VIEW IF EXISTS vw_submission_details;
CREATE VIEW vw_submission_details AS

SELECT

    s.submission_id,

    u.handle,

    c.contest_name,

    p.problem_index,

    p.problem_name,

    s.verdict,

    s.programming_language,

    s.passed_test_count,

    s.execution_time_ms,

    s.memory_bytes,

    s.submission_time,

    s.relative_time_seconds,

    s.source

FROM submissions s

INNER JOIN users u
ON s.user_id = u.user_id

INNER JOIN contests c
ON s.contest_id = c.contest_id

INNER JOIN problems p
ON s.problem_id = p.problem_id;

DESCRIBE submissions;

-- =========================================================
-- VIEW 4 : CONTEST SUMMARY
-- =========================================================

DROP VIEW vw_contest_summary;

CREATE VIEW vw_contest_summary AS

SELECT

    contest_id,

    contest_name,

    contest_type,

    contest_phase,

    duration_seconds,

    start_time,

    is_frozen,

    source

FROM contests;

-- =========================================================
-- VIEW 5 : USER RATING HISTORY
-- =========================================================


DROP VIEW vw_user_rating_history;

CREATE VIEW vw_user_rating_history AS

SELECT

    rh.rating_history_id,

    u.user_id,
    u.handle,

    c.contest_id,
    c.contest_name,

   rh.old_rating,
   rh.new_rating,

  rh.rating_change,

  rh.contest_rank,

  rh.rating_update_time

FROM rating_history rh

INNER JOIN users u
ON rh.user_id = u.user_id

INNER JOIN contests c
ON rh.contest_id = c.contest_id;



-- =========================================================
-- VIEW 6 : PROBLEM STATISTICS
-- =========================================================

DROP VIEW vw_problem_statistics;

CREATE VIEW vw_problem_statistics AS

SELECT

    p.problem_id,

    p.problem_name,

    p.problem_rating,

    COUNT(s.submission_id) AS total_submissions,

    SUM(CASE
            WHEN s.verdict = 'OK'
            THEN 1
            ELSE 0
        END) AS accepted_submissions,

    ROUND(
        SUM(CASE
                WHEN s.verdict='OK'
                THEN 1
                ELSE 0
            END)
        *100.0 /
        NULLIF(COUNT(s.submission_id),0),
        2
    ) AS acceptance_rate

FROM problems p

LEFT JOIN submissions s
ON p.problem_id = s.problem_id

GROUP BY

    p.problem_id,
    p.problem_name,
    p.problem_rating;



-- =========================================================
-- VIEW 7 : USER STATISTICS
-- =========================================================

DROP VIEW vw_user_statistics;

CREATE VIEW vw_user_statistics AS

SELECT

    u.user_id,

    u.handle,

    COUNT(s.submission_id) AS total_submissions,

    SUM(
        CASE
            WHEN s.verdict='OK'
            THEN 1
            ELSE 0
        END
    ) AS accepted_submissions,

    ROUND(
        SUM(
            CASE
                WHEN s.verdict='OK'
                THEN 1
                ELSE 0
            END
        )*100.0/
        NULLIF(COUNT(s.submission_id),0),
        2
    ) AS acceptance_rate,

    AVG(p.problem_rating) AS average_problem_rating,

    MAX(p.problem_rating) AS highest_problem_rating_attempted

FROM users u

LEFT JOIN submissions s
ON u.user_id=s.user_id

LEFT JOIN problems p
ON s.problem_id=p.problem_id

GROUP BY

    u.user_id,
    u.handle;



-- =========================================================
-- VIEW 8 : CONTEST STATISTICS
-- =========================================================

DROP VIEW vw_contest_statistics;

CREATE VIEW vw_contest_statistics AS

SELECT

    c.contest_id,

    c.contest_name,

    COUNT(DISTINCT p.problem_id) AS total_problems,

    COUNT(DISTINCT s.user_id) AS participants,

    COUNT(s.submission_id) AS total_submissions,

    SUM(
        CASE
            WHEN s.verdict='OK'
            THEN 1
            ELSE 0
        END
    ) AS accepted_submissions

FROM contests c

LEFT JOIN problems p
ON c.contest_id=p.contest_id

LEFT JOIN submissions s
ON c.contest_id=s.contest_id

GROUP BY

    c.contest_id,
    c.contest_name;
    
    
    
    
    
  -- TO CHECK ALL THE VIEWS  
SHOW FULL TABLES
WHERE TABLE_TYPE = 'VIEW';