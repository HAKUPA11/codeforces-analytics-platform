-- =========================================================
-- Codeforces Analytics Platform
-- File : 09_analytics.sql
-- Description : Business Analytics Queries
-- =========================================================


USE codeforces_analytics;

-- =========================================================
-- SECTION 1 : DASHBOARD KPIs
-- =========================================================

-- ---------------------------------------------------------
-- KPI 1 : Total Registered Users
-- ---------------------------------------------------------

SELECT
    COUNT(*) AS total_users
FROM users;

-- ---------------------------------------------------------
-- KPI 2 : Total Contests
-- ---------------------------------------------------------

SELECT
    COUNT(*) AS total_contests
FROM contests;

-- ---------------------------------------------------------
-- KPI 3 : Total Problems
-- ---------------------------------------------------------

SELECT
    COUNT(*) AS total_problems
FROM problems;

-- ---------------------------------------------------------
-- KPI 4 : Total Submissions
-- ---------------------------------------------------------

SELECT
    COUNT(*) AS total_submissions
FROM submissions;

-- ---------------------------------------------------------
-- KPI 5 : Total Problem Tags
-- ---------------------------------------------------------

SELECT
    COUNT(*) AS total_tags
FROM tags;


-- ---------------------------------------------------------
-- KPI 6 : Current Rating
-- ---------------------------------------------------------

SELECT
    handle,
    current_rating
FROM users;


-- ---------------------------------------------------------
-- KPI 7 : Highest Rating
-- ---------------------------------------------------------

SELECT
    handle,
    highest_rating
FROM users;


-- ---------------------------------------------------------
-- KPI 8 : Accepted Submission Percentage
-- ---------------------------------------------------------

SELECT
    ROUND(
        (SUM(verdict = 'OK') * 100.0) / COUNT(*),
        2
    ) AS acceptance_percentage
FROM submissions;

-- ---------------------------------------------------------
-- KPI 9 : Accepted Submissions
-- ---------------------------------------------------------

SELECT
    COUNT(*) AS accepted_submissions
FROM submissions
WHERE verdict = 'OK';


-- ---------------------------------------------------------
-- KPI 10 : Current Rank
-- ---------------------------------------------------------

SELECT
    handle,
    current_rank
FROM users;


-- =========================================================
-- SECTION 2 : USER ANALYTICS
-- =========================================================
-- ---------------------------------------------------------
-- Query 1 : User Profile Summary
-- ---------------------------------------------------------

SELECT
    handle,
    current_rank,
    highest_rank,
    current_rating,
    highest_rating,
    contribution,
    friend_count,
    organization,
    country,
    city
FROM users;

-- ---------------------------------------------------------
-- Query 2 : Rating Gap
-- ---------------------------------------------------------

SELECT
    handle,
    current_rating,
    highest_rating,
    highest_rating - current_rating AS rating_gap
FROM users;

-- ---------------------------------------------------------
-- Query 3 : Rank Summary
-- ---------------------------------------------------------

SELECT
    handle,
    current_rank,
    highest_rank
FROM users;

-- ---------------------------------------------------------
-- Query 4 : User Location
-- ---------------------------------------------------------

SELECT
    handle,
    country,
    city,
    organization
FROM users;

-- ---------------------------------------------------------
-- Query 5 : Community Statistics
-- ---------------------------------------------------------

SELECT
    handle,
    contribution,
    friend_count
FROM users;

-- ---------------------------------------------------------
-- Query 6 : Rating Improvement Summary
-- ---------------------------------------------------------

SELECT
    handle,
    current_rating,
    highest_rating,
    ROUND(
        (current_rating * 100.0) / highest_rating,
        2
    ) AS peak_rating_percentage
FROM users;

-- =========================================================
-- SECTION 3 : SUBMISSION ANALYTICS
-- =========================================================
-- ---------------------------------------------------------
-- Query 1 : Submission Verdict Distribution
-- ---------------------------------------------------------

SELECT
    verdict,
    COUNT(*) AS total_submissions
FROM submissions
GROUP BY verdict
ORDER BY total_submissions DESC;

-- ---------------------------------------------------------
-- Query 2 : Programming Language Usage
-- ---------------------------------------------------------

SELECT
    programming_language,
    COUNT(*) AS total_submissions
