# Assistente de Comandos por Voz 

Este projeto é um assistente de comandos por voz desenvolvido em Python que utiliza a biblioteca speech_recognition para reconhecer comandos de voz, pyttsx3 para conversão de texto em fala, pywhatkit para interações com YouTube e Google, e os para executar comandos do sistema. O assistente é capaz de abrir vídeos no YouTube, abrir o Microsoft Excel e realizar pesquisas no Google.




## Funcionalidades

- Reconhecimento de voz: Escuta comandos dados pelo    usuário através do microfone.
- Abertura de vídeos no YouTube: Reproduz vídeos no YouTube com base no comando do usuário.
- Abertura do Microsoft Excel: Executa o Microsoft Excel.
- Pesquisa no Google: Realiza pesquisas no Google com base no comando do usuário.


## Pré-Requisitos
Antes de executar o projeto, você precisa instalar as seguintes bibliotecas Python:

- speech_recognition
- pyttsx3
- pywhatkit

Você pode instalar estas bibliotecas usando o pip:

```bash
pip install SpeechRecognition pyttsx3 pywhatkit
```

Além disso, o projeto requer o Microsoft Excel instalado no seu sistema para abrir o aplicativo.


## Instalação

1. Clone o repositório para o seu ambiente local

```bash
git clone https://github.com/JoaoVitor0077/Projeto-de-assistente-virtual.git
cd Projeto-de-assistente-virtual
```

2. Instale as dependências necessárias

```bash
pip install SpeechRecognition pyttsx3 pywhatkit
```


## Uso

1. Execute o script assistente.py:

```bash
python assistente.py
```

2. Fale os seguintes comandos para interagir com o assistente:

- Para abrir um vídeo no YouTube: Diga abra no YouTube <nome do vídeo>.
- Para abrir o Microsoft Excel: Diga abrir Excel.
- Para realizar uma pesquisa no Google: Diga pesquisar <termo de pesquisa>.



## Problemas conhecidos

- A precisão do reconhecimento de voz pode variar dependendo da qualidade do microfone e do ambiente.
- O comando de abrir o Excel pode não funcionar se o caminho para o executável não estiver configurado corretamente no seu sistema.

