# Chatbot Básico con OpenAI

Este proyecto implementa un chatbot básico utilizando la API de OpenAI. El chatbot puede interactuar con los usuarios utilizando reconocimiento de voz para recibir preguntas y generando respuestas utilizando el modelo GPT-3.5 de OpenAI. Además, utiliza síntesis de voz para comunicar las respuestas al usuario.

Instalación

Clona el repositorio:

bash
Copiar código
git clone https://github.com/tu_usuario/chatbot-basico.git
cd chatbot-basico
Instala las dependencias:

Asegúrate de tener Python 3.x instalado. Luego, instala las bibliotecas necesarias usando pip:

bash
Copiar código
pip install -r requirements.txt
Esto instalará las bibliotecas requeridas como openai, speech_recognition, gtts y pygame.

Configuración

Antes de ejecutar el chatbot, asegúrate de configurar tu clave API de OpenAI en el archivo chatbot_basico.py:

python
Copiar código
openai.api_key = "tu_clave_api_aqui"
Reemplaza "tu_clave_api_aqui" con tu clave API válida. Puedes obtener tu clave API desde https://platform.openai.com/account/api-keys.

Uso

Ejecuta el chatbot:

bash
Copiar código
python chatbot_basico.py
Interactúa con el chatbot:

Permite el acceso al micrófono cuando se solicite.
Habla con el chatbot y espera las respuestas generadas por OpenAI.
Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el chatbot o corregir algún problema, no dudes en enviar un pull request.
