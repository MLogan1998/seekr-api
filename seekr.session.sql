-- SELECT * from seekrapi_seekerprofile


SELECT seekrapi_seekerprofile.id
FROM  seekrapi_seekerprofile
LEFT JOIN seekrapi_employeraction
ON seekrapi_seekerprofile.id = seekrapi_employeraction.seeker_id
WHERE seekrapi_seekerprofile.id NOT IN 
  (
    SELECT seekrapi_employeraction.seeker_id
    FROM seekrapi_employeraction
    WHERE employer_id IS 1
  )
SELECT DISTINCT seeker_id
