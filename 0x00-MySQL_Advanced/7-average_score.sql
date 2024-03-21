-- SQL script that creates a stored procedure ComputeAverageScoreForUser


delimiter $$
CREATE PROCEDURE ComputeAverageScoreForUser (in user_id int)
begin
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
    WHERE id = user_id;

end $$

delimiter ;
