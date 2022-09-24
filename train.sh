if [ $1 == fb15k237 ]; then
	(cd FB15k237 && PYTHONPATH=.. time python FB15k237_TransE.py "${@:2}")
elif [ $1 == wn18rr ]; then
	(cd WN18RR && PYTHONPATH=.. time python WN18RR_TransE.py "${@:2}")
fi
