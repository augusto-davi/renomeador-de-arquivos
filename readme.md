# 📂 Renomeador de Arquivos em Massa

Um script Python para renomear arquivos em massa dentro de um diretório, permitindo organizar grandes quantidades de arquivos de forma rápida e eficiente.

## 🚀 Funcionalidades

- Renomeia arquivos em um diretório com um padrão definido.
- Permite filtrar arquivos por extensão.
- Mantém a ordem alfabética dos arquivos antes de renomeá-los.
- Compatível com Windows, Linux e macOS.

## 🔧 Instalação

1. Clone este repositório ou baixe o código-fonte:

```sh
git clone https://github.com/augusto-davi/renomeador-de-arquivos.git
cd renomeador-de-arquivos
```

2. Certifique-se de que o Python está instalado corretamente.

## 🎯 Como Usar

1. Coloque os arquivos que deseja renomear dentro de um diretório específico.
2. Execute o script informando o diretório e o novo padrão de nomeação:

```sh
python renomeador.py <diretorio> <novo_nome> [extensao]
```

### 📌 Parâmetros

- `<diretorio>`: Caminho da pasta onde estão os arquivos.
- `<novo_nome>`: Prefixo para os novos nomes dos arquivos.
- `[extensao]` (opcional): Se informado, apenas arquivos com essa extensão serão renomeados.
- `[numero_inicial]` (opcional): O nome dos arquivos será ordenado a partir do número informado.

### 📌 Exemplo de Uso

Renomear todos os arquivos de um diretório para "Imagem\_001.jpg", "Imagem\_002.jpg", etc.:

```sh
python renomeador.py ./fotos Imagem jpg
```

### 📂 Antes:

```
fotos/
├── DSC001.jpg
├── IMG_20220101.jpg
├── foto03.jpg
```

### 📂 Depois:

```
fotos/
├── Imagem_001.jpg
├── Imagem_002.jpg
├── Imagem_003.jpg
```

## ⚠️ Cuidados

- O script **substitui os nomes originais**, então faça backup se necessário.
- Caso necessário, certifique-se de que a ordem dos arquivos está correta antes de renomear.
