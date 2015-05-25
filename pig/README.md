Pig
===
* diff
  * diff2.pig
    * [A Simple Explanation of COGROUP in Apache Pig](http://joshualande.com/cogroup-in-pig/)
    * 28억행(2877773812 line), 112GB(119496321285 byte) file 비교에 약 1h 52m 소요
    * 실행 전 `sync; echo 3 > /proc/sys/vm/drop_caches`로 memory 확보함
    * pig version 0.12.0-cdh5.2.0
    * server cpu Intel(R) Xeon(R) CPU E5-2430 0 @ 2.20GHz * 24, memory 49535824 kB
  * diff1.pig
    * [equivalent of linux diff in apache pig](http://stackoverflow.com/questions/5907950/equivalent-of-linux-diff-in-apache-pig)
    * 같은 server인데도 diff2.pig와 달리 실패한 요인은 다음 두 가지로 추정
    * memory를 적게 할당
    * 양쪽 file의 결과를 전부 쓰게 코드 작성
  * cf
    * [Comparing two files using awk](http://theunixshell.blogspot.kr/2012/12/i-have-two-files-file-1-contains-3.html)
    * [comparing 2 large unsorted CSV files based on 2 columns](http://stackoverflow.com/questions/6999705/comparing-2-large-unsorted-csv-files-based-on-2-columns)
    * [Comparing 2 Large Lists (Millions Of Rows) To Identify Shared And Exclusive Elements](https://www.biostars.org/p/63016/)