# src/handlers/relatorio_handler.py
"""Relatório (Reports) Lambda handlers."""

import structlog
from sqlalchemy.ext.asyncio import AsyncSession

from utils.lambda_decorators import (
    lambda_handler, with_auth, require_permission,
    success_response, LambdaException, with_database
)

# Imports necessários
import os
from datetime import datetime

logger = structlog.get_logger()

# === REPORTS HANDLERS ===

@lambda_handler
@with_auth
@require_permission("relatorios:read")
async def get_relatorios_handler(
    event, context, body, path_params, query_params,
    current_user, db: AsyncSession
):
    return {"message": "Reports endpoint - TODO"}


# === UTILITY HANDLERS ===

@lambda_handler
async def health_check_handler(event, context, body, path_params, query_params):
    """Health check endpoint."""
    return success_response({
        "status": "healthy",
        "service": "relatorio-service",
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "unknown"),
        "timestamp": datetime.utcnow().isoformat()
    })