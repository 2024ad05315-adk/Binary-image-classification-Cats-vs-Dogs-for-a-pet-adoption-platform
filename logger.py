"""Structured logging configuration"""

import logging
import json
from datetime import datetime

def get_logger(name):
    """Get configured logger"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(name)

def log_prediction(logger, request_id, label, probabilities, latency_ms):
    """Log prediction with structured format"""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "request_id": request_id,
        "predicted_label": label,
        "probabilities": probabilities,
        "latency_ms": latency_ms,
    }
    logger.info(json.dumps(log_entry))
