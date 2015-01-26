REGISTER /usr/lib/zookeeper/zookeeper.jar
REGISTER /usr/lib/hbase/hbase-server.jar
set hbase.zookeeper.quorum 'zookeeper server'

%default txt population_drift.txt
%default table population_drift
%default col_fam1 num
%default col_fam2 ratio
%default col0 region
%default col1 n_in
%default col2 n_out
%default col3 n_net
%default col4 n_prev
%default col5 r_in
%default col6 r_out
%default col7 r_net
%default col8 r_prev

TXT = LOAD '$txt' using PigStorage('\t') AS ($col0:bytearray, $col1:bytearray, $col2:bytearray, $col3:bytearray, $col4:bytearray, $col5:bytearray, $col6:bytearray, $col7:bytearray, $col8:bytearray);
DATA = FOREACH TXT GENERATE $col0 AS docid, $col1, $col2, $col3, $col4, $col5, $col6, $col7, $col8;
STORE TXT INTO 'hbase://$table' using org.apache.pig.backend.hadoop.hbase.HBaseStorage('$col_fam1:$col1 $col_fam1:$col2 $col_fam1:$col3 $col_fam1:$col4 $col_fam2:$col5 $col_fam2:$col6 $col_fam2:$col7 $col_fam2:$col8');
