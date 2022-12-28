"""
ASGI config for backendsCliente project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "apiCliente"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backendsCliente.settings.local")

django_application = get_asgi_application()

from backendsCliente.websocket import websocket_apllication

async def application(scope,receive,send):
    if scope["type"] == "http":
        await django_application(scope, receive, send)
    elif scope["type"] == "websocket":
        await websocket_apllication(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")