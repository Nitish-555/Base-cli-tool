"""Service layer for code analysis operations"""
from analyzer import CodeAnalyzer
from utils import get_file_stats, validate_file_path

class AnalysisService:
    """Service for orchestrating code analysis"""
    
    def __init__(self):
        self.analyzer = CodeAnalyzer()
    
    def process_file(self, file_path: str) -> dict:
        """Process a single file through analysis"""
        if not validate_file_path(file_path):
            return {"error": "File not found", "file_path": file_path}
        
        # Use analyzer directly
        result = self.analyzer.analyze_file(file_path)
        
        # Also use utility function
        stats = get_file_stats(file_path)
        
        return {
            "primary": result,
            "secondary": stats,
            "processed": True
        }
    
    def process_multiple_files(self, file_paths: list[str]) -> dict:
        """Process multiple files"""
        results = {}
        for path in file_paths:
            results[path] = self.process_file(path)
        return results
    
    def get_analysis_summary(self, file_path: str) -> str:
        """Get a summary of analysis results"""
        result = self.analyzer.analyze_file(file_path)
        if "error" in result:
            return f"Error: {result['error']}"
        
        lines = result.get('lines', 0)
        functions = result.get('functions', 0)
        classes = result.get('classes', 0)
        
        return f"Summary - Lines: {lines}, Functions: {functions}, Classes: {classes}"