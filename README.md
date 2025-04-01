---

# Contagem Volumétrica de Veículos

Bem-vindo ao **Contagem Volumétrica**, um framework dedicado à contagem volumétrica de veículos utilizando técnicas avançadas de visão computacional e deep learning. Nosso objetivo é facilitar a análise e monitoramento de tráfego, integrando o Label Studio para anotação e validação dos dados.

---

## 📋 Visão Geral

Este projeto foi desenvolvido para criar uma solução completa para a contagem volumétrica de veículos, combinando:
- **Detecção de objetos (YOLO)** para identificar veículos.
- **Integração com Label Studio** para gerenciamento e anotação dos dados.
- **Uso de CUDA e PyTorch** para acelerar o processamento com GPU.

---

## 🚀 Requisitos

Antes de iniciar, certifique-se de que os seguintes componentes estão instalados:

- **CUDA** e **PyTorch**  
  Consulte [PyTorch Get Started](https://pytorch.org/get-started/locally/) para as instruções de instalação e configuração de acordo com sua GPU.

- **Docker**  
  Certifique-se de ter o Docker instalado para rodar os serviços do projeto.

---

## 🛠️ Configuração do Projeto

### 1. Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
Contagem-Volumetrica/
├── src/
│   └── label-image/
│       └── ml/
│           └── yolo/         # Diretório com os scripts e modelos YOLO
├── docker-compose.yml        # Arquivo para subir os serviços com Docker
└── README.md                 # Este arquivo
```

### 2. Configuração do Label Studio

- Navegue até o diretório `src/label-image/ml/yolo`.
- Adicione as variáveis de ambiente `LABEL_STUDIO_URL` e `LABEL_STUDIO_API_KEY` no arquivo `docker-compose.yml`.
- Construa a imagem Docker:
  ```bash
  docker build -t contagem-volumetrica .
  ```

- Volte para a raiz do projeto e atualize o arquivo `docker-compose.yml` com as mesmas variáveis de ambiente.
- Inicie os serviços:
  ```bash
  docker compose up -d
  ```

---

## 🎨 Configuração do Label Studio

Após iniciar o serviço, siga estes passos:

1. **Crie um novo projeto** no Label Studio com a seguinte configuração de anotação:

   ```html
   <View>
     <Image name="image" value="$image"/>
     <RectangleLabels name="label" toName="image" model_score_threshold="0.25">
       <Label value="Car" background="blue" predicted_values="jeep,cab,limousine,truck"/>
     </RectangleLabels>
   </View>
   ```

2. **Conecte o modelo** na página de Model do projeto. Utilize a URL padrão:  
   `http://localhost:9090`

3. **Adicione as imagens ou vídeos** (dependendo das tarefas que deseja resolver) no Label Studio.

4. **Visualize as predições** dos modelos YOLO nos dados anotados através do Data Manager.

---

## 📚 Recursos Adicionais

Para mais detalhes sobre a integração do YOLO com o Label Studio, consulte:
- [Exemplo no repositório Label Studio ML Backend](https://github.com/HumanSignal/label-studio-ml-backend/tree/master/label_studio_ml/examples/yolo)

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

---

## ⚠️ Observações Finais

- Garanta que as variáveis de ambiente `LABEL_STUDIO_URL` e `LABEL_STUDIO_API_KEY` estejam configuradas corretamente.
- Certifique-se de utilizar as versões compatíveis de CUDA e PyTorch para aproveitar a aceleração por GPU.

---

Esperamos que este framework auxilie na criação de soluções robustas para análise de tráfego. Bom trabalho!
