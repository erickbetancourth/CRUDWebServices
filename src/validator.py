import re


class Validator:

    @staticmethod
    def validate_id(id):
        """
        Valida un número de documento de identidad.
        Debe contener entre 6 y 10 dígitos.
        """
        if not id:
            return False

        id = str(id).strip()

        pattern = r'^\d{6,10}$'

        return bool(re.fullmatch(pattern, id))


    @staticmethod
    def validate_name(name):
        """
        Valida nombres y apellidos.
        Permite letras, espacios, tildes y ñ.
        """
        if not name:
            return False

        name = str(name).strip()

        pattern = r'^[A-Za-zÁÉÍÓÚáéíóúÜüÑñ]+(?:[ -][A-Za-zÁÉÍÓÚáéíóúÜüÑñ]+)*$'

        return bool(re.fullmatch(pattern, name))


    @staticmethod
    def validate_email(email):
        """
        Valida una dirección de correo electrónico.
        """
        if not email:
            return False

        email = str(email).strip()

        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        return bool(re.fullmatch(pattern, email))


    @staticmethod
    def validate_phone(phone):
        """
        Valida un número celular colombiano.
        Debe comenzar por 3 y tener exactamente 10 dígitos.
        """
        if not phone:
            return False

        phone = str(phone).strip()

        pattern = r'^3\d{9}$'

        return bool(re.fullmatch(pattern, phone))