FROM submissions
GROUP BY programming_language
ORDER BY total_submissions DESC;

-- ---------------------------------------------------------
-- Query 3 : Submission Activity by Date
-- ---------------------------------------------------------

SELECT
    DATE(submission_time) AS submission_date,
    COUNT(*) AS total_submissions
FROM submissions
GROUP BY DATE(submission_time)
ORDER BY submission_date;

-- ---------------------------------------------------------
-- Query 4 : Most Attempted Contests
-- ---------------------------------------------------------

SELECT
    c.contest_name,
    COUNT(*) AS total_submissions
FROM submissions s
JOIN contests c
ON s.contest_id = c.contest_id
GROUP BY c.contest_name
ORDER BY total_submissions DESC
LIMIT 10;

-- ---------------------------------------------------------
-- Query 5 : Average Execution Time
-- ---------------------------------------------------------

SELECT
    ROUND(AVG(execution_time_ms),2) AS average_execution_time_ms
FROM submissions;

-- ---------------------------------------------------------
-- Query 6 : Average Memory Usage
-- ---------------------------------------------------------

SELECT
    ROUND(AVG(memory_bytes)/1024,2) AS average_memory_kb
FROM submissions;

-- ---------------------------------------------------------
-- Query 7 : Accepted vs Non-Accepted
-- ---------------------------------------------------------

SELECT
    CASE
        WHEN verdict='OK'
        THEN 'Accepted'
        ELSE 'Not Accepted'
    END AS submission_status,
    COUNT(*) AS total
FROM submissions
GROUP BY submission_status;

-- ---------------------------------------------------------
-- Query 8 : Most Attempted Problems
-- ---------------------------------------------------------

SELECT
    p.problem_name,
    COUNT(*) AS total_attempts
FROM submissions s
JOIN problems p
ON s.problem_id = p.problem_id
GROUP BY p.problem_name
ORDER BY total_attempts DESC
LIMIT 10;

-- ---------------------------------------------------------
-- Query 9 : Average Execution Time by Verdict
-- ---------------------------------------------------------

SELECT
    verdict,
    ROUND(AVG(execution_time_ms),2) AS average_execution_time_ms
FROM submissions
GROUP BY verdict
ORDER BY average_execution_time_ms DESC;

-- ---------------------------------------------------------
-- Query 10 : Average Memory Usage by Verdict
-- ---------------------------------------------------------

SELECT
    verdict,
    ROUND(AVG(memory_bytes)/1024,2) AS average_memory_kb
FROM submissions
GROUP BY verdict
ORDER BY average_memory_kb DESC;

-- =========================================================
-- SECTION 4 : PROBLEM ANALYTICS
-- =========================================================
-- ---------------------------------------------------------
-- Query 1 : Problem Rating Distribution
-- ---------------------------------------------------------

SELECT
    problem_rating,
    COUNT(*) AS total_problems
FROM problems
WHERE problem_rating IS NOT NULL
GROUP BY problem_rating
ORDER BY problem_rating;

-- ---------------------------------------------------------
-- Query 2 : Rated vs Unrated Problems
-- ---------------------------------------------------------

SELECT
    CASE
        WHEN is_rated = TRUE THEN 'Rated'
        ELSE 'Unrated'
    END AS problem_status,
    COUNT(*) AS total_problems
FROM problems
GROUP BY problem_status;

-- ---------------------------------------------------------
-- Query 3 : Problem Type Distribution
-- ---------------------------------------------------------

SELECT
    problem_type,
    COUNT(*) AS total_problems
FROM problems
GROUP BY problem_type
ORDER BY total_problems DESC;

-- ---------------------------------------------------------
-- Query 4 : Highest Rated Problems
-- ---------------------------------------------------------

SELECT
    problem_name,
    problem_rating
FROM problems
WHERE problem_rating IS NOT NULL
ORDER BY problem_rating DESC
LIMIT 20;

-- ---------------------------------------------------------
-- Query 5 : Average Problem Rating
-- ---------------------------------------------------------

SELECT
    ROUND(AVG(problem_rating),2) AS average_problem_rating
FROM problems
WHERE problem_rating IS NOT NULL;

-- ---------------------------------------------------------
-- Query 6 : Problem Points Distribution
-- ---------------------------------------------------------

SELECT
    points,
    COUNT(*) AS total_problems
