import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

# Load .env file
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Configuration for SAKIPRO."""
    # AI Provider
    ai_provider: str = Field(default="anthropic", alias="SAKIPRO_AI_PROVIDER")
    
    # API Keys
    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")
    gemini_api_key: str | None = Field(default=None, alias="GEMINI_API_KEY")
    anthropic_api_key: str | None = Field(default=None, alias="ANTHROPIC_API_KEY")
    xai_api_key: str | None = Field(default=None, alias="XAI_API_KEY")
    deepseek_api_key: str | None = Field(default=None, alias="DEEPSEEK_API_KEY")
    groq_api_key: str | None = Field(default=None, alias="GROQ_API_KEY")
    
    # Models
    default_model: str = Field(default="claude-sonnet-4-20250514", alias="SAKIPRO_DEFAULT_MODEL")
    light_model: str = Field(default="claude-sonnet-4-20250514", alias="SAKIPRO_LIGHT_MODEL")
    reasoning_model: str = Field(default="claude-sonnet-4-20250514", alias="SAKIPRO_REASONING_MODEL")
    
    # Global Context Profile
    pemda_name: str = Field(default="[Nama Pemda Belum Diatur]", alias="SAKIPRO_PEMDA_NAME")
    opd_name: str = Field(default="[Nama OPD Belum Diatur]", alias="SAKIPRO_OPD_NAME")
    eval_year: str = Field(default="[Tahun Belum Diatur]", alias="SAKIPRO_EVAL_YEAR")
    rpjmd_period: str = Field(default="[Periode Belum Diatur]", alias="SAKIPRO_RPJMD_PERIOD")
    
    # App Settings
    privacy_mode: str = Field(default="standard", alias="SAKIPRO_PRIVACY_MODE")
    output_dir: str = Field(default="outputs", alias="SAKIPRO_OUTPUT_DIR")
    
    # Local paths
    db_path: str = str(Path.home() / ".sakipro" / "sakipro.db")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()

def get_global_context_prompt() -> str:
    """Mengembalikan string konteks pemda untuk di-inject ke dalam system_prompt."""
    return (
        "--- KONTEKS EVALUASI LOKAL ---\n"
        f"1. Nama Pemda / Institusi: {settings.pemda_name}\n"
        f"2. Instansi Fokus (OPD)  : {settings.opd_name}\n"
        f"3. Tahun Evaluasi        : {settings.eval_year}\n"
        f"4. Periode RPJMD         : {settings.rpjmd_period}\n"
        "Gunakan informasi di atas sebagai acuan mutlak (absolute fact) jika Anda memerlukan "
        "nama entitas atau batasan tahun dalam memberikan telaah dokumen atau rekomendasi.\n"
        "------------------------------\n"
    )
