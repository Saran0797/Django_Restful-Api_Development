from rest_framework.authentication import TokenAuthentication as basetoken


class TokenAuthentication(basetoken):
    keyword = "bearer"