FROM problems
WHERE points IS NOT NULL
GROUP BY points
ORDER BY points;

-- ---------------------------------------------------------
-- Query 7 : Contests with Maximum Problems
-- ---------------------------------------------------------

SELECT
    c.contest_name,
    COUNT(*) AS total_problems
FROM problems p
JOIN contests c
ON p.contest_id = c.contest_id
GROUP BY c.contest_name
ORDER BY total_problems DESC
LIMIT 10;

-- ---------------------------------------------------------
-- Query 8 : Average Problem Rating by Contest
-- ---------------------------------------------------------

SELECT
    c.contest_name,
    ROUND(AVG(p.problem_rating),2) AS average_rating
FROM problems p
JOIN contests c
ON p.contest_id = c.contest_id
WHERE p.problem_rating IS NOT NULL
GROUP BY c.contest_name
HAVING COUNT(*) >= 3
ORDER BY average_rating DESC
LIMIT 20;

-- ---------------------------------------------------------
-- Query 9 : Problems Without Rating
-- ---------------------------------------------------------

SELECT
    COUNT(*) AS unrated_problems
FROM problems
WHERE problem_rating IS NULL;

-- ---------------------------------------------------------
-- Query 10 : Problem Rating Buckets
-- ---------------------------------------------------------

SELECT
    CASE
        WHEN problem_rating < 1000 THEN 'Below 1000'
        WHEN problem_rating BETWEEN 1000 AND 1199 THEN '1000-1199'
        WHEN problem_rating BETWEEN 1200 AND 1399 THEN '1200-1399'
        WHEN problem_rating BETWEEN 1400 AND 1599 THEN '1400-1599'
        WHEN problem_rating BETWEEN 1600 AND 1799 THEN '1600-1799'
        WHEN problem_rating BETWEEN 1800 AND 1999 THEN '1800-1999'
        WHEN problem_rating >= 2000 THEN '2000+'
        ELSE 'Unrated'
    END AS rating_bucket,
    COUNT(*) AS total_problems
FROM problems
GROUP BY rating_bucket
ORDER BY MIN(problem_rating);

-- =========================================================
-- SECTION 5 : TAG ANALYTICS
-- =========================================================
-- ---------------------------------------------------------
-- Query 1 : Most Common Problem Tags
-- ---------------------------------------------------------

SELECT
    t.tag_name,
    COUNT(*) AS total_problems
FROM problem_tags pt
JOIN tags t
ON pt.tag_id = t.tag_id
GROUP BY t.tag_name
ORDER BY total_problems DESC;

-- ---------------------------------------------------------
-- Query 2 : Top 10 Most Popular Tags
-- ---------------------------------------------------------

SELECT
    t.tag_name,
    COUNT(*) AS total_problems
FROM problem_tags pt
JOIN tags t
ON pt.tag_id = t.tag_id
GROUP BY t.tag_name
ORDER BY total_problems DESC
LIMIT 10;

-- ---------------------------------------------------------
-- Query 3 : Least Common Tags
-- ---------------------------------------------------------

SELECT
    t.tag_name,
    COUNT(*) AS total_problems
FROM problem_tags pt
JOIN tags t
ON pt.tag_id = t.tag_id
GROUP BY t.tag_name
ORDER BY total_problems ASC
LIMIT 10;

-- ---------------------------------------------------------
-- Query 4 : Average Problem Rating by Tag
-- ---------------------------------------------------------

SELECT
    t.tag_name,
    ROUND(AVG(p.problem_rating),2) AS average_rating
FROM problem_tags pt
JOIN tags t
ON pt.tag_id = t.tag_id
JOIN problems p
ON pt.problem_id = p.problem_id
WHERE p.problem_rating IS NOT NULL
GROUP BY t.tag_name
ORDER BY average_rating DESC;

-- ---------------------------------------------------------
-- Query 6 : Maximum Problem Rating by Tag
-- ---------------------------------------------------------

SELECT
    t.tag_name,
    MAX(p.problem_rating) AS highest_problem_rating
FROM problem_tags pt
JOIN tags t
ON pt.tag_id = t.tag_id
JOIN problems p
ON pt.problem_id = p.problem_id
WHERE p.problem_rating IS NOT NULL
GROUP BY t.tag_name
ORDER BY highest_problem_rating DESC;

