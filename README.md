# Automa-es
Crocofile 🐊

Automação em Python que responde conversas não lidas no WhatsApp Web com uma mensagem que você define. Tem uma janela simples com os botões Start, Confirm e Stop, e pode ser empacotada em um .exe para Windows que já leva o navegador (Chromium) dentro.

O nome é um trocadilho com Dockerfile: um crocodilo carregando as caixas de mensagem.

⚠️ Aviso importante

Automatizar o WhatsApp Web vai contra os termos de uso do WhatsApp, e contas que enviam mensagens automáticas podem ser bloqueadas. Este projeto é de uso pessoal e educacional. Use por sua conta e risco, e não use para envio em massa ou spam.

O que ele faz:
Primeiro será aberta uma tela.
A parte superior terá um campo de texto.
Que deve ser preenchido antes do start.
Com três botões, confirm, start e stop.
Start abre o Chromium no WhatsApp Web.
Confirm, começa a automação.
E stop à para.
Você faz o login (QR code) e clica em Confirm.
O programa passa a monitorar a aba Não lidas.
Quando há uma conversa não lida, ele abre a primeira, envia a mensagem, fecha a conversa e volta para Tudo.
