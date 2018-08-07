init:
	pip3 install -r requirements.txt

run-notebook:
	docker build -t notebook -f notebook/NotebookDockerfile .
	docker run -v ${PWD}:/home/jovyan/ -p 8888:8888 notebook start-notebook.sh --NotebookApp.token=''