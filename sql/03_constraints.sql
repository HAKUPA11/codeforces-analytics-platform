-- =========================================================
-- Codeforces Analytics Platform
-- File : 03_constraints.sql
-- Description : Foreign Keys and Constraints
-- =========================================================

USE codeforces_analytics;

-- =========================================================
-- PROBLEMS
-- =========================================================
ALTER TABLE problems
ADD CONSTRAINT fk_problem_contest
FOREIGN KEY (contest_id)
REFERENCES contests(contest_id)
ON DELETE CASCADE
ON UPDATE CASCADE;


-- =========================================================
-- PROBLEM_TAGS
-- =========================================================
ALTER TABLE problem_tags
ADD CONSTRAINT fk_problem_tags_problem
FOREIGN KEY (problem_id)
REFERENCES problems(problem_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE problem_tags
ADD CONSTRAINT fk_problem_tags_tag
FOREIGN KEY (tag_id)
REFERENCES tags(tag_id)
ON DELETE CASCADE
ON UPDATE CASCADE;


-- =========================================================
-- SUBMISSIONS
-- =========================================================
ALTER TABLE submissions
ADD CONSTRAINT fk_submission_user
FOREIGN KEY (user_id)
REFERENCES users(user_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE submissions
ADD CONSTRAINT fk_submission_contest
FOREIGN KEY (contest_id)
REFERENCES contests(contest_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE submissions
ADD CONSTRAINT fk_submission_problem
FOREIGN KEY (problem_id)
REFERENCES problems(problem_id)
ON DELETE CASCADE
ON UPDATE CASCADE;


-- =========================================================
-- RATING_HISTORY
-- =========================================================	
ALTER TABLE rating_history
ADD CONSTRAINT fk_rating_user
FOREIGN KEY (user_id)
REFERENCES users(user_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE rating_history
ADD CONSTRAINT fk_rating_contest
FOREIGN KEY (contest_id)
REFERENCES contests(contest_id)
ON DELETE CASCADE
ON UPDATE CASCADE;