-- 1. Get all the predictions.

SELECT * 
FROM cardiodiagnosis order by date;

-- 2. Get all the predictions for the day.

SELECT * 
FROM cardiodiagnosis
WHERE DATE(date) = CURRENT_DATE;

SELECT * 
FROM cardiodiagnosis
WHERE DATE(date) = '2019-02-20';

-- 3. Get all the predictions for the day and sort them based on the highest probability percentage at
-- the top.
SELECT * 
FROM cardiodiagnosis
WHERE DATE(date) = '2019-02-20'  
ORDER BY cardioarrestdetected DESC;

-- 4. Get all the unique cities.

SELECT DISTINCT city
FROM addressinfo;

-- 5. Get all the members who are from a city 'Burgos'.

SELECT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Burgos';

-- 6. Get all the members who are from 'Flora' city.

SELECT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Flora';

-- 7. Get the total number of blood tests done for Aisha.

SELECT COUNT(b.blood_id) AS total_blood_tests
FROM bloodtest b
JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'aisha';

-- 8. Get the X-ray details of Ajay whose cardio test was done on 26th of Jan 2019.

SELECT x.*
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'ajay'
  AND DATE(c.date) = '2019-01-26';

-- 9. Get all the members who are from cities 'Burgos' and 'Flora'.
SELECT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city in ('Burgos', 'Flora');

-- 10. Get the total number of blood tests done for Aberson
SELECT COUNT(b.blood_id) AS total_blood_tests
FROM bloodtest b
JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'aberson';

select * from memberinfo where firstname='aberson';

-- 11. Get all address details for member ID M300.
select * from addressinfo 
where memberinfo_member_id='m300';

-- 12. Get all X-ray details for cardio ID CID122.

select * from xray
where cardiodiagnosis_cardio_id='cid122';

-- 13. Get all symptom details whose cardio ID is CID250 and CID300.

SELECT *
FROM symptom
WHERE cardiodiagnosis_cardio_id IN ('cid250', 'cid300');

-- 14. Get all symptom details for the month of July and year 2019

SELECT *
FROM symptom
WHERE EXTRACT(MONTH FROM date) = 7
AND EXTRACT(YEAR FROM date) = 2019;

-- 15. Get X-ray details for the member with the last name "Dailley".
select x.* from xray x
join cardiodiagnosis c on x.cardiodiagnosis_cardio_id=c.cardio_id
join memberinfo m on m.member_id=c.memberinfo_member_id
where m.lastname='dailley';

-- 16. Get wearable device data details for cardio IDs between CID100 and CID200.

SELECT *
FROM wearabledevicedata
WHERE cardiodiagnosis_cardio_id BETWEEN 'cid100' AND 'cid200';

-- 17. Display all cardio diagnosis details where the first name starts with the letter "A".

SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'a%';

-- 18. Display all cardio diagnosis details where the first name starts with "A" and ends with "A".

SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'a%a';

-- 19. Get all the members from the MemberInfo table.

SELECT *
FROM memberinfo;

-- 20. Get all the addresses of members.

SELECT *
FROM addressinfo;



