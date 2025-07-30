# Cliente SUAP Django

![Django 5](https://img.shields.io/badge/Django-5-darkgreen)
![Python 3.13](https://img.shields.io/badge/Python-3.13-blue)

**Última atualização:** <!--LAST_UPDATED-->

## Introdução

Este repositório foi criado com o intuito de facilitar a integração da API do SUAP com o framework Django, tendo em vista a escassez de recursos na internet que auxiliem a sua utilização, seja por parte de alunos e servidores do IFRN, seja pelo público geral de programadores. Sabendo disso, esse repositório serve como base para que outras pessoas interessadas em consumir a API via Django o possam fazer sem maiores dificuldades.

Ressalto que a criação desse projeto tem como um dos pilares a iniciativa *Open Source* (Código Aberto), cujo objetivo é permitir o desenvolvimento colaborativo do software, de modo que qualquer pessoa possa promover a qualidade técnica do código e, consequentemente, difundir a aplicação.

## Sobre

O Cliente SUAP Django implementa a integração com o SUAP/IFRN, tendo 2 principais funcionalidades:

- Logar com o SUAP via protocolo de autenticação OAuth2;
- Consumir a API via OAuth2 e obter recursos em nome do usuário.

## Utilização

### Criação da Aplicação no SUAP

Para que seja possível integrar a API ao Django, você deve possuir acesso ativo ao SUAP, para que seja possível criar a aplicação.

Acesse <https://suap.ifrn.edu.br/admin/api/aplicacaooauth2/> e crie a apliação com as seguintes informações:

| Campo                    | Valor                                  |
|--------------------------|----------------------------------------|
| Name                     | <Nome da sua aplicação>                |
| Authorization Grant Type | Authorization Code                     |
| Redirect URIs            | <http://127.0.0.1:8000/complete/suap/> |
| Client Type              | Confidential                           |
| Algorithm                | No OIDC Support                        |
| Ativo                    | :white_check_mark:                     |

Em **Redirect URIs**, você também pode adicionar o endereço do servidor externo, caso ele esteja hospedado na nuvem. No valor definido acima, o servidor está rodando localmente (localhost).

Lembre-se de anotar as chaves **Client ID** e **Client Secret** antes de salvar a aplicação, pois esta última só pode ser visualizada no ato de criação.

### Instalação e Configuração

Clone o repositório para a máquina, crie um ambiente virtual e instale as dependências (siga os passos de acordo com o seu sistema operacional):

> Antes de executar o código, tenha certeza de que você tem o Python e as suas dependências instalados no sistema, bem como o Git.

<details>
<summary><b>Linux</b></summary><br>

```bash
git clone https://github.com/sergiodantasz/cliente-suap-django.git
cd cliente-suap-django
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

</details><br>

<details>
<summary><b>Windows</b></summary><br>

```powershell
git clone https://github.com/sergiodantasz/cliente-suap-django.git
cd cliente-suap-django
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

</details><br>

Duplique o arquivo `.env.example`, renomeie a cópia para `.env` e configure corretamente as variáveis de ambiente no arquivo.

Os valores das variáveis `SOCIAL_AUTH_SUAP_KEY` e `SOCIAL_AUTH_SUAP_SECRET` são disponibilizados ao criar a aplicação no SUAP.

Feito isso, aplique as migrações e colete os arquivos estáticos.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

Finalmente, inicie a aplicação.

```bash
python manage.py runserver
```

Abra o navegador em <http://127.0.0.1:8000/login/> e você poderá testar o Cliente SUAP Django.

### Exemplo

A aplicação `app` foi criada como modelo base e possui três URLs:

- **Login:** <http://127.0.0.1:8000/login/>;
- **Logout:** <http://127.0.0.1:8000/logout/>;
- **Perfil:** <http://127.0.0.1:8000/accounts/profile/>.

Ao fazer o login, o usuário será redirecionado para o perfil, onde todos os dados recebidos da API são exibidos. Quando o logout é realizado, a autenticação do usuário é removida e ele é redirecionado para a página de login.

Observe a estruturação desse exemplo e replique no seu projeto de forma que ele se adapte à sua configuração de maneira adequada.

## Links Úteis

Abaixo, encontram-se alguns links que serviram como base para a criação desse projeto e que podem ajudar durante a utilização, ou até mesmo para sanar dúvidas.

- Documentação oficial da API do SUAP: <https://suap.ifrn.edu.br/api/docs/>;
- Repositório oficial do cliente OAuth2 do SUAP/IFRN para o Django: <https://github.com/ifrn-oficial/cliente_suap_django>;
- Tutorial de integração da API do SUAP com o Django do Prof. Clayton Maciel: <https://youtu.be/HwR3ELuzxjY?si=jr2gqbKQv5I63Fkp>;
- Tutorial de integração da API do SUAP com o JavaScript do Prof. Clayton Maciel: <https://youtu.be/Fdot8Bu2qAE?si=wZZHd-WMH17Nj4Iy>.

## Stack

Para esse projeto, utilizei a seguinte stack:

- Python como linguagem de programação principal;
- Django como framework web;
- HTML para criação dos templates;
- JavaScript para criação do script de logout;
- Social Auth App Django para integração OAuth2 com o SUAP;
- Django Environ para carregamento das variáveis de ambiente;
- Ruff e Djlint para formatação dos arquivos Python e HTML, respectivamente;
- Poetry para gerenciamento de dependências.

Ressalto que o Ruff, o Djlint e o Poetry não são estritamente necessários para que se utilize esse cliente, são apenas ferramentes que auxiliam no desenvolvimento e na gestão do código.

## Licença

Este repositório está protegido sob a [MIT License](./LICENSE).
