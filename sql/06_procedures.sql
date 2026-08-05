-- =========================================================
-- Codeforces Analytics Platform
-- File : 06_procedures.sql
-- Description : Stored Procedures
-- =========================================================

USE codeforces_analytics;

-- =========================================================
-- PROCEDURE 1 : UPSERT USER
-- =========================================================

DROP PROCEDURE IF EXISTS sp_upsert_user;

DELIMITER $$

CREATE PROCEDURE sp_upsert_user(

    IN p_handle VARCHAR(50),

    IN p_current_rank VARCHAR(30),

    IN p_highest_rank VARCHAR(30),

    IN p_current_rating INT,

    IN p_highest_rating INT,

    IN p_contribution INT,

    IN p_friend_count INT,

    IN p_organization VARCHAR(150),

    IN p_country VARCHAR(100),

    IN p_city VARCHAR(100),

    IN p_source ENUM('Codeforces','LeetCode','CodeChef','AtCoder')

)

BEGIN

    INSERT INTO users(

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

        source,

        last_api_sync

    )

    VALUES(

        p_handle,

        p_current_rank,
        p_highest_rank,

        p_current_rating,
        p_highest_rating,

        p_contribution,
        p_friend_count,

        p_organization,
        p_country,
        p_city,

        p_source,

        CURRENT_TIMESTAMP

    )

    ON DUPLICATE KEY UPDATE

        current_rank = VALUES(current_rank),

        highest_rank = VALUES(highest_rank),

        current_rating = VALUES(current_rating),

        highest_rating = VALUES(highest_rating),

        contribution = VALUES(contribution),

        friend_count = VALUES(friend_count),

        organization = VALUES(organization),

        country = VALUES(country),

        city = VALUES(city),

        source = VALUES(source),

        last_api_sync = CURRENT_TIMESTAMP;

END $$

DELIMITER ;



-- =========================================================
-- PROCEDURE 2 : UPSERT CONTEST
-- =========================================================

DROP PROCEDURE IF EXISTS sp_upsert_contest;

DELIMITER $$

CREATE PROCEDURE sp_upsert_contest(

    IN p_contest_id INT,
    IN p_contest_name VARCHAR(255),
    IN p_contest_type VARCHAR(10),
    IN p_contest_phase VARCHAR(30),
    IN p_is_frozen BOOLEAN,
    IN p_duration_seconds INT,
    IN p_start_time TIMESTAMP,
    IN p_source VARCHAR(30)

)

BEGIN

    INSERT INTO contests(

        contest_id,
        contest_name,
        contest_type,
        contest_phase,
        is_frozen,
        duration_seconds,
        start_time,
        source,
        last_api_sync

    )

    VALUES(

        p_contest_id,
        p_contest_name,
        p_contest_type,
        p_contest_phase,
        p_is_frozen,
        p_duration_seconds,
        p_start_time,
        p_source,
        CURRENT_TIMESTAMP

    )

    ON DUPLICATE KEY UPDATE

        contest_name = VALUES(contest_name),
        contest_type = VALUES(contest_type),
        contest_phase = VALUES(contest_phase),
        is_frozen = VALUES(is_frozen),
        duration_seconds = VALUES(duration_seconds),
        start_time = VALUES(start_time),
        source = VALUES(source),
        last_api_sync = CURRENT_TIMESTAMP;

END $$

DELIMITER ;


-- =========================================================
-- PROCEDURE 3 : UPSERT PROBLEM
-- =========================================================

DROP PROCEDURE IF EXISTS sp_upsert_problem;

DELIMITER $$

CREATE PROCEDURE sp_upsert_problem(

    IN p_contest_id INT,
    IN p_problem_index CHAR(5),
    IN p_problem_name VARCHAR(255),
    IN p_problem_type VARCHAR(20),
    IN p_points DECIMAL(6,2),
    IN p_problem_rating INT,
    IN p_is_rated BOOLEAN,
    IN p_source VARCHAR(30)

)

BEGIN

    INSERT INTO problems(

        contest_id,
        problem_index,
        problem_name,
        problem_type,
        points,
        problem_rating,
        is_rated,
        source,
        last_api_sync

    )

    VALUES(

        p_contest_id,
        p_problem_index,
        p_problem_name,
        p_problem_type,
        p_points,
        p_problem_rating,
        p_is_rated,
        p_source,
        CURRENT_TIMESTAMP

    )

    ON DUPLICATE KEY UPDATE

        problem_name = VALUES(problem_name),
        problem_type = VALUES(problem_type),
        points = VALUES(points),
        problem_rating = VALUES(problem_rating),
        is_rated = VALUES(is_rated),
        source = VALUES(source),
        last_api_sync = CURRENT_TIMESTAMP;

END $$

DELIMITER ;



-- =========================================================
-- PROCEDURE 4 : ADD PROBLEM TAG
-- =========================================================

DROP PROCEDURE IF EXISTS sp_add_problem_tag;

DELIMITER $$

