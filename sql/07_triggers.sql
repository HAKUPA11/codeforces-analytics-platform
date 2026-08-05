-- =========================================================
-- Codeforces Analytics Platform
-- File : 07_triggers.sql
-- Description : Database Triggers
-- =========================================================

USE codeforces_analytics;

-- =========================================================
-- TRIGGER 1 : VALIDATE SUBMISSION
-- =========================================================

DROP TRIGGER IF EXISTS trg_submission_before_insert;

DELIMITER $$

CREATE TRIGGER trg_submission_before_insert

BEFORE INSERT ON submissions

FOR EACH ROW

BEGIN

    IF NEW.execution_time_ms IS NOT NULL
       AND NEW.execution_time_ms < 0 THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Execution time cannot be negative';

    END IF;

    IF NEW.memory_bytes IS NOT NULL
       AND NEW.memory_bytes < 0 THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Memory usage cannot be negative';

    END IF;

    IF NEW.passed_test_count < 0 THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Passed test count cannot be negative';

    END IF;

END $$

DELIMITER ;


-- =========================================================
-- TRIGGER 2 : UPDATE USER RATING
-- =========================================================

DROP TRIGGER IF EXISTS trg_rating_history_after_insert;

DELIMITER $$

CREATE TRIGGER trg_rating_history_after_insert

AFTER INSERT ON rating_history

FOR EACH ROW

BEGIN

    UPDATE users

    SET

        current_rating = NEW.new_rating,

        highest_rating = GREATEST(
            highest_rating,
            NEW.new_rating
        ),

        last_api_sync = CURRENT_TIMESTAMP

    WHERE user_id = NEW.user_id;

END $$

DELIMITER ;


-- =========================================================
-- TRIGGER 3 : UPDATE USER LAST SYNC
-- =========================================================

DROP TRIGGER IF EXISTS trg_submission_after_insert;

DELIMITER $$

CREATE TRIGGER trg_submission_after_insert

AFTER INSERT ON submissions

FOR EACH ROW

BEGIN

    UPDATE users

    SET last_api_sync = CURRENT_TIMESTAMP

    WHERE user_id = NEW.user_id;

END $$

DELIMITER ;