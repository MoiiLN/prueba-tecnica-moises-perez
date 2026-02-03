orders = [
    {"id": 1, "total": 120, "paid": True},
    {"id": 2, "total": 80, "paid": False},
    {"id": 3, "total": 200, "paid": True},
    {"id": 4, "total": 50, "paid": False},
]

def orders_info(orders):
    paid_total = 0
    unpaid_ids = []
    for v in orders.values():
        if v:
            for k in orders.keys():
                if k == "id":
                    unpaid_ids.append(k.values())
                    return unpaid_ids
        else:
            for k in orders.keys():
                if k == "total":
                    paid_total += k.values()
                    return paid_total
# Mi solución no es correcta ni es eficiente siquiera, soy consciente de ello.

user = {
    "email": "test@example.com",
    "age": 17
}

def validate_user(user):
    REGEX = []
    for k, v in user.items():
        if k == "email":
            v.findall(r'[@]')
        else:
            raise AssertionError("El email debe contener '@'")
        if k == "age":
            if not v >= 18:
                raise AssertionError("Debes de ser mayor de edad.")

# Este ejercicio valida un correo y una edad, se debe retornar un error si es que ciertos "requisitos" no son cumplidos.



                
            
