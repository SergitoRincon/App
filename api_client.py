"""
Cliente HTTP — MotoApp Flet → FastAPI backend
Backend gratuito en Render.com + PostgreSQL en Supabase
"""
import json
import threading
import time
import httpx
from pathlib import Path

# ── URL del backend ────────────────────────────────────────────────
API_URL = "https://motoapp-xjlt.onrender.com"   # producción (Render gratis)
# API_URL = "http://localhost:8000"                 # desarrollo local

TOKEN_FILE = Path.home() / ".motoapp_session.json"


# ── Keep-alive: evita que Render duerma el servidor ───────────────
def _keep_alive():
    """Ping cada 14 min para mantener activo el servidor gratuito."""
    while True:
        time.sleep(14 * 60)
        try:
            httpx.get(f"{API_URL}/health", timeout=5)
        except Exception:
            pass

threading.Thread(target=_keep_alive, daemon=True).start()


# ══════════════════════════════════════════════════════════════════
# SESIÓN LOCAL (guarda tokens en disco)
# ══════════════════════════════════════════════════════════════════

def _guardar_sesion(data: dict):
    TOKEN_FILE.write_text(json.dumps(data))

def _cargar_sesion() -> dict:
    if TOKEN_FILE.exists():
        try:
            return json.loads(TOKEN_FILE.read_text())
        except Exception:
            pass
    return {}

def _borrar_sesion():
    if TOKEN_FILE.exists():
        TOKEN_FILE.unlink()

def get_access_token() -> str | None:
    return _cargar_sesion().get("access_token")

def get_usuario_local() -> dict:
    return _cargar_sesion().get("usuario", {})

def sesion_activa() -> bool:
    return bool(get_access_token())

def cerrar_sesion_local():
    _borrar_sesion()


# ══════════════════════════════════════════════════════════════════
# HTTP BASE
# ══════════════════════════════════════════════════════════════════

def _headers() -> dict:
    token = get_access_token()
    return {"Authorization": f"Bearer {token}"} if token else {}

def _get(endpoint: str) -> dict:
    try:
        r = httpx.get(f"{API_URL}{endpoint}", headers=_headers(), timeout=30)
        r.raise_for_status()
        return {"ok": True, "data": r.json()}
    except httpx.HTTPStatusError as e:
        try:
            detail = e.response.json().get("detail", "Error del servidor")
        except Exception:
            detail = f"Error {e.response.status_code}"
        return {"ok": False, "error": detail}
    except httpx.TimeoutException:
        return {"ok": False, "error": "El servidor tardó en responder. Intenta de nuevo."}
    except Exception:
        return {"ok": False, "error": "Sin conexión a internet"}

def _post(endpoint: str, body: dict) -> dict:
    try:
        r = httpx.post(f"{API_URL}{endpoint}", json=body, headers=_headers(), timeout=30)
        r.raise_for_status()
        return {"ok": True, "data": r.json()}
    except httpx.HTTPStatusError as e:
        try:
            detail = e.response.json().get("detail", "Error del servidor")
        except Exception:
            detail = f"Error {e.response.status_code}"
        return {"ok": False, "error": detail}
    except httpx.TimeoutException:
        return {"ok": False, "error": "El servidor tardó en responder. Intenta de nuevo."}
    except Exception:
        return {"ok": False, "error": "Sin conexión a internet"}

def _patch(endpoint: str, body: dict) -> dict:
    try:
        r = httpx.patch(f"{API_URL}{endpoint}", json=body, headers=_headers(), timeout=30)
        r.raise_for_status()
        return {"ok": True, "data": r.json()}
    except httpx.HTTPStatusError as e:
        try:
            detail = e.response.json().get("detail", "Error del servidor")
        except Exception:
            detail = f"Error {e.response.status_code}"
        return {"ok": False, "error": detail}
    except Exception:
        return {"ok": False, "error": "Sin conexión a internet"}

def _delete(endpoint: str) -> dict:
    try:
        r = httpx.delete(f"{API_URL}{endpoint}", headers=_headers(), timeout=30)
        r.raise_for_status()
        return {"ok": True, "data": {}}
    except httpx.HTTPStatusError as e:
        try:
            detail = e.response.json().get("detail", "Error del servidor")
        except Exception:
            detail = f"Error {e.response.status_code}"
        return {"ok": False, "error": detail}
    except Exception:
        return {"ok": False, "error": "Sin conexión a internet"}


# ══════════════════════════════════════════════════════════════════
# AUTH
# ══════════════════════════════════════════════════════════════════

def registrar(nombre: str, email: str, password: str) -> dict:
    res = _post("/auth/registro", {"nombre": nombre, "email": email, "password": password})
    if res["ok"]:
        sesion = res["data"]
        u = _get("/usuarios/me")
        if u["ok"]:
            sesion["usuario"] = u["data"]
        _guardar_sesion(sesion)
    return res

def login(email: str, password: str) -> dict:
    res = _post("/auth/login", {"email": email, "password": password})
    if res["ok"]:
        sesion = res["data"]
        u = _get("/usuarios/me")
        if u["ok"]:
            sesion["usuario"] = u["data"]
        _guardar_sesion(sesion)
    return res


# ══════════════════════════════════════════════════════════════════
# USUARIO
# ══════════════════════════════════════════════════════════════════

def get_perfil() -> dict:
    return _get("/usuarios/me")

def actualizar_perfil(datos: dict) -> dict:
    return _patch("/usuarios/me/perfil", datos)


def get_configuracion() -> dict:
    return _get("/usuarios/me/configuracion")

def actualizar_configuracion(datos: dict) -> dict:
    return _patch("/usuarios/me/configuracion", datos)


# ══════════════════════════════════════════════════════════════════
# VEHÍCULOS
# ══════════════════════════════════════════════════════════════════

def get_vehiculos() -> dict:
    return _get("/vehiculos/")

def crear_vehiculo(placa: str, marca: str, modelo: str, anio: int) -> dict:
    return _post("/vehiculos/", {"placa": placa, "marca": marca,
                                  "modelo": modelo, "anio": anio})

def eliminar_vehiculo(vehiculo_id: int) -> dict:
    return _delete(f"/vehiculos/{vehiculo_id}")


# ══════════════════════════════════════════════════════════════════
# MANTENIMIENTO
# ══════════════════════════════════════════════════════════════════

def get_mantenimiento(vehiculo_id: int) -> dict:
    return _get(f"/vehiculos/{vehiculo_id}/mantenimiento/")

def guardar_modulo(vehiculo_id: int, modulo: str, datos: dict) -> dict:
    return _patch(f"/vehiculos/{vehiculo_id}/mantenimiento/{modulo}", {"datos": datos})


# ══════════════════════════════════════════════════════════════════
# HISTORIAL
# ══════════════════════════════════════════════════════════════════

def get_historial(vehiculo_id: int, modulo: str | None = None) -> dict:
    ep = f"/vehiculos/{vehiculo_id}/mantenimiento/historial/"
    if modulo:
        ep += f"?modulo={modulo}"
    return _get(ep)

def crear_evento(vehiculo_id: int, modulo: str, titulo: str,
                 descripcion: str = "", kilometraje: float | None = None) -> dict:
    body = {"modulo": modulo, "titulo": titulo, "descripcion": descripcion}
    if kilometraje is not None:
        body["kilometraje"] = kilometraje
    return _post(f"/vehiculos/{vehiculo_id}/mantenimiento/historial/", body)