# 🤖 FocoBot - Meu Assistente de Foco para o Discord

![Garota Lofi estudando](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2h1cTZrZ2p0c29oajNncjV2cnY5a3R2c2J1Z2N6a3Nhd2E4d2l6eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/M9gbBd9hFTsaY/giphy.gif)

Criei este bot em Python pra me ajudar a não procrastinar e a gerenciar meu tempo de estudo e trabalho direto no Discord, usando a famosa Técnica Pomodoro.

## 🚀 O que ele faz?

A ideia é ser simples e direto. O bot usa comandos de barra pra facilitar a vida:

-   `/iniciar_foco`: Começa 1 hora de foco total. Sem distrações!
-   `/pausa_curta`: Inicia uma pausa rápida de 5 minutos pra esticar as pernas.
-   `/pausa_longa`: Inicia uma pausa mais longa de 15 minutos pra tomar um café.
-   `/parar`: Cancela qualquer timer que estiver rolando.

## 🛠️ Como usar

1.  É só convidar o bot pro seu servidor.
2.  Digita `/` em qualquer canal e os comandos já aparecem na lista.
3.  Escolhe o que você quer fazer e pronto!

## 🔧 Quer rodar na sua máquina?

Se você quiser testar ou modificar o bot, o setup é esse:

1.  **Clona o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/FocoBot-Discord.git](https://github.com/SEU_USUARIO/FocoBot-Discord.git)
    ```
2.  **Instala o que precisa:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Cria um arquivo `.env`** na pasta do projeto pra guardar seu token.
4.  Dentro do `.env`, coloca a chave do bot assim:
    ```
    TOKEN=SEU_TOKEN_SUPER_SECRETO_AQUI
    ```
5.  **Liga o bot:**
    ```bash
    python main.py
    ```

## 📜 Licença

Este projeto é de código aberto e está licenciado sob a **Licença MIT**. Basicamente, você pode fazer o que quiser com o código, desde que mantenha os créditos.

---
*Criei essa ferramenta pra resolver uma necessidade minha e pra praticar Python com `discord.py`. Espero que seja útil pra mais alguém!*