CREATE PROCEDURE sp_add_problem_tag(

    IN p_problem_id INT,

    IN p_tag_id INT

)

BEGIN

    INSERT IGNORE INTO problem_tags(

        problem_id,

        tag_id

    )

    VALUES(

        p_problem_id,

        p_tag_id

    );

END $$

DELIMITER ;


-- =========================================================
-- PROCEDURE 5 : ADD SUBMISSION
-- =========================================================

DROP PROCEDURE IF EXISTS sp_add_submission;

DELIMITER $$

CREATE PROCEDURE sp_add_submission(

    IN p_submission_id BIGINT,

    IN p_user_id INT,

    IN p_contest_id INT,

    IN p_problem_id INT,

    IN p_programming_language VARCHAR(100),

    IN p_verdict VARCHAR(50),

    IN p_passed_test_count SMALLINT UNSIGNED,

    IN p_execution_time_ms INT UNSIGNED,

    IN p_memory_bytes INT UNSIGNED,

    IN p_submission_time TIMESTAMP,

    IN p_relative_time_seconds INT,

    IN p_source VARCHAR(30)

)

BEGIN

    INSERT IGNORE INTO submissions(

        submission_id,

        user_id,

        contest_id,

        problem_id,

        programming_language,

        verdict,

        passed_test_count,

        execution_time_ms,

        memory_bytes,

        submission_time,

        relative_time_seconds,

        source,

        last_api_sync

    )

    VALUES(

        p_submission_id,

        p_user_id,

        p_contest_id,

        p_problem_id,

        p_programming_language,

        p_verdict,

        p_passed_test_count,

        p_execution_time_ms,

        p_memory_bytes,

        p_submission_time,

        p_relative_time_seconds,

        p_source,

        CURRENT_TIMESTAMP

    );

END $$

DELIMITER ;



-- =========================================================
-- PROCEDURE 6 : ADD RATING HISTORY
-- =========================================================

DROP PROCEDURE IF EXISTS sp_add_rating_history;

DELIMITER $$

CREATE PROCEDURE sp_add_rating_history(

    IN p_user_id INT,

    IN p_contest_id INT,

    IN p_contest_rank INT UNSIGNED,

    IN p_old_rating INT UNSIGNED,

    IN p_new_rating INT UNSIGNED,

    IN p_rating_update_time TIMESTAMP,

    IN p_source VARCHAR(30)

)

BEGIN

    INSERT INTO rating_history(

        user_id,

        contest_id,

        contest_rank,

        old_rating,

        new_rating,

        rating_update_time,

        source,

        last_api_sync

    )

    SELECT

        p_user_id,

        p_contest_id,

        p_contest_rank,

        p_old_rating,

        p_new_rating,

        p_rating_update_time,

        p_source,

        CURRENT_TIMESTAMP

    FROM DUAL

    WHERE NOT EXISTS (

        SELECT 1

        FROM rating_history

        WHERE user_id = p_user_id

          AND contest_id = p_contest_id

    );

END $$

DELIMITER ;


-- =========================================================
-- PROCEDURE 7 : GET USER STATISTICS
-- =========================================================

DROP PROCEDURE IF EXISTS sp_get_user_statistics;

DELIMITER $$

CREATE PROCEDURE sp_get_user_statistics(

    IN p_user_id INT

)

BEGIN

    SELECT *

    FROM vw_user_statistics

    WHERE user_id = p_user_id;

END $$

DELIMITER ;


-- =========================================================
-- PROCEDURE 8 : GET PROBLEM STATISTICS
-- =========================================================

DROP PROCEDURE IF EXISTS sp_get_problem_statistics;

DELIMITER $$

CREATE PROCEDURE sp_get_problem_statistics(

    IN p_problem_id INT

)

BEGIN

    SELECT *

    FROM vw_problem_statistics

    WHERE problem_id = p_problem_id;

END $$

DELIMITER ;


-- =========================================================
-- PROCEDURE 9 : GET CONTEST STATISTICS
-- =========================================================

DROP PROCEDURE IF EXISTS sp_get_contest_statistics;

DELIMITER $$

CREATE PROCEDURE sp_get_contest_statistics(

    IN p_contest_id INT

)

BEGIN

    SELECT *

    FROM vw_contest_statistics

    WHERE contest_id = p_contest_id;

END $$

DELIMITER ;


-- =========================================================
-- PROCEDURE 10 : GET USER SUBMISSION HISTORY
-- =========================================================

DROP PROCEDURE IF EXISTS sp_get_user_submission_history;

DELIMITER $$

CREATE PROCEDURE sp_get_user_submission_history(

    IN p_user_id INT

)

BEGIN

    SELECT

        submission_id,

        contest_name,

        problem_index,

        problem_name,

        verdict,

        programming_language,

        execution_time_ms,

        memory_bytes,

        submission_time

    FROM vw_submission_details

    WHERE handle = (

        SELECT handle
        FROM users
        WHERE user_id = p_user_id

    )

    ORDER BY submission_time DESC;

END $$

DELIMITER ;
