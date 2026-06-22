import smtplib
from email.message import EmailMessage
from pathlib import Path
from typing import Type

from crewai.tools import BaseTool
from dotenv import dotenv_values
from pydantic import BaseModel, Field


ENV_CONFIG_PATH = Path(__file__).resolve().parents[3] / "env.config"


def _read_smtp_settings() -> dict[str, str]:
    env_values = {
        key: value
        for key, value in dotenv_values(ENV_CONFIG_PATH).items()
        if value is not None
    }

    return {
        "SMTP_HOST": str(env_values.get("SMTP_HOST", "")).strip(),
        "SMTP_PORT": str(env_values.get("SMTP_PORT", "")).strip(),
        "SMTP_USERNAME": str(env_values.get("SMTP_USERNAME", "")).strip(),
        "SMTP_PASSWORD": str(env_values.get("SMTP_PASSWORD", "")).strip(),
        "SMTP_FROM_EMAIL": str(env_values.get("SMTP_FROM_EMAIL", "")).strip(),
        "SMTP_USE_TLS": str(env_values.get("SMTP_USE_TLS", "true")).strip(),
    }

class EmailSendingToolInput(BaseModel):
    recipient_email: str = Field(..., description="Recipient email address")
    subject: str = Field(..., description="Email subject")
    body: str = Field(..., description="Plain text email body")

class EmailSendingTool(BaseTool):
    name: str = "email_sending_tool"
    description: str = "Send an email using SMTP credentials from env.config."
    args_schema: Type[BaseModel] = EmailSendingToolInput

    # Values are read from env.config, so make sure to set them there before using this tool.
    def _run(self, recipient_email: str, subject: str, body: str) -> str:
        smtp_settings = _read_smtp_settings()

        smtp_host = smtp_settings["SMTP_HOST"]
        smtp_port_raw = smtp_settings["SMTP_PORT"]
        smtp_username = smtp_settings["SMTP_USERNAME"]
        smtp_password = smtp_settings["SMTP_PASSWORD"]
        smtp_from_email = smtp_settings["SMTP_FROM_EMAIL"]
        smtp_use_tls = smtp_settings["SMTP_USE_TLS"].lower() in ("1", "true", "yes")

        missing = [
            name for name, value in {
                "SMTP_HOST": smtp_host,
                "SMTP_PORT": smtp_port_raw,
                "SMTP_USERNAME": smtp_username,
                "SMTP_PASSWORD": smtp_password,
                "SMTP_FROM_EMAIL": smtp_from_email,
            }.items() if not value
        ]
        if missing:
            raise ValueError(f"Missing SMTP settings: {', '.join(missing)}")

        smtp_port = int(smtp_port_raw)

        msg = EmailMessage()
        msg["From"] = smtp_from_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.set_content(body)

        server = None
        try:
            server = smtplib.SMTP(smtp_host, smtp_port)
            if smtp_use_tls:
                server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
            return f"Email sent successfully to {recipient_email}"
        finally:
            if server is not None:
                server.quit()