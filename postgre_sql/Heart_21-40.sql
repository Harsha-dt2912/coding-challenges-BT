-- 21. Get a list of wearable device information.

SELECT *
FROM wearabledevicedata;

-- 22. Get a list of all the blood tests done.

SELECT *
FROM bloodtest;

-- 23. Get a list of members who are aged greater than 50.
SELECT *
FROM memberinfo
WHERE age > 50;

-- 24. Get a list of addresses for the city 'Flora'.

SELECT *
FROM addressinfo
WHERE city = 'Flora';

-- 25. Get a list of all unique states

SELECT DISTINCT state
FROM addressinfo;

-- 26. Get the total number of members in the database.

SELECT COUNT(*) AS total_members
FROM memberinfo;

-- 27. Get the total number of blood tests done.

SELECT COUNT(*) AS total_blood_tests
FROM bloodtest;

-- 28. Get the average cholesterol level for members

SELECT AVG(serumcholesterol) AS avg_cholesterol
FROM bloodtest;

-- 29. Get the maximum peak value in symptoms.

SELECT MAX(oldpeak) AS max_peak
FROM symptom;

-- 30. Get the list of tests done between January 1, 2015, and January 31, 2019.

SELECT *
FROM bloodtest
WHERE DATE(date) BETWEEN '2015-01-01' AND '2019-01-31';

-- 31. Get the number of males and females aged between 50 and 60.
SELECT gender, COUNT(*) AS total_count
FROM memberinfo
WHERE age BETWEEN 50 AND 60
GROUP BY gender;

-- 32. Get the list of tests where blood pressure is between 100 and 200.
SELECT *
FROM bloodtest
WHERE bloodpressure BETWEEN 100 AND 200;

-- 33. Get the list of symptoms diagnosed for patients.

SELECT *
FROM symptom;

-- 34. Get the average age of patients in the database.

SELECT AVG(age) AS avg_age
FROM memberinfo;

-- 35. Get the total number of cities for each state available.

SELECT state, COUNT(DISTINCT city) AS total_cities
FROM addressinfo
GROUP BY state;

-- 36. Get the number of patients in the following age groups:
-- o 10-20
-- o 20-30
-- o 30-40
-- o 40-50
-- o 50-60
-- o 60-70

SELECT 
    CASE 
        WHEN age BETWEEN 10 AND 20 THEN '10-20'
        WHEN age BETWEEN 21 AND 30 THEN '21-30'
        WHEN age BETWEEN 31 AND 40 THEN '31-40'
        WHEN age BETWEEN 41 AND 50 THEN '41-50'
        WHEN age BETWEEN 51 AND 60 THEN '51-60'
        WHEN age BETWEEN 61 AND 70 THEN '61-70'
    END AS age_group,
    COUNT(*) AS total_patients
FROM memberinfo
WHERE age BETWEEN 10 AND 70
GROUP BY age_group
ORDER BY age_group;

-- 37. Get the list of members and their addresses.

SELECT *
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id;

-- 38. Get the list of members and their cardio history.

SELECT *
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id;

-- 39. Get the list of members and their diseases.

SELECT m.*, d.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id;

-- 40. Get the list of females diagnosed with a heart attack.

SELECT m.*, c.*, d.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
WHERE m.gender = '1'
  AND d.disease_name = 'Heart Attack';




