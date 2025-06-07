# src/handlers/relatorio_handler.py
"""Relatório (Reports) Lambda handlers."""

import os
from datetime import datetime
import structlog
from sqlalchemy.ext.asyncio import AsyncSession

from utils.lambda_decorators import (
    lambda_handler,
    with_database,
    require_auth,
    success_response,
    LambdaException,
)

logger = structlog.get_logger()


# === REPORTS HANDLERS ===

@lambda_handler
@with_database
@require_auth(permissions=["relatorios:read"])
async def get_relatorios_handler(
    event,
    context,
    body,
    path_params,
    query_params,
    db: AsyncSession,
    user_info: dict,
):
    """
    Handler protegido que retorna relatórios.
    user_info já contém userId, email e lista de permissoes.
    """
    try:
        # Exemplo: registrar acesso no log
        logger.info(
            "Gerando relatório",
            user_id=user_info["userId"],
            permissoes=user_info["permissoes"],
        )

        # TODO: substituir pelo seu código de geração de relatório
        report_data = {"message": "Reports endpoint - TODO"}

        return success_response(report_data)

    except Exception as e:
        logger.error("Erro ao gerar relatório", error=str(e))
        raise LambdaException(500, "Error generating report")


# === UTILITY HANDLERS ===

@lambda_handler
async def health_check_handler(event, context, body, path_params, query_params):
    """Health check endpoint."""
    payload = {
        "status": "healthy",
        "service": "relatorio-service",
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "unknown"),
        "timestamp": datetime.utcnow().isoformat(),
    }
    return success_response(payload)
