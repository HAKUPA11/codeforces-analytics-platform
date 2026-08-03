-- =========================================================
-- Codeforces Analytics Platform
-- File : 04_indexes.sql
-- Description : Performance Indexes
-- =========================================================

USE codeforces_analytics;
-- =========================================================
-- USERS
-- =========================================================

CREATE INDEX idx_users_current_rating
ON users(current_rating);

CREATE INDEX idx_users_highest_rating
ON users(highest_rating);

CREATE INDEX idx_users_country
ON users(country);

CREATE INDEX idx_users_organization
ON users(organization);

-- =========================================================
-- CONTESTS
-- =========================================================

CREATE INDEX idx_contests_start_time
ON contests(start_time);

CREATE INDEX idx_contests_phase
ON contests(contest_phase);

CREATE INDEX idx_contests_type
ON contests(contest_type);

-- =========================================================
-- PROBLEMS
-- =========================================================

CREATE INDEX idx_problem_rating
ON problems(problem_rating);

CREATE INDEX idx_problem_name
ON problems(problem_name);

-- =========================================================
-- SUBMISSIONS
-- =========================================================

CREATE INDEX idx_submission_user
ON submissions(user_id);

CREATE INDEX idx_submission_problem
ON submissions(problem_id);

CREATE INDEX idx_submission_contest
ON submissions(contest_id);

CREATE INDEX idx_submission_verdict
ON submissions(verdict);

CREATE INDEX idx_submission_time
ON submissions(submission_time);

CREATE INDEX idx_submission_language
ON submissions(programming_language);

CREATE INDEX idx_submission_user_time
ON submissions(user_id, submission_time);

-- =========================================================
-- RATING HISTORY
-- =========================================================

CREATE INDEX idx_rating_user
ON rating_history(user_id);

CREATE INDEX idx_rating_contest
ON rating_history(contest_id);

CREATE INDEX idx_rating_time
ON rating_history(rating_update_time);

CREATE INDEX idx_rating_user_time
ON rating_history(user_id, rating_update_time);

SHOW INDEX FROM users;

SHOW INDEX FROM contests;

SHOW INDEX FROM problems;

SHOW INDEX FROM submissions;

SHOW INDEX FROM rating_history;


SHOW CREATE TABLE contests;
SHOW CREATE TABLE problems;

