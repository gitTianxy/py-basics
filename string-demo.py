sql_tpl = '''
    SELECT mac.fid,mac.ekey,mac.evalue,mac.insert_time,mac.last_update_time,man.ekey,man.evalue FROM fileextend_inner_0 mac LEFT JOIN
    fileextend_inner_0 man ON mac.fid=man.fid
    WHERE mac.insert_time>='2017-06-16 00:00:00' AND mac.insert_time<'2017-06-23 00:00:00' AND mac.ekey='av_scan_result'
    AND man.ekey='category' AND man.evalue='adult_video'
    '''

print sql_tpl