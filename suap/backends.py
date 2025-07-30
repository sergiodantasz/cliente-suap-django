from social_core.backends.oauth import BaseOAuth2

from app.models import Usuario


class SuapOAuth2(BaseOAuth2):
    name = "suap"
    AUTHORIZATION_URL = "https://suap.ifrn.edu.br/o/authorize/"
    ACCESS_TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"
    ACCESS_TOKEN_METHOD = "POST"
    ID_KEY = "identificacao"
    RESPONSE_TYPE = "code"
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    USER_DATA_URL = "https://suap.ifrn.edu.br/api/rh/eu/"
    EXTRA_USER_DATA_URL = "https://suap.ifrn.edu.br/api/rh/meus-dados/"
    DEFAULT_SCOPE = ["identificacao", "email", "documentos_pessoais"]

    def user_data(self, access_token, *args, **kwargs):
        method = "GET"
        data = {"scope": " ".join(self.DEFAULT_SCOPE)}
        headers = {"Authorization": f"Bearer {access_token}"}
        response = self.request(
            url=self.USER_DATA_URL,
            method=method,
            data=data,
            headers=headers,
        ).json()
        extra_response = self.request(
            url=self.EXTRA_USER_DATA_URL,
            method=method,
            headers=headers,
        ).json()
        curso = extra_response.get("vinculo").get("curso")
        response["curso"] = curso
        return response

    def get_user_details(self, response):
        user_details = {
            "matricula": response.get("identificacao"),
            "nome_completo": (
                response.get("nome_social") or response.get("nome_registro")
            ),
            "cpf": response.get("cpf"),
            "campus": response.get("campus"),
            "curso": response.get("curso"),
            "email_pessoal": response.get("email_secundario"),
            "email_escolar": response.get("email_google_classroom"),
            "email_academico": response.get("email_academico"),
            "tipo_vinculo": response.get("tipo_usuario"),
            "sexo": response.get("sexo"),
            "data_nascimento": response.get("data_de_nascimento"),
            "url_foto": response.get("foto"),
        }
        if not Usuario.objects.filter(pk=user_details["matricula"]).exists():
            Usuario.objects.create(**user_details)
        primeiro_nome, *_, ultimo_nome = user_details["nome_completo"].split()
        return {
            "username": user_details["matricula"],
            "email": user_details["email_pessoal"],
            "fullname": user_details["nome_completo"],
            "first_name": primeiro_nome,
            "last_name": ultimo_nome,
        }
