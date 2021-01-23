rm temp/out.txt
rm temp/out2.txt
timeout 900 python temp/flowgraph.py >> temp/out.txt
iconv -f utf-8 -t utf-8 -c temp/out.txt > temp/out2.txt
rm temp/out.txt