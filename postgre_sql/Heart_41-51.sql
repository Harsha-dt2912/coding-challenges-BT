-- 41. Get the list of female members and their cardio information for those aged above 50.
select * from diseasedetail;
SELECT m.*, c.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE m.gender = '1'
  AND m.age > 50;

-- 42. Get the list of males who have blood pressure > 140 and have not had a heart attack.

SELECT DISTINCT m.*, b.*,d.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
LEFT JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id AND d.disease_name = 'Heart Attack'
WHERE m.gender = '0'
  AND b.bloodpressure > 140
  AND d.disease_name IS NULL;

-- 43. Get the list of members who had a heart attack from the state "Mountain Province".

SELECT DISTINCT m.*, d.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE d.disease_name = 'Heart Attack'
  AND a.state = 'Mountain Province';

-- 44. Get the list of male members and their diseases with symptoms for those aged less than 40.


SELECT m.*, d.*, s.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE m.gender = '0'
  AND m.age < 40;

-- 45. Get the count of members from "Mountain Province" aged between 50 and 60.

SELECT COUNT(*) AS total_members
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Mountain Province'
  AND m.age BETWEEN 50 AND 60;

-- 46. Get the count of male and female members who have blood pressure > 140 and have been
-- detected with a heart attack.

SELECT m.gender, COUNT(*) AS total_members
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
WHERE b.bloodpressure > 140
  AND d.disease_name = 'Heart Attack'
GROUP BY m.gender;

-- 47. Get the average blood pressure of people aged between 40-50 and 50-60.

SELECT 
    CASE 
        WHEN m.age BETWEEN 40 AND 50 THEN '40-50'
        WHEN m.age BETWEEN 51 AND 60 THEN '51-60'
    END AS age_group,
    AVG(b.bloodpressure) AS avg_blood_pressure
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE m.age BETWEEN 40 AND 60
GROUP BY age_group
ORDER BY age_group;

-- 48. Get the list of diseases for people with high blood pressure in the range of 120-180, sorted by
-- gender.

SELECT m.gender, d.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
WHERE b.bloodpressure BETWEEN 120 AND 180
ORDER BY m.gender;

-- 49. Get the count of people who have had their X-rays every month from the state of "Special
-- Province".

SELECT EXTRACT(MONTH FROM x.date) AS month, COUNT(*) AS total_xrays
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Special Province'
GROUP BY EXTRACT(MONTH FROM x.date)
ORDER BY month;


-- 50. Get the average age of people diagnosed with a heart attack for each state, broken down by male
-- and female.

SELECT a.state, m.gender, AVG(m.age) AS avg_age
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE d.disease_name = 'Heart Attack'
GROUP BY a.state, m.gender
ORDER BY a.state, m.gender;


-- 51. Get the count of people for each state diagnosed with a heart attack, who have a slope value of 2,
-- and have had at least one X-ray and one symptom.

SELECT a.state, COUNT(DISTINCT m.member_id) AS total_members
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
JOIN wearabledevicedata w ON c.cardio_id = w.cardiodiagnosis_cardio_id
JOIN xray x ON c.cardio_id = x.cardiodiagnosis_cardio_id
JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE d.disease_name = 'Heart Attack'
  AND w.slope = 2
GROUP BY a.state
ORDER BY a.state;


