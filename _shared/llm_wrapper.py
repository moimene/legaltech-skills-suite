"""
LLM Wrapper - Abstracción para inferencia LLM local en TEE.

Soporta: Ollama, llama.cpp, vLLM
Sin conexión a APIs externas.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from pathlib import Path
import json


@dataclass
class LLMResponse:
    """Respuesta del modelo."""
    text: str
    tokens_used: int
    model: str
    finish_reason: str


class BaseLLM(ABC):
    """Clase base para wrappers de LLM."""
    
    @abstractmethod
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2,
        max_tokens: int = 2048
    ) -> LLMResponse:
        """Genera respuesta del modelo."""
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Verifica si el modelo está disponible."""
        pass


class OllamaLLM(BaseLLM):
    """Wrapper para Ollama (local)."""
    
    def __init__(self, model: str = "llama3:70b-instruct"):
        self.model = model
    
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2,
        max_tokens: int = 2048
    ) -> LLMResponse:
        try:
            import ollama
        except ImportError:
            raise RuntimeError("Ollama no instalado: pip install ollama")
        
        response = ollama.generate(
            model=self.model,
            system=system_prompt or "",
            prompt=prompt,
            options={'temperature': temperature, 'num_predict': max_tokens}
        )
        
        return LLMResponse(
            text=response['response'],
            tokens_used=response.get('eval_count', 0),
            model=self.model,
            finish_reason='stop'
        )
    
    def is_available(self) -> bool:
        try:
            import ollama
            ollama.list()
            return True
        except:
            return False


class MockLLM(BaseLLM):
    """Mock LLM para testing sin modelo real."""
    
    def __init__(self):
        self.model = "mock-llm"
    
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2,
        max_tokens: int = 2048
    ) -> LLMResponse:
        return LLMResponse(
            text='{"analysis": "mock response for testing"}',
            tokens_used=10,
            model=self.model,
            finish_reason='stop'
        )
    
    def is_available(self) -> bool:
        return True


def get_llm(preferred: str = "ollama") -> BaseLLM:
    """Factory para obtener LLM disponible."""
    if preferred == "ollama":
        llm = OllamaLLM()
        if llm.is_available():
            return llm
    
    # Fallback a mock para desarrollo
    return MockLLM()
