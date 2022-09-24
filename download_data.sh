if [ -d raw_data ]; then
	rm -rf raw_data
fi
mkdir raw_data

wget -O raw_data/wn.tar https://everest.hds.utc.fr/lib/exe/fetch.php?media=en:wordnet-mlj12.tar.gz
tar -xf raw_data/wn.tar -C raw_data
mv raw_data/wordnet-mlj12 raw_data/wn

wget -O raw_data/fb.tar https://everest.hds.utc.fr/lib/exe/fetch.php?media=en:fb15k.tgz
tar -xf raw_data/fb.tar -C raw_data
mv raw_data/FB15k raw_data/fb

wget -O raw_data/fb15k237.tar https://github.com/TimDettmers/ConvE/raw/master/FB15k-237.tar.gz
mkdir raw_data/fb15k237
tar -xf raw_data/fb15k237.tar -C raw_data/fb15k237

wget -O raw_data/wn18rr.tar https://github.com/TimDettmers/ConvE/raw/master/WN18RR.tar.gz
mkdir raw_data/wn18rr
tar -xf raw_data/wn18rr.tar -C raw_data/wn18rr
