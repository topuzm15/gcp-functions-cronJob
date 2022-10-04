DELETE FROM {target_table_name}
WHERE file_name IN 
( 
    SELECT file_name
    FROM {processed_table_name}
    WHERE file_name not in ({file_names})
    and dt > '{date}'
)
and dt > '{date}'