# Aula: Git – Fundamentos e Comandos Essenciais

## Objetivo da aula

Entender o que é o Git, por que ele existe e como usar seus **principais comandos** no dia a dia de desenvolvimento. Aqui não tem GitHub, GitLab ou afins — foco total no **Git local**.

---

## O que é Git?

Git é um **sistema de controle de versão distribuído**. Em português claro: ele guarda o histórico do seu código, permite voltar no tempo, comparar mudanças e trabalhar sem medo de quebrar tudo.

Sem Git:

- Alterou algo e deu ruim? Chora.
- Duas versões do mesmo arquivo: `final_v2_agora_vai.js`

Com Git:

- Histórico organizado
- Mudanças rastreadas
- Experimentos sem pânico

---

## Conceitos-chave (entenda isso)

### Repositório

É a pasta do projeto **monitorada pelo Git**.

### Working Directory

Onde você edita os arquivos. O caos acontece aqui.

### Staging Area (Index)

Área intermediária onde você diz ao Git:

> "Essas mudanças aqui eu quero salvar. O resto ignora por enquanto."

### Commit

Uma **foto do estado do projeto** em um determinado momento.

---

## Criando um repositório

```bash
git init
```

- Cria a pasta `.git`
- A partir daqui, o Git começa a vigiar seus passos

Para conferir o estado:

```bash
git status
```

---

## Ciclo básico do Git (grave isso)

1. Edita arquivos
2. `git add`
3. `git commit`

Repete até o fim da vida

---

## git status

Mostra:

- Arquivos modificados
- Arquivos prontos para commit
- Arquivos não rastreados

```bash
git status
```

Use sem dó. É seu painel de controle.

---

## git add

Adiciona arquivos à **staging area**.

Adicionar um arquivo específico:

```bash
git add index.js
```

Adicionar tudo:

```bash
git add .
```

⚠️ `git add .` não é pecado, mas saiba o que está indo junto.

---

## git commit

Cria um commit com as mudanças adicionadas.

```bash
git commit -m "mensagem do commit"
```

Boas mensagens:

- Curta
- Clara
- Diz o que mudou, não como você se sentiu

Exemplo bom:

```bash
git commit -m "adiciona validação no formulário"
```

Exemplo ruim:

```bash
git commit -m "funciona agora"
```

---

## git log

Mostra o histórico de commits.

```bash
git log
```

Versão mais legível:

```bash
git log --oneline
```

Cada commit tem um **hash** (identificador único).

---

## git diff

Mostra diferenças entre versões.

Ver mudanças ainda não adicionadas:

```bash
git diff
```

Ver mudanças já adicionadas:

```bash
git diff --staged
```

Ideal para revisar antes de commitar.

---

## git restore (desfazer mudanças)

Descartar alterações em um arquivo:

```bash
git restore index.js
```

Remover da staging area:

```bash
git restore --staged index.js
```

⚠️ Aqui não tem Ctrl+Z milagroso. Use com consciência.

---

## git checkout (voltar no tempo)

Voltar um arquivo para o estado de um commit:

```bash
git checkout <hash> -- index.js
```

Ou voltar tudo:

```bash
git checkout <hash>
```

Isso é poderoso. E perigoso.

---

## Branches (linhas do tempo paralelas)

Branch é uma **linha independente de commits**.

Branch padrão:

- `main` ou `master`

Criar branch:

```bash
git branch nova-feature
```

Trocar de branch:

```bash
git checkout nova-feature
```

Criar e trocar de uma vez:

```bash
git checkout -b nova-feature
```

---

## git merge

Une uma branch à outra.

```bash
git merge nova-feature
```

Se tudo der certo: alegria.

Se der conflito: resolve no código, depois commit.

---

## Conflitos (bem-vindo ao mundo real)

Acontecem quando:

- Duas mudanças no mesmo trecho

O Git marca assim:

```text
<<<<<<< HEAD
código atual
=======
código da outra branch
>>>>>>> nova-feature
```

Você decide, limpa e commita.

---

## git stash (guardar bagunça temporária)

Salvar mudanças sem commitar:

```bash
git stash
```

Voltar depois:

```bash
git stash pop
```

Útil quando você começou algo no lugar errado.

---

## Arquivo .gitignore

Define o que o Git **não deve rastrear**.

Exemplo:

```text
node_modules/
.env
dist/
```

Se não ignorar, uma hora você vai se arrepender.

---

## Resumo mental

- `git init` → começa tudo
- `git status` → onde estou?
- `git add` → prepara
- `git commit` → salva
- `git log` → histórico
- `git diff` → diferenças
- `git branch / checkout` → linhas paralelas
- `git merge` → juntar tudo

Git não é difícil. Só é literal.

