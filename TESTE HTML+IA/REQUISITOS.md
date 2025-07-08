instalar o ollama na web: https://ollama.com/download/windows



Instale as dependências do Python:



&nbsp;	pip install flask requests



Inicie o Ollama e baixe o modelo Llama 3 (powershell do pc):

&nbsp;  

&nbsp; 	ollama pull llama3:8b

&nbsp; 	ollama serve



Rode o backend Flask (powershell do cursor/IDE utilizada):



&nbsp;	python app.py



Abra o http://localhost:5000/ que é onde o flask está rodando









para parar de rodar só ir no terminal e usar cntrl + c

