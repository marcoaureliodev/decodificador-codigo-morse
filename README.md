#started
To run the server

    pip install -r "requirements.txt"
    python main.py

Pensando de forma simplificada ao escalar a aplicação, penso que a mesma não teria problemas
no momento de processamendo de CPU, nem análise crítica de Gráficos ou algo do tipo.

Acho que a mesma apresentaria um desafio em questão de I/O bound, pensando no número de requisições
que poderiam exigir da ferramenta.

Dessa forma creio que utilizar REDIS, ASYNC do próprio python e o serviço LAMBDA.