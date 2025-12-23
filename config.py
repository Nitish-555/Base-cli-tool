"""Configuration settings"""
import os

class Config:
    """Application configuration"""
    
    DEFAULT_FILE_EXTENSIONS = ['.py', '.pyw']
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    SUPPORTED_LANGUAGES = ['python']
    
    @staticmethod
    def get_output_format() -> str:
        """Get default output format"""
        return os.getenv('OUTPUT_FORMAT', 'json')
    
    @staticmethod
    def is_debug_mode() -> bool:
        """Check if debug mode is enabled"""
        return os.getenv('DEBUG', 'false').lower() == 'true'