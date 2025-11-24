# Comunicação em tempo real com Flask.

## projeto da formação python da rocketseat.
É explorado os conceitos básicos de notificação em tempo real com protocolo websocket, além de discutir estratégias comuns para implementar a comunicação em tempo real como:

### Long Polling

Long Polling, diferente do HTTP e Websockets que são protocolos de comunicação, o Long Polling é "uma técnica baseada em HTTP". 
Como um desenvolvedor conhecido disse uma vez, protocolos na engenharia de software sempre será compreendido como "conjunto de regras", 
ou seja, HTTP não deixa de ser um conjunto de regras para a comunicação entre Cliente e Servidor.

Retomando, Long Polling diferente do Websocket quando nosso cliente faz uma requisição e nosso servidor mantém a conexão aberta caso não exista novos dados para enviar,
mas quando houver retorna a resposta, após isso a conexão entre eles é "fechada", sim, muito parecido com HTTP por isso o Long Polling é frequentemente chamado de ‘HTTP emulando tempo real’.

![0_LGDmwIjFueG1nX3U](https://github.com/user-attachments/assets/2cd9db8d-7ff3-4a77-a2d8-d0136e8fcb3f)

## WebSocket

Diversamente usado e conhecido, Websockets por sua vez possui uma comunicação bidirecional, diferente do Long Polling, 
nosso HTTP mascarado, que possui uma comunicação unidirecional. Ou seja, nosso Cliente e Servidor enviam requisições e 
respostas uns aos outros a partir do momento em que a conexão se estabelece, e enquanto essa conexão se estabelecer. Nosso famoso *handshake*(quando se estabelece conexão entre cliente e servidor).

<img width="1100" height="445" alt="image" src="https://github.com/user-attachments/assets/598968d5-3197-4bc4-be4b-3a1e37685f30" />

## Conclusão 

Esse é o resumo sobre alguns dos conteúdos vistos, texto escrito 100% por um humano e tem como total intuito de revisar e reforçar o meu entendimento sobre comunicação em tempo real e alguns conceitos. E caso tenha ajudado alguém nos seus estudos, ótimo, fico feliz em ajudar! Qualquer dúvida ou dica envie seu PR.

    Como referência eu deixo o artigo escrito por David Mosya no blog 'Medium'
    
[Medium, David Mosya](https://medium.com/@dmosyan/http-long-polling-vs-websockets-dadab8f7f26f)

https://medium.com/@dmosyan/http-long-polling-vs-websockets-dadab8f7f26f
