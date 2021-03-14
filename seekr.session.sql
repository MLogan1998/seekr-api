-- SELECT * from seekrapi_employeraction


SELECT seekrapi_seekerprofile.id
FROM  seekrapi_seekerprofile
LEFT JOIN seekrapi_employeraction
ON seekrapi_seekerprofile.id = seekrapi_employeraction.seeker_id
WHERE seekrapi_seekerprofile.id NOT IN 
  (
    SELECT seeker_id
    FROM seekrapi_employeraction
    WHERE employer_id IS 11
  )
GROUP BY seeker_id
