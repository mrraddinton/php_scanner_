## Este script foi desenvolvido para autoteste e aprendizado de Python e é apenas para fins educacionais

>> O script faz uma chamada GET para o site de destino fornecido e, em seguida, examina o cabeçalho X-Powered-By do cabeçalho de resposta para determinar a versão do PHP que foi entregue.

>> O site está utilizando uma versão antiga do PHP que contém vulnerabilidades conhecidas se a versão do PHP for 5.6 ou inferior. O destinatário do e-mail é informado sobre a vulnerabilidade em um e-mail de notificação.

>> Este script é apenas uma ilustração simples; lembre-se de que, se o servidor de e-mail do destinatário estiver bloqueando a mensagem ou se as credenciais estiverem incorretas, o envio de um e-mail usando SMTP pode não funcionar como planejado.
