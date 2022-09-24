if [ $1 == fb15k237 ]; then
	(cd FB15k237 && PYTHONPATH=.. python FB15k237_evaluation.py FB15k237_TransE/best_valid_model.pkl)
elif [ $1 == wn18rr ]; then
	(cd WN18RR && PYTHONPATH=.. python WN18RR_evaluation.py WN18RR_TransE/best_valid_model.pkl)
fi