-- ---------------------------------------------------------
-- Query 7 : Minimum Problem Rating by Tag
-- ---------------------------------------------------------

SELECT
    t.tag_name,
    MIN(p.problem_rating) AS lowest_problem_rating
FROM problem_tags pt
JOIN tags t
ON pt.tag_id = t.tag_id
JOIN problems p
ON pt.problem_id = p.problem_id
WHERE p.problem_rating IS NOT NULL
GROUP BY t.tag_name
ORDER BY lowest_problem_rating;

-- ---------------------------------------------------------
-- Query 8 : Average Points by Tag
-- ---------------------------------------------------------

SELECT
    t.tag_name,
    ROUND(AVG(p.points),2) AS average_points
FROM problem_tags pt
JOIN tags t
ON pt.tag_id = t.tag_id
JOIN problems p
ON pt.problem_id = p.problem_id
WHERE p.points IS NOT NULL
GROUP BY t.tag_name
ORDER BY average_points DESC;

-- ---------------------------------------------------------
-- Query 9 : Total Unique Tags
-- ---------------------------------------------------------

SELECT
    COUNT(*) AS total_tags
FROM tags;

-- ---------------------------------------------------------
-- Query 10 : Problems with Maximum Number of Tags
-- ---------------------------------------------------------

SELECT
    p.problem_name,
    COUNT(pt.tag_id) AS total_tags
FROM problems p
JOIN problem_tags pt
ON p.problem_id = pt.problem_id
GROUP BY p.problem_id, p.problem_name
ORDER BY total_tags DESC
LIMIT 20;

-- =========================================================
-- SECTION 6 : CONTEST ANALYTICS
-- =========================================================
-- ---------------------------------------------------------
-- Query 1 : Rating Progress Over Time
-- ---------------------------------------------------------

SELECT
    rating_update_time,
    old_rating,
    new_rating,
    rating_change
FROM rating_history
ORDER BY rating_update_time;


-- ---------------------------------------------------------
-- Query 2 : Highest Rating Gains
-- ---------------------------------------------------------

SELECT
    contest_id,
    contest_rank,
    old_rating,
    new_rating,
    rating_change
FROM rating_history
ORDER BY rating_change DESC
LIMIT 10;

-- ---------------------------------------------------------
-- Query 3 : Highest Rating Losses
-- ---------------------------------------------------------

SELECT
    contest_id,
    contest_rank,
    old_rating,
    new_rating,
    rating_change
FROM rating_history
ORDER BY rating_change
LIMIT 10;

-- ---------------------------------------------------------
-- Query 4 : Average Rating Change
-- ---------------------------------------------------------

SELECT
    ROUND(AVG(rating_change),2) AS average_rating_change
FROM rating_history;

-- ---------------------------------------------------------
-- Query 5 : Peak Rating
-- ---------------------------------------------------------

SELECT
    MAX(new_rating) AS highest_rating
FROM rating_history;

-- ---------------------------------------------------------
-- Query 6 : Lowest Rating
-- ---------------------------------------------------------

SELECT
    MIN(new_rating) AS lowest_rating
FROM rating_history;

-- ---------------------------------------------------------
-- Query 7 : Net Rating Improvement
-- ---------------------------------------------------------

SELECT
    MAX(new_rating) - MIN(old_rating) AS total_rating_improvement
FROM rating_history;

-- ---------------------------------------------------------
-- Query 8 : Rating Change Distribution
-- ---------------------------------------------------------

SELECT
    rating_change,
    COUNT(*) AS contests
FROM rating_history
GROUP BY rating_change
ORDER BY rating_change;

-- ---------------------------------------------------------
-- Query 9 : Contest Rank vs Rating Change
-- ---------------------------------------------------------

SELECT
    contest_rank,
    rating_change
FROM rating_history
ORDER BY contest_rank;

-- ---------------------------------------------------------
-- Query 10 : Positive vs Negative Rating Changes
-- ---------------------------------------------------------

SELECT
    CASE
        WHEN rating_change > 0 THEN 'Rating Increased'
        WHEN rating_change < 0 THEN 'Rating Decreased'
        ELSE 'No Change'
    END AS rating_status,
    COUNT(*) AS contests
FROM rating_history
GROUP BY rating_status;
-- =========================================================
-- SECTION 7 : RATING ANALYTICS
-- =========================================================