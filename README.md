# FocoBot - Um Assistente de Foco para o Discord

![Cena de Comida do Studio Ghibli](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzY2ZmNpeGExaGw3bDd3c3FzeHhmeTl6MGZueXN2cXB1NDhlczJkZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6XX4V0O8a0xdS/giphy.gif)

Criei este bot em Python pra me ajudar a não procrastinar e a gerenciar meu tempo de estudo e trabalho direto no Discord, usando a famosa Técnica Pomodoro.

## O que é o FocoBot?

A ideia é ser um assistente simples e direto para gerenciamento de tempo. O bot usa comandos simples para facilitar a vida de quem está trabalhando ou estudando.

## Funcionalidades

-   `/iniciar_foco`: Começa 1 hora de foco total. Sem distrações!
-   `/pausa_curta`: Inicia uma pausa rápida de 5 minutos pra esticar as pernas.
-   `/pausa_longa`: Inicia uma pausa mais longa de 15 minutos pra tomar um café.
-   `/parar`: Cancela qualquer timer que estiver rolando.

## Como Usar

1.  Convide o bot para o seu servidor.
2.  Digite `/` em qualquer canal e os comandos já aparecem na lista.
3.  Escolha o que você quer fazer e pronto!

## Setup para Desenvolvedores

Se você quiser testar ou modificar o bot, o setup é esse:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/FocoBot-Discord.git](https://github.com/SEU_USUARIO/FocoBot-Discord.git)
    ```
2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Crie um arquivo `.env`** na pasta do projeto pra guardar seu token.
4.  Dentro do `.env`, coloque a chave do bot assim:
    ```
    TOKEN=SEU_TOKEN_SUPER_SECRETO_AQUI
    ```
5.  **Ligue o bot:**
    ```bash
    python main.py
    ```

## Licença

Este projeto é de código aberto e está licenciado sob a **[Licença MIT](LICENSE)**. Basicamente, você pode fazer o que quiser com o código, desde que mantenha os créditos.

## Contato

Quer trocar uma ideia, sugerir algo ou só se conectar? Me encontre aqui:

-   **LinkedIn:** [Gabriel Mendes](https://www.linkedin.com/in/gabriel-mendes2499/)
-   **Email:** [gabriel.mendes.rodrigues@gmail.com](mailto:gabriel.mendes.rodrigues@gmail.com)

---
*Criei essa ferramenta pra resolver uma necessidade minha e pra praticar Python com `discord.py`. Espero que seja útil pra mais alguém!*
